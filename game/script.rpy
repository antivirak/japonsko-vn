﻿# The script of the game goes in this file.

transform half_size:
    zoom .5

# The game starts here.

label start:

    scene bg letistenara
    with fade
    play music "StockTune-Neon Pulse Of Japan_1719152100.mp3"

    "Vítej ve hře Cesta po Japonsku"
    "Tvým cílem hry je užít si dovolenou a procestovat velkou část Japonska, nezabít Mimoně, užít si i nějakou romanci a nasbírat co nejméně Gaijin pointů (GP)."
    "Jste parta, která se po internetu domluvila, že vyrazíte na 3 týdny na dovolenou do Japonska."
    "Mezi sebou se moc neznáte. Kromě online nákupu letenek jsi se s některými účastníky nikdy neviděl/a."
    "S tebou do toho šel tvůj kámoš z dětství. A další 3 naprosto cizí lidé."

    menu:
        "Vyber si, zda budeš hrát za holku nebo kluka. Svým výběrem rozhodneš, který z účastníků bude tvůj kamarád z dětství."
        "Dívka":
            $ j.gender = 'f'
        "Kluk":
            $ j.gender = 'm'
    $ j.name = renpy.input("Jak se jmenuješ?").strip()
    $ j.name_5p = j.name[:-1] + "o" if j.gender == "f" else j.name
    scene bg black
    show s neutral at left
    "Tohle je kluk s přezdívkou Sučan."
    if j.gender == 'f':
        "Právě on je tvůj kamarád z dětství."
    "S cestováním má nejvíce zkušeností."
    "Je to hlavní řidič a také zařizoval hotely, protože má na bookingu členské slevy."
    hide s neutral
    show a neutral at right
    "Tohle je Adrian. Podle společných online schůzek působí klidně a mile."
    if j.gender == 'm':
        "Právě on je tvůj kamarád z dětství."
    "Před odjezdem absolvoval jazykový kurz, takže umí alespoň základy japonštiny."
    hide a neutral
    if j.gender == 'f':
        show d neutral at left
        "Tenhle kluk se jmenuje Dante. Během online schůzek toho moc nenamluvil."
        "Ale většina jeho připomínek, byla konstruktivní, jeho hlas na tebe působí velmi uklidňujícím dojmem."
        hide d neutral
    else:
        show h neutral at left
        "Tohle je Hana, zná se se Sučanem."
        "Je to studentka chemické školy, se zájmem o anime a Japonsko"
        "Větší část cesty byla potichu."
        hide h neutral
    show m neutral at right
    "Tak tohle je Mimoň, vůbec netušíte, jak se stalo, že s vámi odletěl."
    "Během online schůzek se v podstatě nevyjadřoval."
    "Poprvé, co jste zjistili, že by mohl být nějaký problém, bylo den před odletem..."
    "Domluvili jste se, že se všichni sejdete u Sučana na bytě, dáte si večeři a pak vyrazíte společně na letiště."
    "Ale den před odletem přišla zpráva od Mimoně, který se ptal, kdo ho vyzvedne autem, že s kufrem 'sockou' rozhodně nepojede."
    "Nakonec se to vyřešilo tak, že ho přivezla sestra."
    "Další scénu ztropil, když zjistil, že v letadle bude muset sedět sám (letenky, jste si koupili bez místenky)."
    "Takže už jen po těch pár společných hodinách máte všichni neblahé tušení, že to bude s Mimoněm asi hodně náročné..."
    show m neutral at right
    show a neutral at left
    show s neutral:
        xalign 0.3
        yalign 1.0
    if j.gender == 'f':
        show d neutral:
            xalign 0.7
            yalign 1.0
        "Takže tohle je tvůj 'harém' pro následující tři týdny."
    else:
        show h neutral:
            xalign 0.7
            yalign 1.0
        "Takže tohle jsou tví spolucestující pro následující tři týdny."


label vyberauta:

    scene bg vyzvednutiauta
    with fade
    "Absolvovali jste dlouhý a náročný let do Japonska a máte si vyzvednout auto, které vám bude dělat společnost další 3 týdny. "
    show s neutral at left
    "A ejhle první problém, auto zařizoval Sučan – fanda do aut. Máte sporťák... "
    "Pro pět lidí s kufry je to docela stísněný prostor."
    hide s neutral
    menu:
        # TODO parametrize for gender
        "Jseš řidička? Pokud ano, jseš ochotná následující 3 týdny strávit za volantem spolu se Sučanem? Mysli na to, že v Japonsku se jezdí vlevo."
        "Ano, budu řídit":
            jump ridicka
        "Ne, řídit nebudu":
            jump neridicka

label ridicka:
    "Díky tomu, že jsi řidička, tak máš výsostné právo spolu s druhým řidičem – Sučanem sedět na místě řidiče a spolujezdce a nemusíš se tlačit vzadu."
    show s neutral at left
    menu:
        "Chceš řídit hned první cestu?"
        "Nechci":
            "Protože Sučan je zvyklý cestovat a nařízeno vlevo má hodně a zodpovědnost za auto jde za ním."
            "Přesunuli jste se do Tokia"
            hide s neutral
            jump tokio1
        "Chci":
            "Cestu z letiště do hotelu řídíš ty. Sučan vypadá spokojeně, že mu parťáka děláš právě ty."
            s "Dávej si pozor na obě strany, je to jiné, když člověk normálně řídí na druhé straně."
            "Vyjedete a samozřejmě, hned při prvním odbočovaní, pouštíš místo blinkrů stěrače."
            $ j.gaijin_points += 1
            "Získáváš 1 GP"
            "[j.show_all_points()]"
            s "V klidu to se mi ze začátku také stávalo."
            "Usměje se na tebe a položí ti ruku na stehno."
            s "Buď v klidu, je to automat a umí to pak spoustu věcí, to tě naučím, teď se soustřeď na rychlost..."
            s "...je tu nižší, než v Evropě."
            "Ještě párkrát se ti místo blinkrů podaří pustit stěrače, a někdy nebezpečně blízko vezmeš kraj cesty,"
            "ale úspešně jste dorazili do Tokia."
            $ j.add_love_points_for_person(s, 1)
            "[j.show_all_points()]"
            hide s neutral
            jump tokio1

label neridicka:
    "Oh, jsi předurčena mačkat se na zadních sedadlech."
    menu:
        "Ale můžeš si vybrat kde budeš sedět."
        "Za řidičem":
            jump zaridicem
        "Ve prostřed":
            jump vprostred
        "Za spolujezdcem":
            jump zaspolujezdcem

label zaridicem:
    "Vybrala sis místo za řidičem, takže vedle tebe si do středu sedá Adrian a za spolujezdce Mimoň."
    show a smile at right
    "Auto je opravdu krásný, ale vážně malý sporťák. Takže i přes tvou urputnou snahu se spíše lepit na dveře než na Adriana, se ramenem a nohou Adriana dotýkáš."
    menu:
        "Otočí se na tebe a mile se usměje. Opětuješ úsměv nebo se raději podíváš z okna?"
        "Opětuji úsměv":
            jump Adrianvaute
        "Stočím pohled ven z okýnka":
            jump Adrivauteodmitnuti

label vprostred:
    "Vybrala sis snad to nejhorší místo, co si mohla."
    show a neutral at left
    show m neutral at right
    "Za řidiče se posadil Adrian a za spolujezdce Mimoň."
    "Auto je opravdu krásný, ale vážně malý sporťák. Takže se na tebe z obou stran tlačí oba urostlí spolujezdci."
    "Cítíš, jak se Mimoň rozcapil na celé sedadlo a ramenem ti drtí to tvé. Tvou pravou nohu ti vytlačil od sebe, takže ji máš v dost nepříjemné pozici uprostřed na vyvýšené části podlahy."
    "A takto rozvalený Mimoň spokojeně usnul, opřený o okénko s otevřenou pusou. "
    a "Můžeš si dát i tu druhou nohu ke mně."
    "šeptá vedle tebe Adrian. Teprve teď si uvědomíš, že vlastně vedle tebe sedí i on."
    "Ačkoliv je lépe stavěný než Mimoň, neutlačuje tě svou přítomností, a když se po jeho slovech na něj otočíš, vidíš, že sám nesedí vůbec komfortně."
    menu:
        "Chceš s Adrianem nějak interagovat, nebo ho raději budeš ignorovat?"
        "Budu ho ignorovat.":
            "Nasadila sis sluchátka a snažíš se také usnout, na Adriana se raději ani nepodíváš."
            "Usnula jsi a probouzíš se až v Tokiu"
            jump tokio1
        "Rozhodneš se nabídku přijmout":
            a "Je to hulvát, měla sis sednout místo mě"
            "Jemně se na tebe usměje a odhodí ti vlasy z tváře"
            a "Máš krásný oči"
            "Poté se odmlčí a podívá se z okénka."
            "Citíš, jak se ti do tváře hrne krev a ty se začínáš červenat."
            "Sklopíš zrak a vytáhneš sluchátka a mobil."
            "Zbytek cesty se nic neděje a rychle uteče."
            "Získáváš LP u Adriana a jeden HP za Mimoně."
            # 1 LP Adrian, 1 HP Mimoň
            $ j.add_love_points_for_person(a, 1)
            $ j.add_hate_points_for_person(m, 1)
            "[j.show_all_points()]"
            "Přesunuli jste se do Tokia."
            jump tokio1

label zaspolujezdcem:
    "Vybrala sis snad to nejhorší místo, co jsi mohla. Za řidiče se posadil Adrian a do středu vedle tebe Mimoň."
    show m neutral
    "Auto je opravdu krásný, ale vážně malý sporťák. Takže se na tebe tlačí Mimoň."
    "Cítíš, jak se Mimoň rozcapil na celé sedadlo  a ramenem ti drtí to tvé. Svou pravou nohu si narval k tobě, takže si musela své nohy nalepit ke dveřím. "
    "A Mimoň usnul s hlavou zakloněnou a opřenou o sedačky."
    "Pokusíš se ho odstrčit, ze začátku lehce pak i velkou silou, ale Mimoň spí tvrdě."
    "Vyndáš si sluchátka a celou cestu koukáš z okénka"
    "Když už podle navigace vjíždíte do Tokia, velmi si oddychneš."
    "Získáváš dva HP pro Mimoně."
    # 2 HP Mimoň
    $ j.add_hate_points_for_person(m, 2)
    "[j.show_all_points()]"
    jump tokio1

label Adrianvaute:
    a "Nevadilo by ti, kdybych se k tobě víc přitulil?"
    "Pohodí hlavou směrem k Mimoňovi a teprve teď sis všimla, že ho Mimoň dosti utiskuje."
    "Je rozvalený přes celou sedačku a ramenem evidentně až bolestivě opřený o Adriana."
    "Spí a nohy má rozcapené tak, že Adrian svou pravou nohu má položenou na prostředním vystouplém sloupku. Což je značně nepohodlná pozice. "
    "Pokusíš se ještě malinko uskromnit, ale vážně už není kam se odsunout."
    a "[j.name_5p], posloucháš mě? Vadilo by ti, kdybych se opřel za tebe, narovnal si trošku záda a ty by ses opřela o mě?"
    menu:
        "Chvíli nad tím přemýšlíš."
        "Vadilo, odsekneš.":
            jump Adrivauteodmitnuti
        "Nevadilo.":
            "Pak se chytíš za sedadlo před tebou a pošoupneš se tak, aby se mohl za tebe opřít. "
            "Opře se o sedadlo za tebou a ruku protáhne za tebe."
            "Chytí tě jemně za rameno a stáhne tě na sebe. Ucítíš jemné mravenčení v břiše. Usměje se na tebe"
            a "Děkuji."
            "Získáváš dva LP u Adriana. Cesta najednou rychle uteče."
            # 2 LP Adrian
            $ j.add_love_points_for_person(a, 2)
            "[j.show_all_points()]"
            jump tokio1

label Adrivauteodmitnuti:
    "Zbytek cesty usilovně koukáš z okýnka a Adrian nepromluví."
    "Přesunuli jste se do Tokia."

label tokio1:

    scene bg mapatokio
    with fade
    "Právě jste dorazili do Tokia, hlavního města Japonska, zde celá cesta začíná."
    "Hotel máte na okraji Tokia, asi 10 minut cesty od metra."
    "Jsou asi čtyři hodiny odpoledne, kdy podle navigace dojíždíte do zabookovaného hotelu."

    scene bg hoteltokio
    with fade
    "Zaparkovali jste vnitrobloku hotelu."
    show s neutral at left
    show a smile at right
    "Napřed do hotelu půjde Sučan s Adrianem, protože Sučan zařizoval ubytovaní a Adrian umí základy Japonštiny."
    hide s neutral
    hide a smile
    show d neutral at left
    show m neutral at right
    "Zůstala jsi sama na parkovišti s Dantem a Mimoňem."
    "Dante si sedl na obrubník a evidentně si něco čte na mobilu."
    "Mimoň zůstal v autě, má nasazená sluchátka a tváří se znechuceně."
    menu:
        "Půjdeš si sednout k Mimoňovi, k Dantemu nebo počkáš bez interakce?"
        "Půjdu do auta k mimoňovi.":
            hide d neutral
            m "Co tu chceš? Vypadni!"
            "Nemáš náladu se s ním dohadovat, takže získáváš jeden HP a vylézáš z auta."
            hide m neutral
            "Získáváš jeden HP u Mimoně"
            $ j.add_hate_points_for_person(m, 1)
            "[j.show_all_points()]"
            "Zbytek čekání, strávíš opřená o přední kapotu auta."
            "Naštěstí, nečekáš dlouho a vidíš, jak se vrací Sučan a Adrian."
            jump problemubytovani

        "Půjdu k Dantemu.":
            hide m neutral
            d "..."
            "Vypadá to, že je opravdu zabraný do četby."
            "Najednou však zvedne oči od mobilu."
            d "Je tu strašný teplo."
            "Jemně se usměje."
            d "Chceš?"
            "Podává ti lahev s vychlazenou vodou."
            d "Koupil jsem ji támhle v automatu."
            "Ale než stihneš odpovědět, vidíš, jak se vrací Sučan a Adrian."
            "Získáváš jeden LP u Danteho"
            $ j.add_love_points_for_person(d, 1)
            "[j.show_all_points()]"
            hide d neutral
            jump problemubytovani

        "Zůstanu čekat sama.":
            hide d neutral
            hide m neutral
            "Čekání strávíš opřená o přední kapotu auta."
            "Naštestí nečekáš dlouho a během pár minut vidíš, jak se vrací Sučan a Adrian."

label problemubytovani:
    show s neutral at left
    show a smile at right
    "Všimneš si, že Sučan se tváří pobaveně, zatímmco Adrian smutně."
    s "Víte, jak jsem řešil, že tenhle hotel někdo hacknul?"
    "říká velmi pobaveným tónem."
    s "Tak to má dohru, nejen, že jsem kvůli tomu musel před odjezdem zablokovat a obstarat si novou kreditku..."
    s "...ale ještě mají nějaký zmatek v systému, takže místo tří pokojů máme jen dva."
    a "Takže se musíme rozdělit do jednoho dvojlůžáku a jednoho trojlůžáku."
    hide s neutral
    hide a neutral
    show m neutral at left
    show a neutral: 
        xalign 0.3
        yalign 1.0
    show s neutral:
        xalign 0.6
        yalign 1.0
    show d neutral at right
    "Pro lepší rozhodování tvé získané bodíky: [j.show_all_points()]"
    "Vyber rozložení cestujících do pokojů."

    scene bg black  # TODO do we want some room background here?
    $ b = d if j.gender == 'f' else h
    $ char_names = [a.name, m.name, s.name, b.name, j.name]  # TODO colors

label problemubytovani_action:
    $ dropdowns = [Dropdown([
        DropdownItem(chars[0], selected=selected[0]),
        DropdownItem(chars[1], selected=selected[1]),  # , Jump('test')
        DropdownItem(chars[2], selected=selected[2]),
        DropdownItem(chars[3], selected=selected[3]),
        DropdownItem(chars[4], selected=selected[4]),
    ]) for chars, selected in zip(
        [char_names] * 5, [
            [True, False, False, False, False],
            [False, True, False, False, False],
            [False, False, True, False, False],
            [False, False, False, True, False],
            [False, False, False, False, True],
        ]
    )]
    $ dropdown_1, dropdown_2, dropdown_3, dropdown_4, dropdown_5 = dropdowns

    # In attr use your variable name
    call screen dropdown('dropdown_1', 'dropdown_2', 'dropdown_3', 'dropdown_4', 'dropdown_5')


label titulky:
    scene bg black
    "konec, nebo se něco pokazilo :D"
    "Tvůrci hry Cerman Jaroslav, Lokajová Eliška a Sedláček Martin"
    "Na příběhu se taktéž podíleli Drahota Matěj a Suchan Tomáš"
    "Obrázky jsou originální fotografie z Japonska"
    "Postavy byly vygenerovány pomocí AI a následně upraveny"
    return
