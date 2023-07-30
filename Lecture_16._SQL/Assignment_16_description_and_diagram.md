

```markdown
1. Write SQL queries for table creation for a data model that you created for prev homework (Airbnb model)

2. Write 3 rows (using INSERT queries) for each table in the data model

3. Create the next analytic queries:

      1. Find a user who had the biggest amount of reservations. Return user name and user_id

      2. (Optional) Find a host who earned the biggest amount of money for the last month. Return hostname and host_id

      3. (Optional) Find a host with the best average rating. Return hostname and host_id

```


```mermaid
erDiagram
    user {
        User_ID int PK
        Name string
        Email string
    }

    host {
        Host_ID int PK
        Nickname str FK
        User_ID int FK
        %% Other attributes specific to Hosts
    }

    guest {
        Guest_ID int PK
        Nickname str FK
        User_ID int FK
        %% Other attributes specific to Guests
    }

    room {
        Room_ID int PK
        Host_ID int FK
    }

    room_description {
        Room_description_id int PK
        Room_ID int FK
        daily_price int
        Residents_amount int
        room_items JSON 
        %% Other attributes for the Room
    }

    room_items {
        room_item_id int PK
        Room_ID int FK
        room_item_name varchar(50)
        quantity int
        is_present bool
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
        daily_price int FK
        Final_price int
        Is_paid bool
        %% Other attributes for the Reservation
    }

    review {
        Review_ID int PK
        Guest_ID int FK
        Host_ID int FK
        Room_ID int FK
        room_items JSON
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
    guest ||--o| reservation:"Makes/Checks"
    guest ||--|| payment:"Makes"
    guest ||--o| review:"Makes"
    reservation ||--o| payment:"Requires"
    payment ||--|| room_description:"Contains price in"
    review }|--|| room_items:"Contains"
    room }|--o| review:"Has"
    room }|--o| reservation:"Has"
    room ||--|| room_description:"Has"
    room_description ||--|| room_items:"Contains"
    host ||--o| review:"Has"
```