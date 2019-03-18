import os
import sys
import csv
import pprint

def main():
    print("start")
    
    filepath = os.path.dirname(__file__)

    birth_date_path = os.path.join(os.path.join(filepath, 'csv'), 'birth_date.csv')
    with open(birth_date_path, 'r') as birth_date:
        birth_date_reader = csv.reader(birth_date)

        for row in birth_date_reader:
            if (int(row[4]) % 2) == 0:
                destiny_id = row[5]
                del row[4]
                removed_birth_date_path = os.path.join(os.path.join(filepath, 'csv'), 'removed_birth_date.csv')

                with open(removed_birth_date_path, 'a') as removed_birth_date:
                    removed_destiny_writer = csv.writer(removed_birth_date)
                    removed_destiny_writer.writerow(row)

    pp = pprint.PrettyPrinter(indent=4)

    print("end")
    pp.pprint(result)

if __name__ == "__main__":
    main()