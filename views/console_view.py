import os

class ConsoleView:
    def __init__(self, controller):
        self.controller = controller

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
        input("Presiona Enter para continuar...")

    def show_menu(self):
        self.clear_screen()
        print("╔═════════════════════════════════╗")
        print("║            MENÚ PRINCIPAL       ║")
        print("╠═════════════════════════════════╣")
        print("║ 1. Agregar equipo               ║")
        print("║ 2. Ver clasificación            ║")
        print("║ 3. Agregar partido              ║")
        print("║ 4. Ver partidos por fecha       ║")
        print("║ 5. Salir                        ║")
        print("╚═════════════════════════════════╝")

    def get_team_input(self):
        self.clear_screen()
        print("╔═════════════════════════════════╗")
        print("║        AGREGAR NUEVO EQUIPO     ║")
        print("╚═════════════════════════════════╝")
        team_name = input("Ingrese el nombre del equipo: ")
        return team_name

    def show_teams(self):
        teams = self.controller.teams.values()
        print("╔═════════════════════════════════╗")
        print("║         EQUIPOS REGISTRADOS     ║")
        print("╚═════════════════════════════════╝")
        for team in teams:
            print(f"- {team.name}")

    def get_match_input(self):
        self.clear_screen()
        self.show_teams()
        print("╔═════════════════════════════════╗")
        print("║        AGREGAR NUEVO PARTIDO    ║")
        print("╚═════════════════════════════════╝")
        team1 = input("Ingrese el nombre del equipo 1: ")
        team2 = input("Ingrese el nombre del equipo 2: ")        

        # Validar que el input ingresado sea de tipo numerico
        while True:
            try:
                score1 = int(input("Ingrese el resultado del equipo 1: "))
                score2 = int(input("Ingrese el resultado del equipo 2: "))
                break
            except ValueError:
                print("Error: Debe ingresar un valor numérico.")
        # Ingresar fecha del resultado        
        date = input("Ingrese la fecha del partido (dd/mm/yyyy): ")
        # Retornar datos
        return team1, team2, score1, score2, date
        

    def truncate_name(self, name, length=14):
        if len(name) > length:
            return name[:length - 3] + "..."
        return name

    def show_standings(self, standings):
        self.clear_screen()
        print("╔═══════════════════════════════════════════════════════════════════════════════════════════════╗")
        print("║                                            CLASIFICACIÓN                                      ║")
        print("╠═════╦════════════════╦══════╦═════╦═══════╦══════╦══════╦════════╦═════════╦══════════════════╣")
        print("║ Pos ║ Equipo         ║ Pts  ║ PJ  ║ PG    ║ PE   ║ PP   ║ GF     ║ GC      ║ Dif              ║")
        print("╠═════╬════════════════╬══════╬═════╬═══════╬══════╬══════╬════════╬═════════╬══════════════════╣")
        for i, team in enumerate(standings, start=1):
            truncated_name = self.truncate_name(team.name)
            print(f"║ {str(i).center(3)} │ {truncated_name.ljust(14)} │ {str(team.points).center(4)} │ {str(team.matches_played).center(3)} │ "
                  f"{str(team.wins).center(5)} │ {str(team.draws).center(4)} │ {str(team.losses).center(4)} │ "
                  f"{str(team.goals_for).center(6)} │ {str(team.goals_against).center(7)} │ {str(team.goal_difference).center(16)} ║")
            if i < len(standings):
                print("╠─────┼────────────────┼──────┼─────┼───────┼──────┼──────┼────────┼─────────┼──────────────────╣")
            else:
                print("╚═════╩════════════════╩══════╩═════╩═══════╩══════╩══════╩════════╩═════════╩══════════════════╝")
        self.pause()



    def show_matches_by_date(self, matches):
        self.clear_screen()
        print("╔═════════════════════════════════╗")
        print("║        PARTIDOS POR FECHA       ║")
        print("╚═════════════════════════════════╝")
        for match in matches:
            print(f"{match[4]}: {match[0]} vs {match[1]} - {match[2]}-{match[3]}")
        self.pause()

    def run(self):
        while True:
            self.show_menu()
            option = input("Ingrese una opción: ")
            if option == "1":
                team_name = self.get_team_input()
                self.controller.add_team(team_name)
                self.pause()
            elif option == "2":
                standings = self.controller.get_standings()  # Llamar al método correcto
                self.show_standings(standings)
            elif option == "3":
                team1, team2, score1, score2, date = self.get_match_input()
                self.controller.add_match(team1, team2, score1, score2, date)
                self.pause()
            elif option == "4":
                matches = self.controller.matches  # Usamos self.controller.matches
                self.show_matches_by_date(matches)
            elif option == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")
                self.pause()