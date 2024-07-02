CREATE DATABASE `marvel`
CREATE TABLE IF NOT EXISTS `marvel`.`user`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(100) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`id`)
    `email` VARCHAR(100) NOT NULL
)