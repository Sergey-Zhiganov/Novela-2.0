import random
import json
import csv

def Chapter1():
    global g_data
    c_text = ['Ты оказался в темном лесу, окруженный древними деревьями. Перед тобой раздваивается тропа.',['Пойти налево', 'Пойти направо']]
    if g_data != c_text[0] and g_data != None:
        Chapter2()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter2()
    else:
        Chapter3()
def Chapter2():
    global g_data
    c_text = ['Ты идешь налево и через некоторое время выходишь к озеру. На берегу виднеется старый чёлн.',['Отправиться на чёлне по озеру','Продолжить идти вдоль берега']]
    if g_data != c_text[0] and g_data != None:
        Chapter3()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter4()
    else:
        Chapter5()
def Chapter3():
    global g_data
    c_text = ['Ты поворачиваешь направо и внезапно вижу светлое сияние вдалеке.',['Идти в сторону светила','Вернуться к предыдущей развилке']]
    if g_data != c_text[0] and g_data != None:
        Chapter4()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter6()
    else:
        Chapter7()
def Chapter4():
    global g_data
    c_text = ['Ты садишься в чёлн и начинаешь плавать по озеру. Вдалеке виднеется остров.',['Направиться к острову','Вернуться к берегу']]
    if g_data != c_text[0] and g_data != None:
        Chapter5()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter8()
    else:
        Chapter9()
def Chapter5():
    global g_data
    c_text = ['Ты продолжаешь идти вдоль берега и натыкаешься на древнюю пещеру.',['Зайти в пещеру','Продолжить путь вдоль берега']]
    if g_data != c_text[0] and g_data != None:
        Chapter6()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter10()
    else:
        Chapter11()
def Chapter6():
    global g_data
    c_text = ['Ты приближаешься к источнику светила и видишь загадочную фигуру.',['Подойти к фигуре','Вернуться к предыдущей развилке']]
    if g_data != c_text[0] and g_data != None:
        Chapter7()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter12()
    else:
        Chapter13()
def Chapter7():
    global g_data
    c_text = ['Ты возвращаешься к предыдущий развилке, где снова стоишь перед выбором.',['Пойти налево', 'Пойти направо']]
    if g_data != c_text[0] and g_data != None:
        Chapter8()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter2()
    else:
        Chapter3()
def Chapter8():
    global g_data
    c_text = ['Ты достигаешь острова и обнаруживаешь таинственный артефакт.',['Взять артефакт','Оставить артефакт']]
    if g_data != c_text[0] and g_data != None:
        Chapter9()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter14()
    else:
        Chapter15()
def Chapter9():
    global g_data
    c_text = ['Ты возвращаешься к берегу и продолжаешь свой путь по лесу.',['Идти глубже в лес','Вернуться на развилку']]
    if g_data != c_text[0] and g_data != None:
        Chapter10()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter16()
    else:
        Chapter7()
def Chapter10():
    global g_data
    c_text = ['Ты заходишь в пещеру и обнаруживаешь её таинственные тайны.',['Исследовать глубже','Выйти из пещеры']]
    if g_data != c_text[0] and g_data != None:
        Chapter11()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter17()
    else:
        Chapter18()
def Chapter11():
    global g_data
    c_text = ['Продолжая свой путь вдоль берега, ты натыкаешься на забытый храм.',['Зайти в храм','Продолжить свой путь']]
    if g_data != c_text[0] and g_data != None:
        Chapter12()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter19()
    else:
        Chapter20()
def Chapter12():
    global g_data
    c_text = ['Ты подходишь к фигуре и оказываешься перед древним мудрецом.',['Поговорить с мудрецом','Вернуться к предыдущей развилке']]
    if g_data != c_text[0] and g_data != None:
        Chapter13()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter21()
    else:
        Chapter22()
def Chapter13():
    global g_data
    c_text = ['Ты возвращаешься на предыдущий развилке, где снова стоишь перед выбором.',['Пойти налево','Пойти направо']]
    if g_data != c_text[0] and g_data != None:
        Chapter14()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter6()
    else:
        Chapter23()
def Chapter14():
    global g_data
    c_text = ['Ты берешь артефакт в руки и чувствуешь внутреннюю силу, но сразу же слышишь странные шепоты.',['Выкинуть артефакт','Сохранить артефакт']]
    if g_data != c_text[0] and g_data != None:
        Chapter16()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter24()
    else:
        Chapter25()
def Chapter15():
    Chapters('[Конец 1] Ты оставляешь артефакт на острове и продолжаешь свой путь, чувствуя себя легче. ')
    SaveCsv(1)
def Chapter16():
    global g_data
    c_text = ['Прогуливаясь глубже в лес, ты внезапно слышишь странные звуки.',['Пойти на звуки','Вернуться к предыдущей развилке']]
    if g_data != c_text[0] and g_data != None:
        Chapter17()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter26()
    else:
        Chapter27()
def Chapter17():
    global g_data
    c_text = ['Ты исследуешь глубины пещеры и находишь древние записи.',['Попытаться разгадать записи','Покинуть пещеру']]
    if g_data != c_text[0] and g_data != None:
        Chapter19()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter28()
    else:
        Chapter29()
def Chapter18():
    Chapters('[Конец 2] Ты покидаешь пещеру и возвращаешься в лес, забрав тайны c собой.')
    SaveCsv(2)
def Chapter19():
    global g_data
    c_text = ['Зайдя в храм, ты видишь алтарь с загадочным артефактом.',['Взять артефакт','Не трогать артефакт']]
    if g_data != c_text[0] and g_data != None:
        Chapter20()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter30()
    else:
        Chapter31()
def Chapter20():
    global g_data
    c_text = ['Продолжая путь, ты натыкаешься на старое дерево с множеством символов.',['Изучить символы','Продолжить свой путь']]
    if g_data != c_text[0] and g_data != None:
        Chapter22()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter32()
    else:
        Chapter33()
def Chapter21():
    Chapters('[Конец 3] Ты начинаешь разговаривать с мудрецом и получаешь мудрые советы.')
    SaveCsv(3)
def Chapter22():
    global g_data
    c_text = ['Ты решаешь вернуться на предыдущий развилке, где стоишь перед выбором.',['Пойти налево','Пойти направо']]
    if g_data != c_text[0] and g_data != None:
        Chapter23()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter12()
    else:
        Chapter23()
def Chapter23():
    global g_data
    c_text = ['Ты продолжаешь свой путь в лесу, и вдруг перед тобой возникает загадочная дверь.',['Открыть дверь','Продолжить свой путь']]
    if g_data != c_text[0] and g_data != None:
        Chapter26()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter34()
    else:
        Chapter35()
def Chapter24():
    Chapters('[Конец 4] Ты выкидываешь артефакт, и он исчезает в воде, как будто никогда не существовал.')
    SaveCsv(4)
def Chapter25():
    Chapters('[Конец 5] Ты сохраняешь артефакт и чувствуешь, как его сила остается с тобой.')
    SaveCsv(5)
def Chapter26():
    global g_data
    c_text = ['Ты идешь на звуки и обнаруживаешь скрытую поляну с сказочными существами.',['Взаимодействовать с существами','Покинуть поляну']]
    if g_data != c_text[0] and g_data != None:
        Chapter27()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter36()
    else:
        Chapter37()
def Chapter27():
    global g_data
    c_text = ['Ты решаешь вернуться к предыдущий развилке, где снова стоишь перед выбором.',['Пойти налево','Пойти направо']]
    if g_data != c_text[0] and g_data != None:
        Chapter30()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter16()
    else:
        Chapter38()
def Chapter28():
    Chapters('[Конец 6] Ты пытаешься разгадать записи и открываешь новые знания.')
    SaveCsv(6)
def Chapter29():
    Chapters('[Конец 7] Ты покидаешь пещеру, но знания остаются с тобой.')
    SaveCsv(7)
def Chapter30():
    global g_data
    c_text = ['Ты берешь артефакт с алтаря и почувствовал, как его сила заполняет тебя.',['Использовать артефакт','Оставить артефакт на месте']]
    if g_data != c_text[0] and g_data != None:
        Chapter34()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter39()
    else:
        Chapter40()
def Chapter31():
    Chapters('[Конец 8] Ты решаешь не трогать артефакт и продолжаешь свой путь в храме.')
    SaveCsv(8)
def Chapter32():
    Chapters('[Конец 9] Изучив символы, ты расшифровываешь древние предсказания.')
    SaveCsv(9)
def Chapter33():
    Chapters('[Конец 10] Проходя мимо дерева с символами, ты продолжаешь свой путь, ничего не понимая.')
    SaveCsv(10)
def Chapter34():
    global g_data
    c_text = ['Открыв дверь, ты оказываешься в загадочном коридоре.',['Идти по коридору','Вернуться к предыдущей развилке']]
    if g_data != c_text[0] and g_data != None:
        Chapter35()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter35()
    else:
        Chapter23()
def Chapter35():
    global g_data
    c_text = ['Ты возвращаешься на предыдущий развилке, где стоишь перед выбором.',['Пойти налево','Пойти направо']]
    if g_data != c_text[0] and g_data != None:
        Chapter37()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter34()
    else:
        Chapter40()
def Chapter36():
    Chapters('[Конец 11] Ты вступаешь в контакт с сказочными существами, и они рассказывают тебе истории этого леса, оставшиеся неведомыми для многих.')
    SaveCsv(11)
def Chapter37():
    global g_data
    c_text = ['Ты покидаешь поляну, но забираешь с собой воспоминания о встрече с чудесными существами.',['Вернуться к развилке','Пойти в глубь леса']]
    if g_data != c_text[0] and g_data != None:
        Chapter38()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter16()
    else:
        Chapter41()
def Chapter38():
    global g_data
    c_text = ['Ты продолжаешь свой путь и встречаешь древнего дракона, который спит у подножия горы.',['Подойти к дракону','Обойти его стороной']]
    if g_data != c_text[0] and g_data != None:
        Chapter39()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter42()
    else:
        Chapter43()
def Chapter39():
    global g_data
    c_text = ['Используя артефакт, ты открываешь портал в другой мир, полный новых приключений.',['Войти в портал','Остаться в этом мире']]
    if g_data != c_text[0] and g_data != None:
        Chapter41()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter44()
    else:
        Chapter45()
def Chapter40():
    Chapters('[Конец 12] Ты оставляешь артефакт на месте и чувствуешь, что принял правильное решение. Ты решаешь покинуть храм и продолжить свое путешествие.')
    SaveCsv(12)
def Chapter41():
    global g_data
    c_text = ['Глубже в лесу, ты находишь древний заброшенный город, который кажется забытым временем.',['Исследовать город','Вернуться к поляне со сказочными существами']]
    if g_data != c_text[0] and g_data != None:
        Chapter42()
    else:
        g_data = None
    number = Chapters(c_text)
    if number == 1:
        Chapter46()
    else:
        Chapter36()
def Chapter42():
    global g_data
    c_text = ['Подойдя к дракону, ты пытаешься разбудить его и завести разговор. (Выберите одну из цифр)',['Цифра 1','Цифра 2']]
    if g_data != c_text[0] and g_data != None:
        Chapter43()
    else:
        g_data = None
    number = Chapters(c_text)
    chance = random.randint(1, 2)
    if chance == number:
        Chapter47()
    else:
        Chapter48()
def Chapter43():
    global g_data
    c_text = ['Обходя дракона, ты находишь тайный вход в гору.',['Войти внутрь','Продолжить свой путь']]
    g_data = None
    if number == 1:
        Chapter49()
    else:
        Chapter50()
def Chapter44():
    Chapters('[Конец 13] Переступив порог портала, ты оказываешься в совершенно другом мире, где правят магия и чудеса.')
    SaveCsv(13)
def Chapter45():
    Chapters('[Конец 14] Оставаясь в этом мире, ты продолжаешь свои приключения, открывая для себя новые тайны и легенды.')
    SaveCsv(14)
def Chapter46():
    Chapters('[Конец 15] Исследуя заброшенный город, ты находишь дневник древних жителей, рассказывающих о загадочных событиях.')
    SaveCsv(15)
def Chapter47():
    Chapters('[Конец 16] Дракон просыпается и начинает рассказывать тебе истории древних времен, передаваемые из поколения в поколение.')
    SaveCsv(16)
def Chapter48():
    Chapters('[Конец 17] Дракон продолжает спать, поэтому ты решаешь уйти и продолжить свою дорогу в надежде найти новые приключения.')
    SaveCsv(17)
def Chapter49():
    Chapters('[Конец 18] Внутри горы ты обнаруживаешь систему пещер, которая ведет к подземному озеру с чистейшей водой.')
    SaveCsv(18)
def Chapter50():
    Chapters('[Конец 19] Продолжая свой путь, ты встречаешь старого путешественника, который рассказывает тебе о ближайших опасностях и дает советы, как их избежать.')
    SaveCsv(19)

def Input(text):
    try:
        choose = int(input('Ваш выбор: '))
    except:
        return None
    if choose == 0 and text[0] != "":
        Saves(text[0])
    if (choose > len(text[1]) or (choose < 1)):
        return None
    return choose

def Chapters(text):
    if len(text) != 2:
        print(text)
        return
    print(text[0])
    a = 1
    for i in text[1]:
        print(f'{a}. {i}')
        a += 1
    choose = None
    while choose == None:
        choose = Input(text)
    return choose

def Saves(text):
    global g_data
    g_data = None
    choose = 1
    while True:
        print("1. Вернуться в игру")
        print("2. Сделать сохранение")
        print("3. Открыть сохранения")
        choose = None
        while choose == None:
            choose = Input(["","aаa"])
        if choose == 1:
            return
        with open('saves.json','r', encoding='utf-8') as saves:
            saves = json.load(saves)
        a = 0
        if choose == 2:
            if text == None:
                print('Начните игру, чтобы сделать сохранение')
            else:
                for i in saves:
                    if i["name"] == user:
                        data = i["data"]
                        if text in data:
                            print("Такое сохранение уже есть")
                        else:
                            data.append(text)
                            saves[a]["data"] = data
                            with open('saves.json', 'w', encoding='utf-8') as save:
                                json.dump(saves, save, indent=4, ensure_ascii=False)
                            print('Сделано сохранение')
                    a += 1
        elif choose == 3:
            for i in saves:
                if i["name"] == user:
                    data = i["data"]
                    if len(data) > 0:
                        x = 0
                        for n in data:
                            x += 1
                            print(f'{x}. {n}')
                        choose = None
                        aa = 'a' * x
                        while choose == None:
                            choose = Input(["", aa])
                        print('1. Загрузить сохранение')
                        print('2. Удалить сохранение')
                        choose1 = None
                        while choose1 == None:
                            choose1 = Input(["", "aa"])
                        if choose1 == 1:
                            g_data = data[choose-1]
                            return
                        else:
                            del data[choose-1]
                            saves[a]["data"] = data
                            with open('saves.json', 'w', encoding='utf-8') as save:
                                json.dump(saves, save, indent=4, ensure_ascii=False)
                    else:
                        print('Сохраненй нет')
                a += 1

def SaveCsv(end):
    heads = ['name', 'ending']
    try:
        with open('endings.csv', 'x', newline='') as ending:
            ending = csv.DictWriter(ending, fieldnames=heads, delimiter=';')
            ending.writeheader()
    except:
        pass
    with open('endings.csv', 'a', encoding='cp1251', newline='') as ending:
        ending = csv.DictWriter(ending, fieldnames=heads, delimiter=';')
        ending.writerow({'name': user, 'ending': end})

print("Добро пожаловать в новеллу \"Путь Избранного\"\nЗдесь вам предстоит делать различные выборы, которые могут привести к различным развитиям событий")
print("В игре присутствуют сохранения. Для выхода в меню игры введите в процессе игры '0'")
user = str(input('\nВведите имя пользователя: '))
try:
    with open('saves.json','x'):
        pass
except:
    pass
try:
    with open('saves.json', 'r', encoding='utf-8') as saves:
        saves = json.load(saves)
    save_u = False
    for i in saves:
        if i["name"] == user:
            save_u = True
        if save_u == False:
            saves.append({"name": user, "data": []})
            with open('saves.json', 'w', encoding='utf-8') as save:
                json.dump(saves, save, indent=4, ensure_ascii=False)

except:
    with open('saves.json', 'w', encoding='utf-8') as saves:
        json.dump([{"name": user, "data": []}], saves, indent=4, ensure_ascii=False)
Saves(None)
Chapter1()