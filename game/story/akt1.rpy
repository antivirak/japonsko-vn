label akt1:
    scene bg letistenara
    with fade

    "Vítej ve hře {i}Cesta po Japonsku{/i}!"
    "Následující příběh je smyšlený a jakákoli podobnost se skutečnými osobami, živými či mrtvými, je čistě náhodná."
    menu:
        "Potřebuješ vysvětlit o jaký druh hry se jedná?"
        "Ano, VN neznám, nebo si nejsem jistý/á":
            "VN – neboli visual novela – je, jak už plný anglický název naznačuje, graficky znázorněný román."
            "Tento žánr, je v Japonsku velmi populární a většinou se jedná spíše o 'randící' hry."
            "Nejčastější motiv je, že hráč je středoškolský student, který se nedopatřením dostal do nějakého pochybného školního klubu plného holek,"
            "se kterými může konverzovat. V závislosti na správnosti svých odpovědí je pak zvát na rande."
            "V naší VN samozřejmě tyto prvky nemohou chybět, ale zároveň přinášíme i verzi pro lidi, kteří by si chtěli udělat výlet po Japonsku."
            "Takže kromě romantických linek si můžete užít fotky a nějaké zážitky z Japonska, bez nutnosti strávit 18 h v letadle :)"
            "V průběhu hry, budete moct udělat desítky rozhodnutí a každé rozhodnutí ovlivní váš postup hrou."
            "Při opakovaném hraní tedy můžete objevit situace, o kterých jste při prvním dohrání neměli ani ponětí, že hra nabízí."
            "Aby to nebylo jen 'nudné' čtení a sem tam nějaká volba, je hra 'nadupaná' i různými minihrami."
            "V průběhu hry se sbírají herní body, které si kdykoliv budete moci prohlédnout v pravém horním rohu obrazovky – teda po zadefinování své postavy."
            "Tvým cílem hry je užít si dovolenou a procestovat velkou část Japonska, nezabít Mimoně – získat málo hate pointů (HP),"
            "užít si i nějakou romanci – získat nějaké love pointy (LP) a nasbírat co nejméně gaijin pointů (GP)."
            "Kde love pointy (LP) jsou bodíky lásky u jednotlivých postav, hate pointy (HP) pak nenávistné body a gaijin pointy (GP) jsou tzv. cizinecké body, ty získáš za nevhodné chování v Japonsku."
            "Jste parta, která se po internetu domluvila, že vyrazíte na 3 týdny na dovolenou do Japonska."
            "Mezi sebou se moc neznáte. Kromě online nákupu letenek jsi se s některými účastníky nikdy neviděl/a."
            "S tebou do toho šel tvůj kámoš z dětství. A další 3 naprosto cizí lidé."

        "Ne, VN hraju na denní bázi.":
            "Tak ti přejeme, aby se ti hra líbila."
            "Tvým cílem hry je užít si dovolenou a procestovat velkou část Japonska, nezabít Mimoně – získat málo hate pointů (HP),"
            "užít si i nějakou romanci – získat nějaké love pointy (LP) a nasbírat co nejméně gaijin pointů (GP)."
            "Kde love pointy (LP) jsou bodíky lásky u jednotlivých postav, hate pointy (HP) pak nenávistné body a gaijin pointy (GP) jsou tzv. cizinecké body, ty získáš za nevhodné chování v Japonsku."
            "Všechny body si můžeš prohlédnout v pravém horním rohu obrazovky – po zadefinování své postavy."
            "Pokud hru chceš hrát pouze jako cestování po Japonsku, nezapomeň všechny romantické nabídky ignorovat."
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
    while (
        j.name.lower() in ["mimon", "sučan", "adrian", "dante", "hana", ""]
        or len(j.name.split(" ")) > 1  # noqa W503
    ):
        $ j.name = renpy.input("Zvol si jiné jméno / jiný tvar zvoleného jména. Takové už tu máme. Jako jméno použij pouze jedno slovo.").strip()
    # TODO fix bug in room selection minigame when character name clashes with predefined names
    # Or add whitespace character before the custom name. Until then, forbid these names.
    # $ j.name_5p = j.name[:-1] + "o" if j.gender == "f" else j.name
    python:
        from vokativ import vokativ


        j.name_5p = vokativ(j.name, woman=j.gender == "f", last_name=False).capitalize()
        print(j.name_5p)

    show screen stats_button_overlay
    scene bg letistenara
    if j.gender == 'f':
        "Na podzim jsi ukončila velmi toxický vztah a hledala jsi nějakou cestu, jak co nejrychleji zapomenout."
        "V té době se ti ozval Sučan, že plánuje jet do Japonska, tak jestli se k němu nechceš přidat."
        "V únoru už byla vaše parta domluvená po internetu a koupili jste si letenky s odletem v červenci."
    if j.gender == 'm':
        "Po Vánocích ti napsal tvůj kamarád z dětství, že shání někoho do party na cestu do Japonska."
        "Ani nevíš, jak se to stalo, ale v únoru už jsi měl letenku s červencovým odletem."
    image black = "#000"
    scene black
    show s neutral at left
    "Tohle je kluk s přezdívkou Sučan."
    if j.gender == 'f':
        "Právě on je tvůj kamarád z dětství."
    "S cestováním má nejvíce zkušeností."
    "Je to hlavní řidič a také zařizoval hotely, protože má na bookingu členské slevy."
    hide s neutral
    show a neutral at right
    if j.gender == 'f':
        "Tohle je Adrian. Podle společných online schůzek působí klidně a mile."
    if j.gender == 'm':
        "Tohle je Adrian. Milý a tichý společník."
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
    "Další scénu ztropil, když zjistil, že v letadle bude muset sedět sám (letenky jste si koupili bez místenky)."
    "Takže už jen po těch pár společných hodinách máte všichni neblahé tušení, že to bude s Mimoněm asi hodně náročné..."
    show m neutral at right
    show a neutral at left
    show s neutral:
        xalign 0.35
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
            $ j.driver = True
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
            $ j.increment_gaijin_points(1)
            "Získáváš 1 GP"
            show screen stats_overview
            s "V klidu to se mi ze začátku také stávalo."
            "Usměje se na tebe a položí ti ruku na stehno."
            s "Buď v klidu, je to automat a umí to pak spoustu věcí, to tě naučím, teď se soustřeď na rychlost..."
            s "...je tu nižší, než v Evropě."
            "Ještě párkrát se ti místo blinkrů podaří pustit stěrače, a někdy nebezpečně blízko vezmeš kraj cesty,"
            "ale úspešně jste dorazili do Tokia."
            $ j.add_love_points_for_person(s, 1)
            show screen stats_overview
            hide s neutral
            jump tokio1

label neridicka:
    "Oh, jsi předurčena mačkat se na zadních sedadlech."
    menu:
        "Ale můžeš si vybrat kde budeš sedět."
        "Za řidičem":
            jump zaridicem
        "Veprostřed":
            jump vprostred
        "Za spolujezdcem":
            jump zaspolujezdcem

label zaspolujezdcem:
    "Vybrala sis místo za spolujezdcem, takže vedle tebe si do středu sedá Adrian a za řidiče Mimoň."
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
            show screen stats_overview
            "Přesunuli jste se do Tokia."
            jump tokio1

label zaridicem:
    "Vybrala sis snad to nejhorší místo, co jsi mohla. Za spolujezdce se posadil Adrian a do středu vedle tebe Mimoň."
    show m neutral
    "Auto je opravdu krásný, ale vážně malý sporťák. Takže se na tebe tlačí Mimoň."
    "Cítíš, jak se Mimoň rozcapil na celé sedadlo  a ramenem ti drtí to tvé. Svou pravou nohu si narval k tobě, takže si musela své nohy nalepit ke dveřím. "
    "A Mimoň usnul s hlavou zakloněnou a opřenou o sedačky."
    "Pokusíš se ho odstrčit, ze začátku lehce pak i velkou silou, ale Mimoň spí tvrdě."
    "Vyndáš si sluchátka a celou cestu koukáš z okénka"
    "Když už podle navigace vjíždíte do Tokia, velmi si oddychneš."
    "Získáváš dva HP pro Mimoně."
    $ j.add_hate_points_for_person(m, 2)
    show screen stats_overview
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
    "Zaparkovali jste ve vnitrobloku hotelu."
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
        "Půjdu do auta k Mimoňovi.":
            hide d neutral
            m "Co tu chceš? Vypadni!"
            "Nemáš náladu se s ním dohadovat, takže získáváš jeden HP a vylézáš z auta."
            hide m neutral
            "Získáváš jeden HP u Mimoně"
            $ j.add_hate_points_for_person(m, 1)
            "Zbytek čekání, strávíš opřená o přední kapotu auta."
            "Naštěstí, nečekáš dlouho a vidíš, jak se vrací Sučan a Adrian."
            return

        "Půjdu k Dantemu.":
            hide m neutral
            d "..."
            "Vypadá to, že je opravdu zabraný do četby."
            "Najednou však zvedne oči od mobilu."
            hide d neutral
            show d neutral smile
            d "Je tu strašný teplo."
            "Jemně se usměje."
            d "Chceš?"
            "Podává ti lahev s vychlazenou vodou."
            d "Koupil jsem ji támhle v automatu."
            "Ale než stihneš odpovědět, vidíš, jak se vrací Sučan a Adrian."
            "Získáváš jeden LP u Danteho"
            $ j.add_love_points_for_person(d, 1)
            hide d neutral smile
            return

        "Zůstanu čekat sama.":
            hide d neutral
            hide m neutral
            "Čekání strávíš opřená o přední kapotu auta."
            "Naštestí nečekáš dlouho a během pár minut vidíš, jak se vrací Sučan a Adrian."
            return
