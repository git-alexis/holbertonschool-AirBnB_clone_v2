-- Create hbnb_test_db database if not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create new user hbnb_test if he doesn't exit with password hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Give all privileges for the database hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Give only SELECT privilege for the database performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Update them
FLUSH PRIVILEGES;
