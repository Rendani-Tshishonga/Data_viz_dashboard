--Create tables for the data visualization dashboard
--Insert table values

USE data_dev_db;
CREATE TABLE IF NOT EXISTS orders(
	order_id VARCHAR(128) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	product_id VARCHAR(128) FOREIGN KEY REFERENCES products(product_id),
	supplier_id VARCHAR(128) FOREIGN KEY REFERENCES suppliers(supplier_id),
	order_date DATETIME NOT NULL,
	quantity_ordered INT NOT NULL,
);

CREATE TABLE IF NOT EXISTS products(
	product_id VARCHAR NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(128) NOT NULL,
	description VARCHAR(1024) NOT NULL,
	unit_price FLOAT NOT NULL,
	quantity_available INT NOT NULL,
);
INSERT INTO products (name, description, unit_price, quantity_available)
VALUES ('Pencom', '1.0 Ballpoint pen', 3.65, 1000);

CREATE TABLE IF NOT EXISTS suppliers(
	supplier_id VARCHAR(128) NOT NULL AUTO_INCREMENT PRIMARY_KEY,
	name VARCHAR(128) NOT NULL,
	address VARCHAR(1024) NOT NULL,
	contact_person VARCHAR(128) NOT NULL,
	phone_number INT NOT NULL,
);

CREATE TABLE IF NOT EXISTS shipments(
	shipment_id VARCHAR(128) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	order_id VARCHAR(128) NOT NULL FOREIGN KEY REFERENCES orders(order_id),
	shipment_date DATETIME NOT NULL,
	estimated_arrival_date DATETIME NOT NULL,
	actual_arrival_date DATETIME NOT NULL,
);

