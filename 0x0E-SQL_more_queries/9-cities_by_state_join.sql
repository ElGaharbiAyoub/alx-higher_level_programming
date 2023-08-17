-- cities by states
SELECT c.id, c.name AS city_name, s.name AS state_name
FROM cities c, states s
WHERE c.state_id = s.id
ORDER BY c.id ASC;
