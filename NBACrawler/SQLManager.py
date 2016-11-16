import pymysql
import datetime
class SQLManager():
    def insert_game_date(self, away_team, home_team, away_sprd, home_sprd, over_under, away_total_streak, home_total_steak, away_season_record, home_season_record):
        game_date = datetime.datetime.now() + datetime.timedelta(days=1)
         # Open database connection
        db = pymysql.connect("localhost", "root", "", "nba_game_data",charset='utf8')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Prepare SQL query to INSERT a record into the database.
        sql = """REPLACE INTO GAME(AWAY_TEAM_NAME, 
               HOME_TEAM_NAME, AWAY_TEAM_SPRD, HOME_TEAM_SPRD, OVER_UNDER, AWAY_TEAM_TOTAL_STREAK, 
               HOME_TEAM_TOTAL_STREAK, AWAY_SEASON_RECORD, HOME_SEASON_RECORD, GAME_DATE) 
               VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format \
               (away_team, home_team, away_sprd, home_sprd,over_under, away_total_streak, 
                 home_total_steak, away_season_record, home_season_record, game_date.strftime("%Y-%m-%d"))
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except Exception as err:
           print(err)
           # Rollback in case there is any error
           db.rollback()

        # disconnect from server
        db.close()

#sqlManager = SQLManager()
#sqlManager.insert_game_date('國王','熱火','5','-5','200.5','3連勝','2連勝','5-4 (客場 3-3)','3-5 (主場 2-2)')

