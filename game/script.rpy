# The script of the game goes in this file.

transform size_1_3:
    zoom 1.3

# The game starts here.

label start:
    call akt1
    call problemubytovani


label titulky:
    scene bg black
    "konec, nebo se něco pokazilo :D"
    "Tvůrci hry Cerman Jaroslav, Lokajová Eliška a Sedláček Martin"
    "Na příběhu se taktéž podíleli Drahota Matěj a Suchan Tomáš"
    "Obrázky jsou originální fotografie z Japonska"
    "Postavy byly vygenerovány pomocí AI a následně upraveny"
    return
