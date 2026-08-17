--Get the number of listings per country
SELECT country, COUNT(id) AS number_of_listings
FROM airbnb_listings
GROUP BY country;