<?php 
    session_start();            //start session
    $_SESSION = array();    //clear session array
    session_destroy();      //destroy session
?>
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Log Out</title>
</head>

<body>
<p>You have successfully logged out!</p>
<p>Return to the <a href="index.php">connect</a> page</p>

</body>
</html>