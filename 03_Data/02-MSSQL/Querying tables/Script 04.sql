--Get the listing id, city, ordered by the number_of_rooms in ascending order
SELECT id, city FROM AirbnbDB.dbo.airbnb_listings
ORDER BY number_of_rooms ASC;