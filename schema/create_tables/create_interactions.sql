IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{{schema_name}}' AND TABLE_NAME = 'interactions')
BEGIN
    DROP TABLE {{schema_name}}.interactions;
END
CREATE TABLE {{schema_name}}.interactions (
    InteractionsID INT IDENTITY(1,1) PRIMARY KEY,
    SupplementID INT,
    Effectiveness VARCHAR(30),
    Interactions VARCHAR(MAX) NULL
);