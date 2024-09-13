import os
import win32api
import win32gui
import webbrowser
import sys
import subprocess
import voice		
#import speech_recognition
import string
import requests
import geocoder
import glob
import pyautogui
import wikipediaapi
import time
import random
import queue
import sounddevice as sd
import vosk 
import json
import psutil
import platform
import keyboard
import ctypes
import winshell
#from main import * 
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from translate import Translator
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow


def setEngLayout():
    window_hadle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_hadle,0x0050,0,0x04090409)
    return(result)
"""Для работы в браузере"""
#открытие поискового окна браузера
def browser(par):
    try:
        webbrowser.open("https://www.google.com", new=2)
    except:
        voice.speaker("Ошибка при открытии браузера,попробуйте повторить запрос")
    finally:
        return

#РАБОТА С ВКЛАДКАМИ
def new_tab(data):
    try:
        setEngLayout()
        pyautogui.hotkey('ctrl','t')
    except:
        voice.speaker("При открытии вкладки произошла ошибка,попробуйте повторить запрос")
    finally:
        return
def tab_return(data):
    try:
        setEngLayout()
        pyautogui.hotkey('ctrl','shift','t')
    except:
        voice.speaker("Невозможно восстонавить вкладку,попробуйте повторить запрос")
    finally:     
        return
def close_tab(data):
    try: 
        setEngLayout()
        pyautogui.hotkey('ctrl','w')
    except:     
        voice.speaker('Невозможно закрыть вкладку,попробуйте повторить запрос')
    finally:     
        return
def print_page(data):
    try:
        setEngLayout()
        pyautogui.hotkey('ctrl','p')
    except:     
        voice.speaker('Печать недоступна,попробуйте повторить запрос')
    finally:     
        return
def back_tab(data):
    try:
        setEngLayout()
        pyautogui.hotkey('alt','left')
    except:     
        voice.speaker('Вернуться к прошлой вкладке невозможно,попробуйте повторить запрос')
    finally:     
        return
#РАБОТА С ВКЛАДКАМИ

#поиск в браузере
def search_google(data):
    try:
        search_list = data.split(" ")
        search_google_comand='+'.join(search_list)
        webbrowser.open(f'https://www.google.com/search?q={search_google_comand}')
    except:     
        voice.speaker('Поиск в браузере недоступен,попробуйте повторить запрос')
    finally:     
        return

#поиск видео в youtube
def search_youtube(search_data):
    try:
        search_list = search_data.split(" ")
        search_youtube_comand='+'.join(search_list)
        webbrowser.open(f'https://www.youtube.com/results?search_query={search_youtube_comand}')
    except:
        voice.speaker('Поиск в ютюбе невозможен,попробуйте повторить запрос')
    finally:
       return

#говорит и открывает погоду изходя из местоположения
def weather(par):
    try:
        #координаты пользоватея по ip
        def get_user_location():
            g = geocoder.ip('me') # определение геоданных на основе IP-адреса пользователя (может быть не всегда точным)
            location = g.latlng # получение координат пользователя
            return location 

        #перевод для корректной работы
        def translate_text(par):
            translator = Translator(from_lang="Russian", to_lang="English")
            result = translator.translate(par)
            return result

        #получаем из координат город
        def get_city_name(lat,lon):
            geolocator = Nominatim(user_agent="my_app")
            location = geolocator.reverse(f"{lat},{lon}")
            address = location.raw['address']
            city = address.get('city','')
            return city

        dataAll_list = []
        dataUse_list = []
        location = get_user_location()
        city = translate_text(get_city_name(location[0],location[1]))
        #print(city)

        url = f"https://yandex.com.am/weather/{city}"
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2526 Yowser/2.5 Safari/537.36',
                'referer':'https://www.google.com/'
        }
        #print(url)

        response = requests.get(url, headers=header)
        response = response.text
        bs = BeautifulSoup(response.encode("utf-8"), 'html.parser')

        webbrowser.open(url)

        #temperature = bs.find('span', 'temp__value temp__value_with-unit').text.strip()
        #wind_speed = bs.find('span', 'wind-speed').text.strip()
        light_day = bs.find("div","sun-card__day-duration-value").text.strip()
        dataAll_list=bs.findAll("div",class_="term__value")
        for data in dataAll_list:
            if data.find('span','temp__value temp__value_with-unit') is not None:
                if '+' in ''.join(dataUse_list):
                    continue
                dataUse_list.append(data.text)
            elif data.find('span', 'wind-speed') is not None:
                dataUse_list.append(data.text)
            elif data.find('i', class_="icon icon_pressure-white term__fact-icon") is not None:
                dataUse_list.append(data.text)
        voice.speaker(f"В {city}, температура {dataUse_list[0]} по цельсию, скорость ветра {dataUse_list[1]},атмосферное давление {dataUse_list[2]}, \
        световой день {light_day}")
    except:
        voice.speaker('Ошибка при полученни данных о погоде,попробуйте повторить запрос')
    finally:    
       return

#для поиска человека по ФИО или ФИ
def search_person_in_socialnetworks(data):
    """
    Поиск человека по базе данных социальных сетей 
    имя, фамилия TODO город
    """
    try:
        data = data.split()
        google_search_term = " ".join(data)
        print(data)
        
        vk_search_term = " ".join(data)
        print(vk_search_term)
        # открытие ссылки на поисковик в браузере
        url = "https://google.com/search?q=" + google_search_term
        webbrowser.open(url)

        # открытие ссылкок на поисковики социальных сетей в браузере
        vk_url = "https://vk.com/people/" + vk_search_term
        webbrowser.open(vk_url)
    except:
        voice.speaker('Ошибка при поиске человека,попробуйте повторить запрос')
    finally:
       return

#поиск в wikipedia
def search_wiki(data):
    try:
        search_list = data.split(" ")
        search_google_comand='_'.join(search_list)
        webbrowser.open(f'https://ru.wikipedia.org/wiki/{search_google_comand}')

        wiki_wiki = wikipediaapi.Wikipedia(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2526 Yowser/2.5 Safari/537.36',language='ru',extract_format=wikipediaapi.ExtractFormat.WIKI)

        p_wiki = wiki_wiki.page(data)
        strq = p_wiki.text
        str_list = strq.split(".")
        str_list = str_list[:3]
        strq = " ".join(str_list)
        voice.speaker(strq)
        #print(strq)
    except:
        voice.speaker('Ошибка при полученнии данных,попробуйте повторить запрос')
    finally:
       return

#перевод предложения от пользователя
def translate(data):
    try:
        data = data.split()
        data = " ".join(data)
        translator = Translator(from_lang="ru", to_lang="en")
        result = translator.translate(data)
        #Выводим информацию в консоль
        command = f'start cmd /k echo {result}'
        subprocess.call(command, shell=True)
        voice.speaker(result)
    except:
        voice.speaker('Перевод недоступен,попробуйте повторить запрос')
    finally:
       return 

#Проигровывание выбранной музыки или на вкус бота
def play_music(data):
    try:
        track_list = ['https://www.youtube.com/watch?v=1ypsYeX6efQ','https://www.youtube.com/watch?v=iRiXwbul_p0','https://www.youtube.com/watch?v=5vVwjSIixuQ','https://www.youtube.com/watch?v=m7lRTT_LuzQ','https://www.youtube.com/watch?v=6CTQtL4tZOk']
        if (data=='') or (data==' '):
            webbrowser.open(f'{random.choice(track_list)}')
            pyautogui.click(x=142,y =433,clicks=1,button='left')
        else:
            #data.split(" ")
            #data='%20'.join(data)
            data = data.replace(' ','%20')
            webbrowser.open(f'https://music.yandex.ru/search?text={data}')
            time.sleep(5)
            pyautogui.click(x=142,y =433,clicks=3,button='left')
    except:
        voice.speaker('При воиспроизведении музыки, произошла ошибка,попробуйте повторить запрос')
    finally:
       return

#Открытие почты
def mail_data(data):
    try:
        webbrowser.open("https://mail.yandex.ru/?uid=672069177#inbox")
    except:
        voice.speaker('Ошибка при открытии почты, попробуйте повторить запрос')
    finally:
       return

#Открытие окна для отправки писем на почте
def send_mail(data):
    try:
        webbrowser.open("https://mail.yandex.ru/?uid=672069177#compose",new=0)
    except:
        voice.speaker('Отправка писем недоступна, попробуйте повторить запрос')
    finally:
        return

#Новости из мира технологий
def news_read(data):
    try:
        url = f"https://habr.com/ru/news/"
        webbrowser.open('https://habr.com/ru/news/')
        response = requests.get(url)
        response = response.text
        bs = BeautifulSoup(response, 'html.parser')
        qwe = bs.findAll('a','tm-title__link')

        dataUse_list=[]

        for data in qwe: 
            if data.find('span',) is not None:
                dataUse_list.append(data.text)
        j=0
        for data in dataUse_list:
            #print(data)
            j+=1
            voice.speaker(f"Новость {j},{data}.")
            pyautogui.scroll(-870)
    except:
        voice.speaker('Ошибка при открытии новостей, попробуйте повторить запрос')
    finally:
       return

#Включает сайт с фильмотекой
def look_film(data):
    try:
        webbrowser.open("https://redheadsound.studio/")
    except:
        voice.speaker('Не удалось получить данные с фильмами, поробуйте повторить запрос')
    finally:
       return

#Включает сайт с мультипликацией
def look_mult(data):
    try:
        webbrowser.open("https://pro.multmania.club/")
    except:
        voice.speaker('Не удалось получить данные с фильмами, поробуйте повторить запрос')
    finally:
       return

#Поиск мест на карте
def search_place_map(data):
    try:
        data=data.split(" ")
        data="%20".join(data)
        webbrowser.open(f'https://yandex.ru/maps/213/moscow/search/{data}')
    except:
        voice.speaker('Ошибка во время поиска мест, повторите запрос')
    finally:
       return

#Поиск отелей
def search_hotel(data):
    try:
        webbrowser.open('https://travel.yandex.ru/hotels/search/')
    except:
        voice.speaker('База с отелями сейчас недоступна, повторите запрос')
    finally:
       return

#OPTIONS_YOUTUBE УПРАВЛЕНИЕ ПЛЕЕРОМ YOUTUBE
def play_youtube(data):
    try:
        setEngLayout()
        pyautogui.press('space')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def fullscreen_youtube(data):  
    try:
        setEngLayout()
        pyautogui.press('f')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def audio_play_youtube(data):
    try:
        setEngLayout()
        pyautogui.press('m')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def rewind_youtube_up(data):
    try:
        setEngLayout()
        pyautogui.press('l')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def rewind_youtube_down(data):
    try:
        setEngLayout()
        pyautogui.press('j')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def subtitels_youtube(data):
    try:
        setEngLayout()
        pyautogui.press('c')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def speed_up_youtube(data):
    try:
        setEngLayout()
        pyautogui.press('>')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def speed_down_youtube(data):
    try:
        setEngLayout()
        pyautogui.press('<')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def next_video_youtube(data):
    try:
        setEngLayout()
        pyautogui.hotkey('shift','n')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def rewind_youtube_percent(data):
    try:
        tuple_comand={'десять':'1','двадцать':'2','тридцать':'3','сорок':'4','пятьдесят':'5','шестьдесят':'6','семьдесят':'7','восемьдесят':'8','девяносто':'9',}
        for i in tuple_comand.keys():
            if i in data:
                pyautogui.press(tuple_comand[i])
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
def click_mouse(data):
    try:
        setEngLayout()
        x,y=pyautogui.position()
        pyautogui.click(x, y, clicks=1, button='left')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
#OPTIONS_YOUTUBE

#Управление курсора с помощью стрелочек
def navigation_cursor(data):
    try:
        setEngLayout()
        def on_key_press(event):
            x,y = pyautogui.position()
            if event.name == 'up':
                #x,y = pyautogui.position()
                pyautogui.moveTo(x, y-55)
            elif event.name == 'left':
                pyautogui.moveTo(x-55, y)
            elif event.name == 'right':
                pyautogui.moveTo(x+55, y)
            elif event.name == 'down':
                pyautogui.moveTo(x, y+55)
        keyboard.on_press(on_key_press)
        keyboard.wait('esc')
    except:
       voice.speaker('Управление курсором недоступно, повторите запрос')
    finally:
       return

#Ввод
def enter(data):
    try:
        setEngLayout()
        pyautogui.press('enter')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return

#Скриншот
def screenshot(data):
    try:
        setEngLayout()
        pyautogui.hotkey('shift','win','s')
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return

#скролит страницу вверх
def scroll_up(data):
    try:
        setEngLayout()
        pyautogui.PAUSE = 0.2
        pyautogui.scroll(720)
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return
#скролит страницу вниз
def scroll_down(data):
    try:
        setEngLayout()
        pyautogui.PAUSE = 0.2
        pyautogui.scroll(-720)
    except:
        voice.speaker('Непредвиденная ошибка, попробуйте ещё раз')
    finally:
       return


"""Для работы в ОС"""
#открытие игр, пока открывает только стим по умолчанию
def game(par):
    try:
        subprocess.Popen('C:\Program Files (x86)\Steam\steam.exe')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он.Повторите запрос')
    finally:
        return

#Выход из системы
def block_pc(data):
    try:
        ctypes.windll.user32.LockWorkStation()
    except:
        voice.speaker('При выходе из системы, произошла ошибка.Повторите запрос')
    finally:
        return

#Эта команда отключает ПК под управлением Windows
def offpc(par):
    try:
        os.system('shutdown /s')
    except:
        voice.speaker('При отключении пк, произошла ошибка. повторите  запрос')
    finally:
        return

#Перезапуск пк
def restart_pc(data):
    try:
        os.system('shutdown /r /f')
    except:
        voice.speaker('При перезапуске пк, произошла ошибка. повторите запрос')
    finally:
       return

#Очистка корзины
def clear_recycle_bin(data):
    try:   
        winshell.recycle_bin().empty(confirm=False,show_progress=False, sound=True)
    except:
        voice.speaker("Очистка невозможна, корзина пуста")
    finally:
        return

#выключает бота
def offBot(data):
    sys.exit()
   
#Открытие приложение из базы часто используемых
def open_app(data):
    try:
        base_data_app = {
        'стим':'C:\\Program Files (x86)\\Steam\\steam.exe',
        'с тим':'C:\\Program Files (x86)\\Steam\\steam.exe',
        'дискорд':'C:\\Users\\Admin\\AppData\\Local\\Discord\\app-1.0.9016\\Discord.exe',
        'дискомфорт':'C:\\Users\\Admin\\AppData\\Local\\Discord\\app-1.0.9016\\Discord.exe',
        'эскорт':'C:\\Users\\Admin\AppData\Local\\Discord\\app-1.0.9016\\Discord.exe',
        'дис':'C:\\Users\\Admin\\AppData\\Local\\Discord\\app-1.0.9015\\Discord.exe',
        'телеграмм':'D:\\repwindow\\Telegram Desktop\\Telegram.exe',
        'телегу':'D:\\repwindow\\Telegram Desktop\\Telegram.exe',
        'калькулятор':"",
        'вк':'',
        'вконтакте':'',
        'проводник':'',
        'документ ворд':'C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE',
        'документ':'C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE',
        'презентацию':'C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE',
        'презентации':'C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE',
        'павер поинт':'C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE',
        'эксель':'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE',
        'таблицу':'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE',
        'таблицы':'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE',
        'антивирус':'C:\\Program Files (x86)\\Kaspersky Lab\\Kaspersky 21.13\\avpui.exe',
        'вижуал студию':'D:\\prg\\Visual_Studio\\vs\\Common7\\IDE\\devenv.exe',
        'вижу студии':'D:\\prg\\Visual_Studio\\vs\\Common7\\IDE\\devenv.exe',
        'вижу студию':'D:\\prg\\Visual_Studio\\vs\\Common7\\IDE\\devenv.exe',
        'вижуал код':'D:\\prg\\VSCODEQ\\Microsoft VS Code\\Code.exe',
        'бежал код':'D:\\prg\\VSCODEQ\\Microsoft VS Code\\Code.exe',
        'майкрософт код':'D:\\prg\\VSCODEQ\\Microsoft VS Code\\Code.exe',
        'майкрософт студию':'D:\\prg\\Visual_Studio\\vs\\Common7\\IDE\\devenv.exe',
        '':'',
        '':'',
        '':'',
        '':'',
        '':'',
        '':'',
        '':'',
        '':'',
        }
        for i in base_data_app.keys():
            if i in data:
                if i == 'калькулятор':
                    subprocess.call('calc.exe')

                elif ('вк' in i) or ('вконтакте'in i):
                    webbrowser.open("https://vk.com/")

                elif ('проводник' in i):
                    subprocess.Popen('explorer')
                
                else:
                    full_path = base_data_app[i]
                    #print(full_path) 
                    subprocess.Popen(full_path,shell=True)
    except:
        voice.speaker('Ошибка при открытии приложения, попробуйте повторить запрос')
    finally:
       return

#Открытие файла на пк работает, только с ру названиями
def file_open(data):
    try:
        def translate_text(par):
            translator = Translator(from_lang="Russian", to_lang="English")
            result = translator.translate(par)
            return result
        def get_disklist(): 
            disk_list = []
            for c in string.ascii_uppercase:
                disk = c + ':'
                if os.path.isdir(disk):
                    disk_list.append(disk)
            return disk_list
        #data = voice.listen_comand()
        data_check = data
        list_data_ignored =['д','де','d','ц','це','c','на','диске','диск','диски','дэ','цэ',]
        data_use_file=data.split()

        for i in list_data_ignored:
            if i in data_use_file:
                data_use_file.remove(str(i))
            data = " ".join(data_use_file)

        if ('ц' in data_check) or ('це' in data_check )or('c'in data_check):
            voice.speaker("Ищу файл на диске Ц")
            for adress,dirs,files in os.walk('C:\\'):
                print(adress)
                for file in files:
                    if (fuzz.ratio(data,file))>=69:
                        full_path =os.path.join(adress,file)
                        print(full_path)
                        voice.speaker('Файл найден')
                        subprocess.Popen(['start','', full_path], shell=True)
                        break
        
        elif ('д' in data_check) or ('де' in data_check )or('d' in data_check ):
            voice.speaker("Ищу файл на диске Д")
            for adress,dirs,files in os.walk('D:\\'):
                print(adress)
                for file in files:
                    if (fuzz.ratio(data,file))>=69:
                        full_path =os.path.join(adress,file)
                        print(full_path)
                        voice.speaker('Файл найден')
                        subprocess.Popen(['start','', full_path], shell=True)
                        break
        else:
            print(":(")
            voice.speaker("Файл не найден")
    except:
        voice.speaker('Ошибка при открытии файла,повторите запрос')
    finally:
       return

#Получение некой информации о системе 
def get_info_pc(data):
    try:
        df = psutil.win_service_iter()
        dfq = []
        for i in df:
            dfq.append(i)

        dfv = "\n".join(map(str, dfq))
        my_system = platform.uname()
        data_read = []
        data_text = f"================================================\n\
        System: {my_system.system}\n\
        Node Name: {my_system.node}\n\
        Release: {my_system.release}\n\
        Version: {my_system.version}\n\
        Machine: {my_system.machine}\n\
        Processor: {my_system.processor}\n\
        \
        {os.name}\n\
        =================================================\n\
        CPU uptime\
        {psutil.cpu_times()}\n\
        \
        =================================================\n\
        current CPU utilization in percent\n\
        {psutil.cpu_percent()}\n\
        \
        =================================================\n\
        number of logical and physical processors\n\
        {psutil.cpu_count()}\n\
        \
        =================================================\n\
        different CPU statistics\n\
        {psutil.cpu_stats()}\n\
        \
        =================================================\n\
        CPU\n\
        {psutil.cpu_freq()}\n\
        \
        =================================================\n\
        average system load\n\
        {psutil.getloadavg()}\n\
        \
        =================================================\n\
        system boot time\n\
        {psutil.boot_time()}\n\
        \
        =================================================\n\
        statistics on system RAM memory utilization\n\
        {psutil.virtual_memory()}\n\
        \
        =================================================\n\
        SWAP usage statistics\n\
        {psutil.swap_memory()}\n\
        \
        =================================================\n\
        all mounted disk partitions\n\
        {psutil.disk_partitions()}\n\
        \
        =================================================\n\
        system-wide disk I/O statistics\n\
        {psutil.disk_io_counters()}\n\
        \
        =================================================\n\
        system-wide network I/O statistics\n\
        {psutil.net_io_counters()}\n\
        \
        =================================================\n\
        addresses associated with each network cardй\n\
        {psutil.net_if_addrs()}\n\
        \
        =================================================\n\
        information about each network card\n\
        {psutil.net_if_stats()}\n\
        \
        =================================================\n\
        list of currently running PIDs\n\
        {psutil.pids()}\n\
        \
        =================================================\n\
        battery status information\n\
        {psutil.sensors_battery()}\n\
        \
        =================================================\n\
        an iterator of instances of all Windows services\n\
        {dfv}"
        file_w = open('D:\lr\data_text.txt','w',encoding='utf-8')
        file_w.write(data_text)
        file_w.close

        result = " ".join(data_read)
        command = 'cmd /c start cmd /k type "data_text.txt"|chcp 65001'
        subprocess.call(command, shell=True)
    except:
        voice.speaker('Ошибка при анализе работы системы, попробуйте повторить запрос')
    finally:
       return

#создание заметок в файле, пока не используется
""" def create_task():
    voice.speaker("Чё добавить?")
    #Вызываем функцию сохраняем результат
    query = voice.listen_comand()
    with open('file.txt','a') as file:
        file.write(f'{query}\n')
    print(f'Заметка {query} успешно добавлена!')
    return voice.speaker(f'Заметка {query} успешно добавлена!')

def open_task():
    with open('file.txt','r') as file:
        task_read =file.read()
        file.close
        print(f'Список заметок\n{task_read}')
    return voice.speaker(f'Список заметок\n{task_read}')

def clear_task():
    with open('file.txt','w') as file:
        file.write("")
        print("Заметки успешно очищены!")
    return voice.speaker(f'Заметки успешно очищены!') """

def passive(par):
	'''Функция заглушка при простом диалоге с ботом'''
	pass
