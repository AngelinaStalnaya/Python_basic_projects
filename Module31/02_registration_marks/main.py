import re

if __name__ == '__main__':
    list_text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
    pattern_auto = r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,}\b'
    pattern_taxi = r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,}\b'

    print('Список номеров частных автомобилей: ', re.findall(pattern_auto, list_text))
    print('Список номеров такси: ', re.findall(pattern_taxi, list_text))
