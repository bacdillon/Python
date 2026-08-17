-- For Japan and the USA, get the average number of rooms per listing in each country
SELECT country, AVG(number_of_rooms) AS average_rooms
FROM AirbnbDB.dbo.airbnb_listings
WHERE country IN ('USA', 'Japan')
GROUP BY country;