<?php
//Application Configurations
$app_id		= "1440716592835083";
$app_secret	= "73dd9b3dbbfcf57e1baf45e928cdf73d";
$site_url	= "http://www.yangwangblog.com/fb/index.php";

try{
	include_once "src/facebook.php";
}catch(Exception $e){
	error_log($e);
}
// Create our application instance
$facebook = new Facebook(array(
	'appId'		=> $app_id,
	'secret'	=> $app_secret,
	));

// Get User ID
$user = $facebook->getUser();
// We may or may not have this data based 
// on whether the user is logged in.
// If we have a $user id here, it means we know 
// the user is logged into
// Facebook, but we don�t know if the access token is valid. An access
// token is invalid if the user logged out of Facebook.

if($user){
//==================== Single query method ======================================
	try{
		// Proceed knowing you have a logged in user who's authenticated.
		$user_profile = $facebook->api('/me');
	}catch(FacebookApiException $e){
		error_log($e);
		$user = NULL;
	}
//==================== Single query method ends =================================
}

if($user){
	// Get logout URL
	$logoutUrl = $facebook->getLogoutUrl();
	
}else{
	// Get login URL
	$loginUrl = $facebook->getLoginUrl(array(
		'scope'			=> 'read_stream, publish_stream, user_birthday, user_location, user_work_history, user_hometown, user_photos',
		'redirect_uri'	=> $site_url,
		));
}

if($user){
	// Proceed knowing you have a logged in user who has a valid session.
	
//========= Batch requests over the Facebook Graph API using the PHP-SDK ========
	// Save your method calls into an array
	$queries = array(
		array('method' => 'GET', 'relative_url' => '/'.$user),
		array('method' => 'GET', 'relative_url' => '/'.$user.'/home?limit=50'),
		array('method' => 'GET', 'relative_url' => '/'.$user.'/friends'),
		array('method' => 'GET', 'relative_url' => '/'.$user.'/photos?limit=8'),
		array('method' => 'GET', 'relative_url' => '/'.$user.'/likes'),
		);

	// POST your queries to the batch endpoint on the graph.
	try{
		$batchResponse = $facebook->api('?batch='.json_encode($queries), 'POST');
	}catch(Exception $o){
		error_log($o);
	}

	//Return values are indexed in order of the original array, content is in ['body'] as a JSON
	//string. Decode for use as a PHP array.
	$user_info		= json_decode($batchResponse[0]['body'], TRUE);
	$feed			= json_decode($batchResponse[1]['body'], TRUE);
	$friends_list	= json_decode($batchResponse[2]['body'], TRUE);
	$photos			= json_decode($batchResponse[3]['body'], TRUE);
	$mylikes          = json_decode($batchResponse[4]['body'], TRUE);
//========= Batch requests over the Facebook Graph API using the PHP-SDK ends =====

	// Update user's status using graph api
	if(isset($_POST['pub'])){
		try{
			$statusUpdate = $facebook->api("/$user/feed", 'post', array(
				'message'		=> 'Check out Our 670 projects',
				'link'			=> 'http://www.yangwangblog.com/fb/index.php',
				'picture'		=> 'http://www.yangwangblog.com/images/670pj.png',
				'name'			=> 'Show personalized news to users',
				'caption'		=> 'Your News.com',
				'description'	=> 'We use your facebook information to recommend news to you',
				));
		}catch(FacebookApiException $e){
			error_log($e);
		}
	}

	// Update user's status using graph api
	if(isset($_POST['status'])){
		try{
			$statusUpdate = $facebook->api("/$user/feed", 'post', array('message'=> $_POST['status']));
		}catch(FacebookApiException $e){
			error_log($e);
		}
	}
}
?>