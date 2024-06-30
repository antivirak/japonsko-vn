# The script of the game goes in this file.

# The game starts here.
label start:
    call akt1
    call problemubytovani
    jump akt2  # TODO investigate why call jumps to titulky


label titulky:
    scene bg black
    "konec, nebo se něco pokazilo :D"
    "Tvůrci hry Cerman Jaroslav, Lokajová Eliška a Sedláček Martin"
    "Na příběhu se taktéž podíleli Drahota Matěj a Suchan Tomáš"
    "Obrázky jsou originální fotografie z Japonska"
    "Postavy byly vygenerovány pomocí AI a následně upraveny"
    return
