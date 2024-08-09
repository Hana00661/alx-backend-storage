-- create name(first letter) and score index
-- Import this table dump: names.sql.zip

CREATE INDEX idx_name_first_score
ON names (name(1), score)
