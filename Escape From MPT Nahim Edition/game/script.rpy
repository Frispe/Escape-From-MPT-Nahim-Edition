# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gg = Character('[ggname]', color="#e4b10c")
define erik = Character("Эрик", color = "#234786")
define gorv = Character("Гор Варданян", color = "#11b34c")
define gord = Character("Гор Давтян", color = "#12c1ca")
define pythn = Character("Python", color = "#ff0000ff")
define kluch = False
define udl = False
define kod = False
#Музыка
define audio.metro = "audio/metro.mp3"
define audio.train = "audio/train.mp3"
define audio.horror = "audio/horror.mp3"
define audio.horror2 = "audio/horror2.mp3"
define audio.heartbeat = "audio/heartbeat.mp3"
define audio.ubegaet = "audio/ubegaet.mp3"
# Игра начинается здесь:
label start:

    scene black
    with fade
    $ ggname = renpy.input("Как зовут главного героя", length = 12, allow = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЮБЬТИМСЧЯъхзщшгнекуцйэждлорпавыфюбьтимсчя").strip()     

    "Однажды по пути в техникум:"
    scene bg metro
    with fade
    play sound metro
    show erik 1 1:
        xalign 0.8
    show gorv 1:
        xalign 0.2 yalign -1.7
    erik "Боже, как же хочется спать"
    gg "Да, не говори, еще и первой парой матан"
    gorv "Вот бы сейчас просто поехать домой и отоспаться"
    erik "Да, не говори"
    gg "Всё, выходим, уже Нахим"
    stop sound fadeout 2.0
    scene bg outside 2
    with fade
    show erik 1:
        xalign 0.5 yalign 0.9
    with dissolve
    show gorv 1:
        xalign 0.1 yalign -1.7
    with dissolve

    erik "Будем ждать Гора Давтяна?"
    gorv "Думаю да, на улице не так прохладно"
    gg "Вон он идет"
    show gor 2:
        xalign 1.1 yalign -0.2
    with dissolve 
    gord "Привет всем"
    "*Приветствуют*"
    gg "Пошли уже, скоро пара начнется"
    
    gord "Да, опоздать на матан не сильно хочется"

    scene bg koridor 2
    with fade
    show erik 1:
        xalign 0.5 yalign 0.9
    with dissolve
    show gor 1:
        xalign 1.1 yalign -0.2
    with dissolve
    show gorv 1:
        xalign 0.1 yalign -1.7
    with dissolve


    gorv "Какой у нас кабинет?"
    erik "207 вроде"
    gord "Ну пошли тогда куртки повесим и в кабинет"
    jump class
    return

# сон в кабинете
label class:
    scene bg parta 1
    with fade
    gg "Блин, уже пара, а препода еще нет, может поспать минут 10 хотя бы"
     
    scene bg parta 2
    with fade

    gg "Эрик, разбуди меня когда препод придёт"

    erik "Хорошо"

    scene black
    with fade
    "прошло некоторое время...."
    jump prosnulsa
return 
# проснулся
label prosnulsa:
    scene bg parta 2 dark
    with fade
    gg "ОАоаооа... что происходит? Сколько я спал?"
    gg "Почему кабинет путой и вокруг так темно?"
    gg "Сейчас ночь? надо проверить время"

    show telefon at center
        
    with dissolve
    gg "ЧТО??? УЖЕ 8 ЧАСОВ??? Эрик меня не разбудил......."
    hide telefon
    scene bg parta 2 dark
    with fade
    gg "Наверняка техникум уже закрыт, так что нужно как-то выбраться и сбежать отсюда..."
    gg "Вроде как я сейчас на 2 этаже"
    gg "Пойду к двери на первый этаж"
    jump lestpervi
return
# Идет на первый этаж
label lestpervi:
    scene bg lestnitsa 2
    with fade
    gg "Мда, и в правду уже темнеет"
    gg "Как я мог так крепко уснуть??"
    gg "Ладно, нужно идти"
    play sound train
    gg "..."
    gg "чт.. что это было??..."
    gg "Это было с третьего этажа"
    gg "Нужно торопится, а то мне здесь как-то не по себе..."
    scene bg turniket 2
    with fade
    gg "Так, дверь закрыта на простой замок и кодовый, так что мне нужен ключ и пароль"
    gg "Но где их искать???"
    gg "Надо подумать логически где они могут находится"
    menu:
        "Где искать предметы?"

        "На столе охраны":
            jump oxrana # находит ключ
            
        "Искать на втором этаже":
            jump vtoroy1 # не находит ключ
return

#Обыскивает стол охраны
label oxrana:
    scene oxr
    with fade
    play sound iskat
    "Обыскивает*"
    $ kluch = True
    gg "Что то есть, кажется это ключ! Отлично, осталось только найти код."
    gg "Теперь надо обыскать второй этаж, надеюсь больше никаких звуков я там не услышу..."
    jump vtoroy2
return



# Идет на второй этаж не найдя ключ ---------------------------------------------------------------------
label vtoroy1:
    scene bg koridor 1
    with fade
    gg "Думаю ключ и код должны быть в учительской, либо в одном из кабинетов"
    menu:
        "Где проверить?"
        
        "В учительской":
            jump uchit1

        "В кабинете":
            jump kabinet1
        
return
# ищет сначала в учительской не найдя ключ
label uchit1:
    scene uchit 
    with fade
    gg "Так, вот и учительская"
    play sound iskat
    "Обыскивает"
    scene kod
    with fade
    gg "Отлично, я нашел код, отсался ключ."
    gg "Надо поискать ключ в кабинете."
    $ kod = True
    scene kab
    with fade
    gg "Так, ну тут парты и стол препода"
    menu:
        "Обыскать кабинет?"
        "Обыскать стол препода":
            scene bg stol
            gg "Ничего годного нет..."
            gg "Только удлиннитель"
            menu: 
                "Что делать?"

                "Взять удлиннитель":
                    "Ладно, выйду в коридор"
                    $ udl = True
                    jump ataka
                "Не брать удлиннитель":
                    "Ладно, выйду в коридор"
                    jump ataka
        "Ничего не обыскивать":
            "Ладно, выйду в коридор"
            jump ataka

return


# ищет сначала в кабинете не найдя ключ
label kabinet1:
    scene kab
    gg "В первом кабинете ничего не было, надеюсь хоть здесь что-нибудь есть.."
    gg "Так, ну тут парты, стол препода и шкаф"
    menu:
        "Обыскать кабинет?"
        "Обыскать стол препода":
            scene bg stol
            gg "Ничего годного нет..."
            gg "Только удлиннитель"
            menu: 
                "Что делать?"

                "Взять удлиннитель":
                    "Ладно, пойду в учительскую"
                    $ udl = True
                "Не брать удлиннитель":
                    "Ладно, пойду в учительскую"
        "Ничего не обыскивать":
            "Ладно, пойду в учительскую"
    scene uchit
    gg "Так, вот и учительская"
    "Обыскивает"
    play sound iskat
    scene kod
    with fade
    $ kod = True
    gg "Отлично, я нашел код, отсался ключ."
    gg "Но где его искать?"
    gg "Ладно, выйду в коридор"
    jump ataka
return







# Идет на второй этаж найдя ключ
label vtoroy2:
    scene bg koridor 1
    gg "Думаю код должен быть в учительской, либо в одном из кабинетов"
    menu:
        "Где проверить?"
        
        "В учительской":
            jump uchit2

        "В кабинете":
            jump kabinet2
return
# ищет сначала в учительской найдя ключ
label uchit2:
    scene uchit 
    with fade
    gg "Так, вот и учительская"
    play sound iskat
    $ kod = True
    "Обыскивает"
    scene kod
    with fade
    gg "Отлично, я нашел код. Теперь я могу сбежать!!!"
    gg " Думаю на всякий заглянуть в кабинет, может что-то еще найду."
    scene kab
    with fade
    gg "Так, ну тут парты и стол препода"
    menu:
        "Обыскать кабинет?"
        "Обыскать стол препода":
            scene bg stol
            gg "Ничего годного нет..."
            gg "Только удлиннитель"
            menu: 
                "Что делать?"

                "Взять удлиннитель":
                    $ udl = True
                    "Ладно, выйду в коридор"
                    jump ataka
                "Не брать удлиннитель":
                    "Ладно, выйду в коридор"
                    jump ataka
        "Ничего не обыскивать":
            "Ладно, выйду в коридор"
            jump ataka
return
# ищет сначала в кабинете найдя ключ
label kabinet2:
    scene kab
    with fade
    gg "Так, ну тут парты и стол препода"
    menu:
        "Обыскать кабинет?"
        "Обыскать стол препода":
            scene bg stol
            gg "Ничего годного нет..."
            gg "Только удлиннитель"
            menu: 
                "Что делать?"

                "Взять удлиннитель":
                    $ udl = True
                    "Ладно, пойду в учительскую"
                "Не брать удлиннитель":
                    "Ладно, пойду в учительскую"
        "Ничего не обыскивать":
            "Ладно, пойду в учительскую"
    scene uchit 
    with fade
    gg "Так, вот и учительская"
    play sound iskat
    "Обыскивает"
    scene kod
    with fade
    $ kod = True
    gg "Отлично, я нашел код."
    gg "Теперь у меня есть все чтобы сбежать!"
    jump ataka
return










label ataka:
    scene bg lestnitsa 1
    play sound horror
    gg "..."
    gg "Что это за звук? Он похож на тот который был раньше"
    gg "Мне страшно...."
    scene horror
    play sound horror2
    gg "ААА ЧТО ЭТО ТАКОЕ?? PYTHON!!!"
    if kluch == True and kod == True and udl == True: 
        play sound heartbeat
        menu:
            "Что делать?"

            "Отвлечь Пайтона, бросив удлиннитель и побежать к выходу":
                "вы бросили удлиннитель, там самым отвлекли пайтона и побежади к выходу."
                jump good
            "Побежать к выходу":
                "Вы пробежали мимо Пайтона и направились к выходу"
                jump bad2
    elif kod == True and udl == True:
        play sound heartbeat
        menu:
            "Что делать?"

            "Отвлечь Пайтона, бросив удлиннитель и побежать к выходу":
                "Вы бросили удлиннитель, там самым отлекли пайтона и побежади к выходу."
                jump bad1
            "Побежать к выходу":
                "Вы пробежали мимо Пайтона и направились к выходу"
                jump bad2
    elif kluch == True and kod == True and udl == False:
        play sound heartbeat
        gg "Надо аккуратно пробежать мимо него и выйти отсюда"
        play sound ubegaet
        gg "О нет, кажется он мнея увидел"
        jump bad2
    elif kluch == False and kod == True and udl == False:
        play sound heartbeat
        gg "Надо аккуратно пробежать мимо него и попробовать выломать дверь"
        jump bad3
    else:
        play sound heartbeat
        gg "Надо аккуратно пробежать мимо него и попробовать выломать дверь"
        jump bad3
    
        
return

label good:
    scene bg turniket 2
    play sound heartbeat
    gg "Быстрей, надо открыть дверь"
    gg "Отлино!!!"
    stop sound fadeout 1
    jump pobeg

return

label pobeg:
    scene bg outside vixod
    gg "Ура, я на свободе!"
    play sound ubegaet
    scene black
    with fade
    ""
    scene vic
    with fade
    "нажмите любую клавишу,чтобы выйти в меню"
return

label bad1:
    scene mon1
    with fade
    gg "НЕТ, Я НЕ МОГУ СБЕЖАТЬ, У МЕНЯ НЕТ КЛЮЧА"
    pythn "Gonna die"
    scene mon2
    with dissolve
    gg "ОН ПРИБЛИЖАЕТСЯ!!!! ААААА!!!!!............"
    scene dead
    with fade
    "нажмите любую клавишу,чтобы выйти в меню"
return

label bad2:
    scene mon1
    with fade
    gg "НЕТ, Я НЕ МОГУ СБЕЖАТЬ, У МЕНЯ НЕТ ВРЕМЕНИ ЧТОБЫ ОТКРЫТЬ ДВЕРЬ!"
    pythn "Gonna die"
    scene mon2
    with dissolve
    gg "ОН ПРИБЛИЖАЕТСЯ!!!! ААААА!!!!!............"
    scene dead
    with fade
    "нажмите любую клавишу,чтобы выйти в меню"
return

label bad3:
    scene mon1
    with fade
    gg "НЕТ, Я НЕ МОГУ СБЕЖАТЬ, ДВЕРЬ СЛИШКОМ ПРОЧНАЯ!"
    pythn "Gonna die"
    scene mon2
    with dissolve
    gg "ОН ПРИБЛИЖАЕТСЯ!!!! ААААА!!!!!............"
    scene dead
    with fade
    "нажмите любую клавишу,чтобы выйти в меню"
return