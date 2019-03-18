import os
import sys
import csv
import json
import pprint

def main():
    print("start")
    
    filepath = os.path.dirname(__file__)

    removed_birth_date_path = os.path.join(os.path.join(filepath, 'csv'), 'removed_birth_date.csv')
    with open(removed_birth_date_path, 'r') as birth_date:
        birth_date_reader = csv.reader(birth_date)

        birth_date_path = os.path.join(os.path.join(filepath, 'data'), 'birth_date')

        for row in birth_date_reader:
            birth_year_path = os.path.join(birth_date_path, row[0])
            birth_month_path = os.path.join(birth_year_path, row[1])
            birth_day_path = os.path.join(birth_month_path, row[2])

            os.makedirs(birth_day_path, exist_ok=True)

            birth_time_path = os.path.join(birth_day_path, '{}.json'.format(row[3]))

            data = {
                "destiny": int(row[4])
            }

            with open(birth_time_path, 'w') as birth_time:
                json.dump(data, birth_time)
          
    print("end")

if __name__ == "__main__":
    main()