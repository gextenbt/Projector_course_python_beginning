-- Create the "user" table
CREATE TABLE "user" (
    id serial PRIMARY KEY,
    Name varchar(255),
    Email varchar(255)
);

-- Create the "host" table
CREATE TABLE host (
    id serial PRIMARY KEY,
    Nickname varchar(255),
    User_ID int not null,
    FOREIGN KEY (User_ID) REFERENCES "user"(id)
);

-- Create the "guest" table
CREATE TABLE guest (
    id serial PRIMARY KEY,
    Nickname varchar(255),
    User_ID int not null,
    FOREIGN KEY (User_ID) REFERENCES "user"(id)
);

-- Create the "room" table
CREATE TABLE room (
    id serial PRIMARY KEY,
    Host_ID int not null,
    FOREIGN KEY (Host_ID) REFERENCES host(id)
);

-- Create the "room_description" table
CREATE TABLE room_description (
    id serial PRIMARY KEY,
    Room_ID int not null,
    daily_price int,
    Residents_amount int,
    room_items JSON,
    CONSTRAINT uk_room_description UNIQUE (id, daily_price),
    FOREIGN KEY (Room_ID) REFERENCES room(id)
);

-- Create the "room_items" table
CREATE TABLE room_items (
    id serial PRIMARY KEY,
    Room_ID int not null,
    room_item_name varchar(50),
    quantity int,
    is_present bool,
    FOREIGN KEY (Room_ID) REFERENCES room(id)
);

-- Create the "reservation" table
CREATE TABLE reservation (
    id serial PRIMARY KEY,
    Guest_ID int not null,
    Room_ID int not null,
    CheckIn_Date date,
    CheckOut_Date date,
    FOREIGN KEY (Guest_ID) REFERENCES guest(id),
    FOREIGN KEY (Room_ID) REFERENCES room(id)
);

-- Create the "payment" table
CREATE TABLE payment (
    id serial PRIMARY KEY,
    Reservation_ID int not null,
    daily_price int not null,
    Final_price int,
    Is_paid bool,
    FOREIGN KEY (id, daily_price) REFERENCES room_description(id, daily_price), --check it
    FOREIGN KEY (Reservation_ID) REFERENCES reservation(id)
);

-- Create the "review" table
CREATE TABLE review (
    id serial PRIMARY KEY,
    Guest_ID int not null,
    Host_ID int not null,
    Room_ID int not null,
    room_items JSON,
    Rating int,
    Comment varchar(255),
    FOREIGN KEY (Guest_ID) REFERENCES guest(id),
    FOREIGN KEY (Host_ID) REFERENCES host(id),
    FOREIGN KEY (Room_ID) REFERENCES room(id)
);