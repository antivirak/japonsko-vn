transform nighttime1:
    matrixcolor BrightnessMatrix(-.55)
transform nighttime2:
    matrixcolor TintMatrix("#7FA5F2")
    # usage: show <background> at nighttime1, nighttime2


label akt4:
    $ j.hoodie = ""  # Whose hoodie does Hracka end up with
    "Ráno jste se sešli všichni na recepci, zase bylo nutné počkat na Mimoně, který s vámi nakonec jede."
    "Pak jste šli narovnat věci do auta. Zabralo vám to víc času, než jste čekali,"
    "takže místo v 6:05 odjíždíte až v 6:20. Příjezd odhaduje navigace na 8:30."
    "Řízení se ujme Sučan."
    if j.driver:
        "Protože jsi druhá řidička, tak si sedneš na místo spolujezdce. Zapojíš mobil přes kabel do panelu, aby se navigace spojila s autem a pustíš Spotify."
        "Vzadu sedí za řidičem rozcapený Mimoň, který jen co dosedl, tak usnul. Veprostřed sedí zkroucený Adrian a za tebe si sedl Dante."
    else:
        "Sedneš si za spolujezdce – Danteho, do středu si sedne Adrian a za Sučana Mimoň. Mimoň ihned usne. Rozvalený přes celou sedačku. Adrian se zase choulí ve středu."
        "Dante připojí mobil pomocí kabelu do carplay a pustí navigaci, pak spustí spotify a playlist, který jste si připravili před odletem."
    "Pro cestu k Fuji-san jste zvolili jet po placených dálnicích. Protože každý úsek dálnice patří jiné společnosti, nemají dálniční známku."
    scene bg cestafuji4
    "Platí se vždy za projetý úsek."
    "Když jste si půjčovali auto ptali se vás v půjčovně, zda chcete ETC kartu. Za poplatek."
    "Ptali jste se, jestli je nutná. Bylo vám řečeno, že nikoliv, jen že na mýtných branách musíte do správného pruhu, kde se nachází pokladna."
    scene bg cestafuji2
    "Takže jste kartičku odmítli."
    "Ale bez problémů se vám daří najíždět a rozpoznávat nájezdy a sjezdy pro placení."
    scene bg cestafuji1
    "Dálnice je převážně na mostech a v tunelech, takže místy se otvírá krásný výhled na okolní krajinu."
    scene bg mapafuji
    "Když z dálnice sjedete kousek od Fuji, tak se dostanete na takové menší okresní silničky."
    scene bg cestafuji3
    "Cestou se koukáš z okýnka, všude je vše krásně zelené. Konečně chápeš, proč je v Anime vždy tráva tak krásně zelená:"
    "ona to totiž není tráva, ale rýže. Kterou pěstují, kde se dá."
    scene bg cestafuji6
    "Konečně se před vámi v mracích zahalená objeví Fuji."
    scene bg cestafuji5
    "A během pár minut už vyjíždíte lesem směr pátá stanice."
    "Míjíte záchytné parkoviště a po chvíli se chystáte odbočit doprava, avšak zde jsou závory. Dozvídáte se, že přes sezónu je vjezd na horní parkoviště zakázán."
    "Musíte tedy zpět na záchytné parkoviště a zaplatit si autobus nahoru."
    scene bg fuji parkoviste
    "Na parkovišti vás přivítají, vysypete se z auta pobalíte si věci a vyrazíte směr zastávka autobusů."
    "Při kupování lístků zjišťujete, že autobus nahoru jezdí v každou celou hodinu – je 8:10, takže vám zrovna autobus ujel a další jede v 9."
    "Vrátíte se tedy k autu a dáte si snídani. Ještě jednou projdete věci, co máte s sebou."
    "Takže sportovní oblečení, větrovku, roušky proti prachu při sestupu dolů, čelovky, jídlo, pití."
    "Chvíli před devátou se přesunete do autobusu."
    "Kde všichni usnete, protože jste toho moc nenaspali, navíc jste toho za poslední tři dny dost nachodili a spojení s doznívajícím jet-lagem je vražedná kombinace."
    scene bg fuji bus screen
    "Takže jste úspěšně zaspali všechny pokyny a doporučení, jak se na Fuji chovat a čemu se vyhnout."
    "Asi po 40 minutách jízdy konečně autobus zastavil na parkovišti, kde vás vysypal."
    "Takže se chvíli rozkoukáváte, je docela mlha. A vyrazíte podle šipek směr Fuji."
    scene bg fuji start
    show fujiguards
    "Na takovém plácku, kde stojí dvě buňky a taxíky, vás před stupem na 'schodiště' vedoucí na stezku nahoru zastaví dva Japonci."
    fujiguards "Are you planning to go to Fuji-san?"
    "Pomyslíte si, že tito dva mají snad nejlepší angličtinu, co jste zatím v Japonsku slyšeli."
    hide fujiguards
    show d fuji
    d "Yes, we are planning to go to the top today."
    hide d fuji
    show fujiguards
    fujiguards "Have you booked the sleeping spot?"
    hide fujiguards
    show d fuji
    d "No, we are planning to go up and down in one day."
    hide d fuji
    show fujiguards
    fujiguards "Oh, really? Do you know that way up and down take about nine hours? And last bus depart at seven."
    hide fujiguards
    show d fuji
    d "We can be back before seven."
    hide d fuji
    show fujiguards
    fujiguards "Fine, do you have jacket?"
    hide fujiguards
    show d fuji
    d "Yes, we have jacket in our bags."
    hide d fuji
    show fujiguards
    fujiguards "Do you have good boots? And enough water and food?"
    hide fujiguards
    show d fuji
    d "Yes, we have."
    hide d fuji
    show fujiguards
    fujiguards "Do you want security helm? It's free to borrow."
    hide fujiguards
    "Zeptají se vás na helmy a ten druhý z dvojice už pro ně jde."
    show d fuji
    d "No, thanks, we don't need them."
    hide d fuji
    show fujiguards
    fujiguards "If you think so, then be careful."
    fujiguards "You can leave here a voluntary donation 1000 yen per person. It will be used for the maintenance of the routes."
    fujiguards "Starting 2024 this fee will be obligatory and raised to 2000 yen."
    hide fujiguards
    "Několik z vás se rozhodne zaplatit a dostanou za to papír s rozpisem stanic, razítko a dřevéný suvenýrek."
    show fujiguards
    fujiguards "Thank you, bye."
    hide fujiguards
    show d fuji
    d "Thank you, arigató, bye."
    hide d fuji
    "Popojdete kousek dál od hlídačů."
    show d fuji
    d "Tak ty helmy, mě trošku znervóznily. Ale Fuji by soptit neměla, a kdyby jo, tak nás helmy nezachrání."
    d "Jo, to, že jede poslední autobus v sedm je asi docela komplikace, když cesta nahoru a dolů trvá 9 h. Právě je 10 dopoledne."
    d "To znamená, že to máme teda tak tak."
    hide d fuji
    show s fuji
    s "Tak v tom případě ikimašó, ať stihneme ten autobus."
    hide s fuji
    menu:
        "Považuješ se spíše za sportovní, nebo méně sportovní typ?"
        "Sportovní":
            $ j.sportovni = True
        "Méně sportovní":
            $ j.sportovni = False
    scene bg fuji before 5th
    "Vyrazíte tedy nahoru po schodech a ty volně přejdou do sopečně-prašné cesty."
    if j.sportovni:
        "Dala ses do dvojice se Sučanem a po cestě si povídáte. Řešíte, že vyrážíte nahoru o 2 h později, než byl plán."
        "A že musíte nastolit trošku svižnější tempo, abyste to stihli."
        "Pak si chvíli povídáte o tom, jak se mají jedni nebo druzí rodiče."
        scene bg fuji 5th
        "A vida, jak si tak povídáte, už jste u páté stanice."
        show s fuji
        s "Super, to jsme stihli o 5 minut dříve, než kolik píše rozpis."
        hide s fuji
        j "Jo, ale kluci jsou ještě kus za námi."
        "Počkáte na zbytek, než přijde."
        "Když dorazí, přitočí se k tobě Dante."
        show d fuji
        d "Viděla jsi, co má Mimoň na nohách?"
        hide d fuji
        j "Ne? Boty?"
        show d fuji
        d "Sandály."
        hide d fuji
        j "Cože? Jak sandály? To není možný, neřešili jsme aspoň 50x, že sice nepotáhneme trekové boty, ale že si všichni musíme sbalit pohodlné tenisky?"
        j "A ten důvod byla právě Fuji, ne?"
        show d fuji
        d "No mně to neříkej... Včera po městě chodil normálně v teniskách."
        hide d fuji
        show m fuji:
            xalign 0
            yalign -0.3
        "Podíváš se tedy Mimoňovým směrem, a opravdu, Mimoň na sobě má (sice sportovní, s plnou špičkou, ale) SANDÁLY."
        "Ten kluk je vážně mimoň."
        hide m fuji
        "Dante donutí Mimoně koupit v páté stanici dřevěnou hůl, aby se o ní mohl opírat, a nepodjíždělo mu to tolik."
    else:
        "Sučan vyrazil trošku rychleji dopředu a ty jdeš ve dvojici s Adrianem za Mimoňem s Dantem."
        "Chvíli jdete a najednou se ozve Mimoň:"
        show m fuji
        m "Kluci, taky máte kameny v botách?"
        hide m fuji
        show a fuji
        a "Jo sem tam mi tam nějaký spadne, je tu strašná cesta."
        a "Počkej, co to máš na sobě? Sandály?"
        hide a fuji
        show m fuji:
            xalign 0
            yalign -0.3
        "A opravdu, Mimoň na sobě má (sice sportovní, s plnou špičkou, ale) SANDÁLY."
        show m fuji
        m "No, co je? Tenisky jsem nosil teď tři dny uplně zbytečně po městě."
        hide m fuji
        j "Jo, takže, ti přišlo jako nejlepší nápad si vzít sandály zrovna na Fuji. Tak proto na nás tak divně koukali ti Japonci u vstupu."
        show m fuji
        m "Stejně za to můžeš ty, že si mi neřekla, jaký boty si mám vzít!"
        hide m fuji
        j "Vážně? Copak jste moje děti, abych kontrolovala, co jste si vzali dneska na sebe?"
        show d fuji
        d "Klid..."
        hide d fuji
        "Šeptne tvým směrem Dante, a pak začne mluvit na Mimoně."
        show d fuji
        "Ale takhle nedojdeš. Navíc dost pospícháme, když potřebujeme stihnout ten poslední autobus."
        hide d fuji
        "Naštěstí je už pátá stanice na dohled. Sučan sedí u stolečku a čeká na vás."
        "Dolezete tedy tam, seznámíte Sučana se situací a donutíte Mimoně koupit dřevěnou hůl, aby se měl o co opírat."
        "Protože když mu to nebude tolik podjíždět, nebude mu padat tolik kamenů do bot."
    scene bg fuji4
    "Vyrazíte tedy dál v pořadí Sučan, Dante, ty, Adrian a ..... Mimoň"
    "Cesta nahoru je opravdu obtížná. Jdete po sopečném prachu, navíc nemáte hikingové hole."
    "V podstatě uděláte 3 kroky nahoru a dva sjedete zpátky dolů."
    "Navíc to dost práší a často se vám noha při podjetí zahrabe několik centimetrů pod povrch."
    "Cestou potkáváte různé skupinky Japonců či pouze jednotlivce, kteří jdou směrem nahoru, ale i dolů."
    "Všichni Japonci jsou na výstup skoro až příliš vybavení, mají trekové boty, sportovní kalhoty s odepínacími nohavicemi,"
    "trika s krátkým rukávem přes trička s dlouhým rukávem, sportovní větrovky, čelenky, sportovní krosny s náhradním oblečením,"
    "jídlem, pitím, náhradním kyslíkem... Vy vedle nich vypadáte jako totální gaijinové."
    "Všichni, kteří vás míjejí, se ale usmívají a zdraví 'koničiva'."
    "Kousek před šestou stanicí se shromažďují Japonci kolem provizorně postaveného stanu ze zahřívací hliníkové fólie."
    "Nechcete tam okounět, takže se nezdržujete a pokračujete v cestě."
    "Uhýbáte Japoncům, kteří jako mravenečci pendlují mezi šestou stanicí a provizorním stanem s kyslíkovými bombami v ruce."
    "Zastavíte se až u šesté stanice, kde si dáte svačinku."
    "Jsou zde záchody, rozhodnete se využít situace."
    "Záchody stojí 100 yenů, což je krásná částka na záchody nacházející se 3000 metrů nad mořem."
    "Avšak do automatu se musí házet přesně stoyenovky."
    "Drobných máš spoustu, ale stoyenovku jako na potvoru ani jednu."
    menu:
        "Dojdeš si rozměnit?"
        "Ano, dojdu si rozměnit do budovy ve stanici.":
            "Vlezl['a' if j.gender == 'f' else ''] jsi s 500 yenovkou v ruce do stanice, rozhlédl['a' if j.gender == 'f' else ''] ses a udělal['a' if j.gender == 'f' else ''] jsi krok dopředu."
            "A už k tobě vybíhá zděšený Japonec."
            "Stop, what do you want?"
            j "Change."
            "Japonec si od tebe vezme 500 yenovku a jde ji rozměnit."
            "Konečně si tvé oči pořádně přivykly na přítmí, které ve stanici oproti venku je."
            "A dochází ti, proč je Japonec tak rozmrzelý."
            "Kdyby si udělal['a' if j.gender == 'f' else ''] ještě půlkrok dopředu, šlápl['a' if j.gender == 'f' else ''] bys na tatami, které tam jsou připravené pro nocležníky."
            $ j.increment_gaijin_points(1)
            "Získáváš jeden GP za nerozměněné mince a boty na tatami"
            show screen stats_overview
            "Japonec se vrátí s rozměněným obnosem. Poděkuješ a vycouváš ven."
            "Konečně si můžeš odskočit."
        "Ne, vydržím to.":
            "No, to asi není dobrý nápad, ale jak myslíš."
            show a fuji
            a "Já mám nějaké stoyenovky navíc, nepotřebuje někdo?"
            hide a fuji
            j "Mně by se asi nějaká hodila."
            show a fuji
            a "Na."
            hide a fuji
            j "Děkuji, vážím si toho."
            "Konečně si můžeš odskočit."
    "Na to, že je to prakticky kadibudka v půlce sopky, tak je velmi luxusní a čistá. Sice zde není typický panel a vestavěný bidet,"
    "ale stejně si není na co stěžovat."
    "Poté, co vyjdeš ven, tak si otřeš ruce vlhčenými ubrousky, které máš s sebou, protože ses při přípravě dočetla, že záchody jsou bez vody."
    "Dojíte, pobalíte se a chcete vyrazit."
    "A vidíte jak jednoho z 'mravenečků' kteří běhali mezi stanicí a stanem, zastavuje jeden ze zaměstnanců stanice."
    "Položí mu otázku v japonštině."
    "A 'mraveneček' jen sklopí oči a špitne 'ie'."
    "Pochopíte, že to s dotyčným nevypadá dobře a rozhodnete se více neočumovat a vyrazit dále."
    "S každým dalším postupem Mimoň čím dál více zaostává."
    "U stanice 7 se Sučan rozhodne, že chce za každou cenu kráter stihnout obejít. Takže půjde napřed."
    "Dante s Adrianem také chtějí stihnout vylézt až nahoru, ale plánují jít malinko pomaleji."
    "Mimoň je ještě pár metrů (ale vzdušnou čarou) pod stanicí číslo 7."
    if j.sportovni:
        menu:
            "Chceš jít se Sučanem, s Dantem a Adrianem nebo počkáš na Mimoně?"
            "Se Sučanem obejít kráter.":
                call sucan_krater
            "S Dantem a Adrianem pokořit top v mírnějším tempu.":
                call top_but_slower
            "Počkat na Mimoně":
                call fuji_mimon_wait
    else:
        menu:
            "Sučan vám utekl, chceš jít s Dantem a Adrianem nebo počkáš na Mimoně?"
            "S Dantem a Adrianem pokořit top v mírnějším tempu.":
                call top_but_slower
            "Počkat na Mimoně.":
                call fuji_mimon_wait
    return

label sucan_krater:
    scene bg fuji after 7th
    "Sučan nastolil vražedné tempo, jen tak tak mu stačíš."
    "Jediné, co tě zachraňuje, je to, že často fotí."
    "Velmi energeticky zdraví všechny Japonce a vypadá velmi šťastně."
    "Máš trošku pocit, že ho zdržuješ, ale když už jste ostatním utekli, tak se nechceš odpojovat."
    "Internet má jen Sučan a Adrian, takže kdyby ses oddělila, tak ztratíš kontakt na zbytek."
    "Jak pomalu míjíte stanice 7b a 8, terén se ještě malinko zhoršuje."
    scene bg fuji3
    "K postupu je nutné zvládat i základy horolezení, takže začíná jít do tuhého."
    "Máš za sebou asi 3 hodiny do prudkého stoupání po v podstatě neupraveném povrchu sopky."
    "Cesta vlastně není o moc více jiná než okolí, které míjíte."
    "Provazy kolem stezky podle všeho slouží jen jako orientační. Protože jsou moc nízko na to, aby se jich mohl člověk držet a přitahovat se nahoru."
    "To znamená, že pouze májí zajišťovat, že někdo v noci z cesty nesejde."
    "Ano, v noci. U Japonců je oblíbené si pronajmout spaní na jedné ze stanic a ještě za tmy dojít na vrchol, aby viděli východ slunce."
    if j.love_points.get(s.name, 0) > 3:
        "Zatímco míjíte další skupinu Japonců"
        "a šplháš na snad stopadesátý kámen,"
        "tak ti Sučan přijde na pomoc."
        show s fuji
        s "Podej mi ruku, bude to tak bezpečnější."
        hide s fuji
        j "Děkuji."
        show s fuji
        s "Bych se nemohl podívat vašim do očí, kdyby se ti něco stalo."
        hide s fuji
        j "Tak hlavně, že to svoje gentlemanství umíš dobře odůvodnit."
        "Se Sučanovou pomocí postupuješ celkem rychle."
        scene bg fuji before 9th
        "S devátou stanicí na dohled se cesta zase trošku zlepší a zvládneš se pohybovat i sama."
        "Máš radost, že už na vrchol zbývá jen kousek. Dokonce se domníváš, že už vidíš vrchol, ale Sučan tě vyvede z omylu."
        show s fuji
        s "Tak tamto je stanice 9b, ale pak už jsme skoro tam. Tak pojď, máme super čas. Dolů to trvá podle papírů 3 hodiny, obejít kráter asi hodinu."
        s "Nahoru to mělo trvat 6 h, ale už jsme ušetřili hodinu. A pokud nám i ty dvě další etapy zaberou o trošku méně, tak bude nahoře čas si i chvíli sednout."
        hide s fuji
        j "Dobře, ale docela mě ženeš. Nezapomínej na to, že jsem holka, jsem jinak stavěná než ty."
        show s fuji
        s "[j.name_5p], já bych si dovolil nesouhlasit, za mě jsi žena. Vlastně ne žena, ale krásná žena."
        s "A jsem moc rád, že jdeš se mnou a ne s klukama."
        hide s fuji
        "Chceš protestovat nebo prostě na to něco říct, ale než si to promyslíš, Sučan pokračuje."
        show s fuji
        s "Nic na to neříkej nebo to zkazíš. Radši pojď, pospícháme."
        hide s fuji
        "A rozejde se dopředu."
        "Chvíli stojíš jak opařená, ale když už je od tebe asi 10 metrů, rychle se rozejdeš, aby ti neutekl."
        "... za mě jsi žena. Vlastně ne žena, ale krásná žena..."
        "Pořád si ta slova přehráváš v hlavě. Jak to asi myslel?"
        "A co jsi neměla zkazit?"
        "Terén se za stanici zase rapidně zhoršil. Takže ti Sučan opět velmi ochotně pomáhá nahoru."
        "Navíc padla mlha, ochladilo se a začalo poprchávat."
        "Takže vybalujete z batohů větrovky a oblékáte si je na sebe."
        "Asi v polovině cesty mezi vrcholem a stanicí 9b konečně vylezete nad mraky a vysvitne sluníčko."
        "Ale dost fouká, takže si bundy necháte na sobě."
        "Konečně je vidět poslední, desátá stanice."
        "To ti dodá sílu. Terén se také změnil na větší pevné kameny, po kterých se dá docela slušně šplhat."
        scene bg fuji top
        "Takže poslední úsek zdoláte v rekordním čase."
        "U brány si uděláte na střídačku fotku."
        "A projdete ke kráteru."
        scene bg fuji krater
        "Před vámi se objeví pár desítek metrů hluboký kráter."
        "Vlastně kdyby člověk nevěděl, že je to sopka a na neměl za sebou tu šílenou cestu,"
        "tak si řekne: díra v zemi..."
        "Jak se tak nakláníš nad okrajem, Sučan tě chytne zezadu za ramena strčí do tebe."
        show s fuji
        s "Padáš!"
        hide s fuji
        "Strašně se lekneš. Samozřejmě tě hned vzápětí chytne, aby se ti nic nestalo. Otočí si tě a obejme tě."
        j "Blbečku, strašně jsem se lekla."
        "Říkáš, zatím co jsi ho tak nějak instinktivně také obejmula."
        show s fuji
        s "Promiň, to byl blbý vtip, přiznávám."
        hide s fuji
        "Zvedneš hlavu a podíváš se mu do obličeje. Usmívá se na tebe."
        show s fuji smile
        s "Přece bych tě dolů neshodil."
        hide s fuji smile
        "Díváš se mu do obličeje a do očí."
        "Na to, že jsme teď zdolali převýšení asi 1200 m, za 4 a půl hodiny, tak vypadá naprosto skvěle. Pomyslíš si."
        "A v jeho objetí ti je také dobře. Najednou ucítíš v břiše takovou zvláštní úzkost, slovy romanopisců, motýlky v břiše."
        "A tobě začíná docházet, že už Sučana nebereš jen jako kamaráda z dětství nebo jako bratra, jak sis do teď myslela."
        "Ale vlastně, že ti je velmi sympatický a je ti s ním dobře."
        "Všechny tyhle myšlenky ti prolétnou hlavou strašně rychle a dojde ti, že bys ho měla pustit."
        j "Vím, jen jsem dost unavená, mám pocit, že se mi podlamují kolena, takže jsem se lekla."
        "Říkáš, zatímco ho pouštíš a trochu si od něj poodstoupíš."
        "V tu ránu se do tebe dá zima."
        "Jemně se oklepeš. Ale Sučan to zaregistroval a už z batohu vyndává mikinu, kterou ti podává."
        $ j.hoodie = s.name
        show s fuji
        s "Na, je tu zima. Svlíkni si tu svoji mokrou mikinu a ven si místo ní moji suchou a přes to až tu bundu."
        hide s fuji
        j "Jak víš, že mám svoji mikinu mokrou?"
        show s fuji
        s "Tak zaprvé, jsme si ty bundy na sebe brali docela pozdě."
        s "Navíc ses asi po cestě nahoru zpotila a jak jsme se teď tady na tom vídrholci zastavili, tak ti ta mikina prochladla. Nemám pravdu?"
        s "Neodmlouvej a ber, nechceš být nemocná, ne? Nebo tě mám převlíknout sám?"
        hide s fuji
        "Dojde ti, že ti je vážně zima a že za to asi vážně může i to, že máš na sobě propocené a promočené oblečení z cesty nahoru."
        j "Děkuji. A nebude zima tobě?"
        show s fuji
        s "Já něco vydržím. Nenarážela jsi sama během cesty na to, že jsme každý jinak stavěný?"
        hide s fuji
        "Odložíš si věci, sundáš si svou mikinu, navlíkneš si Sučanovu a pod ní si ještě sundáš i tričko."
        "Sučan dělá, že se nedívá, ale je ti jasné, že tě po očku sleduje."
        "Nandáš si zpátky větrovku. A najednou ti je příjemné teplo. Mokré tričko a mikinu dáš do igelitky a dáš si to do batohu."
        show s fuji
        s "Můžeme?"
        hide s fuji
        j "Jo."
        "Vylezete na úplně nejvyšší bod Fuji, který má 3776 m, tady už fouká opravdu hodně."
        scene bg fuji krater2
        "Pak pokračujete dále kolem kráteru."
        "Když jste na opačném konci kráteru, píše vám Dante s Adrianem, že dolezli nahoru."
        "Můžete jen předpokládat, že ty tečky na druhé straně jsou právě oni dva."
        show s fuji
        s "Můžeš mě vyfotit?"
        hide s fuji
        "Zeptá se tě Sučan a podává ti svůj telefon."
        j "Jo, jasně.
        Vezmeš si jeho telefon a při tom se vaše ruce dotknou."
        show s fuji
        s "Máš strašně zmrzlé ruce, není ti zima?"
        hide s fuji
        j "Ne, jen ruce mi prochladly, jak tady fouká."
        "Vyfotíš Sučana s kráterem a s výhledem z Fuji (s mraky, Fuji je bez mraků jen vzácně, proto se jí přezdívá 'stydlivá hora')."
        "Když mu vracíš mobil, chytí tě za ruku."
        show s fuji
        s "Podej mi i tu druhou, trochu ti je zahřeju."
        hide s fuji
        "Jeho ruce jsou krásně teplé, a zatímco s nimi objímá tvé, tak tvé zkřehlé prsty zase začínají přicházet k sobě."
        menu:
            "Chceš si nechat ruce ještě chvíli zahřívat?"
            "Ano":
                show s fuji
                s "Už je to lepší, nemáš je tak studené. Proč si nic neřekla?"
                hide s fuji
                j "Už mám tvoji mikinu, teď mi zahříváš ruce. Není to trochu divné?"
                show s fuji
                s "Mně to přijde docela přirozené. Ale když ti to vadí..."
                hide s fuji
                "Pustí ti ruce a udělá si ještě fotku."
                show s fuji
                s "Tak asi půjdeme."
                hide s fuji
                $ j.add_love_points_for_person(s, 0.5)
            "Ne":
                "Ruce mu po chvíli vytrhneš."
                j "Myslím, že už to stačí. Pojď, ať stihneme ten autobus."
        scene bg fuji krater3
        "Vyrazíte dál na cestu. Potkáváte vyústění stezek z jiných směrů, ze kterých se dá Fuji zdolat. Když konečně dorazíte na stranu kráteru, odkud vede vaše cesta dolů, je chvíli po čtvrté hodině."
        scene bg fuji krater
        j "Mám pocit, že ta hodina na oběhnutí kráteru byla hodně podhodnocená, tak snad nám to dolů půjde stejně dobře jako nahoru."
        scene bg fuji before 9th
        "Začnete slézat dolů. Docela dost to po tom prachu klouže, takže asi 3x během chvíle skončíš na zemi."
        "Se slézáním větších kamenů ti Sučan pomáhá."
        $ j.add_love_points_for_person(s, 2)
    else:
        "Míjíte další skupinu Japonců."
        "A vylézáš snad stopadesátý kámen. Noha ti podjela tak dvěstěkrát."
        # TODO repeated says to function label
        scene bg fuji before 9th
        "Nakonec je v dohledu devátá stanice a se cesta zase trošku zlepší."
        "Máš radost, že už na vrchol zbývá jen kousek dokonce se domníváš, že už vidíš vrchol, ale Sučan tě vyvede z omylu."
        show s fuji
        s "Tak tamto je stanice 9b a pak už jsme skoro tam, tak pojď máme super čas. Dolů to trvá podle papírů 3 hodiny, obejít kráter asi hodinu."
        s "Nahoru to mělo trvat 6 h, ale už jsme ušetřili hodinu a pokud nám i ty dvě další etapy zaberou o trošku méně, tak bude nahoře čas si i chvíli sednout."
        hide s fuji
        j "Dobře, ale docela mě ženeš."
        "A rozejdete se dopředu."
        "Terén se za stanici se zase rapidně zhoršil."
        "Navíc padla mlha ochladilo se a začalo poprchávat."
        "Takže vybalujete z batohů větrovky a oblíkáte si je na sebe."
        "Asi v polovině cesty mezi vrcholem a devátou stanicí b, konečně vylezete nad mraky a vysvitne sluníčko."
        "Ale dost fouká, takže si bundy necháte na sobě."
        "Konečně je vidět poslední, desátá stanice."
        "To ti dodá sílu a také se terén změnil na větší pevné kameny po kterých se dá docela slušně šplhat."
        scene bg fuji top
        "Takže poslední úsek zdoláte v rekordním čase."
        "U brány si uděláte na střídačku fotku."
        "A projdete ke kráteru."
        scene bg fuji krater
        "Před vámi se objeví pár desítek metrů hluboký kráter."
        "Vlastně, kdyby člověk nevěděl, že je to sopka a na neměl za sebou tu šílenou cestu,"
        "tak si řekne díra v zemi..."
        "Právě jste zdolali převýšení asi 1200 m, za 4 a půl hodiny."
        "Začíná se do tebe dávat zima."
        "Jemně se oklepeš. vyndáš si z batohu mikinu a tu si oblečeš pod větrovku."
        show s fuji
        s "Můžeme?"
        hide s fuji
        j "Jo."
        "Vylezete na úplně nejvyšší bod Fuji, který má 3776 m, tady už fouká opravdu hodně."
        scene bg fuji krater2
        "Pak pokračujete dále kolem kráteru."
        "Když jste na opačném konci kráteru, tak vám píše Dante s Adrianem, že dolezli nahoru."
        "Můžete jen předpokládat, že ty tečky na druhé straně jsou právě oni dva."
        show s fuji
        s "Můžeš mě vyfotit?"
        hide s fuji
        "Zeptá se tě Sučana a podává ti svůj telefon."
        j "Jo jasně"
        "Vyfotíš Sučana s kráterem a s výhledem z Fuji (s mraky, Fuji je bez mraků jen pár dní v roce)"
        j "Myslím, že už bychom měli jít ať stihneme ten autobus."
        scene bg fuji krater3
        "Vyrazíte dál na cestu, když konečně dorazíte na stranu kráteru odkud vede vaše cesta dolů, je chvíli po čtvrté hodině."
        scene bg fuji krater
        j "Mám pocit, že ta hodina na oběhnutí toho kráteru byla hodně podhodnocená, tak snad nám to dolů půjde stejně dobře jako nahoru."
        scene bg fuji before 9th
        "Začnete slézat dolů, docela dost to po tom prachu klouže, takže asi 3x během chvíle skončíš na zemi."
    scene bg fuji after 7th
    "Mezi stanicemi 9b a 9a potkáváte Mimoně, už je na cestě dolů."
    if j.driver:
        "A protože jste oba řidiči a do taxíku se stejně vejdou maximálně 4, ženete dolů napřed."
    else:
        "A protože je Sučan řidič a do taxíku se stejně vejdou maximálně 4, ženete dolů napřed."
    "Před odchodem dáte Mimoňovi Sučanův mobil s internetem a vezmete od něj dva litry vody, které táhne úplně zbytečně, protože ze svých dalších zásob tekutin ještě upitou ani polovinu."
    "Dozvíš se, že za to můžeš ty, protože jsi mu přeci řekla, že půllitrovka coly nestačí."
    "Tak si koupil litr a půl koly, dvoulitrovku vody, a ještě si nalil litr vody do své cestovní láhve."
    scene bg fuji 5th
    "Danteho s Adrianem dostihnete u šesté stanice."
    "A na parkoviště k autobusu přicházíte ve třičtvrtě na sedm."
    show d fuji
    d "Asi tady Mimoně nemůžeme nechat, sám si taxík neobjedná. Tak já na něj počkám a vy jeďte. Buď nás naberete, nebo přijedeme taxíkem."
    hide d fuji
    "S tím souhlasíte a všichni 3 nastoupíte do autobusu, zatímco se Dante vrací pro Mimoně."
    "V autobuse jste všichni vytuhli a probrali jste se až na parkovišti."
    "Vysypali jste se z autobusu, napsali jste Mimoňovi, který ale neodepsal. Sedli jste do auta; Sučan za volant."
    "Jedete zkusit, zda vás nahoru nepustí, když už autobusy nejezdí."
    "Přijeli jste k závorám, Adrian vystoupil a chvíli s hlídačem komunikuje."
    "Už to skoro vypadá, že se ho podaří přemluvit, když k nim přijde ještě druhý Japonec a Adrian naznačuje, že to nepůjde."
    show a fuji
    a "Tak nic, máme se vrátit na parkoviště a oni mají použít taxíka."
    hide a fuji
    "Vyrazili jste tedy zpátky na parkoviště, najedli jste se, došli si na záchod."
    "Asi v půl deváté píše Dante, že se musel vrátit až k šesté stanici, ale že Mimoně má a že přijedou na parkoviště."
    "Ve chvíli, kdy dostanete tuto dobrou zprávu, všichni vytuhnete."
    "Vzbudí vás až když Dante klepe na okénko."
    "Narovnáte se do auta a vyrazíte na hotel."
    return

label top_but_slower:
    "Vyrazil['a' if j.gender == 'f' else ''] jsi tedy společně s Dantem a Adrianem."
    "Spolu se zvyšující nadmořskou výškou se zhoršuje i terén."
    if j.love_points.get(d.name, 0) > 2:
        # TODO separate label, this is insane
        "Adrianovi evidentně nedělá dobře rychlá změna nadmořské výšky."
        "Docela špatně dýchá."
        show d fuji
        d "Seš v pohodě?"
        hide d fuji
        show a fuji
        a "Jo, jsem, jen se mi trochu motá hlava, ale myslím, že jsem v pohodě. Klidně běžte napřed."
        hide a fuji
        show d fuji
        d "Určitě?"
        hide d fuji
        show a fuji
        a "Tak nejsem debil, kdybych se na to necítil, tak to přiznám. Počkal bych na vás, až půjdete zpátky nebo se sám vrátil."
        hide a fuji
        "Adrian se tedy na chvíli zastavil a vyndal si pití."
        "Ty a Dante pokračujete nahoru."
        "Dante tě pustil před sebe."
        "Pomalu postupuješ směrem vzhůru a terén se postupně zhoršuje."
        "Místy musíte na kameny doslova šplhat."
        "Když zdoláváš jedno místo, kde je nutné šplhat po kamenech, tak blbě šlápneš"
        "na jeden sice větší, ale nestabilní kámen."
        "Ten se ti pod nohou uvolní."
        "Nevíš jak, ale než si stihneš natlouct, tak Dante je u tebe a drží tě zezadu za boky."
        "Takže ačkoliv se držíš jen rukama, nepadáš dolů, ani sis neodřela kolena."
        show d fuji
        d "Opatrně, přitáhni se, pomůžu ti."
        hide d fuji
        "Přitáhla ses rukama a druhou nohou jsi našla stabilnější mezeru, o kterou se můžeš zapřít."
        "Takže tě Dante mohl pustit a ty ses vyhoupla nahoru."
        "Nabídneš Dantemu výměnou ruku."
        show d fuji
        d "To je v pořádku, zvládnu to. Bych se bál, že tě stáhnu dolů."
        hide d fuji
        "Tak mu uhneš a on vyleze nahoru, jako by to vlastně vůbec nic nebylo. V jeho podání to působí jako malý kamínek."
        show d fuji
        d "Akorát jsem porušil tvé pravidlo, že se od tebe mám držet alespoň na deset centimetrů..."
        hide d fuji
        j "Zachránil jsi mě před nepříjemným pádem, za to jsem ti vděčná. Ber to tak, že pravidlo platí na hotelu."
        "Pomalu postupujete nahoru."
        "Adrian postupuje za vámi; stále ho vidíte, ale neslyšíte se."
        scene bg fuji before 9th
        "Po nějaké době je v dohledu devátá stanice a cesta se zase trošku zlepší."
        # TODO parametrize Sucan-Dante and create separate label?
        "Máš radost, že už na vrchol zbývá jen kousek. Dokonce se domníváš, že už vidíš vrchol, ale Dante tě vyvede z omylu."
        show d fuji
        d "Tak tamto je stanice 9b a pak už jsme skoro tam."
        d "Nahoru to mělo trvat 6 h, ale už jsme ušetřili pár minut a pokud nám i ty dvě další etapy zaberou o trošku méně, tak bude nahoře čas si i chvíli sednout."
        hide d fuji
        j "Dobře."
        "A rozejdete se dopředu."
        "Terén se za stanici se zase rapidně zhoršil."
        "Navíc padla mlha ochladilo se a začalo poprchávat."
        "Takže vybalujete z batohů větrovky a oblíkáte si je na sebe."
        "Asi v polovině cesty mezi vrcholem a devátou stanicí b, konečně vylezete nad mraky a vysvitne sluníčko."
        "Ale dost fouká, takže si bundy necháte na sobě."
        "Konečně je vidět poslední, desátá stanice."
        "To ti dodá sílu a také se terén změnil na větší pevné kameny po kterých se dá docela slušně šplhat."
        scene bg fuji top
        "Takže poslední úsek zdoláte v dobrém čase."
        "U brány si uděláte na střídačku fotku."
        "A projdete ke kráteru."
        scene bg fuji krater
        "Před vámi se objeví pár desítek metrů hluboký kráter."
        "Vlastně, kdyby člověk nevěděl, že je to sopka a na neměl za sebou tu šílenou cestu,"
        "tak si řekne díra v zemi..."
        # end of prev TODO
        "Posadíte se na kameny u kráteru a vyndáte si pití a svačinu."
        "Asi za 5 minut dorazí zmožený Adrian."
        "Ale pohled na kráter mu vžene energii do žil."
        "Dostanete zprávu od Sučana, že je na druhé straně kráteru a ať raději jdete napřed."
        "Cesta dolů má trvat tři hodiny. Jsou čtyři odpoledne, takže je akorát čas vyrazit, pokud máte stihnout autobus v sedm."
        scene bg fuji3
        "Vyrazíte zase všichni tři směrem dolů."
        "Adrian jde první a vy dva za ním."
        show m fuji
        "Kousek od vrcholu potkáváte Mimoně, kterému oznamujete, že nahoru chodit nemá."
        "Že je potřeba stihnout autobus a že to bude dost na knop."
        "Uznáte ale, že se ve své obuvi dostal daleko."
        hide m fuji
        "S Mimoněm jste se s Dantem trošku zdrželi, takže vám Adrian malinko utekl."
        "A vy během chvíle utíkáte Mimoňovi."
        "Ale ty začínáš pociťovat únavu, klepou se ti nohy."
        "Každý krok je nejistý, do toho sopečný prach strašně klouže."
        "Takže člověk udělá krok, noha mu podjede a najde se o dva metry dále s nohou pod nánosem prachu."
        "V jednu chvíli slézáš zase nějaký kámen a podlomí se ti unavená noha."
        "Dante je zase poblíž."
        "Chytí tě."
        "A jak tě tak drží, tak se k tobě skloní a do ucha ti pošeptá."
        show d fuji
        d "Doufám, že se ti ty kolena podlamují ze mě. A ne únavou."
        hide d fuji
        "Celá zrudneš."
        j "Únavou, rozhodně únavou,"
        "vyjekneš. A on ti znovu zašeptá něco do ucha."
        show d fuji
        d "Škoda."
        hide d fuji
        "Pustí tě ze svého sevření."
        "Tentokrát, tě ale předejde."
        if j.love_points.get(d.name, 0) > 3:
            "Chytí tě za ruku a dělá ti oporu při klesání. Je to výrazné ulehčení."
            "Dokonce se ti už ani nohy tolik neklepou, když na ně působí už jen únava bez nervozity z toho, kam člověk šlápne."
            "Najednou se dostanete k místu, které je dost příkré."
            "Dante tě popadne do náruče jako nevěstu a než stihneš zaprotestovat, jste dole."
            "Takhle pokračujete i dál, Dante ti buď podává ruku nebo tě přes nepříjemné úseky nosí."
            $ j.add_love_points_for_person(d, 1)

        else:
            "A při každém zhoršeném úseku, ti nabídne svou ruku jako oporu."
        "Za což získává obdiv, potlesk či palce nahoru od Japonců, které míjíte."
        "Když se dostanete k osmé stanici, kde je terén už malinko schůdnější,"
        "začne Dante řešit, že jste trochu v časové tísni. A že by měl někdo autobusem odjet, protože do taxíku se vejdete jen 4."
        "A Adriana jste skoro došli."
        "Spoléhali jste na Sučana, ale ten vás stále nepředešel."
        "Pustíš tedy Danteho napřed – vypadá, že by mohl zvládnout seběhnout dolů výrazně rychleji než vy dva."
        $ j.add_love_points_for_person(d,2)
        menu:
            "Chceš čekat na Mimoně nebo odjet autobusem? Mimoň autobus prakticky jistě nestihne a cena za taxík bude stejná bez ohledu na počet pasažérů."
            "Počkat na Mimoně a sestupovat tedy pomalu.":
                "Rozhodla jsi se, že Mimoně samotného nenecháš a počkáš na něj."
                "Nicméně nechceš absolvovat sestup po setmění, to znamená, stejně musíš být dole kolem sedmé."
                "Daří se ti sestupovat docela dobře, stále vidíš Adriana pár metrů pod sebou."
                "Kousek za sedmou stanicí tě dohání Sučan."
                show s fuji
                s "Mám pro tebe dvě zprávy: jednu dobrou a jednu špatnou."
                s "Ta dobrá je, že oproti plánu jsme o 3 minuty napřed."
                s "Ta špatná, že Mimoň je tak dvacet minut za mnou."
                s "Já běžím napřed, mám klíče od auta, ať se pro vás kdyžtak můžu otočit."
                hide s fuji
                "Zbytek cesty tedy absolvuješ sama, i Adrian ti zmizel z dohledu."
                "Nicméně k autobusu u páté stanice jsi v půl sedmé a podle propozic má cesta k autobusu trvat už jen patnáct minut."
                scene bg fuji under
                "Když dorazíš na plácek, který je kousek od parkoviště autobusů, čeká tam na tebe Dante."
                show d fuji
                d "Jsem rád, že jsi v pořádku dole, měl jsem trošku, výčitky, že jsem tě tam nechal."
                d "Klidně běž k autobusu – kluci přiběhli před chvílí a už nastoupili. Počkám na Mimoně sám."
                hide d fuji
                j "Ne ne, rozhodla jsem se, že na něj počkám, tak počkám."
                j "Za taxík dáme stejně ať jsme dva nebo tři."
                "Čekáte spolu 10 minut."
                "20 minut."
                scene bg fuji under tma
                "Začíná být tma."
                "30 minut."
                "40 minut."
                j "To už je divné, co když se mu něco stalo? Nebo co když čeká v páté stanici?"
                show d fuji
                d "Tak já se tam dojdu podívat."
                hide d fuji
                j "Půjdu s tebou!"
                show d fuji
                d "Ne, vždyť si nahoře tak 10x spadla za dne, co v noci?"
                if j.driver:
                    d "Navíc jsi druhá řidička, když si zlomíš nohu, tak máme po dovolené."
                d "Zůstaň tady, musíš být naprosto vyčerpaná. Já mám na rozdíl od tebe výcvik. Ber to jako svůj trest za nedodržení pravidel na pokoji."
                hide d fuji
                j "Výcvik?"
                show d fuji
                d "Prostě si tu sedni, já ho přivedu."
                hide d fuji
                "Pochopila jsi, že ti Dante na otázku neodpoví a že odmlouvat také nemá smysl."
                "Sedla sis na obrubník chodníku a čekáš na Danteho s Mimoněm."
                "10 minut..."
                "20 minut..."
                "30 minut..."
                "Pokud by byl Mimoň v páté stanici, tak už měli přijít."
                "Dává se do tebe strašná zima, do toho jsi nervózní, že nevíš, kde je Dante a Mimoň."
                "Ke všemu na nikoho nemáš spojení. Jsi sama..."
                "Sem tam se objeví skupinka Japonců, kteří s čelovkami a velmi kvalitní výbavou míří na noční výstup."
                "40 minut..."
                "S úzkostí se upínáš na všechny přicházející lidi, avšak nikdo není ani Dante ani Mimoň."
                "50 minut..."
                "Hodina..."
                "Tvoji mysl začínají ovládat temné myšlenky toho, jak Mimoň v sandálech někde uklouzl a zřítil se kdo ví kam."
                "Nebo ještě hůř, že si ublížil Dante."
                "A že si Fuji vyžádala další oběti."
                "Do toho se vážně hodně ochladilo a vzhledem k tomu, že oblečení máš vlhké z cesty, tak rozhodně nehřeje."
                "Začínáš mít zimnici a nekontrolovatelně drkotáš zuby, cítíš se, jak kdybys měla horečku."
                "Začíná ti být na omdlení."
                "Vstaneš a začneš pochodovat sem a tam."
                "Hodina a dvacet minut..."
                "Začíná ti být na zvracení, nervy opravdu pracují velmi dobře."
                "Začínáš přemýšlet, jestli máte kontakt na Danteho a Mimoňovu rodinu."
                "Jak jim dáte vědět a co jim vlastně řeknete?"
                "Po hodině a půl, kdy jsi zralá na zhroucení, konečně uvidíš přicházet dvojici, ve které jeden člověk svírá dřevěnou tyč a druhý si svítí powerbankou."
                "Spadne ti obrovský kámen ze srdce."
                "Rozběhneš se za nimi."
                j "Díky bohu, jste v pořádku. Já už řešila, jak přepravit vaše těla do Čech."
                "Dante se od Mimoně oddělí a jde ti napřed."
                show d fuji
                d "Tak zle snad nebylo, musel jsem pro něj až k šesté stanici."
                hide d fuji
                j "Co ho tak zdrželo? Vždyť měl být dvacet minut za mnou."
                show d fuji
                d "Sandály? Nebo možná... Vidíš tu tyč? Na každé stanici si na ní cestou dolů nechal vypálit razítko."
                hide d fuji
                j "Cože? To se mi snad zdá. Vždyť věděl, že spěcháme ne? A já se tu můžu posrat strachy."
                show d fuji
                d "Klid, vztekem tomu nepomůžeš. Kluci psali, že je nahoru nepustí, tak půjdu zařídit ten taxík, co ty na to?"
                hide d fuji
                "Jen přikývneš."
                if j.love_points.get(d.name, 0) > 3:
                    show d fuji
                    d "Je mi líto, že si na nás musela čekat tak dlouho."
                    "Odsune ti vlasy z obličeje."
                    d "Brr, ty seš studená."
                    "Šáhne ti na ruce."
                    d "Ty jsi strašně zmrzlá."
                    hide d fuji
                    "Sundá si batoh ze zad a dá ti svoji mikinu"
                    $ j.hoodie = d.name
                    show d fuji
                    d "Vem si ji, je čistá, já jsem ji nepotřeboval."
                    hide d fuji
                    "Jsi tak vyčerpaná, jak fyzicky, tak psychicky, že mikinu přijmeš."
                    "Sundáš si bundu, a svoji vlhkou mikinu a místo ní si oblékneš tu Danteho."
                    "Pak si vezmeš zpátky bundu."
                    "Během chvíle je ti výrazně lépe."
                    $ j.add_love_points_for_person(d, 1)
                "Dante odejde směr parkoviště taxíků."
                "Zůstala jsi tedy na chvíli s Mimoněm sama, ale mlčíš, protože jinak bys na něj musela křičet."
                $ j.add_hate_points_for_person(m, 5)
                "Dante se vrací s nějakým Japoncem."
                show d fuji
                d "Tak pojďte, on nás dolů odveze."
                hide d fuji
                "Při nastupování do taxíku ses pokusil['a' if j.gender == 'f' else ''] sednout za volant – mířila jsi na místo spolujezdce, ale v Japonsku je volant vpravo. Spolu s taxikářem jste se tomu zasmáli."
                "Taxík vás odveze na parkoviště."
                show bg fuji parkoviste at nighttime1, nighttime2
                "Cena překvapivě není tak vysoká."
                "Dante zaplatí, poděkujete a vyrazíte k autu."
                "Kluci spí."
                "Dante zaklepe na okénko a kluci, se vzbudí. Nasáčkujete se k nim do auta a vyrazíte směr hotel."
                return
            "Nechat Mimoně svému osudu a hnát na autobus":
                "Ale rozhodla jsi se, že za Mimoně nemáš zodpovědnost."
                "A že vlastně nechceš absolvovat sestup po setmění, to znamená, stejně musíš být dole kolem sedmé."
                "Daří se ti sestupovat docela dobře, stále vidíš Adriana pár metrů pod tebou."
                "Kousek za sedmou stanicí, tě dohání Sučan."
                show s fuji
                s "Mám pro tebe dvě zprávy: jednu dobrou a jednu špatnou."
                s "Ta dobrá je, že oproti plánu jsme o 3 minuty napřed."
                s "Ta špatná, že Mimoň je tak dvacet minut za mnou."
                hide s fuji
                if j.love_points.get(s.name, 0) > 1:
                    "Zbytek cesty absolvujete spolu."
                    scene bg fuji bus
                    "K autobusu přicházíte za deset minut celá."
                    "Takže jste to stihli."
                else:
                    show s fuji
                    s "Já běžím napřed mám klíče od auta, ať se pro vás kdyžtak můžu otočit."
                    hide s fuji
                    "Zbytek cesty tedy absolvuješ sama, i Adrian ti zmizel z dohledu."
                    scene bg fuji bus
                    "Nicméně k autobusu ses dostala za pět minut sedm, takže stíháš."
        show d fuji
        "U autobusu jste se sešli ty, Dante, Adrian a Sučan."
        d "Asi tady Mimoně nemůžeme nechat, sám si taxík neobjedná. Tak já na něj počkám a vy jeďte. Buď nás naberete nebo přijedeme taxíkem."
        hide d fuji
        "S tím souhlasíte a všichni tři nastoupíte do autobusu, zatímco se Dante vrací pro Mimoně."
        scene bg fuji parkoviste
        "V autobuse jste všichni vytuhli a probrali jste se až na parkovišti."
        "Vysypali jste se z autobusu, napsali jste Mimoňovi, který ale neodepsal. Sedli jste do auta; Sučan za volant."
        scene bg cestafuji5
        "Jedete zkusit, zda vás nahoru nepustí, když už autobusy nejezdí."
        "Přijeli jste k závorám, Adrian vystoupil a chvíli s hlídačem komunikuje."
        "Už, už to vypadá, že vás nahoru pustí, když k nim přijde ještě druhý Japonec a Adrian naznačuje, že to nepůjde."
        show a fuji
        a "Tak nic, máme se vrátit na parkoviště a oni mají použít taxíka."
        hide a fuji
        scene bg fuji parkoviste
        "Dorazili jste tedy zpátky na parkoviště, najedli jste se, došli si na záchod."
        "Asi v půl deváté, píše Dante, že se musel vrátit až k šesté stanici, ale že Mimoně má a že přijedou na parkoviště."
        "Ve chvíli, kdy dostanete tuto dobrou zprávu, všichni vytuhnete."
        "Vzbudí vás až když Dante klepe na okénko."
        "Naskládáte se do auta a vyrazíte na hotel."
        return

    elif j.love_points.get(a.name, 0) > 2:
        "Chvíli šplháte společně všichni tři."
        "A bavíte se pro změnu tím, jaká obuv je na Fuji nejlepší."
        "Samozřejmě, že sandály a vy blbci jste si vzali pevnou obuv."
        "Ale po chvíli vám začne Dante docela utíkat."
        show d fuji
        d "Hele, když vy dva jdete spolu a máte podobné tempo, tak já doženu Sučana."
        hide d fuji
        show a fuji
        a "Jo, běž, sejdeme se nahoře anebo u autobusu."
        hide a fuji
        "Zůstala jsi tedy s Adrianem."
        show a fuji
        a "Mám ti vzít nějaké věci? Nemáš ten batoh těžký?"
        hide a fuji
        j "Ne ne, v pohodě, to unesu."
        j "Spíš mi to dost klouže, tak jestli mi nepomůžeš na těch větších kamenech."
        show a fuji
        a "Rád."
        hide a fuji
        "Pomalu postupujete s Adrianem nahoru."
        "U větších kamenů a v nebezpečných místech ti pomáhá, takže postupujete velmi úspěšně vstříc vrcholu Fuji."
        "Aby byla šance, že stihnete autobus zpátky, napočítali jste, že vrcholu musíte dosáhnout před čtvrtou hodinou."
        # TODO reuse
        scene bg fuji before 9th
        "Po čase je v dohledu devátá stanice a cesta se zase trošku zlepší."
        "Máš radost, že už na vrchol zbývá jen kousek dokonce se domníváš, že už vidíš vrchol, ale Adrian tě vyvede z omylu."
        show a fuji
        a "Tak tamto je stanice 9b a pak už jsme skoro tam."
        a "Nahoru to mělo trvat 6 h, ale už jsme ušetřili pár minut. A pokud nám i ty dvě další etapy zaberou o trošku méně, tak bude nahoře čas si i chvíli sednout."
        hide a fuji
        "Říká Adrian docela ztěžka, ačkoliv se evidentně snaží na tebe působit, že je v pořádku."
        "Rychlá změna nadmořské výšky mu vůbec nedělá dobře."
        j "Dobře."
        "A rozejdete se dopředu."
        "Terén se za stanicí zase rapidně zhoršil."
        "Navíc padla mlha, ochladilo se a začalo poprchávat."
        "Takže vybalujete z batohů větrovky a oblíkáte si je na sebe."
        "Asi v polovině cesty mezi vrcholem a devátou stanicí b, konečně vylezete nad mraky a vysvitne sluníčko."
        "Ale dost fouká, takže si bundy necháte na sobě."
        "Konečně je vidět poslední, desátá stanice."
        "To ti dodá sílu a také se terén změnil na větší pevné kameny po kterých se dá docela slušně šplhat."
        scene bg fuji top
        "Takže poslední úsek zdoláte v dobrém čase."
        "U brány si uděláte na střídačku fotku."
        "A projdete ke kráteru."
        scene bg fuji krater
        "Před vámi se objeví pár desítek metrů hluboký kráter."
        "Vlastně, kdyby člověk nevěděl, že je to sopka a na neměl za sebou tu šílenou cestu,"
        "tak si řekne díra v zemi..."
        "Posadíte se na kameny."
        show a fuji
        a "Jsem rád, že jsme to zvládli a že jsi tady se mnou..."
        hide a fuji
        "Větu ale nedokončí, protože omdlí? A sesune se na tebe."
        "Chytíš ho, aby se nesesunul z kamene na zem do prachu. A začneš s ním třást."
        j "Adriane! Panebože, Adriane! Prober se, prosím."
        "Adrian otevře oči a zmateně se na tebe podívá."
        show a fuji
        a "Stalo se něco?"
        hide s fuji
        j "Asi si omdlel. Vydrž mám v batohu čokoládu. Zhluboka dýchej, ať tě dolů nemusím nést na zádech."
        j "Šup, nádech, výdech, nádech..."
        "Opakuješ, zatímco pravou rukou držíš Adriana opřeného o sebe a levou se hrabeš v batohu."
        "Adrian se asi konečně probere ze zmatení a tvou ruku sundá ze svého ramena. Narovná se."
        show a fuji
        a "Promiň, to jsem nechtěl, tohle se nemělo stát."
        a "Rozhodně jsem nechtěl v tvých očích vypadat jako padavka."
        hide a fuji
        j "Vždyť tak nevypadáš. Na, tady je ta čokoláda. Sněz ji a napij se."
        "Čokoládu si od tebe vezme a sní ji. Pak si vyndá pití z batohu a napije se."
        j "Jak ti je? Je to lepší?"
        "Dostanete zprávu od Sučana, že je s Dantem na druhé straně kráteru a ať raději jdete napřed."
        "Cesta dolů má trvat tři hodiny. Jsou čtyři odpoledne, takže je akorát čas vyrazit, pokud u autobusu máte být v sedm."
        j "Myslíš, že zvládneš cestu dolů? Nebo mám napsat Dantemu, aby ti pomohl?"
        "Adrian vytřeští oči."
        show a fuji
        a "Ne, Dantemu ne... Myslím, že to zvládnu."
        hide a fuji
        "Vyrazíte směrem dolů."
        scene bg fuji3
        "Jdeš před Adrianem a hlídáš, zda je při vědomí."
        "Ačkoliv se snažíš před Adrianem vypadat, že jsi v pořádku a můžeš mu být oporou,"
        "jsi ve skutečnosti na dně svých sil. Nohy se ti klepou při každém kroku vyčerpáním a nervozitou."
        "Protože každý krok dolů je nebezpečný, prach klouže, kameny pod nohama padají."
        "Takže člověk udělá krok, noha mu podjede a najde se o dva metry dále s nohou pod nánosem prachu."
        "A do toho máš obavu, aby Adrian zase neomdlel a nějak blbě nespadl."
        show m fuji
        "Kousek od vrcholu potkáváte Mimoně, kterému oznamujete, že nahoru chodit nemá."
        "Že je potřeba stihnout autobus a že to bude dost na knop."
        "Uznáte ale, že se ve své obuvi dostal daleko."
        hide m fuji
        "S Mimoněm jste se s Adrianem malinko zdrželi."
        "A vy během chvíle utíkáte Mimoňovi,"
        "protože jsi rozhodla, že bude lepší s Adrianem jít napřed a co nejdříve ho dostat do nižších nadmořských výšek."
        "Kousek za sedmou stanicí vás dohání Sučan."
        $ j.add_love_points_for_person(a, 2)
        scene bg fuji2
        show s fuji
        s "Mám pro vás dvě zprávy: jednu dobrou a jednu špatnou."
        s "Ta dobrá je, že oproti plánu jsme o 3 minuty napřed."
        s "Ta špatná, že Mimoň je tak dvacet minut za mnou."
        s "Ale je s ním Dante, tak se nemusíte bát"
        s "Já běžím napřed, mám klíče od auta, ať se pro vás kdyžtak můžu otočit."
        hide s fuji
        "Skoro celou cestu mlčíte. Až kousek před poslední stanicí Adrian promluví."
        show a fuji
        a "Myslíš, že by sis to, co se stalo nahoře, mohla nechat pro sebe?"
        hide a fuji
        j "Jen když mi slíbíš, že mi příště řekneš, že ti není dobře dříve, než omdlíš."
        j "Víš, jak jsem se bála?"
        show a fuji
        a "To mě mrzí. A ještě více mě mrzí, že ty ses musela postarat o mě a ne já o tebe."
        hide a fuji
        j "O čem to mluvíš? Nahoře jsme si vyfotili kráter a šli zase zpátky, ne?"
        "Mrkneš na něj. A přidáš trošku do kroku."
        "I na Adrianovi je vidět, že mu je lépe, takže s tebou stíhá držet krok."
        scene bg fuji bus
        "K autobusu jste se dostali za deset celá, takže stíháte."
        "Sučan už sedí uvnitř."
        show s fuji
        s "Dante psal, že jsou někde mezi sedmou a osmou stanicí. Nemáme na ně čekat."
        hide s fuji
        "Adrian si sedne za Sučana a ty vedle něj."
        "V autobuse jste všichni vytuhli a probrali jste se až na parkovišti."
        scene bg fuji parkoviste
        "Vysypali jste se z autobusu, napsali jste Mimoňovi, který neodepsal, sedli jste do auta."
        scene bg cestafuji5
        "Sučan za volant a jdete zkusit, zda vás nahoru nepustí, když už autobusy nejezdí."
        "Přijeli jste k závorám, Adrian vystoupil a chvíli s hlídačem komunikuje."
        "Už, už to vypadá, že vás nahoru pustí, když k nim přijde ještě druhý Japonec a Adrian naznačuje, že to nepůjde."
        show a fuji
        a "Tak nic, máme se vrátit na parkoviště a oni mají použít taxíka."
        hide a fuji
        scene bg fuji parkoviste
        "Dorazili jste tedy zpátky na parkoviště, najedli se a došli si na záchod."
        "Asi v půl deváté, píše Dante, že s Mimoněm úspěšně dorazili dolů a že přijedou taxíkem na parkoviště."
        "Ve chvíli, kdy dostanete tuto dobrou zprávu tak všichni vytuhnete."
        "Vzbudí vás až když Dante klepe na okénko."
        "Narovnáte se do auta a vyrazíte na hotel."
    else:
        "Míjíte další skupinu Japonců."
        "A vylézáš na snad stopadesátý kámen. Noha ti podjela tak dvěstěkrát."
        scene bg fuji before 9th
        "Nakonec je v dohledu devátá stanice a cesta se zase trošku zlepší."
        "Máš radost, že už na vrchol zbývá jen kousek. Dokonce se domníváš, že už vidíš vrchol, ale kluci tě vyvedou z omylu."
        "Je to teprve stanice 9b"
        "A rozejdete se dopředu."
        "Terén se za stanici se zase rapidně zhoršil."
        "Navíc padla mlha ochladilo se a začalo poprchávat."
        "Takže vybalujete z batohů větrovky a oblékáte si je na sebe."
        "Asi v polovině cesty mezi vrcholem a devátou stanicí b, konečně vylezete nad mraky a vysvitne sluníčko."
        "Ale dost fouká, takže si bundy necháte na sobě."
        "Konečně je vidět poslední, desátá stanice."
        "To ti dodá sílu a také se terén změnil na větší pevné kameny po kterých se dá docela slušně šplhat."
        scene bg fuji top
        "Takže poslední úsek zdoláte v rekordním čase."
        "U brány si uděláte na střídačku fotku."
        "A projdete ke kráteru."
        scene bg fuji krater
        "Před vámi se objeví pár desítek metrů hluboký kráter."
        "Vlastně, kdyby člověk nevěděl, že je to sopka a na neměl za sebou tu šílenou cestu,"
        "tak si řekne díra v zemi..."
        "Právě jste zdolali převýšení asi 1200 m, za 4 a půl hodiny."
        "Začíná se do tebe dávat zima."
        "Jemně se oklepeš. Vyndáš si z batohu mikinu a oblečeš si ji pod větrovku."
        "Když jste se posadili na velký kámen u kráteru, píše vám Sučan, že je na druhé straně kráteru a ať raději jdete napřed."
        j "Myslím, že už bychom měli jít, ať stihneme ten autobus."
        scene bg fuji3
        "Začnete slézat dolů. Docela dost to po tom prachu klouže, takže asi 3x během chvíle skončíš na zemi."
        show m fuji
        "Kousek od vrcholu potkáváte Mimoně, kterému oznamujete, že nahoru chodit nemá."
        "Že je potřeba stihnout autobus a že to bude dost na knop."
        "Uznáte ale, že se ve své obuvi dostal daleko."
        hide m fuji
        scene bg fuji after 7th
        "Krom pár dalších tvých pádů se při cestě dolů nic zajímavého nestalo."
        "A na parkoviště k autobusu přicházíte ve třičtvrtě na sedm."
        "Za pět minut celá přichází Sučan."
        show s fuji
        s "Tak jsem tady, ale Mimoň zůstal někde mezi sedmou a šestou stanicí."
        s "Ale já jsem musel jít, mám klíče od auta. Můžeme ho pak zkusit vyzvednout."
        s "Nechal jsem mu svůj mobil s internetem, takže bez kontaktu není."
        show d fuji
        d "Asi tady Mimoně nemůžeme nechat, sám si taxík neobjedná. Tak já na něj počkám a vy jeďte. Buď nás naberete, nebo přijedeme taxíkem."
        hide d fuji
        scene bg fuji bus
        "S tím souhlasíte a všichni tři nastoupíte do autobusu, zatímco se Dante vrací pro Mimoně."
        "V autobuse jste všichni vytuhli a probrali jste se až na parkovišti."
        scene bg fuji parkoviste
        "Vysypali jste se z autobusu, napsali jste Mimoňovi, který neodepsal, sedli jste do auta."
        "Sučan za volant a jdete zkusit, zda vás nahoru nepustí, když už autobusy nejezdí."
        scene bg cestafuji5
        "Přijeli jste k závorám, Adrian vystoupil a chvíli s hlídačem komunikuje."
        "Už, už to vypadá, že vás nahoru pustí, když k nim přijde ještě druhý Japonec a Adrian naznačuje, že to nepůjde."
        show a fuji
        a "Tak nic, máme se vrátit na parkoviště a oni mají použít taxíka."
        hide a fuji
        scene bg fuji parkoviste
        "Dorazili jste tedy zpátky na parkoviště, najedli se a došli si na záchod."
        "Asi v půl deváté, píše Dante, že se musel vrátit až k šesté stanici, ale že Mimoně má a že přijedou na parkoviště."
        "Ve chvíli, kdy dostanete tuto dobrou zprávu tak všichni vytuhnete."
        "Vzbudí vás až když Dante klepe na okýnko."
        "Narovnáte se do auta vyrazíte na hotel."
    return

label fuji_mimon_wait:
    "Vážně, takových možností jít na Fuji se sexy milými kluky a ty zvolíš Mimoně?"
    "Takže tě všichni opustili a vyrazili směr vrchol."
    "Asi za deset minut přichází Mimoň."
    "Naprosto naštvaný."
    j "Tak si chvíli odpočiň a pak půjdeme dál."
    show m fuji
    m "Nikam nejdu!"
    hide m fuji
    j "Tak nemusíš, jestli nechceš."
    j "Vzdát to v sedmé stanici není ostuda, na to že to jdeš v sandálích."
    j "Klidně běž napřed dolů a počkej na nás, musíme být dole do sedmi."
    show m fuji
    m "..."
    hide m fuji
    # TODO we should give this information to Mimon in every branch. Or at least in every except for the fastest. Or before that
    j "Nebo můžeme jít pomalu nahoru a uvidíš kam zvládneš dojít, než je potkáme, jak jdou dolů."
    show m fuji
    m "..."
    hide m fuji
    j "Nebo můžeš počkat tady a po cestě dolů tě nabereme."
    show m fuji
    m "..."
    hide m fuji
    j "Hele, musíš se mnou komunikovat!"
    show m fuji
    m "..."
    hide m fuji
    j "Tak víš co? Já ten vrchol chci taky pokořit a když se mnou nemluvíš, tak já jdu. Jsi dospělý. Nahoru nepoletíš a dole tě najdeme."
    show m fuji
    m "..."
    "Rozhodneš se, že to nemá cenu. Když trucuje, půjdeš napřed."
    "Takhle praktika většinou funguje na malé děti, když začnou dělat scénu, že nikam nejdou. Prostě je tam necháte a jdete napřed."
    "Děti, když vidí, že jim nevěnujete pozornost, a dokonce odcházíte, se přestanou vztekat a doženou vás."
    "Navíc druhá možnost pro výstup na Fuji se nemusí objevit."
    # TODO reuse repeated says
    "Míjíš další skupinu Japonců."
    "A vylézáš snad stopadesátý kámen. Noha ti podjela tak dvěstěkrát."
    scene bg fuji before 9th
    "Po nějakém čase je v dohledu devátá stanice a cesta se zase trošku zlepší."
    "Máš radost, že už na vrchol zbývá jen kousek. Dokonce se domníváš, že už vidíš vrchol."
    "Když dolezeš k ukazateli, tvá radost zmizí."
    "Je to teprve stanice 9b."
    "Rozejdeš se dopředu."
    "Terén se za stanicí se zase rapidně zhoršil."
    "Navíc padla mlha, ochladilo se a začalo poprchávat."
    "Takže vybaluješ z batohu větrovku a oblékáš si ji na sebe."
    "Asi v polovině cesty mezi vrcholem a stanicí 9b konečně vylezeš nad mraky a vysvitne sluníčko."
    "Ale dost fouká, takže si bundu necháváš na sobě."
    "Konečně je vidět poslední, desátá stanice."
    "To ti dodá sílu a také se terén změnil na větší pevné kameny po kterých se dá docela slušně šplhat."
    scene bg fuji top
    "Takže poslední úsek zdoláš v rekordním čase."
    "U brány tě vyhlíží Dante s Adrianem a udělají ti fotku."
    "A projdete ke kráteru."
    scene bg fuji krater
    "Před vámi se objeví pár desítek metrů hluboký kráter."
    "Vlastně, kdyby člověk nevěděl, že je to sopka a na neměl za sebou tu šílenou cestu,"
    "tak si řekne díra v zemi..."
    "Právě jste zdolali převýšení asi 1200 m, za 4 a půl hodiny."
    "Začíná se do tebe dávat zima."
    "Jemně se oklepeš. Vyndáš si z batohu mikinu a tu si oblečeš pod větrovku."
    "Když ses se posadila na velký kámen u kráteru, píše vám Sučan, že je na druhé straně kráteru a ať raději jdete napřed."
    j "Myslím, že už bychom měli jít ať stihneme ten autobus."
    scene bg fuji3
    "Začnete slízat dolů, docela dost to po tom prachu klouže, takže asi 3x během chvíle skončíš na zemi."
    show m fuji
    "Kousek od vrcholu potkáváte Mimoně, kterému oznamujete, že nahoru chodit nemá."
    "Že je potřeba stihnout autobus a že to bude dost na knop."
    "Uznáte ale, že se ve své obuvi dostal daleko."
    hide m fuji
    scene bg fuji after 7th
    "Krom pár dalších tvých pádů se při cestě dolů nic zajímavého nestalo."
    scene bg fuji bus
    "A na parkoviště k autobusu přicházíte ve třičtvrtě na sedm."
    "Za pět minut celá přichází Sučan."
    show s fuji
    s "Tak jsem tady, ale Mimoň zůstal někde mezi sedmou a šestou stanicí."
    s "Ale já jsem musel jít, mám klíče od auta. Můžeme ho pak zkusit vyzvednout."
    s "Nechal jsem mu svůj mobil s internetem, takže bez kontaktu není."
    show d fuji
    d "Asi tady Mimoně nemůžeme nechat, sám si taxík neobjedná. Tak já na něj počkám a vy jeďte, buď nás naberete, nebo přijedeme taxíkem."
    hide d fuji
    "S tím souhlasíte a všichni 3 nastoupíte do autobusu, zatímco se Dante vrací pro Mimoně."
    scene bg fuji parkoviste
    "V autobuse jste všichni vytuhli a probrali jste se až na parkovišti."
    "Vysypali jste se z autobusu, napsali jste Mimoňovi, který neodepsal, sedli jste do auta."
    scene bg cestafuji5
    "Sučan za volant a jdete zkusit, zda vás nahoru nepustí, když už autobusy nejezdí."
    "Přijeli jste k závorám, Adrian vystoupil a chvíli s hlídačem komunikuje."
    "Už, už to vypadá, že vás nahoru pustí, když k nim přijde ještě druhý Japonec a Adrian naznačuje, že to nepůjde."
    "Vrátil se zpátky do auta"
    show a fuji
    a "Tak nic, máme se vrátit na parkoviště a oni mají použít taxíka."
    hide a fuji
    scene bg fuji parkoviste
    "Dorazili jste tedy zpátky na parkoviště, najedli jste se, došli si na záchod."
    "Asi v půl deváté, píše Dante, že se musel vrátit až k šesté stanici, ale že Mimoně má a že přijedou na parkoviště."
    "Ve chvíli, kdy dostanete tuto dobrou zprávu tak všichni vytuhnete."
    "Vzbudí vás až když Dante klepe na okýnko."
    "Narovnáte se do auta vyrazíte na hotel."
    return
