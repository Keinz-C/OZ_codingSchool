-- MySQL Script generated by MySQL Workbench
-- Tue Aug 20 18:39:58 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`custmers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`custmers` (
  `ustomer_id` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  PRIMARY KEY (`ustomer_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`orders` (
  `order_id` INT NOT NULL,
  `date` DATE NULL,
  `total_amount` INT NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`order_id`),
  INDEX `fk_orders_custmers1_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_custmers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `mydb`.`custmers` (`ustomer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`carts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`carts` (
  `cart_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`cart_id`),
  INDEX `fk_carts_custmers_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_carts_custmers`
    FOREIGN KEY (`customer_id`)
    REFERENCES `mydb`.`custmers` (`ustomer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pubilshers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pubilshers` (
  `pubilsher_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  PRIMARY KEY (`pubilsher_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`books` (
  `book_id` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  `ISBN` VARCHAR(45) NULL,
  `pusblication_date` DATE NULL,
  `prict` INT NULL,
  `publishers_id` INT NOT NULL,
  PRIMARY KEY (`book_id`),
  INDEX `fk_books_pubilshers1_idx` (`publishers_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_pubilshers1`
    FOREIGN KEY (`publishers_id`)
    REFERENCES `mydb`.`pubilshers` (`pubilsher_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`authors` (
  `author_id` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `birth_date` DATE NULL,
  PRIMARY KEY (`author_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`books_authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`books_authors` (
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  `order` INT NULL,
  PRIMARY KEY (`author_id`, `book_id`),
  INDEX `fk_books_authors_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_authors_authors1`
    FOREIGN KEY (`author_id`)
    REFERENCES `mydb`.`authors` (`author_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_books_authors_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `mydb`.`books` (`book_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`carts_books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`carts_books` (
  `cart_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  `quantity` INT NULL,
  `added_date` DATE NULL,
  `price` INT NULL,
  PRIMARY KEY (`cart_id`, `book_id`),
  INDEX `fk_carts_books_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_carts_books_carts1`
    FOREIGN KEY (`cart_id`)
    REFERENCES `mydb`.`carts` (`cart_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_carts_books_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `mydb`.`books` (`book_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;