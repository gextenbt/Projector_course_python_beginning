-- Insert data into tables
INSERT INTO "user" (Name, Email)
VALUES 
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com'),
    ('Michael Johnson', 'michael@example.com');

INSERT INTO host (Nickname, User_ID)
VALUES
    ('SuperHost123', 1),
    ('Traveler456', 2),
    ('FriendlyHost789', 3);

INSERT INTO guest (Nickname, User_ID)
VALUES
    ('AdventureSeeker', 1),
    ('GlobeTrotter', 2),
    ('HappyTraveler', 3);

INSERT INTO room (Host_ID)
VALUES
    (1),
    (2),
    (3);

INSERT INTO room_items (Room_ID, room_item_name, quantity, is_present)
VALUES
    (1, 'bed', 1, true),
    (1, 'bathroom', 1, true),
    (1, 'wifi', 1, true),
    (2, 'bed', 2, true),
    (2, 'bathroom', 1, true),
    (2, 'tv', 1, true), 
    (3, 'bed', 1, true),
    (3, 'bathroom', 1, true),
    (3, 'wifi', 1, true),
    (3, 'kitchenette', 1, true);

INSERT INTO reservation (Guest_ID, Room_ID, CheckIn_Date, CheckOut_Date)
VALUES
    (1, 1, '2023-07-01', '2023-07-05'),
    (2, 2, '2023-08-15', '2023-08-20'),
    (3, 3, '2023-09-10', '2023-09-15');

INSERT INTO room_description (Room_ID, daily_price , Residents_amount, room_items)
VALUES
(1, 200, 1, 
    (SELECT 
        json_agg(
            json_build_object(
                'room_item_id', id,
                'room_item_name', room_item_name,
                'quantity', quantity,
                'is_present', is_present
            )
        ) 
    FROM room_items 
    WHERE Room_ID = 1)),
(2, 300, 1, 
    (SELECT 
        json_agg(
            json_build_object(
                'room_item_id', id,
                'room_item_name', room_item_name,
                'quantity', quantity,
                'is_present', is_present
            )
        ) 
    FROM room_items 
    WHERE Room_ID = 2)),
(3, 200, 2, 
    (SELECT 
        json_agg(
            json_build_object(
                'room_item_id', id,
                'room_item_name', room_item_name,
                'quantity', quantity,
                'is_present', is_present
            )
        ) 
    FROM room_items 
    WHERE Room_ID = 3));

INSERT INTO payment (Reservation_ID, Daily_price, Final_price, Is_paid)
VALUES
    (1, (SELECT Daily_price FROM room_description WHERE Room_ID = 1), 500, true),
    (2, (SELECT Daily_price FROM room_description WHERE Room_ID = 2), 750, true),
    (3, (SELECT Daily_price FROM room_description WHERE Room_ID = 3), 600, true);

INSERT INTO review (Guest_ID, Host_ID, Room_ID, room_items, Rating, Comment)
VALUES
(1, 1, 1, 
    (SELECT 
        json_agg(
            json_build_object(
                'room_item_id', id,
                'room_item_name', room_item_name,
                'quantity', quantity,
                'is_present', is_present
            )
        ) 
    FROM room_items 
    WHERE Room_ID = 1), 
    4, 'Great experience!'),
(2, 2, 2, 
    (SELECT 
        json_agg(
            json_build_object(
                'room_item_id', id,
                'room_item_name', room_item_name,
                'quantity', quantity,
                'is_present', is_present
            )
        ) 
    FROM room_items 
    WHERE Room_ID = 2), 
    4, 'Wonderful stay!'),
(3, 3, 3, 
    (SELECT 
        json_agg(
            json_build_object(
                'room_item_id', id,
                'room_item_name', room_item_name,
                'quantity', quantity,
                'is_present', is_present
            )
        ) 
    FROM room_items 
    WHERE Room_ID = 3), 
    5, 'Highly recommended!');