from tennis import score_tennis
import pytest

@pytest.mark.parametrize("player1_points, player2_points, expected_score",
                         [ (0, 0, "Love-All"),
                           (1, 1, "Fifteen-All"),
                           (2, 2, "Thirty-All")])
def test_score_tennis(player1_points, player2_points, expected_score):
    assert score_tennis(player1_points, player2_points) == expected_score