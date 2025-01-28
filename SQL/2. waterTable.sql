CREATE TABLE water_table (
    last_load VARCHAR(2000),
)

-- Inserting lowest value for `date_id` to `water_table`
-- This will let us take all records for the initial data load
INSERT INTO water_table VALUES('DT00000');