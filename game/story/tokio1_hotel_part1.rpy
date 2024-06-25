label tokio1_hotel_part1:

    menu:
        #pracovně sem hodím menu na ty pokoje, ať se to dá zkoušet
        "S kým budeš na pokoji?"
        "Dvojlůžák se Sučanem":
            jump hracka_Sucan
        "Dvojlůžák s Mimoněm":
            jump hrac_ka_Mimon
        "Dvojlůžák s Adrianem":
            jump hracka_Adrian

    "Po rozdělení jste se rozhodli dojít na pokoje odnést si věci sraz máte v 18 h na recepci, půjdete společně na večeři."

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
        "Dát mu šanci":
            jump sucansance

label sucanvoutu:
    j "Jó jasně, určitě si taky pamatuješ, že jsi ty zásnuby asi v sedmi zrušil, protože sis našel v první třídě Terezku."
    "Pobaveně se zasměješ"
    j "Hele, radši odemkni pokoj a nech si ty blbý fóry od cesty."
    show s neutral at left
    s "Au, to bolelo, ale když si to přeješ."
    "Odemkne kartou pokoj a pustí tě dovnitř."
    hide s neutral
    scene bg dvojluzaksepare
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
            $ j.gaijin_points += 1
            "Získáváš jeden GP!"
            "[j.show_all_points()]"
            j "Ty seš debil!"
            hide s smiling
            "Nadáváš mu, zatímco to na panelu vypíná. Pohledem přepočítáš ručníky a usoudíš, že se jeden dá použít jako hadr na podlahu."
            "Vytřeš vodu, která byla na zemi a umyješ si ruce."

label posprse:
    "Dojdeš si pro věci a vyhodíš Sučana z koupelny."
    "Dopřeješ si vytouženou horkou sprchu, po 13 hodinách letu, 2 hodinách v autě a X hodinách čekání ať už na letištích nebo jinde."
    "Po koupeli, si vyfénuješ vlasy a převlékneš se ještě v koupelně."
    scene bg dvojluzaksepare
    "Pak pustíš Sučana do koupelny."
    "A sama si vybalíš potřebné věci a uklidíš, věci z cesty."
    "A pak je pomalu čas, jít dolů na recepci a na večeři"
    jump recepce

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
    j "Levá je moje!"
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
    "Konečně máš čas prohlédnout si koupelnu."

    menu:
        "První, co tě zaujme, je typický japonský záchod s panelem na zdi."
        "Mobil s překladačem sis nechala v pokoji."
        "Panel budeš ignorovat":
            jump ignorpanel
        "Pomačkáš náhodně všechny čudlíky.":
            "Pomačkala jsi náhodně všechny čudlíky,"
            "a najednou začne cákat voda ze záchodu ven!"
            $ j.gaijin_points += 1
            "Získáváš jeden GP!"
            "[j.show_all_points()]"
            "Ještě něco pomačkáš a ono to přestane."
            "Pohledem zhodnotíš počet ručníků a rozhodneš, že se jeden dá použít jako hadr na podlahu"
            "Vytřeš potopu, co jsi způsobila."
            jump ignorpanel  # TODO necessary?

label ignorpanel:
    "Dáš si rychlou sprchu a usušíš si vlasy fénem. Ano, v Japonsku je fén základní výbava koupelny, stejně jako sprchový gel, šampón, kondicionér..."
    "...soustava ručníků, zubní kartáček, mini-pasta, hřeben, gumičky, holítka..."
    "Po sprše se rozhodneš Sučana malinko provokovat."
    "Takže i přes to, že sis s sebou vzala věci na převlečení,"
    "si vezmeš na sebe jen spodní prádlo a ručník si uvážeš kolem sebe."
    "Vezmeš svoje věci a odemkneš koupelnu."
    j "Volno!"
    scene bg dvojluzakmanp
    "Vycházíš ven s úsměvem. Zahneš doprava a objevíš se v místnůstce s postelí."
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
    hide scantily clad
    j "Plochej!"
    "Zazubíš se na něj. A pak tě napadne, jak z této situace vybruslit."
    j "Šup, oblíkej se, ať na nás kluci nečekají. Já mám už taky docela hlad!"
    $ j.add_love_points_for_person(s, 2)
    "[j.show_all_points()]"
    "Hodíš po něm polštářem zpět."
    "Oba se smějete, Sučan se oblékne. A vyrazíte dolů na recepci."
    jump recepce  # TODO implement recepce

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
    "Došli jste na pokoj 306, odemkl['a' if j.gender == 'f' else ''] jsi kartou a oddychl['a' if j.gender == 'f' else ''] sis, když jsi zjistil['a' if j.gender == 'f' else ''], že jsou postele odděleny"
    scene bg dvojluzak separe
    j "jakou chceš postel?"
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
    "Konečně máš čas prohlídnout si koupelnu."
    "První, co tě zaujme je typický japonský záchod s panelem na zdi."
    menu:
        "Mobil s překladačem sis nechal['a' if j.gender == 'f' else ''] v pokoji."
        "Panel budeš ignorovat":
            jump ignorpanel2
        "Pomačkáš náhodně všechny čudlíky.":
            "Pomačkala jsi náhodně všechny čudlíky."
            "A najednou začne cákat voda ze záchodu ven!"
            $ j.gaijin_points += 1
            "Získáváš jeden GP!"
            "[j.show_all_points()]"
            "Ještě něco pomačkáš, a ono to přestane."
            "Pohledem zhodnotíš počet ručníků a všimneš si, že na zemi je jeden původně bílý ručník..."
            "...celý červený od Mimoňovy barvy na vlasy, tzn. už se dá použít jako hadr na podlahu."
            "Vytřeš potopu, co jsi způsobila."
            jump ignorpanel2  # TODO neccesary?

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
    jump recepce


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
        a "To z mé strany, není potřeba."
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
        scene bg koupelna
        "Teď máš čas prohlédnout si koupelnu."
        "První, co tě zaujme, je typický japonský záchod s panelem na zdi."
        menu:
            "Mobil s překladačem sis nechal['a' if j.gender == 'f' else ''] v pokoji."
            "Panel budeš ignorovat":
                jump ignorpanel3
            "Pomačkáš náhodně všechny čudlíky.":
                "Pomačkal['a' if j.gender == 'f' else ''] jsi náhodně všechny čudlíky."
                "A najednou začne cákat voda ze záchodu ven!"
                $ j.gaijin_points += 1
                "Získáváš jeden GP!"
                "[j.show_all_points()]"
                "Ještě něco pomačkáš, a ono to přestane."
                "Pohledem zhodnotíš počet ručníků a rozhodneš, že se jeden dá použít jako hadr na podlahu"
                "Vytřeš potopu, co jsi způsobila."
                jump ignorpanel3
    label ignorpanel3:
        "Rychle se svlékneš a zapadneš do vany."
        "Po cestování, které si v posledních 24 hodinách absolvoval['a' if j.gender == 'f' else ''],"
        "je pořádná sprcha právě to, co nejvíce potřebuješ."
        "Po pár minutách užívání si horké koupele, usoudíš, že je čas vylézt a pustit do koupelny i Adriana."
        "Vlezeš ven, usušíš se a trochu si vyfénuješ vlasy."
        # TODO v jiných větvích jsi popisovala vybavení hotelových koupelen
        "Oblíkneš se do přineseného oblečení."
        "Zkontroluješ, že po tobě v koupelně nezůstal žádný bordel a odemkneš koupelnu."
        j "Volno!"
        "Napůl křikneš, a jdeš si uklidit věci do kufru."
        show a smile
        a "Díky,"
        hide a smile
        "řekne Adrian, vezme si věci a přesune se do koupelny."
        "Ty si uklidíš věci, z papírového obalu na vstupní kartu vyčteš heslo k wifi a napíšeš domů."
        "Natáhneš se do postele."
        "Potom otevřeš 'socky' a začteš se do toho, co se zatím děje doma."
        "Asi za deset minut vyleze Adrian."
        "Mlčky vstoupí do místnosti a jde s věcmi ke své tašce."
        show a neutral  # možná změna oblečení
        a "Máme ještě skoro hodinu do srazu."
        hide a neutral
        j "To je super. Ale začínám mít hlad."
        show a neutral
        a "Nic k jídlu nemám, ale všiml jsem si u vstupních dveří vody. Chceš ji přinýst?"
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
        "Usměješ se, a šáhneš po mobilu. A podáš mu ho."
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
        "Dojdeš si vzít tašku a vyrazíte společně na recepci"
        jump recepce

    label adrian_hotel_feministka:
        j "Nene, já si ho vezmu sama"
        "Adrian jde tedy napřed."
        "Odemkne pomocí karty, otevře dveře a pustí tě dovnitř."
        scene bg dvojluzaksepare
        "Pokoj je dvojlůžkový a postele jsou naštěstí odděleny nočním stolkem."
        show a neutral
        a "Vyber si postel, a klidně běž první do sprchy."
        hide a neutral
        j "Jo, díky."
        "Vybereš si jednu postel, popadneš věci a přesuneš se do koupelny."
        scene bg koupelna
        "Teď máš čas prohlédnout si koupelnu."
        "První, co tě zaujme, je typický japonský záchod s panelem na zdi."
        menu:
            "Mobil s překladačem sis nechal['a' if j.gender == 'f' else ''] v pokoji."
            "Panel budeš ignorovat":
                jump ignorpanel4
            "Pomačkáš náhodně všechny čudlíky.":
                "Pomačkal['a' if j.gender == 'f' else ''] jsi náhodně všechny čudlíky."
                "A najednou začne cákat voda ze záchodu ven!"
                $ j.gaijin_points += 1
                "Získáváš jeden GP!"
                "[j.show_all_points()]"
                "Ještě něco pomačkáš, a ono to přestane."
                "Pohledem zhodnotíš počet ručníků a rozhodneš, že se jeden dá použít jako hadr na podlahu."
                "Vytřeš potopu, co jsi způsobila."
                jump ignorpanel4
    label ignorpanel4:
        # TODO the same text, parametrize
        "Rychle se svlíkneš a zapadneš do vany."
        "Po cestování, které si v posledních 24 hodinách absolvovala,"
        "je pořádná sprcha právě to, co nejvíce potřebuješ."
        "Po pár minutách užívání horké koupele, usoudíš, že je čas vylézt a pustit do koupelny i Adriana."
        "Vlezeš ven usušíš se a trochu si vyfénuješ vlasy."
        "Oblíkneš se do, přineseného oblečení."
        "Zkontroluješ, že po tobě v koupelně nezůstal, žádný bordel a odemkneš koupelnu."
        j "Volno!"
        "Napůl křikneš, a jdeš si uklidit věci do kufru."
        show a neutral
        a "Děkuji!"
        hide a neztral
        "Řekne, vezme si věci a přesune se do koupelny."
        "Ty si uklidíš věci, z papírového obalu na vstupní kartu vyčteš heslo k wifi a napíšeš domů."
        "Natáhneš se do postele."
        "Potom otevřeš 'socky' a začteš se do toho, co se zatím děje doma."
        "Asi za deset minut vyleze Adrian."
        "Mlčky vstoupí do místnosti, a jde s věcmi ke své tašce."
        "Natáhne se do postele a kouká do mobilu."
        "Takhle strávíte čas do večeře."
        "Chviličku před odchodem se zastavíš v koupelně upravit."
        "Pak se sbalíte a vyrazíte na recepci."
        jump recepce

# jump titulky
