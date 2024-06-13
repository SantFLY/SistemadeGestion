class Team:
    def __init__(self, name):
        self.name = name
        self.matches_played = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0
        self.goals_for = 0
        self.goals_against = 0
        self.goal_difference = 0

    def __str__(self):
        return f"{self.name} - Puntos: {self.points}, PJ: {self.matches_played}, G: {self.wins}, E: {self.draws}, P: {self.losses}, GF: {self.goals_for}, GC: {self.goals_against}, DG: {self.goal_difference}"
