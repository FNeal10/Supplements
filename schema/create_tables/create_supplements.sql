IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{{schema_name}}' AND TABLE_NAME = 'supplement_catalog')
BEGIN
    DROP TABLE {{schema_name}}.supplement_catalog;
END
CREATE TABLE {{schema_name}}.supplement_catalog (
    SupplementID INT IDENTITY(1,1) PRIMARY KEY,
    SupplementName VARCHAR(100) NOT NULL,
    Overview VARCHAR(MAX) NULL,
    SideEffects VARCHAR(MAX) NULL,
    Precautions VARCHAR(MAX) NULL,
    Dosing VARCHAR(MAX) NULL
);
