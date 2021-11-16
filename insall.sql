DROP TABLE IF EXISTS `slave`;
DROP TABLE IF EXISTS `master`;

CREATE TABLE `master` (
  `master_id` int unsigned NOT NULL AUTO_INCREMENT,
  `master_created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `master_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `master_flags` int unsigned NOT NULL DEFAULT '0',
  `master_name` varchar(32) NOT NULL,
  `master_host` varchar(128) NOT NULL,
  `master_wait` int unsigned NOT NULL,
  PRIMARY KEY (`master_id`)
) ENGINE=InnoDB CHARSET=utf8mb3;

CREATE TABLE `slave` (
  `slave_id` int unsigned NOT NULL AUTO_INCREMENT,
  `slave_created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `slave_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `slave_flags` int unsigned NOT NULL DEFAULT '0',
  `slave_name` varchar(128) NOT NULL,
  `slave_directory` varchar(128) NOT NULL,
  `slave_command` varchar(128) NOT NULL,
  `slave_order` int unsigned NOT NULL DEFAULT '0',
  `master_id` int unsigned NOT NULL,
  CONSTRAINT `slave_to_master` FOREIGN KEY (`master_id`) REFERENCES `master` (`master_id`),
  PRIMARY KEY (`slave_id`)
) ENGINE=InnoDB CHARSET=utf8mb3;
