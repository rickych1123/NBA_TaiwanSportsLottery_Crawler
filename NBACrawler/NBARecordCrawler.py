import requests
import json
import sys
from SQLManager import SQLManager

def main():
    sqlManager = SQLManager()
    game_date = '2016-11-16'
    res = requests.get('http://tw.global.nba.com/stats2/scores/daily.json?countryCode=TW&dst=0&gameDate={}&locale=zh_TW&tz=%2B8'.format(game_date))
    res.encoding = 'utf-8'
    data = json.loads(res.text)
    #print(data['payload']['date']['games'])
    for game in data['payload']['date']['games']:
        sqlManager.update_game_data(game['awayTeam']['profile']['displayAbbr'],game['awayTeam']['score']['score'],game['homeTeam']['score']['score'],game_date)
        #print(game['awayTeam']['profile']['name'],game['awayTeam']['score']['score'],game['homeTeam']['profile']['name'],game['homeTeam']['score']['score'])
  
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))
