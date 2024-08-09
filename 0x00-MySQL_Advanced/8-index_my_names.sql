-- Create index on table
-- Import this table dump: names.sql.zip

CREATE INDEX idx_name_first
ON names (name(1))
