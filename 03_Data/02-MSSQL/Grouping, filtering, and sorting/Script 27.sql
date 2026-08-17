--Get the listing with the maximum number of rooms per country
SELECT country, MAX(number_of_rooms)
FROM airbnb_listings
GROUP BY country;