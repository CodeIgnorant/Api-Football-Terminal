# data_processing.py

from modules.fixtures import process_fixture_data
from modules.secondhalf_score import calculate_secondhalf_scores
from modules.result import calculate_match_result
from modules.total_goals import calculate_total_goals
from modules.over_under import calculate_over_under
from modules.goal_range import calculate_goal_range
from modules.both_team_score import calculate_both_team_score

def process_all_data(fixtures, season_year):
    """
    Process all data for fixtures by applying various calculations.
    :param fixtures: List of fixture data.
    :param season_year: Season year for fixtures.
    :return: Processed DataFrame with all calculations.
    """
    df = process_fixture_data(fixtures, season_year)
    df = calculate_secondhalf_scores(df)
    df = calculate_match_result(df)
    df = calculate_total_goals(df)
    df = calculate_over_under(df)
    df = calculate_goal_range(df)
    df = calculate_both_team_score(df)

    return df