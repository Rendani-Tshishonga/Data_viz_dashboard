--Create tables for the data visualization dashboard

USE data_dev_db;
CREATE TABLE IF NOT EXISTS orders(
	order_id INT,
	product_id INT,
	supplier_id INT,
	order_date DATETIME,
	quantity_ordered INT
);

CREATE TABLE IF NOT EXISTS products(
	product_id INT,
	name VARCHAR(128),
	description VARCHAR(1024),
	unit_price FLOAT,
	quantity_available INT
);

CREATE TABLE IF NOT EXISTS suppliers(
	name VARCHAR(128),
	address VARCHAR(1024),
	contact_person VARCHAR(128),
	phone_number INT,
);

CREATE TABLE IF NOT EXISTS shipments(
	shipment_id INT,
	order_id INT,
	shipment_date DATETIME,
	estimated_arrival_date DATETIME,
	actual_arrival_date DATETIME
);

