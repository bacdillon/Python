--Get the listing with the lowest number of rooms across all listings
SELECT MIN(Number_of_rooms)
FROM AirbnbDB.dbo.airbnb_listings