CREATE TRIGGER prevent_past_appointment
BEFORE INSERT ON appointments
BEGIN
    SELECT CASE
        WHEN NEW.appointment_time < datetime('now', 'localtime') THEN
            RAISE(ABORT, 'Нельзя записаться на прошедшую дату и время!')
    END;
END;