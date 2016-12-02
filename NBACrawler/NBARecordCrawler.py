import requests
import json
import sys
from SQLManager import SQLManager
import datetime

def main():
    sqlManager = SQLManager()
    game_date = datetime.datetime.now().strftime("%Y-%m-%d")
    res = requests.get('http://tw.global.nba.com/stats2/scores/daily.json?countryCode=TW&dst=0&gameDate={}&locale=zh_TW&tz=%2B8'.format(game_date))
    res.encoding = 'utf-8'
    data = json.loads(res.text)
    #只取隊名前兩字ex.'塞爾'提克
    for game in data['payload']['date']['games']:
        sqlManager.update_game_data(game['awayTeam']['profile']['displayAbbr'][0 : 2],game['awayTeam']['score']['score'],game['homeTeam']['score']['score'],game_date)
  
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))
