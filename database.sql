-- Create a Database for the dashboard service

CREATE DATABASE IF NOT EXISTS data_dev_db;
CREATE USER IF NOT EXISTS 'data_dev'@'localhost' IDENTIFIED WITH mysql_native_password BY 'data_dev_pwd';
GRANT ALL PRIVILEGES ON `data_dev_db`.* TO 'data_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'data_dev'@'localhost';
FLUSH PRIVILEGES;
