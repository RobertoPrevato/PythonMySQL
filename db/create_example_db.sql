/*
 * Example database to demonstrate use of Python with MySQL and SQLAlchemy.
 * https://github.com/RobertoPrevato/PythonMySQL
 *
 * Copyright 2017, Roberto Prevato
 * https://robertoprevato.github.io
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
*/

CREATE DATABASE `pymysql_example` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `pymysql_example`;

CREATE TABLE `app_user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `guid` char(36) NOT NULL,
  `username` varchar(50) NOT NULL,
  `hashed_password` char(56) NOT NULL COMMENT 'sensitive',
  `salt` char(50) NOT NULL COMMENT 'sensitive',
  `email` varchar(254) NOT NULL,
  `creation_time` datetime NOT NULL,
  `password_reset_token` char(36) DEFAULT NULL COMMENT 'sensitive',
  `confirmation_token` char(36) DEFAULT NULL COMMENT 'sensitive',
  `confirmation_time` datetime DEFAULT NULL,
  `newsletter` tinyint(1) NOT NULL DEFAULT '0',
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `banned` tinyint(1) NOT NULL DEFAULT '0',
  `confirmed` tinyint(1) NOT NULL DEFAULT '0',
  `language` char(2) NOT NULL DEFAULT 'en',
  PRIMARY KEY (`id`),
  UNIQUE KEY `IX_Username` (`username`),
  UNIQUE KEY `IX_Email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


CREATE TABLE `picture` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `guid` char(36) NOT NULL,
  `med_guid` char(36) NOT NULL,
  `thm_guid` char(36) NOT NULL,
  `file_name` varchar(300) NOT NULL,
  `extension` char(3) NOT NULL,
  `type` varchar(45) NOT NULL,
  `width` smallint(5) unsigned NOT NULL,
  `height` smallint(5) unsigned NOT NULL,
  `ratio` double unsigned NOT NULL,
  `creation_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_picture_guid` (`guid`),
  UNIQUE KEY `uk_picture_medguid` (`med_guid`),
  UNIQUE KEY `uk_picture_thmguid` (`thm_guid`),
  KEY `fk_picture_user_id_idx` (`user_id`),
  CONSTRAINT `fk_picture_user_id` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


CREATE TABLE `app_language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `english_name` varchar(45) NOT NULL,
  `original_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code_UNIQUE` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


CREATE TABLE `picture_description` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `picture_id` int(10) unsigned NOT NULL,
  `language_id` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `caption` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_picture_description_picture_id_language_id` (`picture_id`,`language_id`),
  KEY `FK_picture_description_picture_id_idx` (`picture_id`),
  KEY `FK_picture_description_language_id_idx` (`language_id`),
  CONSTRAINT `FK_picture_description_language_id` FOREIGN KEY (`language_id`) REFERENCES `app_language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `FK_picture_description_picture_id` FOREIGN KEY (`picture_id`) REFERENCES `picture` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;