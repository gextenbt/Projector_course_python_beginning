-- 3.1 Find a user who had the biggest amount of reservations. Return user name and user_id
SELECT 
    "user".id, 
    "user".Name, 
    COUNT(reservation.id)
FROM 
    "user"
JOIN 
    guest ON "user".id = guest.User_ID
JOIN 
    reservation ON guest.id = reservation.Guest_ID
GROUP BY 
    "user".id, "user".Name
ORDER BY 
    COUNT(reservation.id) DESC
LIMIT 1;


-- 3.3(Optional) Find a host with the best average rating. Return hostname and host_id
SELECT 
    host.id AS host_id, 
    host.Nickname AS hostname, 
    AVG(review.Rating) AS average_rating
FROM 
    host
LEFT JOIN 
    review ON host.id = review.Host_ID
GROUP BY 
    host.id, host.Nickname
ORDER BY 
    AVG(review.Rating) DESC
LIMIT 1;