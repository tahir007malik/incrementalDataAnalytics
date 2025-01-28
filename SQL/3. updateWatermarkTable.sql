CREATE PROCEDURE updateWatermarkTable
    @lastload VARCHAR(200)
AS
BEGIN
    -- START TRANSACTION
    BEGIN TRANSACTION
    -- UPDATE INCREMENTAL COLUMN IN TABLE
    UPDATE water_table
    SET last_load = @lastload
    COMMIT TRANSACTION
END;