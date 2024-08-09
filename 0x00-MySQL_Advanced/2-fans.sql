-- ranks country origins of bands, ordered by the number.
-- Import this table dump: metal_bands.sql.zip

SELECT `origin` AS `origin`, SUM(`fans`) AS `nb_fans`
FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
