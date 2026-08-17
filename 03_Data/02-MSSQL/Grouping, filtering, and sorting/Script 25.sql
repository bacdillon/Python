-- Grouping, filtering, and sorting
-- Get the total number of rooms for each country
SELECT country, SUM(number_of_rooms) AS total_rooms
FROM AirbnbDB.dbo.airbnb_listings
GROUP BY country;