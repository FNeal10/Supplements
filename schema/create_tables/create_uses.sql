IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{{schema_name}}' AND TABLE_NAME = 'uses')
BEGIN
    DROP TABLE {{schema_name}}.uses;
END;
CREATE TABLE {{schema_name}}.uses (
    UsesID INT IDENTITY(1,1) PRIMARY KEY,
    SupplementID INT,
    Effectiveness VARCHAR(30),
    Uses VARCHAR(MAX) NULL
);