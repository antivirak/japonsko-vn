label dvojluzak_hracka_Sucan2:
    scene bg dvojluzakmanp
    "Po večeři se vrátíte na pokoj a vystřídáte se v koupelně."
    show s white
    s "Jdeš se mnou do onsenu?"
    hide s white
    menu:
        "Chceš jít do hotelového onsenu se Sučanem?"
        "Ano":
            "Vyrazíte do hotelových lázní, Sučan se od tebe oddělí a jde na druhý pokoj vyzvednout kluky."
            "Lázně jsou samozřejmě striktně rozděleny na ženské a mužské."
            # TODO samostatný label
            scene bg onsen
            menu:
                "Půjdeš doleva nebo doprava?"
                "Vlevo":
                    "Správně jsi zvolila dámský onsen. V místnosti před samotnou lázní se svlékneš donaha a své věci odložíš do jedné z proutěných krabic v regálu u stěny."
                    "Osprchuješ se a vlezeš si do horké lázně. Máš štěstí, nikdo jiný zde není. Možná je to tím, že je půl desáté večer."
                    "Po chvíli se rozhodneš, že je čas jít spát."
                    "Takže vylezeš z lázně, osprchuješ se, utřeš se, oblíkneš se a dojde ti, že kartu od pokoje má Sučan."
                    "Napíšeš mu zprávu na mobil, ale je ti jasné, že pokud je s klukama v onsenu, tak si to nepřečte."
                    scene bg chodba
                    "Vylezeš ven z lázní a vyrazíš směr pokoj. Zaklepeš."
                    "..."
                    "Ticho, nic se neozývá, takže Sučan je pravděpodobně ještě v lázních."
                    "Sedneš si na zem vedle dveří, opřeš se zády o stěnu a vytáhneš mobil."
                    "Přijde ti upozornění na zprávu."
                    s "[j.name_5p], promiň, už běžím!"
                    j "V pohodě, počkám..."
                    s "Už jsem ve výtahu, gomenasai"
                    "Za chvíli slyšíš cinknutí dveří od výtahu a Sučan si to rychle rázuje k tobě."
                    show s white
                    s "Promiň, to mi nedošlo, měl jsem kartu nechat tobě."
                    hide s white
                    "Otevře dveře a pustí tě do pokoje."
                    scene bg dvojluzakmanp
                    j "Nečekám tu dlouho, půjdu do koupelny."
                    "Vezmeš si věci na spaní a zalezeš do koupelny."
                    scene bg koupelna
                    "Převlékneš se do trička a kraťásků na spaní, odlíčíš se, vyčistíš si zuby."
                    "Poklidíš po sobě koupelnu a vylezeš ven."
                    scene bg dvojluzakmanp
                    "Sučan se mezitím převlékl do hotelových kalhot a županu. Vypadá trošku, jako by šel na kroužek bojových umění."
                    "Tahle myšlenka, tě rozesměje."
                    show s kimono
                    s "Čemu se zase směješ?"
                    hide s kimono
                    j "Že vypadáš, jak když jdeš do kroužku taekwonda!"
                    "Vyprskneš smíchy."
                    show s kimono
                    s "Nechováš se trošku jako puberťačka?"
                    hide s kimono
                    j "Možná, jsem unavená. To je možná horší, než opilá!"
                    show s kimono
                    s "Tak asi půjdeme spát, ne?"
                    hide s kimono
                    j "Jo, asi jo."
                    "Sučan zaleze ještě do koupelny, ty si mezitím uklidíš věci, dáš je pryč z postele."
                    "Dáš si nabíjet telefon a zalezeš si pod peřinu."
                    "Zjistíš, že kromě toho, že máte manželskou postel, máte společnou i peřinu..."
                    "Sučan vyjde z koupelny. Slyšíš, jak otevírá ledničku. Zvedneš zrak a vidíš, jak nese dvě sklenice studené vody."
                    show s kimono
                    s "[j.name_5p], měla bys víc pít."
                    hide s kimono
                    j "Díky."
                    "Položíš si vodu na noční stolek."
                    "Sučan si také poklidí věci, dá si mobil na nabíječku a zkontroluje pohledem pokoj."
                    show s kimono
                    s "Asi zhasnu?"
                    hide s kimono
                    j "Jo, můžeš."
                    "Protože svítí velké světlo, musí jít zhasnout až do chodbičky."
                    "Když cvakne vypínač, místností se rozlije tma. Chvíli ti trvá, než si oči přivyknou na změnu osvícení."
                    "A na základě světla z ledky klimatizace a nabíječek mobilů zvládneš rozpoznávat obrysy."
                    "Sučan přišel z chodby, evidentně po cestě zakopl o tvůj kufr, který teď leží mezi postelí a zdí."
                    s "Sakra, promiň, to byly asi tvoje věci."
                    s "Nelekni se, vezmu to radši přes postel."
                    "Cítíš, jak se ti u nohou postel lehce prohnula, a vidíš – nebo si možná spíše domýšlíš, jak Sučan po kolenou dolezl na svou stranu postele."
                    s "Kdybych byl v noci náměsíčný, tak mě vzbuď. Dobrou noc, [j.name_5p]."
                    j "Dobrou, Sučane."
                    "Otočíš se na bok, k Sučanovi zády a pokusíš se usnout."
                    "Cítíš, jak Sučan zápasí s dekou."
                    s "Aha, ona je společná, tak já ti ji nechám a budu spát jen tak. Stejně je vedro."
                    j "Díky."
                    "Ještě chvíli jsi ostražitá, jestli se něco nestane. Ani nevíš jak, ale najednou spíš."
                    "Ráno tě probudí Sučanův budík v 7."
                    show s kimono
                    s "Klidně ještě spi, je teprve sedm. Já tě vzbudím tak za 20 minut; půl hodinka ti na vstávaní stačí, ne?"
                    hide s kimono
                    "Jsi hodně rozespalá; dopadl na tebe jet-lag, takže jen zamumláš"
                    j "hmm..."
                    "A zase usneš."
                    show s white
                    s "[j.name_5p], [j.name_5p], vstávej."
                    "Říká jemně Sučan"
                    hide s white
                    "Když rozlepíš oči vidíš, že stojí u tvé strany postele s tácem, na kterém má dva hrnečky."
                    show s white
                    s "Nevěděl jsem, jestli chceš kafe nebo čaj, tak jsem udělal oboje. Tak si vyber."
                    s "Snídani máš na nočním stolku."
                    hide s white
                    j "Díky,"
                    "broukneš rozespale."
                    show s white
                    s "Koukal jsem na internetu, že tu má být nějaký obchod s modely aut."
                    s "Půjdu se tam podívat. Tak se nasnídej, nechávám ti tu kartu a v osm dole na recepci."
                    hide s white
                    j "Jo."
                    "Teprve při zabouchnutí dveří ti dojde obsah jeho slov."
                    "Vypiješ čaj i kafe, sníš lívance, co sis včera koupila ke snídani."
                    "Dojdeš si na záchod, osprchneš se, vyčistíš si zuby, nalíčíš se, oblíkneš se a umyješ po sobě hrnečky."
                    "A máš to jen tak tak, aby ses sbalila a přesunula se na recepci."
                    "Získáváš jeden LP u Sučana."
                    $ j.add_love_points_for_person(s, 1)
                    "[j.show_all_points()]"
                "Vpravo":
                    "Vlezla jsi do pánské sekce!"
                    "Úchyláku!"
                    "Hra zde končí. Příště to zkus jinak."
                    $ j.increment_gaijin_points(1000)
                    "[j.show_all_points()]"
                    jump titulky
        "Ne":
            "Dojdeš si vyčistit zuby, převlékneš se do pyžama – trička a kraťásek."
            show s white
            s "Tak já jdu s klukama do onsenu. Vezmu si kartu, ať tě v noci nebudím."
            hide s white
            j "Jo, jasně, díky."
            "Když odejde, uklidíš si věci z postele, dáš si nabít mobil a natáhneš se do postele."
            "Zjistíš, že kromě manželské postele máte ještě společnou i peřinu."
            "Přikryješ se a jdeš spát."
            if j.love_points.get(d.name, 0) > 0:
                "Už skoro spíš, když někdo klepe na dveře."
                "Chvíli ti trvá, než se doopravdy probereš."
                j "Už jdu!"
                "křikneš, vstaneš z postele, rozsvítíš a otevřeš dveře."
                "Ale za dveřmi nikdo nestojí. Rozhlížíš se po chodbě, ale ta je prázdná."
                "Už chceš naštvaně zabouchnout dveře, když si všimneš, že na zemi leží obálka."
                "[j.name]"
                "Je na ní krasopisně tvé jméno, tak ji zvedneš a zabouchneš dveře."
                "Na chodbičce u koupelny ji otevřeš. Vevnitř na tvrdém dopisním papíře jsou tři řádky."
                "Krásné oči září,"
                "úsměv jak slunce svítí,"
                "v Japonsku s námi."
                "Chvíli na to nechápavě hledíš, a pak ti dojde, že jde o haiku –"
                "japonskou poezii, která si hraje s volným veršem a více hledí na melodičnost a vyznění."
                "Vyznačuje se tvarem 5, 7 a 5 slabik."
                "Chvíli si dopis ještě prohlížíš, jestli ti něco neuniklo. Celý text je vykreslen krásným psacím písmem."
                "Byl pravděpodobně psaný s lehkostí a precizností, protože ačkoli byl psán perem, nikoli propiskou, tak všechny linie jsou krásně hladké."
                "Ještě jednou vykoukneš na chodbu, ale tam nikdo není. Dokonce se až s tvým otevřením dveří se spustí fotobuňka světlem."
                "Dopis uložíš zpátky do obálky, hodíš si ji do kufru a jdeš si zase lehnout."
            "Ačkoli se Sučan snaží být potichu, vzbudí tě, když zakopne o tvůj kufr s věcmi mezi postelí a zdí."
            s "Sakra!"
            "V pokoji je tma."
            j "Proč si nerozsvítíš?"
            s "Nechtěl jsem tě budit."
            j "Možná by mě to světlo budilo míň, než ten hluk."
            "Slyšíš, jak jde do chodbičky. Klapne vypínač a ty v tu ránu musíš zavřít oči, protože tě oslepilo pokojové osvětlení."
            j "Co v onsenu?"
            show s kimono
            s "Jo, bylo to super, myslím, že toho využiju i zítra."
            hide s kimono
            "Teprve teď jsi se rozkoukala a vidíš, že se Sučan mezitím převlékl do hotelových kalhot a županu."
            # TODO move to label to reference from both options
            "Vypadá trošku, jako by šel na kroužek bojových umění."
            "Tahle myšlenka tě rozesměje."
            show s kimono
            s "Čemu se zase směješ?"
            hide s kimono
            j "Že vypadáš, jak když jdeš do kroužku taekwonda!"
            "Vyprskneš smíchy."
            show s kimono
            s "Nechováš se trošku, jako puberťačka?"
            hide s kimono
            j "Možná, jsem unavená. To je možná horší, než opilá!"
            show s kimono
            s "Tak asi půjdeme spát, ne?"
            hide s kimono
            j "Jo, asi jo."
            "Sučan zajde do chodbičky a slyšíš jak otevírá ledničku a přinese sobě i tobě studenou vodu."
            show s kimono
            s "[j.name_5p], měla by si víc pít. Máš otlačený polštář na tváři."
            hide s kimono
            j "Super... Díky."
            "Položíš si vodu na noční stolek."
            "Sučan si poklidí věci, dá si mobil na nabíječku, zkontroluje pohledem pokoj."
            show s kimono
            s "Asi zhasnu?"
            hide s kimono
            j "Jo, můžeš."
            "Protože svítí velké světlo, musí jít zhasnout až do chodbičky."
            "Když cvakne vypínač místností se rozlije tma, chvíli ti trvá, než si oči přivyknou na změnu osvícení."
            "A na základě světla z klimatizace, nabíjecích mobilů zvládneš rozpoznávát obrysy."
            "Sučan přišel z chodby."
            s "Po druhé to riskovat nebudu."
            s "Nelekni se, vezmu to radši přes postel."
            "Cítíš, jak se ti u nohou postel lehce prohnula, a vidíš nebo si možná spíše domýšlíš, jak Sučan po kolenou dolezl na svou stranu postele."
            s "Kdybych byl v noci náměsíčný, tak mě vzbuď, a jinak dobrou noc, [j.name_5p]."
            j "Dobrou, Sučane."
            "Otočíš se na bok k Sučanovi zády a pokusíš se usnout."
            "Cítíš, jak Sučan zápasí s dekou."
            s "Aha, ona je společná, tak já ti ji nechám a budu spát jen tak, stejně je vedro."
            j "Díky."
            "Ještě chvíli jsi ostražitá, jestli se něco nestane a nevíš jak, ale najednou spíš."
            "Ráno tě probudí Sučanův budík v 7."
            show s kimono
            s "Klidně ještě spi je teprve sedm. Já tě vzbudím tak za 20 minut, půl hodinka ti na vstávaní stačí ne?"
            hide s kimono
            "Jsi hodně rozespalá, dopadl na tebe jet-lag takže jen zamumláš"
            j "hmm..."
            "A zase usneš."
            show s white
            s "[j.name_5p], [j.name_5p], vstávej."
            "Říká jemně Sučan"
            hide s white
            "Když rozlepíš oči vidíš, že stojí u tvé strany postele s tácem, na kterém má dva hrnečky."
            show s white
            s "Nevěděl jsem jestli chceš kafe, nebo čaj, tak jsem udělal oboje, tak si vyber."
            s "Snídani máš na nočním stolku."
            hide s white
            j "Díky"
            "Broukneš rozespale."
            show s white
            s "Koukal jsem na internetu, že tu má být nějaký obchod s modely aut."
            s "Tak se tam půjdu asi podívat, tak se nasnídej, nechávám ti tu kartu a v osm dole na recepci."
            hide s white
            j "Jo."
            "Teprve při zabouchnutí dveří ti dojde obsah jeho slov."
            "Vypiješ čaj i kafe sníš lívance, co sis včera koupila k snídani."
            "Dojdeš si na záchod, osprchneš se, vyčistíš si zuby, nalíčíš se, oblékneš se a umyješ po sobě hrnečky."
            "A máš to jen tak tak, aby ses sbalila a přesunula se na recepci."
            "Získáváš jeden LP u Sučana."
            $ j.add_love_points_for_person(s, 1)
            "[j.show_all_points()]"
    return

label dvojluzak_hracka_Dante2:
    scene bg dvojluzakmanp
    "Po večeři se vrátíte na pokoj a vystřídáte se v koupelně."
    show d black
    d "Jdeš do onsenu?"
    hide d black
    menu:
        "Chceš jít do hotelového onsenu?"
        "Ano":
            j "Jo půjdu to zkusit, když je máme v ceně."
            show d black
            d "V tom případě si vem kartu od pokoje, ať se sem pak dostaneš."
            hide d black
            j "Jo díky. Ty nejdeš?"
            show d black
            d "Ne ne, mám ještě nějakou práci."
            hide d black
            "Vezeš si kabelku a vyrazíš do onsenu."
            "Lázně jsou samozřejmě striktně rozděleny na ženské a mužské."
            "Na chodbě před vstupem nikoho nevidíš"
            # TODO samostatný label
            scene bg onsen
            menu:
                "Půjdeš doleva nebo doprava?"
                "Vlevo":
                    "Správně jsi zvolila dámský onsen. V místnosti před samotnou lázní se svlékneš donaha a své věci odložíš do jedné z proutěných krabic v regálu u stěny."
                    "Osprchuješ se a vlezeš si do horké lázně. Máš štěstí, nikdo jiný zde není. Možná je to tím, že je půl desáté večer."
                    "Po chvíli se rozhodneš, že je čas jít spát."
                    "Takže vylezeš z lázně, osprchuješ se, utřeš se, oblíkneš se a vyrazíš zpátky na pokoj."
                    scene bg chodba
                    "Odemkneš pomocí karty a velmi pomalu otevíráš dveře."
                    j "[d.name_5p], už jsem zpátky, můžu dovnitř?"
                    d "Jo pojď."
                    scene bg dvojluzakmanp
                    "Vlezeš tedy dovnitř a zavřeš za sebou dveře."
                    "Dante sedí u stolečku u okna a něco dělá na notebooku."
                    "Dáš si kabelku na postel, vyndáš si pyžamo a věci na večerní rutinu."
                    j "Půjdu ještě do koupelny, nevadí?"
                    show d black
                    d "Ne, běž."
                    hide d black
                    show bg koupelna
                    "Zalezeš si do koupelny, zamkneš se dojdeš si na záchod, odlíčíš se, umyješ si obličej, učešeš, vyčistíš si zuby ... a převlíkneš se"
                    show bg dvojluzakmanp
                    "Vylezeš ven a [d.name] stále hledí do počítače. A něco píše."
                    "Jdeš si uklidit věci a sundáš si kufr z postele, dáš si mobil na nabíječku a natáhneš se do postele."
                    show d black
                    d "Už chceš jít spát?"
                    hide d black
                    j "Jo už asi jo, dolehl na mě jet-lag, a také je už docela pozdě."
                    show d black
                    d "Dobře."
                    hide d black
                    "Ještě něco rychle dopíše, pak zacvakne notebook, šáhne do kufru pro věci, jde do chodbičky, zhasne, a slyšíš, jak zalezl do koupelny a cvaknul zámek."
                    "V místnosti je docela tma, jen klimatizace a elektronika vydávají jemné světlo."
                    "Rozhodneš se přikrýt a zjistíš, že i pokrývka je společná. Takže se přikryješ jen zlehka a kouskem."
                    "Nevíš, jak a kdy jsi usnula, ale vzbudí tě až to, že se prohnula postel, když si Dante lehl do postele."
                    d "[j.name_5p], spíš? Dobrou."
                    j "Dobrou Dante."
                    "V noci se ještě jednou vzbudíš, a zjistíš, že jsi zády nalepená na Dantem,"
                    "odsuneš se zkontroluješ rozložení postele a zjistíš, že jsi spala na jeho půlce postele."
                    "Odskočíš si a usneš hodně na kraji své půlky postele."
                    "Ráno ti zazvoní budík, vstaneš, rozhlídneš se po pokoji a Dante nikde, na jeho straně postele najdeš lísteček."
                    "Kde je napsáno tiskacím písmem:"
                    "Šel jsem si zaběhat přijdu v 7:30, bylo by fajn kdyby byla volná koupelna. Díky D."
                    j "Blázen."
                    "Rozhodneš se mu vyjít vstříc, takže nejdříve zamíříš do koupelny. Rychle se osprchneš, usušíš, nalíčíš, učešeš, převlíkneš se."
                    "Vylezeš ven z ledničky si vyndáš snídani a jdeš se najíst."
                    "Je přesně 7:30, když uslyšíš, jak se odemkly dveře a Dante vstoupí dovnitř."
                    show d run
                    d "Můžu jít do koupelny?"
                    hide d run
                    "Zeptá se zatímco, si ještě protahuje ruce."
                    j "Jo, je tam volno."
                    show d run
                    "Super, díky."
                    hide d run
                    "Usměje se na tebe, dojde si do pokoje pro věci a zapadne do koupelny."
                    "Ty mezitím dosnídáš, uklidíš po sobě a jdeš si uvařit kafe."
                    j "Dante, jdu si dělat kafe, chceš taky? Je tu nějaké od hotelu."
                    "Zavoláš na Danteho do koupelny."
                    d "Jo, díky."
                    "Zkontroluješ, že v konvici je voda. A naštěstí je. Uděláš dvě kávy."
                    "Dante se mezitím vykoupe, otevře dveře a ještě si otírá vlasy ručníkem, když vykoukne ven."
                    "Na sobě už má zase černé tričko a kraťasy. Svaly má naběhlé více než normálně."
                    show d black
                    d "Díky, za kávu [j.name_5p]"
                    hide d black
                    "Ručník pověsí na držák v koupelně, vezme si své úhledně složené prádlo, a přesune se do pokoje."
                    "Ty si dopiješ kávu a využiješ toho, že máš ještě chvilku času a vyčistíš si zuby, a ještě se jemně doupravíš."
                    "Když vyjdeš do pokoje pro věci, Dante má připravený batoh s věcmi na stolečku a vypadá, že čeká na tebe."
                    "Jdeš si tedy pobalit"
                    "A on mezitím umyje hrnečky po snídani."
                    show d black
                    d "Můžeme?"
                    hide d black
                    j "Jo."
                    "Oba si vezmete baťůžky a vyrazíte na recepci."
                    $ j.add_love_points_for_person(d, 1)
                    "[j.show_all_points()]"

                "Vpravo":
                    "Vlezla jsi do pánské sekce!"
                    "Úchyláku!"
                    "Hra zde končí. Příště to zkus jinak."
                    $ j.increment_gaijin_points(1000)
                    "[j.show_all_points()]"
                    jump titulky
        "Ne":
            j "Ne, je pozdě a já jsem unavená, ty jdeš?"
            show d black
            d "Ne ne, mám ještě nějakou práci."
            hide d black
            "Dojdeš se převlíknout do pyžama a odlíčit do koupelny."
            "Když vylezeš Dante něco klape na notebooku. Uklidíš si věci a natáhneš se na postel."
            j "Nejsi tady na dovolené?"
            show d black
            d "No ne tak úplně...Ale tím se netrap."
            "Zaklapne notebook."
            hide d black
            "Samozřejmě o to více tě zajímá, co Dante přijel do Japonska dělat, celou dobu je tak tajemný."
            "A zároveň se chová, jako pan dokonalý z nějakého přitroublého amerického filmu."
            j "Počkej, počkej to mě zajímá. Proč tu jsi?"
            show d black
            d "Kdybych ti to řekl, tak bych tě musel zabít."
            "Řekne s kamennou tváří."
            hide d black
            j "No jasně, tak si to nech pro sebe ty tajnůstkáři."
            "A začneš se smát."
            show d black
            d "Myslíš, že žertuju?"
            hide d black
            j "Popravdě? Spíš v to doufám, že nejsem na pokoji s nějakým šílencem."
            show d black
            d "Jestli se se mnou bojíš, můžu se prohodit například se Sučanem, s tím se znáš od dětství, ne?"
            hide d black
            j "Vážně v deset hodin večer? To asi ne, navíc své rozhodnutí měnit nehodlám, ale slib mi, že se dožiju rána."
            "Hodíš po něm polštářem."
            "Velmi hbitě a elegantně ho chytí."
            show d black
            d "Tak do zítra bych tě žít nechat mohl. Navíc, jsem si zatím nevybral, jak tě potrestám, za nedodržení pravidel."
            hide d black
            "Polštář ti položí k nohám na postel. Vezme si věci a zajde do koupelny."
            j "Vždyť si to na mě nahrál, to neplatí!"
            "Dante po chvíli, vychází ven z koupelny v pyžamu."
            show d pyjama
            d "Ty pravidla sis nastavila sama a já je neporušil."
            hide d pyjama
            "Zase si věci srovná do poličky, dá si mobil na nabíječku."
            "Šáhne do batohu a vyndá si knížku."
            show d pyjama
            d "Věř tomu nebo ne, já mám radši život bez pravidel."
            hide d pyjama
            "Natáhne se na postel a začne si číst."
            j "Co to čteš?"
            show d pyjama
            d "Nějaký thriller."
            hide d pyjama
            j "Aha."
            show d pyjama
            d "Chceš abych četl nahlas?"
            hide d pyjama
            j "Naposledy mi četla mamka, když jsem byla malá, ale jo, jestli ti to neva."
            show d pyjama
            d "A tak Marylin uložila dítě do postýlky v patře, zapla chůvičku a sešla dolů do kuchyně."
            "Začne Dante číst nahlas, jeho hlas je opravdu krásný a styl čtení je skoro jako rozhlasová hra."
            d "Když Marylin došla do kuchyně, začala mít pocit, že je něco špatně, že je něco jinak, než by mělo být."
            "Hledíš mu do tváře a posloucháš."
            d "Rozhlédla se po místnosti a její pohled ulpěl na držáku na nože. Přísahala by, že po večeři všechny nože umyla a uložila na místo."
            d "Držák však byl nyní prázdný. 'Je tu někdo?' zvolala oparně po místnosti. Opovědí jí bylo ticho..."
            "Dante se na chvíli dramaticky odmlčí."
            d "'To se mi muselo jen zdát,' pomyslí si. Jak nesnášela být v jejich velkém rodinném domě sama. Avšak Thomas odjížděl na pracovní cesty čím dál častěji."
            d "A tak Marylin zůstávala se svou malou dcerkou jménem [j.name] sama ve velkém domě na předměstí Phoenixu."
            d "Jé, ta malá se jmenuje stejně jako ty."
            "Přeruší Dante na chvíli čtení"
            hide d pyjama
            j "Nepřestávej, je to napínavý."
            show d pyjama
            "To jsem netušil, že tě ta knížka tak zaujme."
            hide d pyjama
            j "Já si myslím, že svou zásluhu na tom má forma podání, ale čti už, prosím, Dante."
            "A tak čte Dante dál a přečte ti asi 20 stránek, ale ke konci začínáš být hodně unavená a začneš usínat."
            show d pyjama
            d "A tak Marylin s dcerkou v náručí..., lesem.... a větvičky stromů jí... do obličeje..."
            d "[j.nape5p], spíš?"
            hide d pyjama
            j "Promiň Dante, asi ano. Poslední, co si pamatuji, je, že vyběhla zadním vchodem s malou."
            show d pyjama
            d "Tak to nevadí, stejně už je pozdě. Dobrou noc, [j.name_5p]"
            hide d pyjama
            "Zavře knihu a odloží ji na noční stolek."
            j "Dobrou noc, Dante."
            "Dante vstane a jde zhasnout. Ty se chceš přikrýt a zjišťuješ, že deka je společná."
            "Zhasne."
            "Přikryješ se tedy jen kouskem, jen tak zlehka."
            "Cítíš, jak si Dante lehl do postele"
            "V noci se ještě jednou vzbudíš a zjistíš, že jsi zády nalepená na Dantem."
            "Odsuneš se, zkontroluješ rozložení postele a zjistíš, že jsi spala na jeho půlce postele."
            "Odkulíš se a usneš hodně na kraji své půlky postele."
            "Ráno ti zazvoní budík, vstaneš, rozhlédneš se po pokoji, ale Dante nikde. Na jeho straně postele najdeš lísteček,"
            "kde je napsáno tiskacím písmem:"
            "Šel jsem si zaběhat, přijdu v 7:30. Bylo by fajn, kdyby byla volná koupelna. Díky D."
            j "Blázen."
            "Rozhodneš se mu vyjít vstříc, takže nejdříve zamíříš do koupelny. Rychle se osprchneš, usušíš, nalíčíš, učešeš, převlékneš."
            "Vylezeš ven, z ledničky si vyndáš snídani a jdeš se najíst."
            "Je přesně 7:30, když uslyšíš, jak se odemkly dveře a Dante vstoupí dovnitř."
            show d run
            d "Můžu jít do koupelny?"
            hide d run
            "zeptá se, zatímco si ještě protahuje ruce."
            j "Jo, je tam volno."
            show d run
            "Super, díky."
            hide d run
            "Usměje se na tebe, dojde si do pokoje pro věci a zapadne do koupelny."
            "Ty mezitím dosnídáš, uklidíš po sobě a jdeš si uvařit kafe."
            j "Dante, jdu si dělat kafe, chceš taky? Je tu nějaké od hotelu,"
            "zavoláš na Danteho do koupelny."
            d "Jo, díky."
            "Zkontroluješ, že v konvici je voda. A naštěstí je. Uděláš dvě kávy."
            "Dante se mezitím vykoupe, otevře dveře a ještě si otírá vlasy ručníkem, když vykoukne ven."
            "Na sobě už má zase černé tričko a kraťasy. Svaly má naběhlé více než normálně."
            show d black
            d "Díky, za kávu [j.name_5p]"
            hide d black
            "Ručník pověsí na držák v koupelně, vezme si své úhledně složené prádlo a přesune se do pokoje."
            "Ty si dopiješ kávu a využiješ toho, že máš ještě chvilku času. Vyčistíš si zuby, a ještě se jemně doupravíš."
            "Když vyjdeš do pokoje pro věci, Dante má připravený batoh se svými věcmi na stolečku a vypadá, že čeká na tebe."
            "Jdeš si tedy pobalit."
            "A on mezitím umyje hrnečky po snídani."
            show d black
            d "Můžeme?"
            hide d black
            j "Jo."
            "Oba si vezmete baťůžky a vyrazíte na recepci."
            $ j.add_love_points_for_person(d, 1)
            "[j.show_all_points()]"
    return

label dvojluzak_hracka_Adrian2:
    scene bg dvojluzakmanp
    "Po večeři se vrátíte na pokoj a vystřídáte se v koupelně."
    show a neutral
    a "Jdeš do onsenu?"
    hide a neutral
    menu:
        "Chceš jít do hotelového onsenu?"
        "Ano":
            "Vyrazíte do hotelových lázní."
            scene bg onsen
            "Lázně jsou samozřejmě striktně rozděleny na ženské a mužské."
            menu:
                "Půjdeš doleva nebo doprava?"
                "Vlevo":
                    show a neutral
                    a "Počkej, dám ti kartu. Nevím, kdo bude rychlejší. Ale nechci, aby si čekala na chodbě."
                    hide a neutral
                    "Podá ti kartu od pokoje a rozejde se k druhým dveřím."
                    "Správně jsi zvolila dámský onsen. V místnosti před samotnou lázní se svlékneš donaha a své věci odložíš do jedné z proutěných krabic v regálu u stěny."

                "Vpravo":
                    "Rozejdeš se ke dveřím vpravo. Na to tě Adrian jemně chytí za zapěstí."
                    show a neutral
                    a "Počkej, dámské jsou nalevo."
                    hide a neutral
                    $ j.increment_gaijin_points(1)
                    "Získáváš 1 GP"
                    "[j.show_all_points()]"
                    j "Jé, děkuji, to by byl trapas."
                    show a neutral
                    a "Ještě ti dám kartičku od pokoje, ať na mě nemusíš čekat."
                    hide a neutral
                    "Podá ti kartu od pokoje a rozejde se k druhým dveřím."
                    "Díky Adrianovu jsi správně zvolila dámský onsen. V místnosti před samotnou lázní se svlékneš donaha a své věci odložíš do jedné z proutěných krabic v regálu u stěny."

            "Osprchuješ se a vlezeš si do horké lázně. Máš štěstí, nikdo jiný zde není. Možná je to tím, že je půl desáté večer."
            "Po chvíli se rozhodneš, že je čas jít spát."
            "Osprchuješ se, oblékneš se. A vyrazíš na pokoj."
            scene bg chodba
            "Vyjedeš nahoru výtahem a když se otevřou dveře výtahu vidíš, že u pokoje sedí na zemi opřený zády o stěnu Adrian."
            "Když přijdeš blíže, vidíš že má zavřené oči."
            j "Adriane, proč si mi nenapsal?"
            "Otevře oči a usměje se."
            show a neutral
            "Nechtěl jsem tě uhánět. Čekám tu jen chvíli."
            hide a neutral
            "Začne se zvedat a ty odemkneš."
            "Vstoupili jste do pokoje."
            scene bg dvojluzakmanp
            show a neutral
            a "Běž do koupelny první, počkám. Teda pokud chceš. Vrátili jsme se zrovna z onsenu, ale chci si vyčistit zuby."
            hide a neutral
            j "Jo, půjdu, ale nemusíš být tak přehnaně ohleduplný."
            show a neutral
            a "Promiň"
            hide a neutral
            "Vezmeš si věci na spaní."
            "On mezitím natočí do konvice vodu."
            show a neutral
            a "Nedáš si čaj?"
            hide a neureal
            j "Asi ne, jen vodu, plánuju jít už spát."
            "S věcmi se přesuneš do koupelny a věnuješ se svému každovečernímu rituálu."
            "Když vyjdeš ven, Adrian sedí u stolu a pije čaj. Na tvém nočním stolku se objevila sklenička s vodou."
            j "Můžeš."
            show a neutral
            a "Děkuji, sluší ti to."
            hide a neutral
            "Cítíš, jak se ti do obličeje hrne krev."
            j "Díky za kompliment a vodu."
            show a neutral
            a "Za pravdu se neděkuje. A ta voda je maličkost."
            "Odloží hrneček s čajem, vezme si z postele připravené věci a vyrazí do koupelny."
            "Ty se napiješ, uložíš si věci do kufru a zalezeš si do postele."
            "Chceš si připravit peřinu a zjistíš, že je pouze jedna společná."
            "Natáhneš se do postele a čteš si něco na mobilu."
            "Adrian mezitím vyjde z koupelny. Uloží si věci k sobě do tašky."
            show a neutral
            a "Nemám přeci jen spát na zemi? Koukám, že i přikrývka je společná."
            hide a neutral
            j "Ne, a jestli máš problém s přikrývkou, mám cestovní ručník, můžu se přikrýt tím."
            show a neutral
            a "Dobře, ale kdyby ti cokoliv vadilo, tak si řekni. Nečekal jsem, že budu sám s holkou na pokoji hned první večer dovolené."
            hide a neutral
            j "Neboj, řeknu."
            "Natáhne se do postele vedle tebe."
            "A když zvedneš oči od telefonu, že bys chtěla pokračovat v konverzaci, tak zjistíš, že Adrian usnul."
            "Dáš si nabíjet mobil vedle Adrianova, zhasneš a pokusíš se také usnout."
        "Ne":
            "Dojdeš si vyčistit zuby, převlékneš se do pyžama – trička a kraťásek."
            show a neutral
            a "Tak já jdu s klukama do onsenu. Vezmu si kartu, ať tě v noci nebudím."
            hide a neutral
            j "Jo, jasně, díky."
            "Když odejde, uklidíš si věci z postele, dáš si nabít mobil a natáhneš se do postele."
            "Zjistíš, že kromě manželské postele máte ještě společnou i peřinu."
            "Přikryješ se a jdeš spát."
            if j.love_points.get(d.name, 0) > 0:
                "Už skoro spíš, když někdo klepe na dveře."
                "Chvíli ti trvá, než se doopravdy probereš."
                j "Už jdu!"
                "křikneš, vstaneš z postele, rozsvítíš a otevřeš dveře."
                "Ale za dveřmi nikdo nestojí. Rozhlížíš se po chodbě, ale ta je prázdná."
                "Už chceš naštvaně zabouchnout dveře, když si všimneš, že na zemi leží obálka."
                "[j.name]"
                "Je na ní krasopisně tvé jméno, tak ji zvedneš a zabouchneš dveře."
                "Na chodbičce u koupelny ji otevřeš. Vevnitř na tvrdém dopisním papíře jsou tři řádky."
                "Krásné oči září,"
                "úsměv jak slunce svítí,"
                "v Japonsku s námi."
                "Chvíli na to nechápavě hledíš, a pak ti dojde, že jde o haiku –"
                "japonskou poezii, která si hraje s volným veršem a více hledí na melodičnost a vyznění."
                "Vyznačuje se tvarem 5, 7 a 5 slabik."
                "Chvíli si dopis ještě prohlížíš, jestli ti něco neuniklo. Celý text je vykreslen krásným psacím písmem."
                "Byl pravděpodobně psaný s lehkostí a precizností, protože ačkoli byl psán perem, nikoli propiskou, tak všechny linie jsou krásně hladké."
                "Ještě jednou vykoukneš na chodbu, ale tam nikdo není. Dokonce se až s tvým otevřením dveří se spustí fotobuňka světlem."
                "Dopis uložíš zpátky do obálky, hodíš si ji do kufru a jdeš si zase lehnout."
            "Vzbudí tě až Adrian, který lehce zatáhl za přikrývku, kterou jsi měla na sobě."
            show a neutral
            a "Promiň, myslel jsem, že máme každý svou. Nechtěl jsem tě vzbudit."
            hide a neutral
            j "To nevadí, počkej, uvolním ti ji."
            "Otočíš se k němu. A začneš se vymotávat z přikrývky, abys mu uvolnila jeho půlku."
            show a neutral
            a "To je dobré, nech to, zvládnu to bez ní."
            hide a neutral
            "Natáhne se do postele vedle tebe, hodně ke kraji."
            show a neutral
            a "Dobrou, [j.name_5p]."
            hide a neutral
            j "Dobrou, Adriane."
            "Oba usnete."
    "Ráno tě probudí, zvuk budíku, ale ne tvého. Adrianův mobil zvoní na celý pokoj."
    show a neutral
    a "Promiň, to jsem nechtěl, už to vypínám. Omlouvám se, mrzí mě to,"
    hide a neutral
    "špitá, zatímco se přes tebe naklání k tvému nočnímu stolku, aby vypl ten budík."
    "Když ho konečně vypne, je nad tebou nakloněný, a podívá se ti do očí."
    "Vaše obličeje jsou od sebe vzdáleny jen pár centimetrů. Zadíváš se mu do očí."
    "Má je krásně modré a i když je rozespalý, tak jsou vlídné."
    show a neutral
    a "Ještě jednou se omlouvám, nedošlo mi, že když dám mobil u tebe nabíjet, tak tu bude řvát budík na celou místnost."
    hide a neutral
    j "V pořádku."
    "Adrianovi asi dojde, v jaké pozici se nachází, protože najednou vytřeští oči a rychle z tebe sleze na svou polovinu postele."
    "Vezmeš si svůj mobil a podíváš se kolik je. 7:22, takže za cca půl hodiny máte být na recepci. Chtěla si vstávat v 7:00."
    "Ale z nějakého důvodu ti nezazvonil budík."
    j "To už je tolik? Já jsem chtěla vstávat v sedm."
    show a neutral
    a "Promiň, to jsem nevěděl."
    hide a neutral
    "Vyskočíš z postele, čapneš věci na převlečení a zapluješ do koupelny."
    "Rychle si dojdeš na záchod, osprchuješ se, vyčistíš zuby, učešeš se nalíčíš, oblíkneš a vylezeš ven."
    "Adrian už je převlečený, sbalený a snídá."
    "Jdeš si sbalit věci s sebou, vyndáš snídani a naházíš ji do sebe."
    "Adrian mezitím navštíví koupelnu."
    "Když finishuješ se snídaní, tak vyleze ven a je akorát čas k odchodu, abyste nepřišli pozdě na ranní sraz."
    "Vezmete si věci a vyrazíte k výtahu."
    scene bg chodba
    "Ve výtahu ti vyklouzne z ruky karta, tak se pro ni sehneš."
    "Samozřejmě se sehnul i Adrian a byl rychlejší, takže místo karty ses dotkla jeho ruky."
    show a neutral
    "Na."
    hide a neutral
    "Řekne a podává ti spadlou kartu."
    j "Děkuji."
    "Oba se narovnáte a mlčíte až do chvíle, kdy se dostanete na recepci."
    $ j.add_love_points_for_person(a, 1)
    "[j.show_all_points()]"
    return

label hracka_nolove:
    scene bg hoteltokio
    menu:
        "Chceš jít do hotelového Onsenu?"
        "Ano":
            "Přijdeš na pokoj, odložíš si věci a vyrazíš do hotelových lázní."
            "Samozřejmě jsou striktně rozděleny na ženské a mužské."
            scene bg onsen
            menu:
                "Půjdeš doleva nebo doprava?"
                "Vlevo":
                    "Správně si zvolila dámský onsen. V místnosti před samotnou lázní se svlékneš donaha a své věci odložíš do jedné z proutěných krabic v regálu u stěny."
                    "Osprchuješ se a vlezeš si do horké lázně. Máš štěstí, nikdo jiný zde není."
                    "Po chvíli se rozhodneš, že je čas jít spát."
                "Vpravo":
                    "Vlezla si do pánské sekce!"
                    "Úchyláku!"
                    "Hra zde končí."
                    jump titulky
        "Ne":
            "Dojdeš si vyčistit zuby, převlíkneš se do pyžama a jdeš spát."
    return
