--Get all the listings where number_of_rooms is not missing
SELECT * FROM AirbnbDB.dbo.airbnb_listings
WHERE number_of_rooms IS NOT NULL;