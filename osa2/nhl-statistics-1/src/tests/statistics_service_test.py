import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_existing_player(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.points, 124)

    def test_search_returns_none_if_player_not_found(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_returns_all_players_from_same_team(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertTrue(all(p.team == "EDM" for p in edm_players))

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)

    def test_top_returns_players_sorted_by_points_descending(self):
        top_players = self.stats.top(3)
        self.assertTrue(all(top_players[i].points >= top_players[i+1].points
                            for i in range(len(top_players) - 1)))

    def test_top_includes_highest_point_player_first(self):
        top_player = self.stats.top(1)[0]
        self.assertEqual(top_player.name, "Gretzky")
