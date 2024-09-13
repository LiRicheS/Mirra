import pyttsx3		#pip install pyttsx3
import speech_recognition

#Инициализация голосового "движка" при старте программы
#
#Голос берется из системы, первый попавшийся

engine = pyttsx3.init()
engine.setProperty('voice', 135)	#скорость речи
engine.setProperty('volume',0.6)
engine.setProperty('pitch', 70)
def speaker(text):
	'''Озвучка текста'''
	engine.say(text)
	engine.runAndWait()








#Создаём объект класса, который представляет собой набор функций распознавания речи.
sr = speech_recognition.Recognizer()
#Время после которого текст будет принят, то есть если пауза между словами 0.5<=, фраза будет считаться принятой
sr.pause_threshold = 0.5
sr.phrase_threshold = 0.15

#Общая функция для прослушивания микрофона
def listen_comand():
    #Создаём объект класса Microphone, в контекстном менеджере ресурсов
    with speech_recognition.Microphone() as mic:
        #Контроль уровня шум + более точная калибровка микрофона балгодоря этому    
        sr.adjust_for_ambient_noise(source=mic,duration=0.5)
        try:
            #Запуск процесса прослушивания c сохранением в переменную query
            print("Слушаю...")
            speaker("Слушаю")
            audio = sr.listen(source=mic)#timeout=10)#phrase_time_limit=7)
        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return
        try:
            print("Выполняю запрос...")
            speaker("Выполняю запрос")
            query = sr.recognize_google(audio_data=audio,language='ru').lower()
            print(query)
        except speech_recognition.UnknownValueError:
            return 'Dawn...Не удалось распознать команду!'
        return query