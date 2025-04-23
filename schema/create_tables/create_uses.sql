IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{{schema_name}}' AND TABLE_NAME = 'uses')
BEGIN
    DROP TABLE {{schema_name}}.uses;
END
CREATE TABLE {{schema_name}}.uses (
    UsesID INT IDENTITY(1,1) PRIMARY KEY,
    SupplementID INT,
    UsesCategoryID INT,
    Uses VARCHAR(MAX) NULL

    CONSTRAINT FK_Uses_Supplement FOREIGN KEY (SupplementID)
        REFERENCES {{schema_name}}.supplement_catalog(SupplementID)
);