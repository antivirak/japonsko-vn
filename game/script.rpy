# The script of the game goes in this file.

# The game starts here.
label start_:
    play music "StockTune-Neon Pulse Of Japan_1719152100.mp3"
    call akt1
    call problemubytovani
    call akt2
    call akt3


label titulky:
    image black = "#000"
    scene black
    "konec části co máme hotovou, nebo se něco pokazilo :D"
    "Tvůrci hry Cerman Jaroslav, Lokajová Eliška a Sedláček Martin"
    "Na příběhu se taktéž podíleli Drahota Matěj a Suchan Tomáš"
    "Obrázky jsou originální fotografie z Japonska"
    "Postavy byly vygenerovány pomocí AI a následně upraveny"
    $ MainMenu(confirm=False)()
