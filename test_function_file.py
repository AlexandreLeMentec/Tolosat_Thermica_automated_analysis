# the sole purpose of this file is to test things before implementing them in the main file
# it's not intended to stay in the final product

card_database = {}

def read_database():
    with open('database.csv', "r") as database:
        for line in database:
            info = line.split()
            card_database[info[0]] = [info[1], info[2], info[3]] # [thickness, dissipation, node]
    print(card_database)

read_database()