from player_reader import PlayerReader



class StatisticsService:
    def __init__(self, reader):
        self._reader = reader 

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        return [player for player in self._players if player.team == team_name]

    def top(self, how_many):
        # metodin käyttämä apufufunktio voidaan määritellä näin

        sorted_players = sorted(
            self._players,
            key=lambda player: player.points,
            reverse=True
        )
        return sorted_players[:how_many]
