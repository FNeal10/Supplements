IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{{schema_name}}' AND TABLE_NAME = 'interactions_category')
BEGIN
    DROP TABLE {{schema_name}}.interactions_category;
END
CREATE TABLE {{schema_name}}.interactions_category (
    InteractionsCategoryID INT IDENTITY(1,1) PRIMARY KEY,
    INteractionsCategory VARCHAR(MAX) NULL
);