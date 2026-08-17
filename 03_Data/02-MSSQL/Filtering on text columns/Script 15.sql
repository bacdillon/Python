-- Filter one column on many conditions�Get the listings based in the 'USA' and in �France�
SELECT * FROM AirbnbDB.dbo.airbnb_listings
WHERE country IN ('USA', 'France');