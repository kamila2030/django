CREATE VIEW top_masters AS
SELECT 
    s.id,
    s.name,
    s.specialization,
    s.photo_url,
    s.experience_years,
    COALESCE(ms.total_appointments, 0) as total_appointments,
    COALESCE(ms.total_revenue, 0) as total_revenue,
    s.is_top
FROM specialists s
LEFT JOIN master_statistics ms ON s.id = ms.specialist_id
ORDER BY total_appointments DESC;