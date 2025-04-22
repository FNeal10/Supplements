IF NOT EXISTS (
    SELECT name FROM sys.databases WHERE name = '{{database_name}}'
)
BEGIN
    EXEC('CREATE DATABASE {{database_name}}')
END