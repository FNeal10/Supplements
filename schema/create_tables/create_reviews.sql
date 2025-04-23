IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{{schema_name}}' AND TABLE_NAME = 'user_reviews')
BEGIN
    DROP TABLE {{schema_name}}.user_reviews;
END
CREATE TABLE {{schema_name}}.user_reviews (
    ReviewID INT IDENTITY(1,1) PRIMARY KEY,
    SupplementID INT NOT NULL,
    ReviewedBy VARCHAR(100) NULL,
    AgeRange VARCHAR(20) NULL,
    MedicationDuration VARCHAR(50) NULL,
    Condition VARCHAR(100) NULL,
    Rating FLOAT DEFAULT 0,
    Effectiveness FLOAT DEFAULT 0,
    EaseOfUse FLOAT DEFAULT 0,
    Satisfaction FLOAT DEFAULT 0,
    Review VARCHAR(MAX) NULL

);



