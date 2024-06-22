# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character(_("Mimoň"), color="#fe0303")
define s = Character(_("Sučan"), color="#0303fe")
define a = Character(_("Adrian"), color="#094611")
define d = Character(_("Dante"), color="#000000")

transform half_size:
    zoom .5

# The game starts here.

label start:

    scene bg letistenara at half_size
    with fade

    "Vítej ve hře cesta po Japonsku"
    "Tvým cílem hry je užít si dovolenou a procestovat velkou část Japonska, nezabít Mimoně, užít si i nějakou romanci a nasbírat co nejméně Gaijin pointů (GP)."
    "Jste parta, která se po internetu domluvila, že vyrazíte na 3 týdny na dovolenou do Japonska. Mezi sebou se moc neznáte. Kromě online nákupu letenek jsi se s některými účastníky nikdy neviděl/a. S tebou do toho šel tvůj kámoš z dětství. A další 3 naprosto cizí lidé."
    # Tady mi udělejte výběr postavy

label vyberauta:

    scene bg vyzvednutiauta
    with fade
    "Absolvovali jste dlouhý a náročný let do Japonska a máte si vyzvednout auto, které vám bude dělat společnost další 3 týdny. "
    show s neutral at left, half_size
    "A ejhle první problém, auto zařizoval Sučan - fanda do aut. Máte sporťák… "
    "Pro pět lidí s kufry, je to docela stísněný prostor."
    hide s neutral
    menu:
        "Jseš řidička? Pokud ano, jseš ochotná následující 3 týdny strávit za volantem spolu se Sučanem? Mysli na to, že v Japonsku se jezdí vlevo."
        "Ano, budu řídit":
            jump ridic
        "Ne, řídit nebudu":
            jump neridic

label ridic:
    "Díky tomu že jsi řidička máš výsostné právo spolu s druhým řidičem – Sučanem sedět na místě řidiče spolujezdce a nemusíš se tlačit vzadu."
    "Přesunuli jste se do hotelu v Tokiu"
    jump tokio1
label neridic:
    "Oh, jsi předurčena mačkat se na zadních sedadlech."
    menu:
        "Ale můžeš si vybrat kde budeš sedět"
        "Za řidičem":
            jump zaridicem
        "Vprostřed":
            jump veprostred
        "Za spolujezdcem":
            jump zaspolujezdcem
label zaridicem:
    "Vybrala sis místo za řidičem takže vedle tebe si do středu sedá Adrian a za spolujezdce Mimoň."
    show a smile at right
    "Auto je opravdu krásný, ale vážně malý sporťák. Takže i přes tvou urputnou snahu se spíše lepit na dveře, než na Adriana, se ramenem a nohou Adriana dotýkáš."
    menu:
        "Otočí se na tebe a mile se usměje. Opětuješ úsměv nebo se raději podíváš z okna?"
        "Opětuji úsměv":
            jump Adrianvaute
        "Stočím pohled ven z okýnka":
            jump Adrivauteodmitnuti
label veprostred:
    "Přesunuli jste se do hotelu v Tokiu"
    jump tokio1
label zaspolujezdcem:
    "Přesunuli jste se do hotelu v Tokiu"
    jump tokio1
label Adrianvaute:
    a "Nevadilo by ti kdybych se k tobě víc přitulil?"
    "pohodí hlavou směrem k Mimoňovi a teprve teď sis všiml/a, že ho Mimoň dosti utiskuje."
    "Je rozvalený přes celou sedačku ramenem evidentně až bolestivě opřený o Adriana."
    "Spí a nohy má rocapené tak, že Adrian svou pravou nohu má položenou na prostředním vystouplém sloupku. Což je značně nepohodlná pozice. "
    "Pokusíš se ještě malinko uskromnit, ale vážně už není kam se odsunout."
    #potřebuji do textu dostat jméno hráče
    a "XX, posloucháš mě? Vadilo by ti kdybych se opřel za tebe narovnal si trošku záda a ty by ses opřela o mě?"
    menu:
        "Chvíli nad tím přemýšlíš."
        "Vadilo, odsekneš":
            jump Adrivauteodmitnuti
        "Nevadilo":
            "Pak se chytíš za sedadlo před tebou a pošoupneš se tak aby se mohl za tebe opřít. "
            "Opře se o sedadlo za tebou a ruku protáhne za tebe."
            "Chytí tě jemně za rameno a stáhne tě na sebe. Ucítíš jemné mravenčení v břiše. Usměje se na tebe"
            a "Děkuji"
            "Cesta najednou rychle uteče a už se hledá hotel, kde máte dnešní noc spát."
            jump tokio1
label Adrivauteodmitnuti:
    "Zbytek cesty usilovně koukáš z okýnka a Adrian nepromluví"
    "Přesunuli jste se do hotelu v Tokiu"
    jump tokio1    
label tokio1:

    scene bg mapatokio
    with fade

    # This ends the game.

    return
