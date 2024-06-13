import csv
import os
from models.team import Team

class MatchController:
    def __init__(self, data_file):
        self.data_file = data_file
        self.teams_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'teams.csv')  
        self.matches_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'matches.csv')  
        self.teams = self.load_teams()
        self.matches = self.load_matches()

    def load_teams(self):
        teams = {}
        try:
            with open(self.teams_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) > 0:  
                        team_name = row[0].strip().zfill(3)  
                        teams[team_name] = Team(team_name)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.teams_file}")
        return teams

    def load_matches(self):
        matches = []
        try:
            with open(self.matches_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) == 5:  
                        matches.append((row[0], row[1], int(row[2]), int(row[3]), row[4]))
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.matches_file}")
        return matches

    def add_team(self, team_name):
        if team_name in self.teams:
            print("Error: El equipo ya existe.")
            return
        self.teams[team_name] = Team(team_name)
        self.save_data()  # Guardar los cambios después de agregar el equipo

    def save_data(self):
        try:
            with open(self.teams_file, 'w', newline='') as file:
                writer = csv.writer(file)
                for team in self.teams.values():
                    writer.writerow([team.name])
            print("Datos de equipos guardados correctamente.")
        except IOError:
            print(f"Error al guardar los datos en {self.teams_file}")

    def save_matches(self):
        try:
            with open(self.matches_file, 'w', newline='') as file:
                writer = csv.writer(file)
                for match in self.matches:
                    writer.writerow(match)
            print("Datos de partidos guardados correctamente.")
        except IOError:
            print(f"Error al guardar los datos en {self.matches_file}")

    def get_standings(self):
        standings = sorted(self.teams.values(), key=lambda team: (-team.points, -team.goal_difference))
        return standings

    def add_match(self, team1, team2, score1, score2, date):
        if team1 not in self.teams or team2 not in self.teams:
            print("Error: Uno o ambos equipos no existen.")
            return
        team1_obj = self.teams[team1]
        team2_obj = self.teams[team2]
        team1_obj.matches_played += 1
        team2_obj.matches_played += 1
        if score1 > score2:
            team1_obj.wins += 1
            team2_obj.losses += 1
            team1_obj.points += 3
        elif score1 < score2:
            team2_obj.wins += 1
            team1_obj.losses += 1
            team2_obj.points += 3
        else:
            team1_obj.draws += 1
            team2_obj.draws += 1
            team1_obj.points += 1
            team2_obj.points += 1
        team1_obj.goals_for += score1
        team1_obj.goals_against += score2
        team2_obj.goals_for += score2
        team2_obj.goals_against += score1
        team1_obj.goal_difference = team1_obj.goals_for - team1_obj.goals_against
        team2_obj.goal_difference = team2_obj.goals_for - team2_obj.goals_against
        self.matches.append((team1, team2, score1, score2, date))
        self.save_data()  # Guardar los datos de equipos actualizados
        self.save_matches()  # Guardar el nuevo partido en matches.csv

