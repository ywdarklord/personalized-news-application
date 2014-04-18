
DROP TABLE `webpage`;
DROP TABLE `article`;

CREATE TABLE IF NOT EXISTS `webpage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `unique_id` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '0',
  `url` varchar(255) NOT NULL,
  `title` varchar(500) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  `raw_categories` varchar(255) DEFAULT NULL,
  `publisher` varchar(50) NOT NULL,
  `tries` tinyint DEFAULT 0,
  `created` DATETIME DEFAULT NULL,
  `published` DATETIME DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_unique` (`unique_id`),
  KEY `idx_publisher` (`publisher`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE IF NOT EXISTS `article` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`unique_id` varchar(100) NOT NULL,
	`publisher` varchar(50) NOT NULL,
	`categories` varchar(255) DEFAULT NULL,
	`title` varchar(500) NOT NULL,
	`url` varchar(255) NOT NULL,
	`content` longtext DEFAULT NULL,
	`content_html` longtext DEFAULT NULL,
	`image` varchar(500) DEFAULT NULL,
	`raw_categories` varchar(255) DEFAULT NULL,
	`created` DATETIME DEFAULT NULL,
	`published` DATETIME DEFAULT NULL,
	PRIMARY KEY (`id`),
	UNIQUE KEY `idx_unique` (`unique_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


INSERT INTO webpage (`unique_id`, `status`, `url`, `title`, `html`, `publisher`, `created`, `published`)
VALUES (%(uniqueId)s, %(status)s, %(url)s, %(title)s, %(html)s, %(publisher)s, now(), %(publishedSql)s)