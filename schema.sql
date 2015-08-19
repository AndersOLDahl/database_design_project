-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project` DEFAULT CHARACTER SET latin1 ;
USE `project` ;

-- -----------------------------------------------------
-- Table `project`.`Structures`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`Structures` (
  `structure_id` INT(11) NOT NULL COMMENT '' AUTO_INCREMENT,
  `cost_to_build` INT(11) NULL DEFAULT NULL COMMENT '',
  `year_built` INT(11) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`structure_id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `project`.`Bridges`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`Bridges` (
  `bridge_id` INT(11) NOT NULL COMMENT '',
  `bridge_name` VARCHAR(45) NULL DEFAULT NULL COMMENT '',
  `bridge_type` VARCHAR(45) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`bridge_id`)  COMMENT '',
  FOREIGN KEY (`bridge_id`)
  REFERENCES `project`.`Structures` (`structure_id`)
  ON DELETE CASCADE
  ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `project`.`Houses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`Houses` (
  `house_id` INT(11) NOT NULL COMMENT '',
  `house_type` VARCHAR(45) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`house_id`)  COMMENT '',
  FOREIGN KEY (`house_id`)
  REFERENCES `project`.`Structures` (`structure_id`)
  ON DELETE CASCADE
  ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `project`.`Rooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`Rooms` (
  `room_id` INT(11) NOT NULL COMMENT '' AUTO_INCREMENT,
  `room_house_id` INT(11) NOT NULL COMMENT '',
  `room_type` VARCHAR(45) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`room_id`)  COMMENT '',
  FOREIGN KEY (`room_house_id`)
  REFERENCES `project`.`Houses` (`house_id`)
  ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


CREATE INDEX `FKRooms` ON `project`.`Rooms` (`room_house_id` ASC)  COMMENT '';

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
