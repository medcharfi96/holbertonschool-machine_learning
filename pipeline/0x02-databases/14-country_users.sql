-- creation de table user

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users`(
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `email` CHAR(255) NOT NULL UNIQUE,
    `name` CHAR(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US', 
    PRIMARY KEY (`id`)
);

