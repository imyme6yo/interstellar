import os
import sys
import csv
import pprint

def main():
    result = []
    print("start")
    
    filepath = os.path.dirname(__file__)

    birth_date_path = os.path.join(os.path.join(filepath, 'csv'), 'birth_date.csv')
    with open(birth_date_path, 'r') as birth_date:
        birth_date_reader = csv.reader(birth_date)

        destiny_id = -1
        prev_row = None
        for row in birth_date_reader:

            if (int(row[4]) % 2) == 0:
                destiny_id = row[5]
                prev_row = row[:4]
            else:
                if prev_row == row[:4]:
                    if destiny_id == row[5]:
                        pass
                    else:
                        result.append((prev_row, row[:4]))

    pp = pprint.PrettyPrinter(indent=4)

    print("end")
    pp.pprint(result)
    print(idx)

if __name__ == "__main__":
    main()