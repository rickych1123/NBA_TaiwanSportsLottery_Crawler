import requests
from bs4 import BeautifulSoup as bs
import datetime
import pymysql
from distutils import sys
from GameData import GameData
from SQLManager import SQLManager

game_data = GameData()

def main():
    res = requests.get('http://www.fengyuncai.com/asp/nba.asp')
    res.encoding = 'utf-8'
    soup = bs(res.text, "html.parser")
    date = datetime.datetime.now().strftime("%Y-%m-%d") + "\n"
    sqlManager = SQLManager()

    data = ''
    k = 0
    for match in soup.select('#mytable tr'):
        k = k + 1
        if (k % 6 == 0 or k % 6 == 1 or k % 6 == 2 or k % 6 == 3):
            continue
        for i in range(len(match.select('th'))):
            print(match.select('th')[i].text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding), end=",")
            data += (match.select('th')[i].text + ",")
        print()
        data += "\n"
    
    resolve_data(data)
    demo = ''
    for i in range(len(game_data.away_team_list)):
        demo+=(game_data.away_team_list[i] + game_data.away_sprd_list[i] + game_data.home_team_list[i] + game_data.home_sprd_list[i] + game_data.over_under_list[i] + game_data.away_total_streak_list[i] + game_data.home_total_streak_list[i] + game_data.away_season_record_list[i] + game_data.home_season_record_list[i] + '\n')
        sqlManager.insert_game_data(game_data.away_team_list[i], game_data.home_team_list[i], game_data.away_sprd_list[i], game_data.home_sprd_list[i], game_data.over_under_list[i], game_data.away_total_streak_list[i], game_data.home_total_streak_list[i], game_data.away_season_record_list[i], game_data.home_season_record_list[i])
    print(demo.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
    #with open("C:\\Users\\admin\\Documents\\NBA\\NBA_Day1.csv", 'a',
    #encoding='utf-8') as csvFile:
    #    csvFile.write(demo)

def resolve_data(data):
    data_array = data.split(',')
    for i in range(len(data_array)):
        if(i % 22 == 0):
            if(data_array[i].strip() != ''):
                game_data.away_team_list.append(data_array[i].strip())
        if(i % 22 == 1):
            if(RepresentsFloat(data_array[i])):
                if(float(data_array[i]) < 0):
                    game_data.away_sprd_list.append(data_array[i])
                    game_data.home_sprd_list.append(data_array[i][1:])
                else:
                    game_data.over_under_list.append(data_array[i])
            else:
                 game_data.away_sprd_list.append('')
                 game_data.home_sprd_list.append('')
                 game_data.over_under_list.append('')
        if(i % 22 == 5):
            game_data.away_total_streak_list.append(data_array[i])
        if(i % 22 == 6):
            game_data.away_season_record_list.append(data_array[i])
        if(i % 22 == 11):
            if(data_array[i].strip() != ''):
                game_data.home_team_list.append(data_array[i].strip())
        if(i % 22 == 12):
             if(RepresentsFloat(data_array[i])):
                 if(float(data_array[i]) < 0):
                    game_data.home_sprd_list.append(data_array[i])
                    game_data.away_sprd_list.append(data_array[i][1:])
                 else:
                    game_data.over_under_list.append(data_array[i])
             #else:
                  #game_data.away_sprd_list.append('')
                  #game_data.home_sprd_list.append('')
                  #game_data.over_under_list.append('')
        if(i % 22 == 16):
            game_data.home_total_streak_list.append(data_array[i])
        if(i % 22 == 17):
            game_data.home_season_record_list.append(data_array[i])

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def RepresentsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    sys.exit(int(main() or 0))