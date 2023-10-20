DROP DATABASE IF EXISTS bincomtest;

CREATE DATABASE bincomtest;
CREATE USER IF NOT EXISTS 'bincom_dev'@'localhost' IDENTIFIED BY 'bincom_dev_1234';


GRANT ALL PRIVILEGES ON `bincomtest`.* TO 'bincom_dev'@'localhost';
-- ALTER ROLE bincom_dev SET client_encoding TO 'utf8';
-- ALTER ROLE bincom_dev SET default_transaction_isolation TO 'read committed';
-- ALTER ROLE bincom_dev SET timezone TO 'UTC';
-- ALTER DATABASE bincomtest OWNER TO bincom_dev;
GRANT SELECT ON `perfomance_schema`.* TO 'bincom_dev'@'localhost';
FLUSH PRIVILEGES
