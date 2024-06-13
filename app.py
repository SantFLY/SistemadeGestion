import os
from controllers.match_controller import MatchController
from views.console_view import ConsoleView
import csv

def main():
    current_dir = os.path.dirname(__file__)
    data_file = os.path.join(current_dir, 'data', 'teams.csv')

    if not os.path.isfile(data_file):
        print(f"Error: File '{data_file}' not found.")
        return

 
    teams = []
    with open(data_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            teams.append(row)

    controller = MatchController(teams)
    view = ConsoleView(controller)
    view.run()

if __name__ == '__main__':
    main()