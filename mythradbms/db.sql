CREATE DATABASE airplane_db1;
USE airplane_db1;

CREATE TABLE airplane_details (
    id VARCHAR(10) PRIMARY KEY,
    model VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    capacity INT NOT NULL
);

INSERT INTO airplane_details VALUES ('A001', 'Boeing 737', 'Boeing', 200);
INSERT INTO airplane_details VALUES ('A002', 'Airbus A320', 'Airbus', 180);
INSERT INTO airplane_details VALUES ('A003', 'Boeing 787', 'Boeing', 240);

SELECT * FROM airplane_details;