-- cities by states
SELECT c.id, c.name, s.name FROM cities AS c, states AS s
WHERE c.state_id = s.id
GROUP BY c.id ASC;
