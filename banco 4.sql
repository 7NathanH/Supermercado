

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


CREATE SCHEMA IF NOT EXISTS `db_supermercado` ;
USE `db_supermercado` ;

CREATE TABLE IF NOT EXISTS `db_supermercado`.`clientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `db_supermercado`.`produtos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  `preco` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `db_supermercado`.`pedidos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `clientes_id` INT NOT NULL,
  `produtos_id` INT NOT NULL,
  `data_pedido` DATE NOT NULL,
  PRIMARY KEY (`id`, `clientes_id`, `produtos_id`),
  INDEX `fk_pedidos_clientes_idx` (`clientes_id` ASC) VISIBLE,
  INDEX `fk_pedidos_produtos1_idx` (`produtos_id` ASC) VISIBLE,
  CONSTRAINT `fk_pedidos_clientes`
    FOREIGN KEY (`clientes_id`)
    REFERENCES `db_supermercado`.`clientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pedidos_produtos1`
    FOREIGN KEY (`produtos_id`)
    REFERENCES `db_supermercado`.`produtos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;