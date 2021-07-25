import bs4
import requests
import time

f=open('slova.txt','w',encoding='UTF-8')
s='''Абу Бар Ван Гам Дар Евл Жан Зай Иве Кан Лал Мак Най Обу Пас Рай Сан Так Уде Фак Хак Цар Чар Шап Щед Эвр Юди Ягу Ада Без Вве Гек Дел Его Жев Зан Идо Кас Лас Мар Нат Ожи Пер Рац Сев Тва Уим Фед Хар Цви Чел Шва Щеп Эйф Юли Яко Акт Бер Вес Геф Дец Ежо Жен Зах Ико Ким Лег Мау Ней Оку Пис Рел Сет Тер Улм Фид Хат Цен Чер Шен Щер Экт Юнг Яку Алт Бит Вин Гно Дин Ели Жиг Зее Имп Кож Леп Мер Нет Опо Плу Рич Ско Тих Уни Фин Хим Цер Чес Шин Щит Эли Юри Ямб Анд Бол Вла Гон Дов Епи Жир Зен Инт Кон Лин Мим Нил Орн Пор Рой Сод Топ Урб Фок Хок Циг Чиж Шма Щук Энг Юрк Яно Апп Боя Вок Гра Дор Еро Жуа Зин Иос Кра Лов Мож Нов Осл Пре Рот Спе Три Урю Фоф Хоп Цин Чка Шта Щуч Эпо Юрь Яро Арх Бул Вос Гру Дув Ест Жуп Зом Исм Кря Лук Мот Ном Отк Пуг Рут Стр Тум Утр Фро Хре Цна Чум Шув Щёг Эсс Юсу Яст'''
mas=s.split(' ')
z=0
for x in mas:
    try:
        f2=open('stop.txt','a',encoding='UTF-8')
        print(x)
        f2.write(x+'\n')
        f2.close()
        url='https://ru.wiktionary.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8/ru&from='+x
        #print(url)
        s=requests.get(url)
        b=bs4.BeautifulSoup(s.text, "html.parser")
        p=b.select('.CategoryTreeItem a')
        for x in p:
            ctg=(x.text.replace('/ru','').lower())
            url2=('https://ru.wiktionary.org/'+x.get('href'))
            s2=requests.get(url2)
            if(s2.status_code!=200):
                print('WARNING!')
            b2=bs4.BeautifulSoup(s2.text, "html.parser")
            p2=b2.select('.mw-content-ltr li a')
            for x2 in p2:
                wrd=(x2.text.replace('/ru','').lower())
                f.write(wrd+'|'+ctg+'\n')
                print(z)
                z=z+1
                #print(x.get('href'))
    except:
        time.sleep(5)
f.close()
        


    
