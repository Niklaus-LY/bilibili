CREATE DATABASE bilibili IF NOT EXISTS ;
USE bilibili;
CREATE TABLE video(
    `id` INT AUTO_INCREMENT,
    `title` VARCHAR(100) NOT NULL,
    `author` VARCHAR(50) ,
    `like_count`  FLOAT NOT NULL,
    `coin_count`  FLOAT NOT NULL,
    `collect_count`  FLOAT NOT NULL,
    `view_count`  FLOAT NOT NULL,
    `dm_count`  FLOAT NOT NULL,
    `bv` VARCHAR(20) NOT NULL ,
    `dm` LONGTEXT,
    PRIMARY KEY(id)
)CHARSET=utf8mb4;