--Get the average number of rooms for each country
SELECT country, AVG(number_of_rooms)
FROM airbnb_listings
GROUP BY country;