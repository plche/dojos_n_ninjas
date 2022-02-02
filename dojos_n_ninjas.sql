-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_n_ninjas_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojos_n_ninjas_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_n_ninjas_schema` DEFAULT CHARACTER SET utf8 ;
USE `dojos_n_ninjas_schema` ;

-- -----------------------------------------------------
-- Table `dojos_n_ninjas_schema`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_n_ninjas_schema`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(90) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_n_ninjas_schema`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_n_ninjas_schema`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NULL,
  `age` TINYINT NOT NULL,
  `dojo_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_n_ninjas_schema`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

USE dojos_n_ninjas_schema;

INSERT INTO dojos (name)
VALUES ('Dojo #1'),
('Dojo #2'),
('Dojo #3');

DELETE FROM dojos
WHERE id <= 3;

INSERT INTO dojos (name)
VALUES ('Dojo #4'),
('Dojo #5'),
('Dojo #6');

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Percy', 'Che', 46, 4),
('Edgard', 'Rodríguez', 32, 4),
('Sebastian', 'Alvarado', 22, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Isabel', 'Benites', 33, 5),
('Roberto', 'Villamar', 55, 5),
('Miguel', 'Iglesias', 29, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Margarita', 'Lezama', 34, 6),
('Briana', 'Paz', 28, 6),
('Carolina', 'Espinoza', 40, 6);

SELECT *
FROM ninjas
WHERE dojo_id = 4;

SELECT *
FROM ninjas
WHERE dojo_id = (
	SELECT dojo_id
	FROM ninjas
	ORDER BY dojo_id DESC
	LIMIT 1);

SELECT dojo_id
FROM ninjas
ORDER BY id DESC
LIMIT 1;