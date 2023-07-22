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
        Price int
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
        Amount int
        Is_paid bool
        %% Other attributes for the Reservation
    }

    review {
        Review_ID int PK
        Guest_ID int FK
        Host_ID int FK
        Room_ID int FK
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
    guest ||--o| payment:"Makes"
    guest ||--o| review:"Makes"
    reservation ||--o| payment:"Requires"
    room ||--o| review:"Has"
    room ||--o| reservation:"Has"
    host ||--o| review:"Has"