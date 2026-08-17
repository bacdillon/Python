--Simple aggregations--
--Get the total number of rooms available across all listings 
SELECT SUM(Number_of_rooms) 
FROM AirbnbDB.dbo.airbnb_listings