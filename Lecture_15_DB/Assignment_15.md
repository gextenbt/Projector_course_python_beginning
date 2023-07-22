
Create a data model for a [AirBnb.com](http://airbnb.com/) system. 
- Your model should give ability to store information about the:

	- users | You should have two types of users:

		- Hosts
			- Host should be able to:
				- create rooms with different attributes (amount of residents, price, A/C, refrigerator, etc.)

		- Guests
			- Guest should be able to make a:
				- Check availability of any rooms
				- Make Reservation for a room.
				- (Optional):
					- Pay for reservation
					- Review for the host.

	- the rooms, 
	- the reservations, 
	- the reviews

For each table you should describe what is the primary key and what are the foreign keys (if any).

Result of the work might be description in a table.
You can create tables in text file with description of each field. 

(Optional): Add this possibilities for a guest
- Pay for reservation
- Review for the host.

-------------------------------------------------------------------------
List of this tool: [https://www.holistics.io/blog/top-5-free-database-diagram-design-tools/](https://www.holistics.io/blog/top-5-free-database-diagram-design-tools/)

You also can use any graphic tool that you might use to create data model. For example use [DRAW.io](http://draw.io/).
------------------------------------------------------------------------



```mermaid
erDiagram
    user {
        User_ID int PK
        Name string
        Email string
        Type string
    }

    host {
        Host_ID int PK
        User_ID int FK
        %% Other attributes specific to Hosts
    }

    guest {
        Guest_ID int PK
        User_ID int FK
        %% Other attributes specific to Guests
    }

    room {
        Room_ID int PK
        Host_ID int FK
    }

    room_items {
        Room_items_id int PK
        Room_ID int FK
        Daily_price int
        Residents_amount int
        Refrigerator bool
        AC bool
        %% Other attributes for the Room
    }

    reservation {
        Reservation_ID int PK
        Guest_ID int FK
        Room_ID int FK
        CheckIn_Date date
        CheckOut_Date date
        %% Other attributes for the Reservation
    }

    payment {
        Payment_ID int PK
        Reservation_ID int FK
        Daily_price int FK
        Final_price int
        Is_paid bool
        %% Other attributes for the Reservation
    }

    review {
        Review_ID int PK
        Guest_ID int FK
        Host_ID int FK
        Room_ID int FK
        Room_items_id int FK
        Rating int(5)
        Comment string
        %% Other attributes for the Review
    }

%% May has one or more ||--|{ Has only one
%% |o	o|	Zero or one
%% ||	||	Exactly one
%% }o	o{	Zero or more (no upper limit)
%% }|	|{	One or more (no upper limit)

    user ||--|{ host:""
    user ||--|{ guest:""
    host ||--o| room:"Has"
    guest ||--o| reservation:"Makes"
    guest ||--o| reservation:"Checks of availability for"
    guest ||--o| payment:"Makes"
    guest ||--o| review:"Makes"
    reservation ||--o| payment:"Requires"
    payment ||--o| room_items:"Contains price in"
    review ||--o| room_items:"Contains"
    room ||--o| review:"Has"
    room ||--o| reservation:"Has"
    room ||--o| room_items:"Has"
    host ||--o| review:"Has"
```