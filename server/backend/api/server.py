from typing import Optional

from fastapi import FastAPI

from sportsipy.nba.teams import Teams
from sportsipy.nba.boxscore import Boxscore
from sportsipy.nba.roster import Player, Roster

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'Test'}


@app.get('/teams')
def read_teams():
    teams = Teams(2018)

    for team in teams:
        schedule = team.schedule  # Returns a Schedule instance for each team
        # Returns a Pandas DataFrame of all metrics for all game Boxscores for
        # a season.
        df = team.schedule.dataframe_extended
    # team = Team(2018)
    # print(team)

    # team = Roster('HOU')
    # print(team)

    # player = Player('hardeja01')
    # print(player)

    # game_data = Boxscore('201806080CLE')
    # print(game_data.away_points)

    # teams = Teams(2018)

    # for team in teams:
    #     print(team.name)
