# the sole purpose of this file is to test things before implementing them in the main file
# it's not intended to stay in the final product

def read_database():
    with open("mission1_results\results.xls", "r") as database:
        for line in database:
            info = line.split()
            print(info)

read_database()