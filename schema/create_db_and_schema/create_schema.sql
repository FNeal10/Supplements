IF NOT EXISTS (
    SELECT * FROM sys.schemas WHERE name = '{{schema_name}}'
)
BEGIN
    EXEC('CREATE SCHEMA {{schema_name}}')
END