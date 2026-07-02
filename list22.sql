CREATE TRIGGER update_master_stats
AFTER INSERT ON appointments
BEGIN
    UPDATE master_statistics 
    SET 
        total_appointments = total_appointments + 1,
        total_revenue = total_revenue + (SELECT price FROM services WHERE id = NEW.service_id),
        last_appointment_date = NEW.appointment_time
    WHERE specialist_id = NEW.specialist_id;
END;