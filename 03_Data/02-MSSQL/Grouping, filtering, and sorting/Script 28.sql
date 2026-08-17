--Get the listing with the lowest amount of rooms per country
SELECT country, MIN(number_of_rooms)
FROM airbnb_listings
GROUP BY country;