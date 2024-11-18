import pandas as pd

off_passing = pd.read_html('https://www.nfl.com/stats/team-stats/', index_col=False)[0]
off_passing = off_passing.iloc[:, [0, 1, 3, 4, 5, 7]]
off_passing.Team = off_passing.Team.str.split()
off_passing.Team = [x[1] for x in off_passing.Team]
off_passing.sort_values(by=['Att'], ascending=False, inplace=True)
off_passing['Att Rank'] = off_passing['Att'].rank(method='min', ascending=False)
off_passing.sort_values(by=['Cmp %'], ascending=False, inplace=True)
off_passing['Cmp % Rank'] = off_passing['Cmp %'].rank(method='min', ascending=False)
off_passing.sort_values(by=['Yds/Att'], ascending=False, inplace=True)
off_passing['Yds/Att Rank'] = off_passing['Yds/Att'].rank(method='min', ascending=False)
off_passing.sort_values(by=['Pass Yds'], ascending=False, inplace=True)
off_passing['Pass Yds Rank'] = off_passing['Pass Yds'].rank(method='min', ascending=False)

off_rushing = pd.read_html('https://www.nfl.com/stats/team-stats/offense/rushing/2024/reg/all', index_col=False)[0]
off_rushing = off_rushing.iloc[:, [0, 1, 2, 3, 10]]
off_rushing.Team = off_rushing.Team.str.split()
off_rushing.Team = [x[1] for x in off_rushing.Team]
off_rushing.sort_values(by=['Att'], ascending=False, inplace=True)
off_rushing['Att Rank'] = off_rushing['Att'].rank(method='min', ascending=False)
off_rushing.sort_values(by=['Rush Yds'], ascending=False, inplace=True)
off_rushing['Rush Yds Rank'] = off_rushing['Rush Yds'].rank(method='min', ascending=False)
off_rushing.sort_values(by=['YPC'], ascending=False, inplace=True)
off_rushing['YPC Rank'] = off_rushing['YPC'].rank(method='min', ascending=False)

def_passing = pd.read_html('https://www.nfl.com/stats/team-stats/defense/passing/2024/reg/all', index_col=False)[0]
def_passing = def_passing.iloc[:, [0, 3, 4, 5, 7]]
def_passing.Team = def_passing.Team.str.split()
def_passing.Team = [x[1] for x in def_passing.Team]
def_passing.sort_values(by=['Cmp %'], ascending=True, inplace=True)
def_passing['Cmp % Rank'] = def_passing['Cmp %'].rank(method='min', ascending=True)
def_passing.sort_values(by=['Yds/Att'], ascending=True, inplace=True)
def_passing['Yds/Att Rank'] = def_passing['Yds/Att'].rank(method='min', ascending=True)
def_passing.sort_values(by=['Yds'], ascending=True, inplace=True)
def_passing['Yds Rank'] = def_passing['Yds'].rank(method='min', ascending=True)

def_rushing = pd.read_html('https://www.nfl.com/stats/team-stats/defense/rushing/2024/reg/all', index_col=False)[0]
def_rushing = def_rushing.iloc[:, [0, 2, 3, 10]]
def_rushing.Team = def_rushing.Team.str.split()
def_rushing.Team = [x[1] for x in def_rushing.Team]
def_rushing.sort_values(by=['Rush Yds'], ascending=True, inplace=True)
def_rushing['Rush Yds Rank'] = def_rushing['Rush Yds'].rank(method='min', ascending=True)
def_rushing.sort_values(by=['YPC'], ascending=True, inplace=True)
def_rushing['YPC Rank'] = def_rushing['YPC'].rank(method='min', ascending=True)


def matchup(team1, team2):
    print('')
    print('### ' + team1 + ' Rushing vs ' + team2 + ' Defense' + ' ###')
    att = int(off_rushing[off_rushing['Team'] == team1]['Att Rank'].iloc[0])
    rush_yds = int(off_rushing[off_rushing['Team'] == team1]['Rush Yds Rank'].iloc[0]) - int(def_rushing[def_rushing['Team'] == team2]['Rush Yds Rank'].iloc[0])
    ypc = int(off_rushing[off_rushing['Team'] == team1]['YPC Rank'].iloc[0]) - int(def_rushing[def_rushing['Team'] == team2]['YPC Rank'].iloc[0])
    fumble = int(off_rushing[off_rushing['Team'] == team1]['Rush FUM'].iloc[0])
    def_fumble = int(def_rushing[def_rushing['Team'] == team2]['Rush FUM'].iloc[0])
    print('Rush Attempts Rank: ' + str(att))
    print('Rush Yds Diff: ' + str(rush_yds))
    print('YPC Diff: ' + str(ypc))
    print('Fumbles: ' + str(fumble) + ', Forced Fumbles: ' + str(def_fumble))
    print('')
    print('### ' + team1 + ' Passing vs ' + team2 + ' Defense' ' ###')
    pass_att = int(off_passing[off_passing['Team'] == team1]['Att Rank'].iloc[0])
    pass_yds = int(off_passing[off_passing['Team'] == team1]['Pass Yds Rank'].iloc[0]) - int(def_passing[def_passing['Team'] == team2]['Yds Rank'].iloc[0])
    yds_per_att = int(off_passing[off_passing['Team'] == team1]['Yds/Att Rank'].iloc[0]) - int(def_passing[def_passing['Team'] == team2]['Yds/Att Rank'].iloc[0])
    comp_per = int(off_passing[off_passing['Team'] == team1]['Cmp % Rank'].iloc[0]) - int(def_passing[def_passing['Team'] == team2]['Cmp % Rank'].iloc[0])
    interceptions = int(off_passing[off_passing['Team'] == team1]['INT'].iloc[0])
    def_interceptions = int(def_passing[def_passing['Team'] == team2]['INT'].iloc[0])
    print('Pass Attempts Rank: ' + str(pass_att))
    print('Pass Yds Diff: ' + str(pass_yds))
    print('Yds Per Attempt Diff: ' + str(yds_per_att))
    print('Completion % Diff: ' + str(comp_per))
    print('Interceptions: ' + str(interceptions) + ', Forced Interceptions: ' + str(def_interceptions))
    print('')

    print('### ' + team2 + ' Rushing vs ' + team1 + ' Defense' + ' ###')
    att = int(off_rushing[off_rushing['Team'] == team2]['Att Rank'].iloc[0])
    rush_yds = int(off_rushing[off_rushing['Team'] == team2]['Rush Yds Rank'].iloc[0]) - int(def_rushing[def_rushing['Team'] == team1]['Rush Yds Rank'].iloc[0])
    ypc = int(off_rushing[off_rushing['Team'] == team2]['YPC Rank'].iloc[0]) - int(def_rushing[def_rushing['Team'] == team1]['YPC Rank'].iloc[0])
    fumble = int(off_rushing[off_rushing['Team'] == team2]['Rush FUM'].iloc[0])
    def_fumble = int(def_rushing[def_rushing['Team'] == team1]['Rush FUM'].iloc[0])
    print('Rush Attempts Rank: ' + str(att))
    print('Rush Yds Diff: ' + str(rush_yds))
    print('YPC Diff: ' + str(ypc))
    print('Fumbles: ' + str(fumble) + ', Forced Fumbles: ' + str(def_fumble))
    print('')
    print('### ' + team2 + ' Passing vs ' + team1 + ' Defense' ' ###')
    pass_att = int(off_passing[off_passing['Team'] == team2]['Att Rank'].iloc[0])
    pass_yds = int(off_passing[off_passing['Team'] == team2]['Pass Yds Rank'].iloc[0]) - int(def_passing[def_passing['Team'] == team1]['Yds Rank'].iloc[0])
    yds_per_att = int(off_passing[off_passing['Team'] == team2]['Yds/Att Rank'].iloc[0]) - int(def_passing[def_passing['Team'] == team1]['Yds/Att Rank'].iloc[0])
    comp_per = int(off_passing[off_passing['Team'] == team2]['Cmp % Rank'].iloc[0]) - int(def_passing[def_passing['Team'] == team1]['Cmp % Rank'].iloc[0])
    interceptions = int(off_passing[off_passing['Team'] == team2]['INT'].iloc[0])
    def_interceptions = int(def_passing[def_passing['Team'] == team1]['INT'].iloc[0])
    print('Pass Attempts Rank: ' + str(pass_att))
    print('Pass Yds Diff: ' + str(pass_yds))
    print('Yds Per Attempt Diff: ' + str(yds_per_att))
    print('Completion % Diff: ' + str(comp_per))
    print('Interceptions: ' + str(interceptions) + ', Forced Interceptions: ' + str(def_interceptions))

first_team = input('Team 1: ')
second_team = input('Team 2: ')
matchup(first_team, second_team)