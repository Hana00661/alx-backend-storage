--  creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0 if the

DELIMITER $ ;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
NO SQL
BEGIN
	IF b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END
$
