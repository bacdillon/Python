--Get all the listings in "Paris" OR the ones that were listed after 2012
SELECT * FROM AirbnbDB.dbo.airbnb_listings
WHERE city = 'Paris' OR year_listed > 2012;