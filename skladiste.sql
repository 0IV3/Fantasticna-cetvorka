DROP DATABASE IF EXISTS skladiste;
CREATE DATABASE IF NOT EXISTS skladiste;
USE skladiste;

DROP TABLE IF EXISTS Proizvodi, Kupci, Osoblje, Porudzbine;

CREATE TABLE Proizvodi (
    'id' INT NOT NULL AUTO_INCREMENT,
    'name' VARCHAR(45) NOT NULL,
    'price' FLOAT NOT NULL,
    'amount' INT NOT NULL,
    'created_at' DATE NULL,
    'updated_at' DATE NULL,
    PRIMARY KEY ('id'),
    UNIQUE INDEX 'name' ('name')
)   ENGINE = InnoDB;

CREATE TABLE Kupci (
    'id' INT NOT NULL AUTO_INCREMENT,
    'first_name' VARCHAR(45) NOT NULL,
    'last_name' VARCHAR(45) NOT NULL,
    'street' VARCHAR(150) NOT NULL,
    'post_code' INT NOT NULL,
    'age' INT NOT NULL,
    'created_at' DATE NULL,
    'updated_at' DATE NULL,
    PRIMARY KEY ('id'),
    INDEX 'last_name' ('last_name', 'first_name')
)   ENGINE = InnoDB;

CREATE TABLE Osoblje (
    'id' INT NOT NULL AUTO_INCREMENT,
    'first_name' VARCHAR(45) NOT NULL,
    'last_name' VARCHAR(45) NOT NULL,
    'employee_since' DATE NOT NULL,
    'age' INT NOT NULL,
    'created_at' DATE NULL,
    'updated_at' DATE NULL,
    PRIMARY KEY ('id'),
    INDEX 'last_name' ('last_name', 'first_name')
)   ENGINE = InnoDB;

CREATE TABLE Porudzbine (
    'id' INT NOT NULL AUTO_INCREMENT,
    'product_id' INT NOT NULL,
    'customer_id' INT NOT NULL,
    'staff_id' INT NOT NULL,
    'count' INT NOT NULL,
    'created_at' DATE NULL,
    'updated_at' DATE NULL,
    PRIMARY KEY ('id'),
    INDEX 'product_tbl_idx' ('product_id'),
    INDEX 'customer_tbl_idx' ('customer_id'),
    INDEX 'staff_tbl_idx' ('staff_id'),
    CONSTRAINT 'product_tbl'
        FOREIGN KEY ('product_id')
        REFERENCES 'skladiste'.'Proizvodi' ('id')
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT 'customer_tbl'
        FOREIGN KEY ('customer_id')
        REFERENCES 'skladiste'.'Kupci' ('id')
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT 'staff_tbl'
        FOREIGN KEY ('staff_id')
        REFERENCES 'skladiste'.'Osoblje' ('id')
        ON DELETE NO ACTION
        ON UPDATE NO ACTION    
)   ENGINE = InnoDB;

insert into Proizvodi values
(1001, 'Testera', 129.94, 87, '2022-01-10', '2022-01-10'),
(1002, 'Cekic', 124.80, 100, '2022-01-10', '2022-01-10'),
(1003, 'Busilica', 329.95, 40, '2022-01-10', '2022-01-10'),
(1004, 'Sraf', 4.20, 1500, '2022-01-10', '2022-01-10'),
(1005, 'Ekser', 3.90, 3000, '2022-01-10', '2022-01-10'),
(1006, 'Stega', 322.60, 15, '2022-01-10', '2022-01-10'),
(1007, 'Srafciger', 29.40, 80, '2022-01-10', '2022-01-10'),
(1008, 'Francuz kljuc', 22.90, 95, '2022-01-10', '2022-01-10');

insert into Kupci values
(101, 'Milan', 'Jovanovic', 'Beograd', 11000, 45, '2022-01-10', '2022-01-10'),
(102, 'Ivana', 'Petrovic', 'Nis', 10000, 34, '2022-01-10', '2022-01-10'),
(103, 'Marko', 'Nikolic', 'Novi Sad', 21000, 33, '2022-01-10', '2022-01-10'),
(104, 'Jelena', 'Milenkovic', 'Kragujevac', 34000, 40, '2022-01-10', '2022-01-10'),
(105, 'Stefan', 'Radovic', 'Beograd', 11000, 30, '2022-01-10', '2022-01-10'),
(106, 'Ana', 'Kostic', 'Novi Sad', 21000, 41, '2022-01-10', '2022-01-10'),
(107, 'Nikola', 'Ristic', 'Subotica', 24000, 38, '2022-01-10', '2022-01-10'),
(108, 'Sara', 'Lukic', 'Zrenjanin', 23000, 35, '2022-01-10', '2022-01-10'),
(109, 'Tamara', 'Stojanovic', 'Beograd', 11000, 35, '2022-01-10', '2022-01-10'),
(110, 'Aleksandar', 'Mihajlovic', 'Kragujevac', 34000, 42, '2022-01-10', '2022-01-10');

insert into Osoblje values
(1001, 'Nemanja', 'Vasic', '2018-03-14', 34, '2022-01-10', '2022-01-10'),
(1002, 'Jovana', 'Djordjevic', '2019-07-24', 30, '2022-01-10', '2022-01-10'),
(1003, 'Milos', 'Ilic', '2009-03-15', 28, '2022-01-10', '2022-01-10'),
(1004, 'Teodora', 'Marinkovic', '2016-03-20', 35, '2022-01-10', '2022-01-10'),
(1005, 'Lazar', 'Popovic', '2020-03-01', 34, '2022-01-10', '2022-01-10');

insert into Porudzbine values
(1, 1002, 103, 1002, 1, '2022-01-10', '2022-01-10'),
(2, 1004, 103, 1002, 10, '2022-01-10', '2022-01-10'),
(3, 1004, 105, 1004, 15, '2022-01-10', '2022-01-10'),
(4, 1004, 107, 1005, 10, '2022-01-10', '2022-01-10'),
(5, 1004, 105, 1005, 15, '2022-01-10', '2022-01-10'),
(6, 1004, 104, 1004, 12, '2022-01-10', '2022-01-10'),
(7, 1004, 101, 1002, 10, '2022-01-10', '2022-01-10'),
(8, 1008, 109, 1001, 2, '2022-01-10', '2022-01-10'),
(9, 1003, 110, 1003, 1, '2022-01-10', '2022-01-10'),
(10, 1001, 106, 1001, 1, '2022-01-10', '2022-01-10'),
(11, 1005, 103, 1001, 3, '2022-01-10', '2022-01-10'),
(12, 1007, 109, 1002, 2, '2022-01-10', '2022-01-10');