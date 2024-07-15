label bathroom_common(your_mates, clothes=True):
    $ len_mates = len(your_mates)
    scene bg koupelna
    "Konečně máš čas prohlédnout si koupelnu."
    "První, co tě zaujme je typický japonský záchod s panelem na zdi."
    menu:
        "Mobil s překladačem sis nechal['a' if j.gender == 'f' else ''] v pokoji."
        "Panel budeš ignorovat":
            $ ignore = True
        "Pomačkáš náhodně všechny čudlíky.":
            $ ignore = False
    if not ignore:
        "Pomačkal['a' if j.gender == 'f' else ''] jsi náhodně všechny čudlíky."
        "A najednou začne cákat voda ze záchodu ven!"
        $ j.increment_gaijin_points(1)
        "Získáváš jeden GP!"
        "[j.show_all_points()]"
        "Ještě něco pomačkáš, a ono to přestane."
        if len_mates == 1 and your_mates[0] == m:
            "Pohledem zhodnotíš počet ručníků a všimneš si, že na zemi je jeden původně bílý ručník..."
            "...celý červený od Mimoňovy barvy na vlasy, tzn. už se dá použít jako hadr na podlahu."
        else:
            "Pohledem zhodnotíš počet ručníků a rozhodneš, že se jeden dá použít jako hadr na podlahu"
        "Vytřeš potopu, co jsi způsobila."
    if len_mates == 1 and your_mates[0] == s and not clothes:
        call bathroom_sucan
        return
    "Rychle se svlékneš a zapadneš do vany."
    "Po cestování, které si v posledních 24 hodinách absolvoval['a' if j.gender == 'f' else ''],"
    "je pořádná sprcha právě to, co nejvíce potřebuješ."
    if len_mates == 1:
        "Po pár minutách užívání si horké koupele, usoudíš, že je čas vylézt a pustit do koupelny i [your_mates[0].name_2p]."
    else:
        "Po pár minutách užívání si horké koupele, usoudíš, že je čas vylézt a pustit do koupelny i [your_mates[0].name_2p] a [your_mates[1].name_2p]."
    "Vylezeš ven, usušíš se a trochu si vyfénuješ vlasy."
    # TODO u Sučana jsi popisovala vybavení hotelových koupelen
    if not clothes and len_mates == 1:
        "Chceš se obléknout a zjistíš, že sis v tom spěchu vzala jen kalhotky a tričko."
        "Podprsenka a kraťasy musely zůstat ležet na posteli."
        "Rozhodneš se, že to není tak zlé; že pustíš [your_mates[0].name_2p] do koupelny a dooblékneš se v pokoji."
        "Zkontroluješ, že po tobě v koupelně nezůstal žádný bordel a odemkneš koupelnu."
        return
    if not clothes:
        "Chceš se obléknout, ale zjistíš, že sis vzala jen kahotky a tričko."
        j "Super, to to hezky začíná, dva pěkný kluci na pokoji a já se tu budu promenádovat v kalhotkách."
        "Rozhodneš se, že si mokrý ručník ale vázat kolem pasu nebudeš, a že proběhneš jen tak."
        "Zkontroluješ zda po tobě nezůstal moc velký bordel."
        "Odemkneš a vylezeš ven."
        j "Volno!"
        "Napůl křikneš."
        return
    "Oblékneš se do přineseného oblečení."
    "Zkontroluješ, že po tobě v koupelně nezůstal žádný bordel a odemkneš koupelnu."
    j "Volno!"
    "Napůl křikneš, a jdeš si uklidit věci do kufru."
    return


label bathroom_sucan:
    "Dáš si rychlou sprchu a usušíš si vlasy fénem. Ano, v Japonsku je fén základní výbava koupelny, stejně jako sprchový gel, šampón, kondicionér..."
    "...soustava ručníků, zubní kartáček, mini-pasta, hřeben, gumičky, holítka..."
    "Po sprše se rozhodneš Sučana malinko provokovat."
    "Takže i přes to, že sis s sebou vzala věci na převlečení,"
    "si vezmeš na sebe jen spodní prádlo a ručník si uvážeš kolem sebe."
    "Vezmeš svoje věci a odemkneš koupelnu."
    j "Volno!"
    return


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

    image black = "#000"
    scene black  # TODO do we want some room background here?
    $ b = d if j.gender == 'f' else h
    $ chars = [a, m, s, b, j]
    $ char_names = [char.name for char in chars]
    $ color_map = {char.name: char.color for char in chars}

label problemubytovani_action:
    $ dropdowns = [Dropdown([
        DropdownItem(chars[0], selected=selected[0]),
        DropdownItem(chars[1], selected=selected[1]),  # , Jump('test')
        DropdownItem(chars[2], selected=selected[2]),
        DropdownItem(chars[3], selected=selected[3]),
        DropdownItem(chars[4], selected=selected[4]),
    ], color_map) for chars, selected in zip(
        [char_names] * 5, [
            [True, False, False, False, False],
            [False, True, False, False, False],
            [False, False, True, False, False],
            [False, False, False, True, False],
            [False, False, False, False, True],
        ]
    )]

    call screen dropdown(dropdowns)


label tokio1_hotel_part1:
    scene bg hoteltokio
    $ room, partners = resolve_room_selection([dropdown.selected_item.value for dropdown in dropdowns])
    $ chars = {char.name: char for char in (a, d, h, m, s)}
    $ partners = [chars[partner_name] for partner_name in partners if partner_name != j.name]

    hide m neutral
    hide a neutral
    hide d neutral
    hide s neutral

    "Po rozdělení jste se rozhodli dojít na pokoje odnést si věci. Sraz máte v 18 h na recepci a pak půjdete společně na večeři."
    if room == "Dvojlůžák" and s in partners and j.gender == "f":
        jump hracka_Sucan
    if room == "Dvojlůžák" and m in partners:
        call hrac_ka_Mimon
        call hracka_nolove  # TODO hrac
        return
    if room == "Dvojlůžák" and h in partners and j.gender == "m":
        "Tome, vážně? Klučičí linka stále není :P"
        jump recepce
    if room == "Dvojlůžák" and a in partners and j.gender == "f":
        jump hracka_Adrian
    if room == "Dvojlůžák" and d in partners and j.gender == "f":
        jump hracka_Dante
    if room == "Trojlůžák" and m in partners:
        call hrac_ka_Mimon3p(partners)
        call recepce
        call hracka_nolove  # TODO hrac
        return
    if room == "Trojlůžák" and d in partners and a in partners and j.gender == "f":
        jump hracka_Adri_Dante
    if room == "Trojlůžák" and d in partners and s in partners and j.gender == "f":
        jump hracka_Sucan_Dante
    if room == "Trojlůžák" and s in partners and a in partners and j.gender == "f":
        jump Hracka_Sucan_Adrian
    else:
        "Tahle možnost není ještě implementována."
        jump titulky

label hracka_Sucan:
    show s neutral at left
    s "To už bude doba, co jsme spolu strávili noc na pokoji."
    s "Jak je to dlouho, co jsme spolu byli na nějaké dovolené?"
    hide s neutral
    j "Tak 10 let?"
    "Povídáte si, zatímco míříte chodbou k pokoji 306, kde strávíte dvě noci."
    show s neutral at left
    s "Vyrostla si; myslím, že je na čase abych si u vašich zažádal o tvou ruku, mám ji přislíbenou pamatuješ?"
    hide s neutral
    "Když jste byli malí, tak jste jezdili spolu na dovolené a vaše rodiny trávily spolu hodně času."
    "A když vám bylo asi 5 let, tak se Sučan nechal slyšet, že si tě vezme."
    menu:
        "Chceš to zahrát do outu, a nebo by sis se Sučanem možná chtěla něco začít?"
        "Zahrát do outu.":
            jump sucanvoutu
        "Dát mu šanci.":
            jump sucansance

label sucanvoutu:
    j "Jó jasně, určitě si taky pamatuješ, že jsi ty zásnuby asi v sedmi zrušil, protože sis našel v první třídě Terezku."
    "Pobaveně se zasměješ"
    j "Hele, radši odemkni pokoj a nech si ty blbý fóry od cesty."
    show s neutral at left
    s "Au, to bolelo, ale když si to přeješ."
    "Odemkne kartou pokoj a pustí tě dovnitř."
    hide s neutral
    scene bg dvojluzak separe
    "Pokoj není velký, po pravé straně je koupelna, a když projdete malou uličkou, tak se vám otevře prostor pokoje."
    "Dvě postele, a máte štěstí, jsou od sebe odděleny nočním stolkem."
    show s neutral at left
    s "Předpokládám, že chceš postel u stěny. Já půjdu k oknu, kdyby ze závěsů padali pavouci."
    hide s neutral
    "Jsi unavená z cesty a uvařená z auta, takže jeho narážku necháš být, hodíš batoh a kufr na svou postel."
    "Vyndáš si čisté oblečení."
    j "Jestli chceš něco v koupelně, tak běž teď, jinak se jdu koupat"
    show s neutral at left
    s "Tak mi dej chvilku"
    hide s neutral
    "Sučan zaleze do koupelny; ty si zatím z papírového obalu na kartu opíšeš heslo na WiFi a napíšeš domů."
    show s neutral at left
    "Otevřou se dveře do koupelny, a vykoukne rozesmátý Sučan."
    s "Pojď sem, to musíš vidět!"
    hide s neutral
    "Vstaneš a jdeš se podívat do koupelny."
    show s smiling at right
    scene bg koupelna
    s "Ten japonskej záchod je ultra hustej, koukej!"
    "Mobilem míří na panel na zdi, kde má otevřený překladač 'vyhřívané prkénko' 'bidet muži' 'bidet ženy' ... "
    s "A největší sranda je, když se podíváš odkud vyjíždí ta tryska."
    menu:
        "Podíváš se? Hned se Sučanem, nebo třeba později bez něho, nebo tě to nezajímá?"
        "Nezajímá/znám/podívám se později":
            jump posprse
        "Podívám se":
            "Sučan přimáčkne bačkorou prkénko a něco navolí na displeji, vyjede bidetová tryska a vystříkne tvým směrem, jen tak tak uhneš!"
            $ j.increment_gaijin_points(1)
            "Získáváš jeden GP!"
            "[j.show_all_points()]"
            j "Ty seš debil!"
            hide s smiling
            "Nadáváš mu, zatímco to na panelu vypíná. Pohledem přepočítáš ručníky a usoudíš, že se jeden dá použít jako hadr na podlahu."
            "Vytřeš vodu, která byla na zemi a umyješ si ruce."

label posprse:
    "Dojdeš si pro věci a vyhodíš Sučana z koupelny."
    "Dopřeješ si vytouženou horkou sprchu, po 13 hodinách letu, 2 hodinách v autě a X hodinách čekání ať už na letištích nebo jinde."
    "Po koupeli si vyfénuješ vlasy a převlékneš se ještě v koupelně."
    scene bg dvojluzak separe
    "Pak pustíš Sučana do koupelny."
    "A sama si vybalíš potřebné věci a uklidíš věci z cesty."
    "A pak je pomalu čas jít dolů na recepci a na večeři."
    call recepce
    call hracka_nolove
    return

label sucansance:
    j "K tomu by si musel mít ještě prstýnek a kytku, víš? V dnešní době je zvykem se ptát nejdříve nastávající, a ne jejích rodičů!"
    "Zazubíš se na něho."
    j "Nekecej a odemykej!"
    scene bg dvojluzakmanp
    j "To snad né..."
    show s neutral at left
    s "Copak, snad ti nevadí, že máš spát se mnou."
    s "Dřív jsme spolu spali i na normální posteli."
    hide s neutral
    j "Jo, ale to nám bylo sedm."
    show s neutral at left
    s "Jestli ti to tak vadí, tak já můžu spát na zemi."
    hide s neutral
    j "Tak kdyby mi to vadilo, tak si tě nevyberu do pokoje."
    j "Milionkrát radši s tebou než s Mimoněm."
    j "Pravá je moje!"
    "Rozeběhneš se k posteli a zabereš si pravou stranu postele."
    "Sučan v klidu dojde do místnosti a dá si věci na levou stranu postele"
    "Otevřeš si kufr a vyndáš si věci na převlečení. Podíváš se po Sučanovi, mrkneš na něj a rozeběhneš se do koupelny."
    j "Koupelna je moje!"
    "Ačkoli to Sučan má do koupelny dál, než stihneš doběhnout na úroveň dveří, tak tě dožene a zezadu obejme."
    show s neutral at center
    s "No prr, holčičko, nepřijde ti to nefér?"
    hide s neutral
    j "Pusť, vždyť ti to muselo být jasné, že to udělám!"
    j "Vždyť mě znáš!"
    show s neutral at center
    s "No to jsem si myslel, že tě znám."
    "Silou, a přesto jemně si tě otočí tak, aby ti viděl do obličeje."
    s "Ale vypadá to, že mám nějaké zastaralé informace."
    s "Například [j.name], kterou znám, byla totálně plochá."
    hide s neutral
    show s smiling at center
    "Začne se smát."
    s "A byla víc vychovaná!"
    j "Ty blbečku, že já tě praštím!"
    "Začneš se smát a Sučana odstrčíš"
    hide s smiling
    scene bg koupelna
    "Zapadneš do koupelny a rychle za sebou zamkneš dveře."
    "Sučan jemně buší na dveře a se smíchem v hlase huláká"
    s "Vždyť to říkám, nevychovaná. Pusť mě aspoň na záchod, než zabereš koupelnu na dvě hodiny!"
    j "Jdi si ke klukům, bývalá plošina zabrala koupelnu na následující půl hodinu."
    s "Vážně si tě tu mám nechat samotnou v pokoji a odejít s kartou ke klukům?"
    s "Máme jen jednu kartu na vstup, nezapomeň."
    j "No, tak budeš muset chvíli počkat."
    "Slyšíš, jak Sučan odchází od dveří koupelny."

    call bathroom_common([s], clothes=False)

label ignorpanel:
    scene bg dvojluzakmanp
    "Vycházíš ven s úsměvem. Zahneš doprava a objevíš se v místnůstce s postelí."
    show s neutral at left
    s "To mi děláš schválně?"
    hide s neutral
    j "Co?"
    "Jdeš si k posteli rovnat věci"
    show s neutral at left
    s "Co to máš na sobě? To sis nemohla vzít věci na převlečení?"
    s "Co si myslíš, že asi tak udělám? Když se mi tu pohybuje polonahá holka? Nenapadlo tě, že bych tě taky mohl znásilnit?"
    s "Jsme tu sami na pokoji. Zbytek kluků je o dvě patra níže..."
    "Při poslední větě trošku ztlumí hlas a nechá jí vyznít do ticha."
    j "Ale prosím tě, za prvé tě znám, za druhé si mě nahou už viděl. Pravda bylo mi pět a byla jsem, jak si to říkal před chvílí... Plochá?"
    j "Běž se koupat, ať na nás kluci dole nečekají."
    "Sučan si bere věci a odchází do koupelny."
    hide s neutral
    "Když se za ním zabouchnou dveře, tak sundáš ručník a oblíkneš se."
    "Najdeš vstupní kartu a z papírové kapsičky si opíšeš heslo na wifi. Napíšeš domů, že jsi v pořádku."
    "Pak zkontroluješ 'socky'."
    "Sučan se mezitím vysprchuje a přijde do pokoje."
    show s scantily clad
    "Zaznamenala jsi, že přišel. Zvedneš oči od mobilu a zůstaneš zírat doslova s otevřenou pusou."
    "Před tebou stojí Sučan jen ve spodním prádle, po celém těle se mu rýsují svaly."
    "Na kráse tomu přidávají jemné kapičky vody, které nedokonale utřel"
    s "Aby si nezapomněla dýchat!"
    "Začne se smát Sučan."
    s "Vždyť si mě přece nahýho už viděla, kdy že to bylo? Když nám bylo pět?"
    hide s scantily clad
    "Konečně se probereš z úžasu, rychle zavřeš pusu, a začneš se červenat."
    j "No taky si byl plošší!"
    "Snažíš se tuhle trapnou situaci zahrát do outu."
    show s scantily clad
    s "Cože jsem byl?"
    "Šáhne po polštáři a hodí ho po tobě."
    hide s scantily clad
    j "Plochej!"
    "Zazubíš se na něj. A pak tě napadne, jak z této situace vybruslit."
    j "Šup, oblíkej se, ať na nás kluci nečekají. Já mám už taky docela hlad!"
    $ j.add_love_points_for_person(s, 2)
    "[j.show_all_points()]"
    "Hodíš po něm polštářem zpět."
    "Oba se smějete, Sučan se oblékne. A vyrazíte dolů na recepci."
    call recepce
    call dvojluzak_hracka_Sucan2
    return

label hrac_ka_Mimon:
    "Vybral['a' if j.gender == 'f' else ''] sis do pokoje Mimoně, asi aby se kluci nemuseli s Mimoněm štvát."
    "Nebo věříš, že s ním dokážeš vycházet?"
    show m neutral
    m "Nechci s tebou být na pokoji!"
    hide m neutral
    j "To bude dobrý uvidíš. Kluci chtěli být spolu, tak my dva budeme dva večery spát v jednom pokoji. Vždyť o nic nejde."
    j "Pojď, musíme být v šest zpátky, chceme jít společně na večeři."
    show m neutral
    m "Nikam nejdu!"
    hide m neutral
    j "Tak nemusíš jít na večeři, ale teď pojď na pokoj, máme jen jednu vstupní kartu."
    "Došli jste na pokoj 306, odemkl['a' if j.gender == 'f' else ''] jsi kartou a oddychl['a' if j.gender == 'f' else ''] sis, když jsi zjistil['a' if j.gender == 'f' else ''], že jsou postele odděleny."
    scene bg dvojluzak separe
    j "Jakou chceš postel?"
    show m neutral
    m "..."
    hide m neutral
    j "Jakou chceš postel? Vyber si."
    show m neutral

    m "..."
    hide m neutral
    "Ale nakonec se k jedné rozejde."
    "Takže ty si jdeš dát věci na druhou. Začneš se vybalovat a hledat si věci do sprchy."
    j "Půjdu se koupat, půjdeš po mě?"
    show m neutral
    m "..."
    hide m neutral
    "Když ještě chvíli neodpovídá, tak si vyndáš věci na koupání a převlečení a chceš jít do koupelny."
    "Najednou se Mimoň rozejde směr koupelna, zabouchne a slyšíš klapnout zámek."
    j "Tak aspoň 'Búúú'!"
    "Za ním zavoláš."
    "Zůstal['a' if j.gender == 'f' else ''] jsi na pokoji ['sama' if j.gender == 'f' else 'sám'], tak si z papírového obalu, kde byla uložena vstupní karta, opíšeš údaje na WiFi a napíšeš domů."
    "Zkontroluješ 'socky'."
    "Pak začneš být trošku nervózní, protože na šestou máte být na recepci kvůli večeři."
    "Je půl šesté a Mimoň už asi hodinu nevylezl z koupelny."
    "Najednou se rozletí dveře koupelny."
    j "Hurá!"
    "Zaraduješ se, bereš věci a běžíš do koupelny."
    call bathroom_common([m])

label ignorpanel2:
    "Dáš si rychlou sprchu, vlasy si ani nefénuješ, jen si je usušíš ručníkem."
    "Oblékneš se, vyběhneš do pokoje."
    scene bg dvojluzak separe
    j "Tak já jdu na večeři, nechám ti tu kartu na vstup. Kdyby si někam šel tak mi napiš."
    j "Domluvíme se, kde si ji předáme."
    show m neutral
    m "..."
    hide m neutral
    "Čapneš tašku, mobil a běžíš na recepci."
    "Získáváš 3 HP u Mimoňě!"
    $ j.add_hate_points_for_person(m, 3)
    "[j.show_all_points()]"
    call recepce
    return


label hracka_Adrian:
    "Vybrala sis pro následující dvě noci strávit společný čas s Adrianem."
    "Vzali jste si kufry z auta a výtahem se necháte vyvést do šestého patra."
    show a neutral at right
    a "Můžu ti pomoct s kufrem?"
    hide a neutral
    menu:
        "Necháš si pomoct s kufrem? Nebo nemáš o interakci s Adrianem zájem?"
        "Nechat si pomoct s kufrem.":
            jump adrian_hotel_pomoc
        "Ne, chci být silná, nezávislá žena.":
            jump adrian_hotel_feministka

label adrian_hotel_pomoc:
    "Adrian ti vezme kufr a zamíříte chodbou k pokoji číslo 607."
    "Odemkne pomocí karty, otevře dveře a pustí tě dovnitř."
    scene bg dvojluzakmanp
    "V pokoji je pouze manželská postel."
    j "..."
    show a neutral
    a "Jestli se mnou nechceš spát v posteli, tak já klidně budu spát na zemi."
    hide a neutral
    j "Neblázni, přece nebudeš spát na zemi."
    j "Ta postel je dost velká pro oba, ale jestli nechceš spát se mnou, tak mezi sebe můžeme naskládat kufr a tašky."
    show a smile
    a "To z mé strany není potřeba."
    a "Jen tě nechci omezovat."
    hide a smile
    j "Mě neomezuješ, na které straně chceš spát?"
    show a neutral
    a "Mně je to jedno, vyber si ty."
    hide a neutral
    "Tak si vybereš pravou stranu postele. A začneš si vybalovat věci."
    show a neutral
    a "Běž do koupelny první, já počkám. Můžu jít klidně i pryč jestli chceš?"
    hide a neutral
    j "No, jasně, že chci... hezky se sbal a odleť tak na 20 minut? Například do Evropy."
    "Všimneš si, jak zesmutněl a snad na tím i přemýšlí?"
    j "Normálně tu zůstaň, určitě je v koupelně klíč. A i kdyby ne, tak přece víš, že tam budu."
    "Usměješ se na něj a mrkneš."
    "Popadneš věci a přesuneš se do koupelny."
    call bathroom_common([a])

label ignorpanel3:
    show a smile
    a "Díky,"
    hide a smile
    "řekne Adrian, vezme si věci a přesune se do koupelny."
    "Ty si uklidíš věci; z papírového obalu na vstupní kartu vyčteš heslo k wifi a napíšeš domů."
    "Natáhneš se do postele."
    "Potom otevřeš 'socky' a začteš se do toho, co se zatím děje doma."
    "Asi za deset minut vyleze Adrian."
    "Mlčky vstoupí do místnosti a jde s věcmi ke své tašce."
    show a neutral  # TODO možná změna oblečení
    a "Máme ještě skoro hodinu do srazu."
    hide a neutral
    j "To je super. Ale začínám mít hlad."
    show a neutral
    a "Nic k jídlu nemám, ale všiml jsem si u vstupních dveří vody. Chceš ji přinést?"
    hide a neutral
    j "To by bylo skvělé."
    "Odloží věci a dojde ti pro vodu."
    j "Děkuji."
    "Poděkuješ a usměješ se."
    "Natáhne se vedle tebe do postele."
    "Zvedne se na loktech."
    show a neutral  # možná nějaká postelovější pozice
    a "Myslíš, že bych tě mohl poprosit o podání mobilu?"
    a "Nechal jsem ho položený u tebe na nočním stolku."
    a "Tam totiž byla zásuvka."
    hide a neutral
    j "No jasně!"
    "Usměješ se a sáhneš po mobilu. A podáš mu ho."
    "Akorát u toho zavadíš svojí rukou o jeho."
    show a neutral
    a "Děkuji."
    hide a neutral
    "Vezme si mobil a zadívá se do něj."
    j "Odkud se vlastně znáš s Dantem?"
    show a neutral
    a "Ze školy, máme stejný gympl."
    a "Ty se znáš ze Sučanem odkud?"
    hide a neutral
    j "Měli kousek od nás chalupu, takže rodinný známý."
    j "Strávili jsme spolu spoustu dovolených, je něco jako brácha."
    show a neutral
    a "Aha, tak proč si nechtěla jít na pokoj s ním?"
    hide a neutral
    j "A víš, že vlastně ani nevím? Možná z rozmaru. Možná jsem chtěla strávit nějaký čas s tebou."
    j "Vadilo by ti to?"
    show a neutral
    a "Ne... Ne, rozhodně ne."
    a "Ale nebojíš se?"
    hide a neutral
    j "A čeho?"
    show a neutral
    a "No být sama s cizím klukem na pokoji, být tu teď se mnou?"
    hide a neutral
    j "Ne."
    "Docela si užíváš, jak je Adrian z tebe v rozpacích."
    "A dostaneš 'geniální' nápad."
    "Jak tak ležíte vedle sebe, tak se překulíš a obkročmo si na něj klekneš někam do půli stehen."
    j "A nebojíš se ty být s cizí holkou na pokoji? Nebojíš se tu být se mnou?"
    show a confuse
    a "..."
    hide a confuse
    j "Promiň, to jsem asi přehnala."
    "Opřeš se pravou rukou o postel, abys z něho mohla slézt."
    show a confuse
    a "Počkej!"
    "Řekne a a chytí tě za levou ruku. Abys z něj nemohla slézt."
    a "Přece neuděláš něco takového a hned mi zase neutečeš."
    a "Zůstaň takhle chvíli."
    "Ruku ti zase pustí."
    a "A řekni mi, proč zrovna já? A ne Dante?"
    show a confuse
    j "Protože se mi líbíš a jsi milý."
    "Odpovíš a využiješ toho, že ti ruku pustil a slezeš z něho."
    j "Myslím, že se půjdu trošku upravit a měli bychom vyrazit na večeři."
    show a neutral
    a "Jo to máš pravdu."
    hide a neutral
    "Dojdeš si upravit vlasy do koupelny a lehce se nalíčit. A už slyšíš, jak se Adrian balí."
    "Dojdeš si vzít tašku a vyrazíte společně na recepci."
    call recepce
    call dvojluzak_hracka_Adrian2
    return

label adrian_hotel_feministka:
    j "Nene, já si ho vezmu sama."
    "Adrian jde tedy napřed."
    "Odemkne pomocí karty, otevře dveře a pustí tě dovnitř."
    scene bg dvojluzak separe
    "Pokoj je dvojlůžkový a postele jsou naštěstí odděleny nočním stolkem."
    show a neutral
    a "Vyber si postel a klidně běž první do sprchy."
    hide a neutral
    j "Jo, díky."
    "Vybereš si jednu postel, popadneš věci a přesuneš se do koupelny."
    call bathroom_common([a])

label ignorpanel4:
    # TODO the same text, parametrize
    show a neutral
    a "Děkuji!"
    hide a neutral
    "Řekne, vezme si věci a přesune se do koupelny."
    "Ty si uklidíš věci, z papírového obalu na vstupní kartu vyčteš heslo k wifi a napíšeš domů."
    "Natáhneš se do postele."
    "Potom otevřeš 'socky' a začteš se do toho, co se zatím děje doma."
    "Asi za deset minut vyleze Adrian."
    "Mlčky vstoupí do místnosti a jde s věcmi ke své tašce."
    "Natáhne se do postele a kouká do mobilu."
    "Takhle strávíte čas do večeře."
    "Chviličku před odchodem se zastavíš v koupelně upravit."
    "Pak se sbalíte a vyrazíte na recepci."
    call recepce
    call hracka_nolove
    return

label hracka_Dante:
    "Jako jediná holka jsi měla možnost si vybrat, s kým a kde budeš spát."
    "Zvolila jsi k sobě do pokoje Danteho."
    "Jdete spolu do výtahu a vyjedete do šestého patra."
    "Pustí tě před sebe. Dojdete na konec chodby k pokoji 608."
    "Celou dobu oba mlčíte a je mezi vámi takové zvláštní napětí."
    "Kartou odemkne dveře. A pustí tě do pokoje jako první."
    if j.love_points.get(d.name, 0) > 0:
        scene bg dvojluzakmanp
        "Vstoupíš do pokoje a vidíš, že se v pokoji nachází pouze manželská postel."
        "Podíváš se rozpačitě na Danteho."
        show d neutral
        d "..."
        hide d neutral
        "Dante mlčí. Pravděpodobně čeká, jak se zachováš."
        j "Aha, to jsem netušila, že kromě toho, že nám dali o pokoj méně, máme ještě manželské apartmá."
        j "Vezmu si pravou stranu, neva?"
        show d neutral
        d "Ne."
        "Zakroutí hlavou."
        hide d neutral
        "Zamíříš k posteli a začneš si vybalovat věci."
        j "Asi bychom si měli ujasnit nějaký pravidla."
        show d neutral
        d "Dobře."
        hide d neutral
        j "Každý máme svou půlku postele. A budeš si držet aspoň deseticentimetrový rozestup."
        show d neutral
        d "Dobře. Ale v tom případě platí stejná pravidla i pro tebe."
        hide d neutral
        j "Ok. A jestli ti to nevadí, zamířím do sprchy jako první."
        show d neutral
        d "Běž."
        hide d neutral
        "Vezmeš si věci a vyrazíš do koupelny."
        "Pro jistotu se zamkneš."
        call bathroom_common([d], clothes=False)
        jump ignorpanel5
    else:
        scene bg dvojluzak separe
        "Vstoupíš do pokoje. Je to normální dvojlůžák, postele jsou odděleny nočním stolkem."
        show d neutral
        "..."
        hide d neutral
        "Dante mlčí, ale stojí za tebou a čeká."
        "Rozhodneš si jednu postel vybrat a vyrazíš k ní. Vybalíš si věci."
        j "Bude ti vadit, když se půjdu koupat jako první?"
        show d neutral
        d "Ne, běž."
        hide d neutral
        "Vezmeš si tedy věci a vyrazíš do koupelny."
        "Pro jistotu se zamkneš."
        call bathroom_common([d])
        jump ignorpanel6

label ignorpanel5:
    scene bg dvojluzakmanp
    show d reading
    "Vlezeš do pokoje. Dante sedí u okna a čte si knihu."
    hide d reading
    j "Máš tam volno."
    show d neutral
    d "Jo, díky"
    hide d neutral
    "Odloží knihu a teprve teď se podívá tvým směrem."
    "Cítíš, jak tě pohledem hodnotí."
    "Zadržíš dech. Nejsi schopná promluvit. Jen cítíš, jak se ti do hlavy hrne krev."
    "Ale mlčí, zvedne se, z postele si vezme věci a jde do koupelny."
    "Při zaklapnutí zámku z tebe opadne nervozita. A konečně vydechneš."
    "Ta situace byla strašně zvláštní."
    "Evidentně tě Dante silně přitahuje."
    "Ale nevíš, co si máš myslet o jeho reakci."
    "Rozhodneš se ihned převléct, aby tě Dante nenačapal nahou."
    "Poté z papírového obalu na kartu opíšeš heslo na wifi a napíšeš domů."
    "Lehneš si na postel a zkontroluješ 'socky'."
    show d black
    "Dante asi za 10 minut vyjde z koupelny v kraťasech a černém tričku."
    hide s black
    "Oblečení, které měl před tím na sobě, má úhledně složené v rukou."
    "Odloží ho do výklenku vestavěné skříně a jde si sednout k oknu."
    "Otevře knihu a zase začne číst."
    "Nemůžeš se přinutit přestat na něj koukat; lépe řečeno zírat."
    "Dante po chvíli zvedne oči od knihy."
    show d reading
    d "Děje se něco?"
    hide d reading
    "Jeho slova tě konečně probudí. Zatřeseš hlavou."
    j "Ne, nic."
    show d reading
    d "Že na mě tak zíráš, něco není v pořádku?"
    hide d reading
    j "Jen jsem se zamyslela, promiň."
    "Kuňkneš, zatímco sklápíš zrak. Cítíš, že musíš být červená jako rajče."
    "Rychle rozsvítíš mobil a děláš, že tam něco strašně naléhavě musíš řešit."
    "A odmítáš zvednou zrak od mobilu."
    "..."
    "Po nějaké době se odhodláš odlepit zrak od mobilu."  # TODO přeformulovat, moc zraku v mobilu
    "A podívat se Danteho směrem."
    "Zjistíš, že má hlavu podepřenou rukou a zavřené oči."
    "Spí?"
    "Koukneš na čas a zjistíš, že máte být za půl hodiny dole na recepci."
    "Opatrně a potichu vstaneš z postele, šáhneš po kosmetické taštičce a jdeš se do koupelny upravit"
    scene bg koupelna
    "Upravíš si vlasy a jemně se namaluješ. Stříkneš se trošku parfémem a vylezeš ven z koupeny."
    scene bg dvojluzakmanp
    "Přendáš si důležité věci do tašky, kterou si plánuješ vzít s sebou."
    "Koukneš na mobil: za deset minut máte být dole. Rozhodneš se Danteho vzbudit."
    "Dojdeš k němu a tlumeným hlasem ho oslovíš"
    j "Dante?"
    show d black
    d "..."
    hide d black
    j "Dante?"
    "Zopakuješ trošku hlasitěji."
    show d black
    d "..."
    hide d black
    j "Dante? Budeme muset jít."
    "Řekneš nahlas a s důrazem."
    show d black
    d "..."
    hide d black
    j "Dante?"
    "Zopakuješ po čtvré a jemně se dotkneš jeho ramena."
    "Dante otevře oči."
    show d black
    d "Neříkali jsme bez doteků? Myslím, že porušuješ pravidla. Už je čas na večeři?"
    hide d black
    j "Že ty jsi to jenom hrál? Jo, a je čas vyrazit na večeři."
    show d black
    d "Tak asi pojďme."
    hide d black
    "Vezmeš si věci a vyrazíte směr recepce."
    "Těsně před tím, než se výtah zastaví a otevřou se dveře, se k tobě Dante skloní a zašeptá ti do ucha."
    show d black
    d "Porušovat pravidla se nevyplácí."
    "Mrkne na tebe a narovná se."
    hide d black
    "Chceš mu odpovědět, ale akorát se otevřou dveře od výtahu a jste na doslech ostatním."
    call recepce
    call dvojluzak_hracka_Dante2
    return

label ignorpanel6:
    scene bg dvojluzak separe
    show d neutral
    d "Děkuji,"
    hide d neutral
    "poděkuje a vezme si věci do koupelny."
    "Zůstala jsi v pokoji sama."
    "Poté z papírového obalu na kartu opíšeš heslo na wifi a napíšeš domů."
    "Lehneš si na postel a zkontroluješ 'socky'."
    show d black
    "Dante asi za 10 minut vyjde z koupelny v kraťasech a černém tričku."
    hide s black
    "Oblečení, které měl před tím na sobě, má úhledně složené v rukou."
    "Odloží ho do výklenku vestavěné skříně a jde si sednout k oknu."
    "Otevře knihu a začne si číst."
    "Ty pokračuješ v prohlížení postů."
    "Pak si všimneš, že do domluveného srazu zbývá dvacet minut."
    "Vyhrabeš kosmetickou taštičku a dojdeš se do koupelny upravit."
    "Pak si přebalíš důležité věci do tašky, kterou si chceš vzít s sebou."
    "A vyrazíte směr recepce."
    call recepce
    call hracka_nolove
    return

label hrac_ka_Mimon3p(partners):
    "Vybral['a' if j.gender == 'f' else ''] sis do pokoje [' a '.join(partner.name_4p for partner in partners)]."
    $ b = d if j.gender == 'f' else h
    $ chars = [a, m, s, b]
    "Takže na dvojlůžák zamířili [' a '.join(char.name for char in chars if char.name not in (partner.name for partner in partners))]."
    "Vyrážíte tedy společně na pokoj. Je to číslo 516 v pátém patře."
    "Takže nahoru vyjíždíte výtahem."
    show m neutral
    m "Nechci být s vámi na pokoji!"
    hide m neutral
    j "To bude dobrý."
    "Jdeš napřed a otevřeš pomocí karty dveře."
    "Vstoupíte dovnitř."
    scene bg dvojluzak separe
    "Před vámi se otevře malý pokoj se třemi postelemi a koupelnou."
    $ partner_not_mimon = partners[not partners.index(m)]
    # or $ partner_not_mimon = [partner for partner in partners if partner.name != "Mimoň"][0]
    "[partner_not_mimon.name] se zastaví."
    $ not_mimon_tag = partner_not_mimon.name[0].lower()
    show expression f'{not_mimon_tag} neutral' as not_mimon_neutral
    partner_not_mimon "Vyberte si první, já počkám."
    hide not_mimon_neutral
    j "Díky."
    show m neutral
    m "..."
    hide m neutral
    j "Jakou chceš postel? Vyber si."
    show m neutral
    m "..."
    hide m neutral
    "Když se Mimoň k ničemu nemá, rozejdeš se k posteli u okna."
    "Už už, pokládáš batoh na postel, když přiběhne Mimoň a do té postele skočí."
    "Rozhodneš se, že se nebudeš rozčilovat"
    j "Tak já si vezmu tu u zdi, když Mimoň má postel u okna."
    "A jdeš si dát věci na postel u zdi, co nejdále od Mimoně."
    "[partner_not_mimon.name] si jde tedy dát věci na postel uprostřed."
    j "Bude někomu vadit, když se půjdu koupat první?"
    show m neutral
    m "..."
    hide m neutral
    show expression f'{not_mimon_tag} neutral' as not_mimon_neutral
    partner_not_mimon "Nevadí, jen běž."
    hide not_mimon_neutral
    "Vezmeš si věci a zamíříš do koupelny."
    "Pro jistotu se zamkneš."
    call bathroom_common(partners)
    scene bg dvojluzak separe
    "Vidíš jak se [partner_not_mimon.name] balí a chce se rozejít do koupelny."
    "Ale z ničeho nic se zase Mimoň zvedne vezme si svoje věci a zajde do koupelny."
    show expression f'{not_mimon_tag} neutral' as not_mimon_neutral
    partner_not_mimon "Dobře? Tak já asi ještě počkám."
    hide not_mimon_neutral
    j "To bude ještě těžký, snad tam nebude dlouho."
    "Natáhneš se na postel, z papírového obalu na vstupní kartu opíšeš heslo na wifi."
    "Zkontroluješ 'socky'."
    "Pak začneš být trošku nervózní, protože na šestou máte být na recepci kvůli večeři."
    "Je po půl šesté a Mimoň už asi hodinu nevylezl z koupelny."
    "Najednou se rozletí dveře koupelny."
    show expression f'{not_mimon_tag} neutral' as not_mimon_neutral
    partner_not_mimon "Hurá!"
    hide not_mimon_neutral
    "Vezme si věci a jde do koupelny."
    "Ty si zatím zabalíš věci, co si chceš vzít s sebou."
    "Během pár minut vyjde [partner_not_mimon.name] a dá si věci na postel."
    "Koukne na hodinky."
    "Měli bychom vyrazit, za chvíli máme být na recepci."
    show m neutral
    m "Nikam nejdu!"
    hide m neutral
    j "Tak nechoď, ale budeš mít hlad."
    "Rozhodneš se, že s ním budeš jednat jak s dítětem."
    j "Tak my půjdeme na večeři, necháme ti tu kartu na vstup. Kdyby si někam šel tak nám napiš."
    j "Domluvíme se, kde si ji předáme."
    "Položíš významně kartu na stoleček a s [partner_not_mimon.name_7p] vyrazíte směr recepce."
    $ j.add_hate_points_for_person(m, 2)
    "Získáváš 2 HP pro Mimoně"
    "[j.show_all_points()]"
    return

label hracka_Adri_Dante:
    "Do pokoje si tě vzali Dante s Adrianem a Sučan bude na dvojlůžáku s Mimoněm."
    "Vzali jste si kufry z auta a výtahem se necháte vyvést do šestého patra."
    show a neutral at right
    a "Můžu ti pomoct s kufrem?"
    hide a neutral
    "Usměješ se na něj."
    j "Děkuji"
    "Dante mlčí, z výtahu vyjde jako první. Dojde k příslušnému pokoji a odemkne pomocí karty."
    scene bg dvojluzak separe
    "Otevře dveře a nechá vás vstoupit první."
    "V pokoji jsou tři oddělené postele, dva noční stolky, jeden stoleček, vestavěná stěna s televizí a koupelna."
    show a neutral
    a "Vyber si, kde chceš spát. My se přizpůsobíme."
    hide a neutral
    "Vybereš si tedy postel u okna. Tam si dáš baťůžek a Adrian ti tam donese kufr."
    "Sám si dá věci na postel vedle tebe a Dante si vezme postel u zdi."
    show a neutral
    a "Klidně běž do koupelny první my počkáme."
    hide a neutral
    j "Díky."
    "Řekneš a vezmeš si věci do koupelny."
    "Pro jistotu se zamkneš."
    $ clothes = not(j.love_points.get(d.name, 0) > 0 and j.love_points.get(a.name, 0) > 1)
    call bathroom_common(partners, clothes=clothes)
    scene bg dvojluzak separe
    a "Díky."
    if not clothes:
        "Zdržíš se zavíráním dveří od koupelny. A mezitím se Adrian dostane do 'chodbičky' k tobě."
        show a neutral
        "..."
        "Konsternovaně na tebe hledí."
        hide a neutral
        "Cítíš, jak se ti krev hrne do obličeje."
        "Po pár vteřinách se probere."
        show a neutral
        "Dovolíš?"
        hide a neutral
        "Řekne a protáhne se do koupelny."
        "Jdeš tedy do pokoje uklidit si věci a doobléknout se."
        show d reading
        "Dante sedí u tvé postele u stolečku a čte si knížku."
        hide d reading
        "Rozejdeš se tedy ke svým věcem. Dante zvedne oči od knížky."
        show d reading
        "To jsem nečekal, že hned první den tě uvidím v kalhotkách."
        hide d reading
        j "Děláš jako bys nikdy žádnou holku v kalhotkách neviděl, a navíc už se oblíkám."
        "Rychle si nandáš kraťasy."
        show d reading
        "Jen se usměje a vypadá, že se věnuje knížce."
        hide d reading
        "Zapojíš si mobil do zásuvky a z papírové kapsičky na vstupní kartu opíšeš heslo na wifi."
        "Natáhneš se do postele a napíšeš domů."
        "Zkontroluješ 'socky'."
        "Během chvíle vyjde z koupelny Adrian."
        show a neutral
        a "Dante, můžeš,"
        hide a neutral
        "řekne klidně a jde si ke svým věcem."
        "Dante odloží knížku, dojde si k úhledně složené kupičce věcí a přesune se do koupelny."
        "Zůstala si na pokoji sama s Adrianem."
        show a neutral
        a "Promiň, že jsem tě tak blbě očumoval, překvapila si mě."
        hide a neutral
        j "Nerozmazávej to. Moje blbost, že jsem v tom spěchu nechala půlku věcí v pokoji."
        "Dál se koukáš do mobilu, po chvíli na sobě ucítíš něčí pohled."
        "Zvedneš oči a Adrian rychle sklopí zrak ke svým věcem."
        j "Je na mně něco špatně?"
        show a neutral
        a "Ne.. Ne! Jen si říkám, jestli se nechceš víc přiobléct, když si tu s námi."
        hide a neutral
        j "Vždyť jsem oblečená..."
        "Váš rozhovor přeruší přicházející Dante."
        "Své dosavadní oblečení si nese úhledně složené."
        show d black
        d "Vyrušil jsem vás u něčeho?"
        hide d black
        show a neutral
        a "Ne."
        hide a neutral
        show d black
        "Dobře?"
        hide d black
        "Řekne nevěřícně."
        "Koukneš na mobil a zjistíš, že za chvíli je čas na večeři."
        "Vezmeš si kosmetickou taštičku a podprsenku a zapluješ do koupelny."
        scene bg koupelna
        "Oblékneš si podprsenku, upravíš se a lehce se nalíčíš."
        "Vylezeš ven."
        scene bg dvojluzak separe
        j "Asi je pomalu čas jít."
        "Vlezeš do pokoje a oba divně zmlknou."
        "Ale vypadá to, že se o něco dohadovali."
        "Dojdeš si k posteli sbalit věci, co si chceš vzít s sebou, a jdeš čekat před pokoj."
        "Kluci tě po chvíli následují. A vyrazíte směr recepce."
        "Získáváš u každého jeden LP."
        $ j.add_love_points_for_person(a, 1)
        $ j.add_love_points_for_person(d, 1)
        "[j.show_all_points()]"
        call recepce
        # TODO new label for the trojluzak, where something happened
    else:
        "Zavolá Adrian a potkáte se po cestě, kdy on míří do koupelny a ty do pokoje."
        "Dante si u stolu čte knížku."
        "Dáš si věci do kufru."
        "Z papírového obalu na vstupní kartu opíšeš heslo na wifi a napíšeš domů."
        "Natáhneš se na svoji postel a zkontroluješ 'socky'."
        "Kluci se mezitím vystřídají v koupelně."
        "Chvíli před šestou se dojdeš do koupelny trošku upravit a nalíčit."
        "Pak se sbalíš a na šestou všichni vyrazíte na recepci."
        call recepce
        call hracka_nolove
    return

label hracka_Sucan_Dante:
    "Do pokoje jste se rozdělili ty, Sučan a Dante. Takže na dvojlůžák zamíří Mimoň s Adrianem."
    "Vzali jste si kufry z auta a výtahem se necháte vyvést do šestého patra."
    show s neutral
    s "To už bude doba, co jsme spolu strávili noc na pokoji."
    s "Jak je to dlouho, co jsme spolu byli na nějaké dovolené?"
    hide s neutral
    j "Tak 10 let?"
    "Povídáte si, zatímco míříte chodbou k pokoji 506, kde strávíte dvě noci."
    "Dante mlčí, z výtahu vyjde jako první. Dojde k příslušnému pokoji a odemkne pomocí karty."
    scene bg dvojluzak separe
    "Otevře dveře a nechá vás vstoupit první."
    "V pokoji jsou tři oddělené postele dva noční stolky, jeden stoleček, vestavěná stěna s televizí a koupelna."
    show s neutral
    s "Vyber si, kde chceš spát, my se přizpůsobíme."
    hide s neutral
    "Vybereš si tedy postel u okna."
    "Sučan si dá věci na postel vedle tebe."
    show s neutral
    s "Pro jistotu."
    "Mrkne na tebe."
    hide s neutral
    "Dante si vezme postel u zdi."
    show s neutral
    s "Klidně běž do koupelny první, my počkáme."
    hide s neutral
    j "Díky,"
    "řekneš a vezmeš si věci do koupelny."
    "Pro jistotu se zamkneš."
    $ clothes = not(j.love_points.get(d.name, 0) > 0 and j.love_points.get(s.name, 0) > 0)
    call bathroom_common(partners, clothes=clothes)
    scene bg dvojluzak separe
    s "Díky."
    if not clothes:
        "Zdržíš se zavíráním dveří od koupelny. A mezitím se Sučan dostane do 'chodbičky' k tobě."
        show s neutral
        "..."
        "Konsternovaně na tebe hledí."
        hide s neutral
        "Cítíš, jak se ti krev hrne do obličeje."
        "Po pár vteřinách se probere."
        show s neutral
        "Takhle chceš jít do pokoje? Nemám ti přinést něco na převlečení?"
        hide s neutral
        j "Jsem snad malá holka? Běž se koupat,"
        "řekneš a on se protáhne do koupelny."
        "Jdeš tedy do pokoje uklidit si věci a doobléknout se."
        show d reading
        "Dante sedí u tvé postele u stolečku a čte si knížku."
        hide d reading
        "Rozejdeš se tedy ke svým věcem. Dante zvedne oči od knížky."
        show d reading
        "To jsem nečekal, že hned první den tě uvidím v kalhotkách."
        hide d reading
        j "Děláš jako bys nikdy žádnou holku v kalhotkách neviděl, a navíc už se oblíkám."
        "Rychle si nandáš kraťasy."
        show d reading
        "Jen se usměje a vypadá, že se věnuje knížce."
        hide d reading
        "Zapojíš si mobil do zásuvky a z papírové kapsičky na vstupní kartu opíšeš heslo na wifi."
        "Natáhneš se do postele a napíšeš domů."
        "Zkontroluješ 'socky'."
        "Během chvíle vyjde z koupelny Sučan."
        show a neutral
        a "Dante, můžeš."
        hide a neutral
        "Řekne klidně a jde si ke svým věcem."
        "Dante odloží knížku, dojde si k úhledně složené kupičce věcí a přesune se do koupelny."
        "Zůstala jsi na pokoji sama se Sučanem."
        show s neutral
        s "Promiň, vím, že nejsi malá holka, ale vážně si myslíš, že je dobré pobíhat polonahá na pokoji s cizím klukem?"
        hide s neutral
        j "Tak za prvé, nebyla jsem polonahá. Za druhé, nejsi moje matka, aby si mi říkal, co mám nosit. A za třetí, s tebou se mi nic nestane, ne?"
        show s neutral
        s "Hele, já tu taky nemusím být pořád. Tak si říkám, jestli se nechceš víc přiobléct, když si tu s námi."
        hide s neutral
        j "No dobře"
        "Vyndáš podprsenku natočíš se směrem k zataženému oknu, zády k Sučanovi. Sundáš si tričko, nandáš si podprsenku a oblíkneš si tričko."
        j "Spokojený?"
        show s neutral
        s "Je ti jasné, že jsem také kluk. Tohle mi nemůžeš dělat."
        hide s neutral
        j "Vždyť jsem ti jen vyšla vstříc."
        "Váš rozhovor přeruší přicházející Dante."
        "Své stálé oblečení si nese úhledně složené."
        show d black
        d "Vyrušil jsem vás u něčeho?"
        hide d black
        show s neutral
        s "Ne."
        hide s neutral
        show d black
        "Dobře?"
        hide d black
        "Řekne nevěřícně."
        "Koukneš na mobil a zjistíš, že za chvíli je čas na večeři."
        "Vezmeš si kosmetickou taštičku a zapluješ do koupelny."
        scene bg koupelna
        "Upravíš se a lehce se nalíčíš."
        "Vylezeš ven."
        scene bg dvojluzak separe
        j "Asi je pomalu čas jít."
        "Vlezeš do pokoje a oba divně zmlknou."
        "Ale vypadá to, že se o něco dohadovali."
        "Dojdeš si k posteli sbalit věci, co si chceš vzít s sebou, a jdeš čekat před pokoj."
        "Kluci tě po chvíli následují. A vyrazíte směr recepce."
        $ j.add_love_points_for_person(s, 1)
        $ j.add_love_points_for_person(d, 1)
        "[j.show_all_points()]"
        call recepce
        # TODO
    else:
        "Zavolá Sučan a potkáte se po cestě, kdy on míří do koupelny a ty do pokoje."
        "Dante si u stolu čte knížku."
        "Dáš si věci do kufru."
        "Z papírového obalu na vstupní kartu opíšeš heslo na wifi a napíšeš domů."
        "Natáhneš se na svoji postel a zkontroluješ 'socky'."
        "Kluci se mezitím vystřídají v koupelně."
        "Chvíli před šestou se dojdeš do koupelny trošku upravit a nalíčit."
        "Pak se sbalíš a na šestou všichni vyrazíte na recepci."
        call recepce
        call hracka_nolove
    return

label Hracka_Sucan_Adrian:
    "Dante si vzal na dvojlůžák Mimoně. Takže ty, Sučan a Adrian jste spolu na trojlůžáku."
    "Vyzvedli jste si kufry v autě." 
    show a neutral
    a "Chceš vzít kufr?"
    hide a neutral 
    "Už, už se chystáš říct, že ano. Když přijde Sučan a kufr ti vezme."
    show s neutral
    s "Jsme v osmém patře, tak pojďme k výtahu."
    hide s neutral 
    "Přesunete se do výtahu."
    show s neutral 
    s "Jak dlouho jsme nespali spolu na jednom pokoji?"
    s "Tak 10 let?"
    hide s neutral 
    j "Nene, naposledy jsem u tebe spala, jak měla tvoje mamka taneční soutěž v Bratislavě."
    show s neutral
    s "Vidíš, na to jsem skoro zapomněl."
    hide s neutral 
    "Jak si tak povídáte, došli jste až ke dveřím do pokoje."
    "Sučan otevře dveře kartou a pustí tě před sebe."
    scene bg dvojluzak separe 
    "Před vámi se otevře minichodbička zakončená pokojem se třemi postelemi, oddělenými dvěma nočními stolky. U okna se nachází stoleček. Naproti postelím je vestavěná skříň s televizí. V chodbičce za dveřmi je ještě vstup do koupelny."
    show s neutral
    s "Vyber si postel"
    hide s neutral 
    "Vybereš si postel u okna"
    "Sučan ti tam přinese kufr a sám si zabere postel vedle tebe." 
    show s neutral 
    s "Pro jistotu,"
    hide s neutral 
    "mrkne na tebe."
    "Adrian tiše zamíří k poslední volné posteli."
    show s neutral
    s "Běž do koupelny první, my počkáme."
    hide s neutral
    j "Díky."
    "Šáhneš si do kufru pro věci a vyrazíš do koupelny, abys nezdržovala."
    "Pro jistotu se zamkneš."
    $ clothes = not(j.love_points.get(s.name, 0) > 0 or j.love_points.get(a.name, 0) > 0)
    call bathroom_common(partners, clothes=clothes)
    scene bg dvojluzak separe
    s "Díky."
    if not clothes and j.love_points.get(s.name, 0) > 0:
        "Zdržíš se zavíráním dveří od koupelny. A mezitím se Sučan dostane do 'chodbičky' k tobě."
        show s neutral
        "..."
        "Konsternovaně na tebe hledí."
        hide s neutral
        "Cítíš, jak se ti krev hrne do obličeje."
        "Po pár vteřinách se probere."
        show s neutral
        "Takhle chceš jít do pokoje? Nemám ti přinést něco na převlečení?"
        hide s neutral
        j "Tak jo, přineseš mi kraťásky a podprsenku? Leží někde na posteli."
        "Odejde na chvíli do pokoje a za chvíli se vrací s tvými věcmi."
        j "Díky."
        "Vezmeš si věci od něj a zapluješ ještě na chvíli do koupelny."
        "Převlíkneš se a znovu vylezeš ven."
        j "Lepší?"
        show s neutral
        s "Kdybychom tu byli sami, tak ne, ale za těhle okolností lepší."
        hide s neutral
        "S těmito slovy zaleze do koupelny."
        "Přesuneš se tedy do pokoje, kde je Adrian."
        "Ten leží na posteli a něco si čte na mobilu."
        "Srovnáš si věci do kufru a dáš si nabíjet mobil. Z papírového obalu na kartu si opíšeš heslo na wifi."
        "Natáhneš se do postele, napíšeš domů a zkontroluješ 'socky'."
        "Během pár minut přijde Sučan z koupelny a mlčky se vymění s Adrianem."
        "Sučan si uklízí věci a po chvíli tě osloví."
        show s neutral
        s "To oblečení sis zapomněla schválně?"
        hide s neutral
        j "Ne, nějak jsem ho v tom spěchu vysypala na postel. Nebo kde si ho našel?"
        show s neutral
        s "Jo, na posteli. No, tak ještěže jsem se šel koupat jako druhý já a ne Adrian."
        hide s neutral
        j "Jak to myslíš?"
        show s neutral
        "Tak, že by ses neměla vystavovat polonahá cizím klukům."
        hide s neutral 
        j "Tak s tebou jsem se pořádně pár let neviděla, jsi pro mě v podstatě taky cizí kluk."
        "Váš rozhovor přeruší přicházející Adrian."
        show a neutral
        a "Vyrušil jsem vás u něčeho?"
        hide a neutral
        show s neutral
        s "Ne."
        hide s neutral
        show a neutral
        a "Dobře?"
        hide a neutral
        "Řekne nevěřícně."
        "Koukneš na mobil a zjistíš, že za chvíli je čas na večeři."
        "Vezmeš si kosmetickou taštičku a zapluješ do koupelny."
        scene bg koupelna
        "Upravíš se a lehce se nalíčíš."
        "Vylezeš ven."
        scene bg dvojluzak separe
        j "Asi je pomalu čas jít."
        "Vlezeš do pokoje a oba divně zmlknou."
        "Ale vypadá to, že se o něco dohadovali."
        "Dojdeš si k posteli sbalit věci, co si chceš vzít s sebou, a jdeš čekat před pokoj."
        "Kluci tě po chvíli následují. A vyrazíte směr recepce."
        show s neutral
        s "Jak se řekne japonsky jdeme?"
        hide s neutral
        show a neutral
        a "Ikimašó"
        hide a neutral
        show s neutral
        s "Ikimašó"
        hide s neutral
        "Získáváš jeden LP u Sučana"
        $ j.add_love_points_for_person(s, 1)
        "[j.show_all_points()]"
        call recepce
        # TODO
    
    elif not clothes and j.love_points.get(a.name, 0) > 1:
        # TODO is it correct to first check for suchan and then for adrian?
        "Zdržíš se zavíráním dveří do koupelny. A mezitím se Sučan dostane do 'chodbičky' k tobě."
        show s neutral
        "..."
        "Konsternovaně na tebe hledí."
        hide s neutral
        "Cítíš, jak se ti krev hrne do obličeje."
        "Po pár vteřinách se probere."
        show s neutral
        "Takhle chceš jít do pokoje? Nemám ti přinést něco na převlečení?"
        hide s neutral
        j "Nejsem malá holka, běž se koupat."
        "řekneš a on se protáhne do koupelny."
        "Jdeš tedy do pokoje uklidit si věci a doobléknout se."
        show a neutral
        "Adrian leží na posteli a kouká do mobilu."
        hide a neutral
        "Rozejdeš se tedy ke svým věcem. Adrian zvedne oči od mobilu."
        show a neutral
        "..."
        hide a neutral
        j "Můžeš se prosím otočit? Potřebovala bych se převlíknout."
        show a neutral
        "Jo, promiň."
        hide a neutral
        "Vyndáš podprsenku natočíš se směrem k zataženému oknu, zády k Adrianovi. Sundáš si tričko, nandáš si podprsenku a oblíkneš si tričko."
        "Zapojíš si mobil do zásuvky a z papírové kapsičky na vstupní kartu opíšeš heslo na wifi."
        "Natáhneš se do postele a napíšeš domů."
        "Zkontroluješ 'socky'."
        "Během chvíle vyjde z koupelny Sučan."
        show a neutral
        a "Adriane, můžeš."
        hide a neutral
        "Řekne klidně a jde si ke svým věcem."
        "Adrian odloží mobil a přesune se do koupelny."
        "Zůstala jsi na pokoji sama se Sučanem."
        show s neutral
        s "Promiň, vím, že nejsi malá holka, ale vážně si myslíš, že je dobré pobíhat polonahá na pokoji s cizím klukem?"
        hide s neutral
        j "Tak za prvé, nebyla jsem polonahá. Za druhé, nejsi moje matka, aby si mi říkal, co mám nosit. A za třetí, s tebou se mi nic nestane, ne?"
        show s neutral
        s "Hele, já tu taky nemusím být pořád... Kdy sis oblíkla tu podprsenku?"
        hide s neutral
        j "Není to jedno? Jsem oblečená? Jsem."
        j "Spokojený?"
        show s neutral
        s "Je ti jasné, že jsem také kluk? Teď na Adriana začínám dost žárlit..."
        hide s neutral
        j "Vždyť jsem ti jen vyšla vstříc. Oblíkla se."
        "Váš rozhovor přeruší přicházející Adrian."
        show a neutral
        a "Vyrušil jsem vás u něčeho?"
        hide a neutral
        show s neutral
        s "Ne."
        hide s neutral
        show a neutral
        a "Dobře?"
        hide a neutral
        "Řekne nevěřícně."
        "Koukneš na mobil a zjistíš, že za chvíli je čas na večeři."
        "Vezmeš si kosmetickou taštičku a zapluješ do koupelny."
        scene bg koupelna
        "Upravíš se a lehce se nalíčíš."
        "Vylezeš ven."
        scene bg dvojluzak separe
        j "Asi je pomalu čas jít."
        "Vlezeš do pokoje a oba divně zmlknou."
        "Ale vypadá to, že se o něco dohadovali."
        "Dojdeš si k posteli sbalit věci, co si chceš vzít s sebou, a jdeš čekat před pokoj."
        "Kluci tě po chvíli následují. A vyrazíte směr recepce."
        show s neutral
        s "Jak se řekne japonsky jdeme?"
        hide s neutral
        show a neutral
        a "Ikimašó"
        hide a neutral
        show s neutral
        s "Ikimašó"
        hide s neutral
        "U každého s kluků získáváš jeden LP."
        $ j.add_love_points_for_person(a, 1)
        $ j.add_love_points_for_person(s, 1)
        "[j.show_all_points()]"
        call recepce
        # TODO
    else:
        "Zavolá Sučan a potkáte se po cestě, kdy on míří do koupelny a ty do pokoje."
        "Adrian si v posteli čte něco na mobilu."
        "Dáš si věci do kufru."
        "Z papírového obalu na vstupní kartu opíšeš heslo na wifi a napíšeš domů."
        "Natáhneš se na svoji postel a zkontroluješ 'socky'."
        "Kluci se mezitím vystřídají v koupelně."
        "Chvíli před šestou se dojdeš do koupelny trošku upravit a nalíčit."
        "Pak se sbalíš a na šestou všichni vyrazíte na recepci."
        show s neutral
        s "Jak se řekne japonsky jdeme?"
        hide s neutral
        show a neutral
        a "Ikimašó"
        hide a neutral
        show s neutral
        s "Ikimašó"
        hide s neutral
        call recepce
        call hracka_nolove
    return
