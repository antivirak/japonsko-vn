# The script of the game goes in this file.

# The game starts here.
label start:
    play music "StockTune-Neon Pulse Of Japan_1719152100.mp3"
    call akt1
    call problemubytovani
    call akt2
    call akt2_after_ichiran
    call akt3
    call akt4
    call hotel_fuji
    call akt5
    call akt6


label titulky:
    image black = "#000"
    scene black
    "Konec části, co máme hotovou, nebo se něco pokazilo :D"
    "Tvůrci hry Cerman Jaroslav, Lokajová Eliška a Sedláček Martin"
    "Na příběhu se taktéž podíleli Drahota Matěj a Suchan Tomáš"
    "Hlavní konzultantka příběhu Tereza Petrová."
    "Betatesteři Tomáš Suchan, Tereza Petrová a další."
    "Obrázky jsou originální fotografie z Japonska"
    "Postavy byly vygenerovány pomocí AI a následně upraveny"
    $ MainMenu(confirm=False)()
