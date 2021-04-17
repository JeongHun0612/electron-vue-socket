import datetime
from decimal import Decimal

pinnacle = [{"site": "피나클", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "승무패", "team1" : "A", "team2" : "B", "win" : "1.92", "draw" : "3.85", "lose" : "3.77"},
            {"site": "피나클", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.0", "team1" : "A", "team2" : "B", "win" : "1.45", "draw" : "0", "lose" : "2.85"},
            {"site": "피나클", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.25", "team1" : "A", "team2" : "B", "win" : "1.68", "draw" : "-0.25", "lose" : "2.25"},
            {"site": "피나클", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.5", "team1" : "A", "team2" : "B", "win" : "1.83", "draw" : "-0.5", "lose" : "1.88"},
            {"site": "피나클", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.75", "team1" : "A", "team2" : "B", "win" : "2.22", "draw" : "-0.75", "lose" : "1.68"},
            {"site": "피나클", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "오버/언더1", "team1" : "A", "team2" : "B", "win" : "1.85", "draw" : "1", "lose" : "1.92"},
            {"site": "피나클", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "오버/언더3", "team1" : "A", "team2" : "B", "win" : "1.88", "draw" : "3", "lose" : "1.93"}]

            
sbobet = [{"site": "스보뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "승무패", "team1" : "A", "team2" : "B", "win" : "1.88", "draw" : "3.88", "lose" : "3.65"},
            {"site": "스보뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.0", "team1" : "A", "team2" : "B", "win" : "1.48", "draw" : "0", "lose" : "2.76"},
            {"site": "스보뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.25", "team1" : "A", "team2" : "B", "win" : "1.65", "draw" : "-0.25", "lose" : "2.33"},
            {"site": "스보뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.5", "team1" : "A", "team2" : "B", "win" : "1.85", "draw" : "-0.5", "lose" : "1.99"},
            {"site": "스보뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.75", "team1" : "A", "team2" : "B", "win" : "2.28", "draw" : "-0.75", "lose" : "1.71"},
            {"site": "스보뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "오버/언더1", "team1" : "A", "team2" : "B", "win" : "1.90", "draw" : "1", "lose" : "1.92"},
            {"site": "스보뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "오버/언더3", "team1" : "A", "team2" : "B", "win" : "1.92", "draw" : "3", "lose" : "1.96"}]

                    
maxbet = [{"site": "맥스뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "승무패", "team1" : "A", "team2" : "B", "win" : "1.95", "draw" : "3.95", "lose" : "3.72"},
            {"site": "맥스뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.0", "team1" : "A", "team2" : "B", "win" : "1.49", "draw" : "0", "lose" : "2.81"},
            {"site": "맥스뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.25", "team1" : "A", "team2" : "B", "win" : "1.71", "draw" : "-0.25", "lose" : "2.24"},
            {"site": "맥스뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.5", "team1" : "A", "team2" : "B", "win" : "1.95", "draw" : "-0.5", "lose" : "1.92"},
            {"site": "맥스뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "핸디0.75", "team1" : "A", "team2" : "B", "win" : "2.25", "draw" : "-0.75", "lose" : "1.73"},
            {"site": "맥스뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "오버/언더1", "team1" : "A", "team2" : "B", "win" : "1.85", "draw" : "1", "lose" : "1.92"},
            {"site": "맥스뱃", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "오버/언더3", "team1" : "A", "team2" : "B", "win" : "1.96", "draw" : "3", "lose" : "1.91"}]


totime = [{"site": "토타임", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "승무패", "team1" : "A", "team2" : "B", "win" : "1.9", "draw" : "3.75", "lose" : "3.69"},
            {"site": "토타임", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "오버/언더1", "team1" : "A", "team2" : "B", "win" : "1.75", "draw" : "1", "lose" : "1.72"},
            {"site": "토타임", "sport": "축구", "league": "리그", "time": "2021-04-08 23:00", "type": "오버/언더3", "team1": "A", "team2": "B", "win": "1.83", "draw": "3", "lose": "1.93"}]
            
class SiteList():
    data = []
    def __init__(self):
        pass

    def get_all_data(self):
        return self.data

    def printDataList(self):
        for i in self.data:
            i.printData()
    
    def append_site(self, site_data):
        # self.site = data[0].get_site_name()
        # self.createdAt =  Decimal(datetime.datetime.now().timestamp())
        self.data = self.data + site_data    

    # 해외 데이터 중에 특정 타입을 주면 해당 타입의 모든 해외사이트 데이터를 반환하는 함수
    def get_overseas_data_by_game_type(self, game_type):
        site_betting_info = []
        game_data = sorted(self.data, key=lambda x: x.get_site_name()) 
        for i in game_data:
            # only overseas site !!
            site_list = ['스보뱃', '맥스뱃', '피나클']
            if not i.get_site_name() in site_list: 
                continue
            
            if i.get_game_type() == game_type:
                site_betting_info.append(i.get_betting_info())
        return site_betting_info

    def get_korea_data_by_game_data(self, game_data):
        site_betting_info = []
        game_data = sorted(self.data, key=lambda x: x.get_site_name()) 
        for i in game_data:
            # only overseas site !!
            site_list = ['스보뱃', '맥스뱃', '피나클']
            if i.get_site_name() in site_list: 
                continue
            
            site_betting_info.append({'site':i.get_site_name(), 'game_type': i.get_game_type(), 'bedang_list': i.get_betting_info()})
        return site_betting_info

    def split_by_game_type(self):
        return sorted(list(set([game_type.get_game_type() for game_type in self.data])))

    @classmethod
    def get_result_data_by_max_bedang_list(cls, max_bedang_list):
        def func1():
            winning = round(korean_win_bedang * betting_money)
            win_bet = round(winning / korean_win_bedang)
            lose_bet = round(winning / overseas_lose_bedang)
            draw_bet = round(winning / overseas_draw_bedang)
            total = win_bet + draw_bet + lose_bet
            result = winning - total
            return {'홈팀' : win_bet, '무': draw_bet, '원정' : lose_bet, '총액': total, '당첨': winning, '결과': result}
        def func2():
            winning = round(korean_win_bedang * betting_money)
            win_bet = round(winning / korean_win_bedang)
            lose_bet = round(winning / overseas_lose_bedang)
            draw_bet = round((winning - lose_bet)/3.95)
            total = win_bet + draw_bet + lose_bet
            result = winning - total
            return {'홈팀' : win_bet, '무': draw_bet, '원정' : lose_bet, '총액': total, '당첨': winning, '결과': result}
        def func3():
            winning = round(korean_win_bedang * betting_money)
            win_bet = round(winning / korean_win_bedang)
            lose_bet = round(winning / overseas_lose_bedang)
            draw_bet = round(((winning-lose_bet)/2)/3.95)
            total = win_bet + draw_bet + lose_bet
            result = winning - total
            return {'홈팀' : win_bet, '무': draw_bet, '원정' : lose_bet, '총액': total, '당첨': winning, '결과': result}
        def func4():
            winning = round(korean_win_bedang * betting_money)
            win_bet = round(winning / korean_win_bedang)
            lose_bet = round(winning / overseas_lose_bedang)
            draw_bet = 0
            total = win_bet + draw_bet + lose_bet
            result = winning - total
            return {'홈팀' : win_bet, '무': draw_bet, '원정' : lose_bet, '총액': total, '당첨': winning, '결과': result}
        def func5():
            winning = round(korean_win_bedang * betting_money)
            win_bet = round(winning / korean_win_bedang)
            lose_bet = round(winning / overseas_lose_bedang)
            draw_bet = 0
            total = win_bet + draw_bet + lose_bet
            result = winning - total
            return {'홈팀' : win_bet, '무': draw_bet, '원정' : lose_bet, '총액': total, '당첨': winning, '결과': result}
        def func6():
            winning = 0
            win_bet = 0
            lose_bet = 0
            draw_bet = 0
            total = 0
            result = 0
            return {'홈팀' : win_bet, '무': draw_bet, '원정' : lose_bet, '총액': total, '당첨': winning, '결과': result}
        def func7():
            winning = 0
            win_bet = 0
            lose_bet = 0
            draw_bet = 0
            total = 0
            result = 0
            return {'홈팀' : win_bet, '무': draw_bet, '원정' : lose_bet, '총액': total, '당첨': winning, '결과': result}

        result_data_list = []
        betting_money = 500000

        # draw 배팅률 
        overseas_win_bedang = float(i['max_bedang'][0][1:])
        overseas_draw_bedang = float(i['max_bedang'][1][1:])
        overseas_lose_bedang = float(i['max_bedang'][2][1:])

        korean_win_bedang = float(korean_bedang_list[0]['bedang_list'][0])
        korean_draw_bedang = float(korean_bedang_list[0]['bedang_list'][1])
        korean_lose_bedang = float(korean_bedang_list[0]['bedang_list'][2])

        function_list = {'승무패': func1, '핸디0.0': func2, '핸디0.25': func3, '핸디0.5':func4, '핸디0.75':func5, '오버/언더1' : func6, '오버/언더3' : func7}

        result_data_list.append({'game_type': i['game_type'], 'result_data': function_list[i['game_type']]()})

        return result_data_list

    @classmethod
    def get_max_bedang(cls, bedang_list):
        max_bedang_list_tmp = []
        for i in bedang_list:
            max_value_list= [0.0, 0.0, 0.0]
            max_value_site_list = ['','','']
            bedang = i['bedang_list']
            for j in bedang: 
                for idx, k in enumerate(j):
                    float_value = float(k[1:])
                    if float_value > max_value_list[idx]:
                        max_value_list[idx] = float_value
                        max_value_site_list[idx] = k[0]
            max_value_list = list(map(lambda x, y: x+str(y), max_value_site_list, max_value_list))
            max_bedang_list_tmp.append({'game_type':i['game_type'], 'max_bedang':max_value_list})
        return max_bedang_list_tmp

    # @classmethod
    # def 

class Site():
    def __init__(self, site, sport, league, time, game_type, team1, team2, win, draw, lose):
        self.site = site
        self.sport = sport
        self.league = league
        self.time = time
        self.game_type = game_type
        self.team1 = team1
        self.team2 = team2
        self.win = win
        self.draw = draw
        self.lose = lose

    def get_site_name(self):
        return self.site

    def get_game_type(self):
        return self.game_type
    
    def get_betting_info(self):
        if self.site == '스보뱃':
            return ('S'+self.win, 'S'+self.draw, 'S'+self.lose)
        elif self.site == '맥스뱃':
            return ('M'+self.win, 'M'+self.draw, 'M'+self.lose)
        elif self.site == '피나클':
            return ('P'+self.win, 'P'+self.draw, 'P'+self.lose)
        return (self.win, self.draw, self.lose)

    def printData(self):
        print(self.site, self.sport, self.league, self.time, self.game_type, self.team1, self.team2, self.win, self.draw, self.lose)

def init_data(data):
    class_data = []
    for i in data:
        # site, sport, league, time, type, team1, team2, win, draw, lose
        class_data.append(Site(i['site'], i['sport'], i['league'], i['time'], i['type'], i['team1'], i['team2'], i['win'], i['draw'], i['lose']))
    return class_data
    

if __name__ == '__main__':
    pinnacle_site = init_data(pinnacle)
    sbobet_site = init_data(sbobet)
    maxbet_site = init_data(maxbet)
    totime_site = init_data(totime)
    
    site_list = SiteList()
    site_list.append_site(sbobet_site)
    site_list.append_site(maxbet_site)
    site_list.append_site(pinnacle_site)
    site_list.append_site(totime_site)

    site_list.printDataList()

    game_type_list = site_list.split_by_game_type()

    overseas_bedang_list = []
    for game_type in game_type_list:
        overseas_bedang_list.append({'game_type': game_type, 'bedang_list':site_list.get_overseas_data_by_game_type(game_type)})

    korean_bedang_list = site_list.get_korea_data_by_game_data(site_list.get_all_data())

    # for i in korean_bedang_list:
    #     print(i)

    # for i in bedang_list:
    #     print(i)

    overseas_max_bedang_list = site_list.get_max_bedang(overseas_bedang_list)

    betting_caculator_result = []
    for i in overseas_max_bedang_list:
        print(i)
        betting_caculator_result.append(site_list.get_result_data_by_max_bedang_list(i))

    for i in betting_caculator_result:
        print(i)