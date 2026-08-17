-- Filtering columns within a range�Get all the listings with 3 to 6 rooms
SELECT * 
FROM AirbnbDB.dbo.airbnb_listings
WHERE number_of_rooms BETWEEN 3 AND 6;