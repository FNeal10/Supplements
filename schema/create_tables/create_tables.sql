IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{{schema_name}}' AND TABLE_NAME = 'supplement_catalog')
BEGIN
    DROP TABLE {{schema_name}}.supplement_catalog;
END
CREATE TABLE {{schema_name}}.supplement_catalog (
    SupplementID INT IDENTITY(1,1) PRIMARY KEY,
    SupplementName VARCHAR(100) NOT NULL,
    SupplementUrl VARCHAR(MAX) NOT NULL,
    Overview VARCHAR(MAX) NULL,
    SideEffects VARCHAR(MAX) NULL,
    Precautions VARCHAR(MAX) NULL,
    Dosing VARCHAR(MAX) NULL
);
CREATE UNIQUE INDEX IX_SupplementName ON {{schema_name}}.supplement_catalog(SupplementName);



IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{{schema_name}}' AND TABLE_NAME = 'user_reviews')
BEGIN
    DROP TABLE {{schema_name}}.user_reviews;
END
CREATE TABLE {{schema_name}}.user_reviews (
    ReviewID INT IDENTITY(1,1) PRIMARY KEY,
    User VARCHAR(100) NULL,
    AgeRange VARCHAR(20) NULL,
    MedicationDuration VARCHAR(50) NULL,
    Condition VARCHAR(100) NULL,
    Rating FLOAT DEFAULT 0,
    Effectiveness FLOAT DEFAULT 0,
    EaseOfUse FLOAT DEFAULT 0,
    Satisfaction FLOAT DEFAULT 0,
    Review VARCHAR(MAX) NULL
);



