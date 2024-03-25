-- Create hbnb_dev_db database if not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create new user hbnb_dev if he doesn't exit with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Give all privileges for the database hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Give only SELECT privilege for the database performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Update them
FLUSH PRIVILEGES;
