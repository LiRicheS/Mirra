import threading
import sys
import pyttsx3
import json
import random
import queue
import sounddevice as sd
import vosk 
#json Так как vosk обрабатывает инфо с микрофона в виде json кода
#Наши триггеры-фраз для бота
import words
from words import data_set 
"""Для машиного обучения. """
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
#Импорт функций
from skills import *
import voice
import PySide6
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow

#from PySide6.QtCore import QTimer, QCoreApplication

from ui_py.main_window import Ui_MainWindow
from ui_py.info_instruction import Ui_Dialog

work = True
class Mira(QMainWindow,Ui_MainWindow,threading.Thread):
    def __init__(self):
        super(Mira,self).__init__()
        #self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.info.clicked.connect(self.open_info_window)
        
        self.clear_poleList.pressed.connect(self.clear_List)
        ####
        self.mic_on.pressed.connect(self.start_thread_assist )
        self.mic_off.pressed.connect(self.off)
        ####
        
    
    def open_info_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

      # Вызываем функцию снова через 3 секунды
    
    def clear_List(self):
        self.listWidget.clear()

    
    def off(self):
        global work
        work = False
        os._exit(0) 
        

    def main(self):
        global work
        work = True
        while work:
            try:
                self.listen()
            except:
                pass

    def start_thread_assist(self):
        thread = threading.Thread(target=self.main, args=())
        thread.start()

    def listen(self):
        #Обрабатываем полученный запрос, запускается в main() в цикле
        def recognize(data,vectorizer,clf):
            #Проверяем называли ли имя бота {intersection}->Найти общие элементы для множества и последовательности. То есть есть ли в {data} имя нашего бота из {TRIGGERS}.
            trg = words.TRIGGERS.intersection(data.split())
            if not trg:
                #Если нет то, функция прекращает свою работу 
                return
            """Если есть, то мы удаляем имя бота, упрощения распознования. в {text_vector} наш запрос обрабатывается в вектор,после этого в {answer} формируется
            самый подходящий ответ на данный вектор,то есть на что из words будет максимально похожа фраза сказанная пользователем, то нам и вернеться """
            data=data.replace(list(trg)[0],'')
            search_data=''
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeft)
            item.setText('Вы сказали :' + '\n' + data)
            self.listWidget.addItem(item)
            #print("ЭТО ТЫ СКАЗАЛ: "+data)
            for i in data_set.keys():
                if i in data:
                    search_data = data.replace(i,'')
                    break
                #print("ДАННЫЕ ДЛЯ ПОИСКА: "+search_data)
                
            text_vector = vectorizer.transform([data]).toarray()[0]
            answer = clf.predict([text_vector])[0]
            """Получаем имя функции получая первое слово из значений в words,далее озвучиваем ответ бота без функции."""
            func_name=answer.split()[0]
            voice.speaker(answer.replace(func_name,''))
            #Метод exec () в Python выполняет динамически созданную программу, которая является либо строкой, либо объектом кода. 
            exec(func_name+ '(search_data)')
            

        #Позволяет создать контейнер который позволяет создать очередь из неких данных
        q = queue.Queue()

        #Добавляем скаченную модель vosk
        model = vosk.Model('model_small')

        #Получаем список устройств вход\выход по умолчанию
        device = sd.default.device
        #Узнаём default чистоту дискридетации у устройств по умолчанию на вход
        samplerate = int(sd.query_devices(device,'input')['default_samplerate'])

        #Как только поток накопит blocksize, то ему их нужно куда-то записать и он их записывает в callback
        def callback(indata, frames, time, status):
        #Добавить конвертированные в байты данные из сэмплов из blocksize 
            q.put(bytes(indata))

        """Для машиного обучения. Здесь создаем объект CountVectorizer, вызываем его метод fit_transform,в который передаём список состоящий из ключей(примеры фраз для бота)
        из словаря words. Данный метод их хэширует(находит закономерности между ключами(чем схожи)и строит на их принципе векторы(матрицу цифр))и при дальнейшей обработке
        их хэши будут совпадать"""
        vectorizer = CountVectorizer()
        vectors = vectorizer.fit_transform(list(words.data_set.keys()))

        """Мы обработали наши ключи и записали их в {vectors},далее мы вызываем объект LogisticRegression и его метод fit. В него мы передаем наши ключи
        и список значений(возможные ответы бота) и он сопаставляет такой то вектор такая то фраза"""
        clf = LogisticRegression()
        clf.fit(vectors, list(words.data_set.values()))

        #удаляем словарь из оперативки, просто шоб не мешал
        del words.data_set

        """Создаётся поток безостановочной прослушки данных, samplerate ->Сколько раз в сек микрофон слушает уровень шума,blocksize->Сколько сэмплов за раз поток
        поток будет отдавать на обработку(усл в samplerate 48000, он 16000 отдаст на обработку)device->Устройство с которого слушаем, callback ->Как только поток накопит
        blocksize, то ему их нужно куда-то записать и он их записывает в callback
        """
        with sd.RawInputStream(samplerate=samplerate, blocksize = 16000, device=device, dtype="int16", 
                            channels=1, callback=callback):
            #Обработка распознования потока
            rec = vosk.KaldiRecognizer(model, samplerate)

            while True:
                #Принимает поступившие данные сэмплов
                data = q.get()
                #Если прием данных прикрашается(тишина, пользователь молчит)
                if rec.AcceptWaveform(data):
                    #В переменную мы получаем конечное значение после тишины, по ключу 'text'
                    data = json.loads(rec.Result())['text']
                    recognize(data,vectorizer,clf)
                    #Обрабатываем полученный запрос, запускается в main() в цикле

        











    

        


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mira()
    window.show()
    sys.exit(app.exec())