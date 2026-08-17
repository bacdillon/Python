-- Get all the listings in "Paris" where number_of_rooms is bigger than 3
SELECT * FROM AirbnbDB.dbo.airbnb_listings
WHERE city = 'Paris' AND number_of_rooms > 3;