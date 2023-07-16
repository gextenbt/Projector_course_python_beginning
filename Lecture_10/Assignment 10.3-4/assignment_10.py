import string
import random
import csv

# 1
"""
Write a program that:
- generates 26 text files named A.txt, B.txt, and so on up to Z.txt. 
- To each file append a random number between 1 and 100. 
- Create a summary file (summary.txt) that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98
"""

def create_ascii_num_files_and_summary():
    alphabet = string.ascii_uppercase
    summary_dict = dict()

    #Create ascii named files with random int inside
    for letter in alphabet:
        rand_num = random.randint(1, 100)
        file_name = f"{letter}.txt"

        with open(file_name, 'w') as f:
            f.write(f"{rand_num}")
        summary_dict[file_name] = rand_num

    #Create summary: file name - num
    with open("summary.txt", 'w') as f:
        for key, value in summary_dict.items():
            f.write(f'{key}: {value}\n')


# 2
"""
Create a file with some content.   
Create a second file and copy the content of the first file to the second file in upper case.
"""

def copy_paste_content():
    content = '''
                Lorem ipsum dolor sit amet, 
                consectetur adipiscing elit, 
                sed do eiusmod tempor incididunt 
                ut labore et dolore magna aliqua.'''

    with open("first_file.txt", 'w') as file_1:
        file_1.write(content)
    with open("first_file.txt", 'r') as file_1, open("second_file.txt", 'w') as file_2:
        data = (file_1.read()).upper()
        file_2.write(data)


# 3
'''
Write a program that will simulate user scores in a game. 
- Create a list with 5 players’ names 
- after that simulate 100 rounds for each player. 
- As a result of the game create a list with the player's name and score (0-1000 range). 
- Save it to a CSV file.  
      
The file should look like this:   
    Player name, Score  
    Josh, 56  
    Luke, 784  
    Kate, 90  
    Mark, 125  
    Mary, 877  
    Josh, 345  
    ...
'''

## Option 1
def player_genscore():

    import random
    players = [{'Player name':'John', 'Score':0},
                {'Player name':'George', 'Score':0},
                {'Player name':'Joel', 'Score':0},
                    {'Player name':'Joe', 'Score':0},
                    {'Player name':'Joster', 'Score':0}]

    for player in players:
        rand_start = random.uniform(0, 10)
        rand_end = random.uniform(rand_start, 10)
        for i in range(100): 
            rand_num = random.uniform(rand_start, rand_end)
            player['Score'] += rand_num
        player['Score'] = int(player['Score'])

    with open('players_score.csv', mode='w', newline="") as f:
        headers = ['Player name', 'Score']
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(players)


## Option 2 (Optional)
def random_weights_gen(quantity):
    # Take input time
    before_input = time.time()
    input_name = input("Input player name: ")
    after_input = time.time()
    # Take input time -> multiply to quantity of points to assure decimal part > quantity 
    random_num = int((after_input - before_input)*(100**quantity))
    # Turn random number into reversed string -> then return list of weights, name
    rand_weights_str = f"{random_num}"[-1:((-quantity)-2):-1]
    return input_name, [int(digit) for digit in rand_weights_str]

def player_genscore_2():
    players_quantity = int(input("Input quantity of players: "))
    rounds_quantity = int(input("Input quantity of rounds: "))
    max_score = int(input("Input maximum score: "))
    max_round_score = int(max_score / rounds_quantity)

    # players = [{'Player name':'John', 'Score':0},
    #             {'Player name':'George', 'Score':0},
    #             {'Player name':'Joel', 'Score':0},
    #                 {'Player name':'Joe', 'Score':0},
    #                 {'Player name':'Joster', 'Score':0}]

    round_points_range = [i for i in range(max_round_score+1)]

    with open('players_score_2.csv', mode='w', newline="") as f:
        headers = ['Player name', 'Score']
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for player in range(players_quantity):
            name, weights = random_weights_gen(max_round_score)
            points_list = random.choices(round_points_range, weights=weights, k=100)
            writer.writerow({'Player name': name, 'Score': sum(points_list)})

# 4
'''
Write a script that:
- reads the data from the previous CSV file (Task 3) 
- creates a new file called high_scores.csv where 
	- each row contains the player name and their highest score. 
	- The final score should be sorted by descending to the highest score.  
      
    The output CSV file should look like this:  
    Player name, Highest score  
    Kate, 907  
    Mary, 897  
    Luke, 784  
    Mark, 725  
    Josh, 345
'''
        
def sort_csv_file(filename: str):
    def get_score(player):
        return int(player['Score'])

    with open(filename, mode='r') as input_file, \
         open('highest_score.csv', mode='w', newline="") as output_file:
        
        reader = csv.DictReader(input_file)
        sorted_reader = sorted(reader, key=get_score, reverse=True)

        headers = ['Player name', 'Highest score']
        writer = csv.DictWriter(output_file, fieldnames=headers)
        writer.writeheader()
        for i in range(len(sorted_reader)):
            writer.writerow({'Player name': sorted_reader[i]['Player name'], 
                             'Highest score': sorted_reader[i]['Score']})

#################
# Changed code for Task 3-4

def player_genscore_changed():

    players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

    scores = []

    for player in players:
        for _ in range(100):
            score = random.randint(0, 1000)
            scores.append((player, score))

    # Save scores to a CSV file
    with open("game_scores_changed.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Player name", "Score"])
        writer.writerows(scores)

    print("Scores saved to game_scores.csv file.")

#####################
def sort_csv_file_changed(filename: str):
    # Read data from the previous CSV file
    scores = []
    with open("game_scores_changed.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            player = row[0]
            score = int(row[1])
            scores.append((player, score))

    # Sort scores in descending order based on highest score
    scores.sort(key=lambda x: x[1], reverse=True)

    # Get highest score for each player
    highest_scores = []
    players_seen = set()
    for player, score in scores:
        if player not in players_seen:
            highest_scores.append((player, score))
            players_seen.add(player)

    # Save highest scores to a new CSV file
    with open("high_scores_changed.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Player name", "Highest score"])
        writer.writerows(highest_scores)

    print("Highest scores saved to high_scores_changed.csv file.")


if __name__ == "__main__":
    # create_ascii_num_files_and_summary()
    # copy_paste_content()
    # player_genscore()
    # # player_genscore_2()
    # sort_csv_file('players_score.csv')

    #Task 3-4 - Changed code
    player_genscore_changed()
    sort_csv_file_changed('players_score_changed.csv')

    

    
