CREATE VIEW service_statistics AS
SELECT 
    s.id,
    s.name as service_name,
    s.price,
    COUNT(a.id) as total_bookings
FROM services s
LEFT JOIN appointments a ON a.service_id = s.id
GROUP BY s.id
ORDER BY total_bookings DESC;