# 1
"""
Create add method to add two countries together. 
- This method should create:
	- another country object with the name of the two countries combined 
	- and the population of the two countries added together.
"""


class Country:
    # adding custom attributes
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
    def add(self, other_country):
        comb_name = self.name + " " + other_country.name
        comb_population = self.population + other_country.population
        return Country(comb_name, comb_population)

        
bosnia = Country('Bosnia', 10_000_123)
herzegovina = Country('Herzegovina', 5_000_477)
bosnia_herzegovina = bosnia.add(herzegovina)

# 2

"""
Implement the previous method (Task 1) with a magic method 
"""

class mCountry:
    # Adding custom attributes
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
    
    # Magic method __add__
    def __add__(self, other_country):
        comb_name = self.name + " " + other_country.name
        comb_population = self.population + other_country.population
        return mCountry(comb_name, comb_population)


czech = mCountry('Czech', 10_000_000)
slovakia = mCountry('Slovakia', 5_000_000)
czech_slovakia = czech + slovakia

# Task 3
"""
Create a Car class with the following attributes: 
- brand
- model
- year
- speed

The Car class should have the following methods: 
- accelerate:
	- increase the speed by 5
- brake:
	- decrease the speed by 5.
- display_speed. 

Remember that the speed cannot be negative.
"""

class Car:
    # Adding custom attributes
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    # decrease the speed by 5.
    def brake(self):
        if (self.speed-5) < 0:
            self.speed = 0 
            return ValueError("Speed cannot be negative") 
        self.speed -= 5
    # increase the speed by 5
    def accelerate(self):
        self.speed += 5

    def display_speed(self):
        print(f"The current speed of the {self.brand} {self.model} is {self.speed} km/h")


# Test
#######
# car_1 = Car("Lada", "Riva", 1980, 7)
# print(car_1.model) # "Riva"
# print(car_1.speed) # "5"
# car_1.brake() 
# car_1.display_speed()
# car_1.brake()
# car_1.display_speed()
# car_1.accelerate()
# car_1.display_speed()
#######

# Task 4

"""
(Optional) Create a Robot class with the following attributes:
- orientation (left, right, up, down), 
- position_x, 
- position_y. 

The Robot class should have the following methods: 
- move:
	- take a number of steps -> move the robot in the direction it is currently facing.
- turn:
	- take a direction (left or right) and turn the robot in that direction
- display_position:
	- print the current position of the robot.
"""

class Robot:

    # Change orientation map
    ORIENTATION_TURNS = {
        "up": {"left": "left", "right": "right"},
        "left": {"left": "down", "right": "up"},
        "down": {"left": "right", "right": "left"},
        "right": {"left": "up", "right": "down"}
    }

    # Move with orientation map (x and y axis)
    ORIENTATION_MOVES = {
        "up": (0, 1),
        "down": (0, -1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    # Adding custom attributes
    def __init__(self, orientation: str, position_x: int, position_y: int,):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    # Move Robot with orientation (in the direction of x or y axis)
    def move(self, steps):
        # Assign tuple axis(x, y) to vars
        move_x, move_y = self.ORIENTATION_MOVES[self.orientation]
        # Calculate move with steps 
        self.position_x += steps * move_x
        self.position_y += steps * move_y

    # Change Robot orientation
    def turn(self, direction):
        self.orientation = self.ORIENTATION_TURNS[self.orientation][direction]

    # Display Robot Cartesian coordinates and orientation
    def display_position(self):
        print(f"Cartesian coordinates of the robot is ({self.position_x}, {self.position_y}). Orientation is {self.orientation}")


# Test
###
# robot_1 = Robot("left", 5, 4)
# robot_1.display_position()
# robot_1.move(3)
# robot_1.display_position()
# robot_1.turn("right")
# robot_1.display_position()
# robot_1.move(6)
# robot_1.display_position()
###

if __name__ == "__main__":
    pass
    # # Task 1
    # print(bosnia_herzegovina.population) # -> 15_000_600
    # print(bosnia_herzegovina.name) # -> 'Bosnia Herzegovina'

    # # Task 2
    # print(czech_slovakia.population) # -> 15_000_000
    # print(czech_slovakia.name) # -> 'Czech Slovakia'

    # Task 3
    # car_1 = Car("Lada", "Riva", 1980, 7)
    # car_1.brake() 
    # car_1.display_speed()
    # car_1.accelerate()
    # car_1.display_speed()

    # Task 4
    # robot_1 = Robot("left", 5, 4)
    # robot_1.display_position()
    # robot_1.move(3)
    # robot_1.display_position()
    # robot_1.turn("right")
    # robot_1.display_position()
    # robot_1.move(6)
    # robot_1.display_position()



    
    
