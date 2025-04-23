IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{{schema_name}}' AND TABLE_NAME = 'uses_category')
BEGIN
    DROP TABLE {{schema_name}}.uses_category;
END
CREATE TABLE {{schema_name}}.uses_category (
    UsesCategoryID INT IDENTITY(1,1) PRIMARY KEY,
    UsesCategory VARCHAR(MAX) NULL
);