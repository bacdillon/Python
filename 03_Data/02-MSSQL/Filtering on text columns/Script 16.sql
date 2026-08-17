-- Get all listings where city starts with "j" and where it does not end with "t"
SELECT * 
FROM AirbnbDB.dbo.airbnb_listings
WHERE city LIKE 'j%' AND city NOT LIKE '%t';