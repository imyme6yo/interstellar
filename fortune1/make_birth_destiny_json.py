import os
import sys
import csv
import json
import pprint

def main():
    print("start")
    
    filepath = os.path.dirname(__file__)

    birth_destiny_path = os.path.join(os.path.join(filepath, 'csv'), 'birth_destiny.csv')
    with open(birth_destiny_path, 'r') as birth_destiny:
        birth_destiny_reader = csv.reader(birth_destiny)

        birth_destiny_path = os.path.join(os.path.join(filepath, 'data'), 'birth_destiny')

        for row in birth_destiny_reader:
            birth_destiny_file = os.path.join(birth_destiny_path, '{}.json'.format(row[0]))

            data = {
                "destiny": row[1]
            }

            with open(birth_destiny_file, 'w') as birth_destiny_target:
                json.dump(data, birth_destiny_target)
          
    print("end")

if __name__ == "__main__":
    main()