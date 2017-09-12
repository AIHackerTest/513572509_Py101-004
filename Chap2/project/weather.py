# coding:utf-8

import requests


def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json',params = {
        'key': 'ra1uyjh2z3esaoj9',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout = 1)
    return result.json()


def show_weather(weather_dic):
    name = weather_dic['results'][0]['location']['name']
    text = weather_dic['results'][0]['now']['text']
    temp = weather_dic['results'][0]['now']['temperature']
    last_update = weather_dic['results'][0]['last_update'][:-6].replace('T', ' ')
    weather = f"""{name} 的天气为 {text}, 温度为 {temp} 度.
        \n更新时间: {last_update}\n"""
    return weather     
    

def play():
    history_list = []
    while True:
        try:
            user_city = input("请输入您要查询的城市： ")
            result = fetchWeather(user_city)
            user_weather = show_weather(result)
            print(user_weather)
            history_list.append(user_weather)
            
        except:
            if user_city in ['h','H','help','Help']:
                print('''
                    输入城市名，查询该城市的天气
                    输入h,H,help,Help其中的一个，查询帮助文档
                    输入history，获取查询历史
                    输入exit，或者quit，退出天气查询系统
                    ''')
            elif user_city == 'history':
                for history in history_list:
                    print(history)
            elif user_city in ['exit','quit']:
                print('已退出！')
                exit()
            else:
                print("城市不存在，输入help查看帮助")
            

play()













    
