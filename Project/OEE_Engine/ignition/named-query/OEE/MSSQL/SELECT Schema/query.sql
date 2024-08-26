SELECT
    SCHEMA_NAME(tab.schema_id) AS SchemaName,
    tab.name AS TableName,
    col.column_id AS ColumnId,
    col.name AS ColumnName,
    t.name AS DataType,
    col.max_length AS MaxLength,
    col.precision AS Precision
FROM sys.tables AS tab
JOIN sys.all_columns AS col ON tab.object_id = col.object_id
JOIN sys.types AS t ON col.system_type_id = t.system_type_id
WHERE tab.name LIKE 'OEE_%'
ORDER BY SchemaName, TableName, ColumnId;