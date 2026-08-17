--Get all the listings where number_of_rooms is missing
SELECT * FROM AirbnbDB.dbo.airbnb_listings
WHERE number_of_rooms IS NULL;