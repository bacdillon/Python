-- Get the listing id, city, ordered by the number_of_rooms in descending order
SELECT ID, City FROM AirbnbDB.dbo.airbnb_listings
ORDER BY number_of_rooms DESC;