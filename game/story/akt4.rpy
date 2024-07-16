label akt4:
    "Ráno jte se sešli všichni na recepci, zase bylo nutné počkat na Mimoně, který s vámi nakonec jede."
    "Pak jste šli narovnat věci do auta, zabralo vám to víc času, než jste čekali."
    "Takže místo v 6:05 odjíždíte až v 6:20, příjezd podle navigace 8:30."
    "Řízení se ujme Sučan."
    if j.driver:
        "Ty si sedneš na místo spolujezdce. Zapojíš mobil přes kabel do panelu, aby se navigace spojila s autem a pustíš spotify."
        "V zádu sedí za řidičem rocapený Mimoň, který jen co dosedl, tak usnul, ve prostřed sedí zkroucný Adrian a za tebe si sedl Dante. "
    else:
        "Sedneš si za spolujezdce - Danteho, do středu si sedne Adrian a za Sučana Mimoň. Mimoň ihned usne. Rozvalý přes celou sedačku. Adrian se zase choulí ve středu."
        "Dante připojí mobil pomocí kabelu do carplay a pustí navigaci, pak spustí spotify a playlist, který jste si připravili před odletem."
    "Pro cestu k fuji jste zvolili jet po placených dálnicích, protože každý úsek dálnice patří jiné společnosti, nemají dálniční známku."
    scene bg cestafuji4
    "Platí se vždy za projetý úsek."
    "Když jste si půjčovali auto ptali se vás v půjčovně, zda chcete ETC kartu. Za poplatek."
    "Ptali jste se jestli je nutná, bylo vám řečeno, že nikoliv, jen že na mýtných branách musíte do správného pruhu, kde se nachází pokladna."
    scene bg cestafuji2
    "Takže jste kartičku odmítli."
    "Ale bez problémů se vám daří najíždět a rozpoznávat nájezdy a s jezdy pro placení."
    scene bg cestafuji1
    "Dálnice je převážně na postech a v tunelech, takže místy se otvírá krásný výhled na okolní krajinu."
    "Když z dálnice sjedete kousek od Fuji, tak se dostanete na takové menší okresná silničky."
    scene bg cestafuji3
    "Cestou se koukáš z okýnka, všude je vše krásně zelené. Konečně chápeš proč, je v Anime vždy tráva tak krásně zelená,"
    "ona to totiž není tráva, ale rýže. Kterou pěstují kde se dá."
    scene bg cestafuji6
    "Konečně se před vámi v mracích zahalená objeví Fuji."
    scene bg cestafuji5
    "A během pár minut už vyjíždíte lesem směr pátá stanice."
    "Míjíte záchytné parkoviště a po chvíli se chystáte odbočit doprava, avšak zde jsou závory, dozvídáte se, že přes sezónu, je vjezd na horní parkoviště zakázán."
    "Musíte tedy zpět na záchytné parkoviště, a zaplatit si autobus nahoru."
    scene bg fuji parkoviste
    "Na parkovišti vás přivítají, vysypete se z auta pobalíte si věci a vyrazíte směr zastávka autobusů."
    "Při kupování lístků, zjišťujete, že autobus nahoru jezdí v každou celou hodinu - je 8:10, takže vám zrovna autobus ujel a další jede v 9."
    "Vrátíte se tedy k autu a dáte si snídani. Ještě jednou projdete věci co máte s sebou."
    "Takže sportovní oblečení, větrovku, roušky proti prachu při sestupu dolů, čelovky, jídlo, pití."
    "Chvíli před devátou se přesunete do autobusu."
    "Kde všichni usnete, protože jste toho moc nenaspali, navíc jste toho za poslední tři dny dost nachodili a spojení s doznívajícím jetlagem je vražedná kombinace."
    "Takže jste úspešně zaspali, všechny pokyny a doporučení jak se na Fuji chovat a čemu se vyhnout."
    "Asi po 40 minutách jízdy konečně autobus zastavil na parkovišti, kde vás vysypal."
    "Takže se chvíli rozkoukáváte, je docela mlha. A vyrazíte podle šipek směr fuji."
    scene bg fuji start
    show fujiguards
    "Na takovém plácku, kde stojí 2 buňky a taxíky, vás před stupem na 'schodiště' vedoucí na stezku nahoru zastaví dva japonci."
    fujiguards "Are you plannig go to Fuji?"
    hide fujiguards
    show d fuji
    d "Yes, we are plannig go to the top today."
    hide d fuji
    show fujiguards
    fujiguards "Do you have booked the sleeping spot?"
    hide fujiguards
    show d fuji
    d "No, we are plannig go up and down in one day."
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
    d "Yes, we have jacket in ours bags."
    hide d fuji
    show fujiguards
    fujiguards "Do you have good boots? And enought water and food?"
    hide fujiguards
    show d fuji
    d "Yes, we have."
    hide d fuji
    show fujiguards
    fujiguards "Do you want security helm? It's free to borrow."
    hide fujiguards
    "Zeptají se vás na helmy a už ten druhý z dvojice pro ně jde."
    show d fuji
    d "No, thanks, we don't need them."
    hide d fuji
    show fujiguards
    fujiguards "If you think so, so be carefull, bye"
    hide fujiguards
    show d fuji
    d "Thanks you, arigató, bye."
    hide d fuji
    "Popojdete kousek dál od hlídačů."
    show d fuji
    d "Tak ty helmy, mě trošku znervóznily. Ale Fuji by soptit neměla a kdyby jo tak nás helmi nezachrání."
    d "Jo to, že jede poslední autobus v sedm je asi docela komplikace, když cesta nahoru a dólů trvá 9 h, máme 10."
    d "To znamená, že to máme teda tip ťop."
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
    "Vyrazíte tedy nahoru po schodech a ty vloně přejdou do sopečně-prašné cesty."
    if j.sportovni:
        "Dala ses do dvojice se Sučanem a po cestě si povídáte, tak nějak řešíte, že vyrážíte nahoru o 2 h později než byl plán."
        "A že musíte nastolit, trošku svižnější tempo abyste to stihli."
        "Pak si chvíli povídáte o tam jak se mají jedni nebo druzí rodiče."
        scene fuji 5th
        "A během chvilky, už jste u páté stanice."
        show s fuji
        s "Super to jsme stihli o 5 minut dříve, než kolik píše rozpis."
        hide s fuji
        j "Jo, ale kluci jsou ještě kus za námi."
        "Počkáte na zbytek než přijde."
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
        d "No mně to neříkej..."
        hide d fuji
        "Podíváš se tedy Mimoňovým směrem a opravdu Mimoň na sobě má sice sportovní sandály s plnou špičkou, ale SANDÁLY."
        "Ten kluk je vážně mimoň."
        "Dante donutí mimoně koupit v páté stanici dřevěnou hůl, aby se o ní mohl opírat a nepodjíždělo mu to tolik."
    else:
        "Sučan vyrazil trošku rychleji do předu a ty jdeš ve dvojici s Adrianem za Mimoňem s Dantem."
        "Chvíli jdete a najednou se ozve Mimoň"
        show m fuji
        m "Kluci, taky máte kameny v botech."
        hide m fuji
        show a fuji
        a "Jo sem tam mi tam nějaký spadne, je tu strašná cesta."
        a "Počkej co to máš na sobě? Sandály?"
        hide a fuji
        "A opravdu Mimoň na sobě má sice sportovní sandály s plnou špičkou, ale SANDÁLY."
        show m fuji
        m "No co je? Tenisky jsem nosil teď tři dny uplně zbytečně po městě."
        hide m fuji
        j "Jo takže, ti přišlo jako nejlepší nápad si vzít tenisky, zrovna na Fuji. Tak proto na nás tak divně koukali ty japonci u vstupu."
        show m fuji
        m "Stejně za to můžeš ty, že si mi neřekla jaký boty si mám vzít!"
        hide m fuji
        j "Já vážně? Copak jste moje děti, abych kontrolovala, co jste si vzali dneska na sebe?"
        show d fuji
        d "Klid..."
        hide d fuji
        "Šepne tvým směrem Dante a pak začne mluvit na Mimoně."
        show d fuji
        "Ale takhle nedojdeš. Navíc dost pospícháme když potřebujeme stihnout ten poslední autobus."
        hide d fuji
        "Naštěstí, už je pátá stanice na dohled, Sučan už sedí u stolečku a čeká na vás."
        "Dolezete tedy tam, seznámíte Sučana se situací a donutíte Mimoně koupit dřevěnou hůl, aby se měl o co opírat."
        "Protože, když mu to nebude tolik podjíždět, nebude mu padat tolik kamenů do bot."
    scene bg fuji4
    "Vyrazíte tedy dál v pořadí Sučan, Dante, ty, Adrian a ..... Mimoň"
    "Cesta nahoru je opravdu obtížná, jak je to sopečný prach navíc nemáte hikingové hole."
    "Tak v podstaě uděláte 3 kroky nahoru a dva sjedete zpátky dolů."
    "Navíc to dost přáší a často se vám noha při podjetí zahrabe několik centimetrů pod povrch."
    "Cestou potkáváte různé skupinky japonců, či pouze jednotlivce, kteří jdou směrem nahoru, ale i dolů."
    "Všichni japonci jsou na výstup skoro až převybavení, mají trekoví boty, sportovní kalhoty s odepínacími nohavicemi,"
    "Trika s krátkým rukávem přes trička s dlouhým rukávem, sportovní větrovky, čelenky, sportovní krosny, s náhradním oblečením,"
    "jídlem, pitím, náhradním kyslíkem a vy vedle nich vypadáte jako totální gaijinové."
    "Všichni kteří vás míjejí, se ale usmívají a zdraví 'koničiva'."
    "Kousek před šestou stanicí, se shromažďují japonci kolem provizorně postaveného stanu, ze zahřívací hliníkové fólie."
    "Nechcete tam okounět, takže se nezdržujete a pokračujete v cestě."
    "Uhýbáte japoncům, kteří jako mravenečci pendlují mezi šestou stanicí a provizorním stanem s kyslíkovými bombami v ruce."
    "Zastavíte se až u šesté stanice, kde si dáte svačinku."
    "Jsou zde záchody, rozhodnete se využít situace."
    "Avšak záchody stojí 100 yenů, což je krásná částka na záchody nacházející se 3000 metrů nad mořem."
    "A do automatu se musí házet přesně stoyenovky."
    "Drobných máš spoustu, ale stoyenovku jako na potvoru ani jednu."
    menu:
        "Dojdeš si rozměnit?"
        "Ano, dojdu si rozměnit do stanice.":
            "Vlezla si s 500 yenovkou v ruce do stanice, rozhlédla ses a udělala jsi krok dopředu."
            "A už k tobě vybíhá zděšený japonec."
            "Stop, what you want?"
            j "change"
            "Japonec si od tebe vezme 500 yenovku a jde jí rozměnit."
            "Konečně si tvé oči pořádně přivikli na přítmí, které ve stanici oproti venku je."
            "A dochází ti proč, je japonec tak rozmrzelý."
            "Kdyby si udělala ještě půlkrok dopředu šlápla by si na tatami, které tam jsou připravené pro nocležníky."
            $ j.increment_gaijin_points(1)
            "Získáváš jeden GP za nerozměnené mince a boty na tatami"
            "[j.show_all_points()]"
            "Japonec se vrátí s rozměněným obnosem, poděkuješ a vycouváš ven."
            "Konečně si můžeš odskočit."
            "Na to že je to v podstatě kadibudka uprostřed sopky, tak je velmi luxusní a čistá. Sice zde není typická panel a vestavěný bidet."
            "Ale stejně si není na co ztěžovat."
            "Po té co vyjdeš ven, tak si otřeš ruce vlhčenými ubrousku, které máš s sebou protože ses při přípravě dočetla, že záchody jsou bez vody."
        "Ne, vydržím to.":
            "No to asi není dobrý nápad, ale jak myslíš."
            show a fuji
            a "Já mám nějaké stoyenovky navíc, nepotřebuje někdo?"
            hide a fuji
            j "Mně by se asi nějáká hodila."
            show a fuji 
            a "Na."
            hide a fuji
            j "Děkuji, važím si toho."
            "Konečně si můžeš odskočit."
            "Na to že je to v podstatě kadibudka uprostřed sopky, tak je velmi luxusní a čistá. Sice zde není typická panel a vestavěný bidet."
            "Ale stejně si není na co ztěžovat."
            "Po té co vyjdeš ven, tak si otřeš ruce vlhčenými ubrousku, které máš s sebou protože ses při přípravě dočetla, že záchody jsou bez vody."
    "Dojíte pobalíte se a chcete vyrazit."
    "A vydíte jak jednoho z 'mravenečků' kteří běhali mezi stanící a stanem, zastavuje jeden ze zaměstnanců stanice."
    "Položí mu otázku v japonštině."
    "A 'mraveneček jen sklopí oči a špitne 'IE'."
    "Pochopíte, že to s dotyčným nevypadá dobře a rozhodnete se více neočumovat a vyrazit dále."
    "S každým dalším postupem, Mimoň čím dál více zaostává."
    "U stanice 7 se Sučan rozhodne, že chce za každou cenu kráter stihnout obejít. Takže půjde napřed."
    "Dante s Adrianem, také chtejí stihnout vylézt až na horu, ale planují jít malinko pomaleji."
    "Mimoň je ještě pár metrů (ale vzdušnou čarou) pod stanicí číslo 7."
    if sportovni:
        menu:
            "Chceš jít se Sučanem, s Dantem a Adrianem nebo počkáš na Mimoně?"
            "Se Sučanem obejít kráter.":
                scene bg fuji after 7th
                "Sučan nastolil vražedné, tempo, jen tak tak mu stačíš."
                "Jediné co tě zachraňuje, je to, že často fotí."
                "Velmi energeticky, zdraví všechny Japonce a vypadá velmi šťastně."
                "Máš trošku pocit, že ho zdržuješ, ale když už jste ostaním utekli, ta se nechceš odpojovat."
                "Internet má jen Sučan a Adrian, takže kdyby ses oddělila, tak ztratíš kontakt na zbytek."
                "Když minete stanici 7b a 8, tak se terén ještě malinko zhoršil."
                scene bg fuji3
                "K postupu je nutné zvládat i základy horolezování."
                "Takže začíná jít do tuhého máš za sebou asi 3 hodiny do prudkého stoupání po v podstatě neupraveném povrchu sopky."
                "Cesta vlastně není o moc více jiná, než okolí, které míjíte."
                "Podle všeho provazi, vytičující cestu, slouží jen jako orientační. Protože jsou moc nízko na to, aby se jich mohl člověk držet a pomocí nich přitahovat nahoru."
                "To znamená, že pouze májí zajišťovat, že někdo v noci z cesty nesejde."
                "Ano v noci, je oblíbené u japonců si pronajmout spaní na fuji, a ještě za tmy dojít jen část Fuji, aby z jejího vrcholu viděli východ slunce."
                if j.love_points.get(s.name, 0) > 3:
                    "Zatímco míjíte další skupinu japonců."
                    "A vylízáš snad stopadesátý kámen."
                    "Tak ti Sučan přijde na pomoc."
                    show s fuji
                    s "Podej mi ruku, bude to tak bezpečnější."
                    hide s fuji
                    j "Děkuji."
                    show s fuji
                    s "Bych se nemohl podívat vašim do očí, kdyby se ti něco stalo."
                    hide s fuji
                    j "Tak hlavně, že to svoje gentlemanství umíš dobře schovat."
                    "Se Sučanovou pomocí, postupuješ celkem rychle."
                    scene bg fuji before 9th
                    "Když je v dohledu devátá stanice, tak se cesta zase trošku zlepší a zvládneš se pohybovat i sama."
                    "Máš radost, že už na vrchol zbývá jen kousek dokonce se domníváš, že už vidíš vrchol, ale Sučan tě vyvede z omylu."
                    show s fuji
                    s "Tak tamto je stanice 9b a pak už jsme skoro tam, tak pojď máme super čas. Dolů to trvá podle papírů 3 hodiny, obejít kráter asi hodinu."
                    s "Nahoru to mělo trvat 6 h, ale už jsme ušetřili hodinu a pokud nám i ty dvě další etapy zaberou o trošku méně, tak bude nahoře čas si i chvíli sednout."
                    hide s fuji
                    j "Dobře, ale docela mě ženeš, nezapomínej na to, že jsem holka, jsem jinak stavěná než ty."
                    show s fuji
                    s "[j.name_5p], já bych si dovolil nesouhlasit, za mě jsi žena. Vlastně ne žena, ale krásná žena."
                    s "A jsem moc rád, že jdeš se mnou a ne s klukama."
                    hide s fuji
                    "Chceš protestovat, nebo prostě na to něco říct, ale než si to promyslíš. Tak tě Sučan předběhne."
                    show s fuji
                    s "Nic na to neříkej, nebo to zkazíš a radši pojď pospícháme."
                    hide s fuji
                    "A rozejde se dopředu."
                    "Chvíli stojíš jak opařená, ale když už je od tebe asi 10 metrů. Tak se rychle rozejdeš, aby ti neutekl."
                    "... za mě jsi žena. Vlastně ne žena, ale krásná žena..."
                    "Pořád si ty slova přemítáš v hlavě, jak to asi myslel?"
                    "A co si neměla zkazit?"
                    "Terén se za stanici se zase rapidně zhoršil. Takže ti zase Sučan velmi ochotně pomáhá nahoru."
                    "Navíc padla mlha ochladilo se a začalo poprchávat."
                    "Takže vybalujete z batohů větrovky a oblíkáte si je na sebe."
                    "Asi v polovině cesty mezi vrcholem a devátou stanicí b, konečně vylezete nad mraky a vysvitne sluníčko."
                    "Ale dost fouká, takže si bundy necháte na sobě."
                    "Konečně je vidět poslední, desátá stanice."
                    "To ti dodá sílu a také se terén změnil na větši pevné kameny po kterých se dá docela slušně šplhat."
                    scene bg fuji top
                    "Takže poslední úsek zdoláte v rekordním čase."
                    "U brány si uděláte na střídačku fotku."
                    "A ptojdete ke kráteru."
                    scene bg fuji krater
                    "Před vámi se objeví pár desítek metrů hluboký kráter."
                    "Vlastně, kdyby člověk nevěděl, že je to sopka a na neměl za sebou tu šílenou cestu,"
                    "tak si řekne díra v zemi..."
                    "Jak se tak nakláníš nad okrajem. Tak tě sučan chytne ze zadu za ramena strčí do tebe."
                    show s fuji
                    s "Padáš!"
                    hide s fuji
                    "Strašně se lekneš. Samozřejmě tě, hned v zápětí chytne, aby se ti nic nestalo. Otočí si tě a obejme tě."
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
                    "Na to že jsme teď zdolali převýšení asi 1200 m, za 4 a půl hodiny. Tak vypadá naprosto skvěle. Pomyslíš si."
                    "A v jeho objetí ti je také dobře. Najednou ucítíš v břiše takovou zvláštní úzkost, slovy romanopisců, motýlky v břiše."
                    "A tobě začíná docházet, že už Sučana nebereš jen jako kamaráda s dětství, nebo jako bratra, jak sis do teď myslela."
                    "Ale vlastně, že ti je velmi sympatický a je ti s ním dobře."
                    "Všechny tyhle myšlenky ti prolítnou hlavou strašně rychle a dojde ti, že by si ho měla pustit."
                    j "Vím, jen jsem dost unavená, mám pocit, že se mi podlamují kolena, takže jsem se lekla."
                    "Říkáš zatím co ho pouštíš a trochu si od něj poodstoupíš."
                    "V tu ránu se do tebe dá zima."
                    "Jemně se oklepeš. Ale Sůčan to zaregistroval a už z baťohu vyndává mikinu, kterou ti podává."
                    show s fuji
                    s "Na, je tu zima, svlíkni si tu svojí mokrou mikinu a ven si místo ní tuhle mojí suchou a přes to až tu bundu."
                    hide s fuji
                    j "Jak víš, že mám svojí mikinu mokrou."
                    show s fuji
                    s "Tak zaprvé, jsme si ty bundy na sebe brali docela pozdě,"
                    s "navíc ses asi po cestě nahoru spotila a jak jsme se teď tady na tom výdrholci zastavili, tak ti ta mikina prochladla, nemám pravdu?"
                    s "Neodmlouvej a ber, nechceš být nemocná ne? Nebo tě mám převlíknout sám?"
                    hide s fuji
                    "Dojde ti, že ti je vážně zima a že za to asi vážně může i to, že máš na sobě propocené a promočené oblečení z cesty nahoru."
                    j "Děkuji a nebude zima tobě?"
                    show s fuji
                    s "Já něco vydržím"
                    hide s fuji
                    "Odložíš si věci sundáš si svou mikinu, navlíkneš si Sučanovu a pod ní si ještě sundáš i tričko."
                    "Sučan dělá, že se nedívá, ale je ti jasné, že tě po očku sleduje."
                    "Nandáš si zpátky větrovku. A najednou ti je příjemné teplo. Mokré tričko a mikinu dáš do igelitky a daš si to do batohu."
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
                    j "Jo jasně, vezmeš si jeho telefon a přitom se vaše ruce dotknou."
                    show s fuji
                    s "Máš strašně zmrzlé ruce, není ti zima?"
                    hide s fuji
                    j "Ne, jen ruce mi prochladli jak tady fouká."
                    "Vyfotíš Sučana s kráterem a s výhledem z Fuji (s mraky, Fuji je bez mraků jen pár dní v roce)"
                    "Když mu vracíš mobil, tak tě chytí za ruku."
                    show s fuji
                    s "Podej mi i tu druhou, trochu ti je zahřeju."
                    hide s fuji
                    "Jeho ruce jsou krásně teplé a zatímco ti objímá tvé, tak tvé skřehlé prsty zase začínají přicházet k sobě."
                    menu:
                        "Chceš si nechat ruce ještě chvíli zahřívat?"
                        "Ano":
                            show s fuji
                            s "Už je to lepší, nemáš je tak studené. Proč si nic neřekla?"
                            hide s fuji
                            j "Už mám tvojí mikinu, teď mi zahříváš ruce. Není to trochu divné?"
                            show s fuji
                            s "Mě to přijde docela přirozené. Ale když ti to vadí."
                            hide s fuji
                            "Pustí ti ruce, udělá si ještě fotku."
                            show s fuji
                            s "Tak asi půjdeme."
                            hide s fuji
                            $ j.add_love_points_for_person(s, 0.5)
                        "Ne":
                            "Ruce mu po chvíli, vytrhneš."
                            j "Myslím, že už to stačí, pojď ať stihneme ten autobus."
                    scene bg fuji krater3
                    "Vyrazíte dál na cestu, když konečně dorazíte na sranu kráteru odkud vede vaše cesta dolů, je chvíli po čtvrté hodině."
                    scene bg fuji krater
                    j "Mám pocit, že ta hodina na oběhnutí toho kráteru byla hodně podhodnocená, tak snad nám to dolů půjde stejně dobře jako nahoru."
                    scene bg fuji before 9th
                    "Začnete slízat dolů, docela dost to po tom prachu klouže, takže asi 3x během chvíle skončíš na zemi."
                    "Se slézáním větších kamenů ti Sučan pomáhá."
                    $ j.add_love_points_for_person(s, 2)
                else:
                    "Míjíte další skupinu japonců."
                    "A vylízáš snad stopadesátý kámen. Noha ti podjela tak dvěstěkrát."
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
                    "Jemně se oklepeš. vyndáš si z batohu mikinu a tu si oblečeš, pod větrovku."
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
                    "Vyrazíte dál na cestu, když konečně dorazíte na sranu kráteru odkud vede vaše cesta dolů, je chvíli po čtvrté hodině."
                    scene bg fuji krater1
                    j "Mám pocit, že ta hodina na oběhnutí toho kráteru byla hodně podhodnocená, tak snad nám to dolů půjde stejně dobře jako nahoru."
                    scene bg fuji before 9th
                    "Začnete slízat dolů, docela dost to po tom prachu klouže, takže asi 3x během chvíle skončíš na zemi."
                scene bg after 7th
                "Mezi stanicemi 9b a 9a potkáváte Mimoně."
                "Řeknete mu, že autobus odjíždí v sedm, takže by měl pohnout."
                if driver:
                    "A protože jste oba řidiči a do taxíku se stejně vejdou maximálně 4, ženete dolů napřed."
                else:
                    "A protože je Sučan řidič a do  taxíku se stejně vejdou maximálně 4, ženete dolů napřed."
                "Před odchodem dáte Mimoňovi Sůčanův mobil s internetem, vezmete od něj 4 litry vody, které táhne úplně zbytečne."
                "Protože si mu přeci řekla, že půllitrovka koli nestačí."
                "Tak si koupil litr a půl koly, dvojlitrovku vody, nalil si litr vody do své cestovní láhve a ještě si sbalil půllitrovku, co jste dostali v hotelu."
                "Danteho s Adrianem dostihujete u šesté stanice."
                "A na parkoviště k autobusu přicházíte ve třičtvrtě na sedm."
                show d fuji
                d "Asi tady Mimoně nemůžeme nechat. Tak já na něj počkám a vy jeďte, buď nás naberete, nebo přijedeme taxíkem."
                hide d fuji
                "S tím souhlasíte a všichni 3 nastoupíte do autobusu, zatímco se Dante vrací pro Mimoně."
                "V autobuse jste všichni vytuhli a probrali jste se až na parkovišti."
                "Vysypali jste se z autobusu, napsali jste Mimoňovi, který neodepsal, sedli jste do auta."
                "Sučan za volant a jdete zkusit zda vás nahoru nepustí, když už autobusy nejezdí."
                "Přijeli jste k závorám, Adrian vystoupil a chvíli s hlídačem komunikuje."
                "Už už to vypadá, že vás nahoru pustí, když k nim přijde ještě druhý japonec a Adrian naznačuje, že to nepůjde."
                "Vrátil se zpátky do auta"
                show a fuji
                a "Tak nic, máme se vrátit na parkoviště a mají použít taxíka."
                hide a fuji
                "Dorazili jste tedy zpátky na parkoviště, najedli jste se, došli si na záchod."
                "Asi v půl deváté, píše Dante, že se musel vrátit až k šesté stanici, ale že Mimoně má a že přijedou na parkoviště."
                "Ve chvíli, kdy dostanete tuto dobrou zprávu tak všichni vytuhnete."
                "Vzbudí vás až když Dante klepe na okýnko."
            "S Dantem a Adrianem pokořit top v mírnějším tempu.":
                "Vyrazila jsi tedy společně s Dantem a Adrianem."
                "Spolu se zvyšující nadmořskou výškou se zhoršuje i terén."
                if j.love_points.get(d.name, 0) > 2:
                    "Adrianovi evidentně nedělá dobře, rychlá změna nadmořské výšky."
                    "Docela špatně dýchá."
                    show d fuji
                    d "Seš v pohodě?"
                    hide d fuji
                    show a fuji
                    a "Jo jsem, jen se mi trochu motá hlava, ale myslím, že jsem v pohodě, klidně běžte napřed."
                    hide a fuji
                    show d fuji
                    d "Určitě?"
                    hide d fuji
                    show a fuji
                    a "Tak nejsem debil, kdybych se na to necítil, tak to přiznám."
                    hide a fuji
                    "Adrian se tedy na chvíli zastavil a vyndal si pití."
                    "Ty a Dante pokračujete nahoru."
                    "Dante tě pustil před sebe."
                    "Pomalu postupuješ směrem vzhůru postupně se terén čím dál tím víc zhoršuje."
                    "Místy doslova musíte horolezovat."
                    "Když zdoláváš jedno místo, kde je nutné šplhat po kamenech, tak blbě šlápneš."
                    "Na jeden sice docela větší, ale nestabilní kámen."
                    "Ten se ti pod nohou uvolní."
                    "Nevíš jak, ale než si stihneš natlouct, tak Dante je u tebe a drží tě za zadu za boky."
                    "Takže ačkoliv se držíš jen rukama, tak si nespadla dolů, ani sis neodřela kolena."
                    show d fuji
                    d "Opatrně, přitáhni se, pomůžu ti." 
                    hide d fuji
                    "Přitáhla ses rukama a druhou nohou si našla stabilnější mezeru o kterou se můžeš zapřít."
                    "Takže tě Dante mohl pustit a ty ses vyhoupla nahoru."
                    "Nabídneš Dantemu výměnoou ruku."
                    show d fuji
                    d "To je v pořádku, zvládnu to, bych se bál, že tě stáhnu dolů"
                    hide d fuji
                    "Tak mu uhneš a on vyleze nahoru jako by to vlastně vůbec nebylo k horolezení, v jeho podání to působí, jako malý kamínek."
                    "Takhle postupujete až nahoru."
                    "Adrian postupuje za vámi, stále ho vidíte, ale neslyšíte se."
                    scene bg fuji before 9th
                    "Nakonec je v dohledu devátá stanice a se cesta zase trošku zlepší."
                    "Máš radost, že už na vrchol zbývá jen kousek dokonce se domníváš, že už vidíš vrchol, ale Dante tě vyvede z omylu."
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
                    "Posadíte se na kameny, u kráteru a vyndáte si pití a svačinu."
                    "Asi za 5 minut dorazí zmožený Adrian."
                    "Ale pohled na kráter mu vžene energii do žil."
                    "Dostanete zprávu od Sučana, že je na druhé straně kráteru a ať raději jdete napřed."
                    "Cesta dolů má trvat tři hodiny jsou čtyři, takže akorát čas vyrazit, pokud u autobusu máte být v sedm."
                    "Vyrazíte zase všichni tři směrem dolů."
                    "Adrian jde první a vy dva za ním."
                    "Kousek od vrcholu potkáváte Mimoně, kterému oznamujete, že nahoru chodit nemá."
                    "Že je potřeba stihnout autobus a že to bude dost na knop."
                    "S Mimoněm jste se s Dantem trošku zdželi, takže vám Adrian malinko utekl."
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
                    j "Únavou, rozhodně únavou."
                    "Vyjekneš. A on ti znovu zašeptá něco do ucha."
                    show d fuji
                    d "Škoda."
                    hide d fuji
                    "Pustí tě ze svého sevření."
                    "Tentokrát, tě ale předejde."
                    if j.love_points.get(d.name, 0) > 3:
                        "Chytí tě za ruku a dělá ti oporu při klesání, je to výrazné ulehčení."
                        "Dokonce se ti už ani nohy tolik neklepou, když na ně působí, už jen únava, bez nervozity z toho kam člověk šlápne."
                        "Najednou se dostanete místu, které je dost příkré."
                        "Dante tě popadne do náruče jako nevěstu a než stihneš zaprotestovat, jste dole."
                        "Takhle pokračujete i dál, Dante ti buď podává ruku nebo tě přes nepřijemné úseky nosí."
                    else:   
                        "A při každém zhoršeném úseku, ti nabídne svou ruku, jako oporu."
                    "Za což získává obdiv, potlesk či palce nahoru od japonců, které míjíte."
                    "Když se dostanete k osmé stanici, kde je terén už malinko schůdnější."
                    "Tak Dante začne řešit, že jste trochu v časové tísni. A že by měl někdo autobusem odjet protože do taxíku se vejdete jen 4."
                    "A Adrian jste skoro došli."
                    "Spoléhali jste na Sučana, ale ten vás stále nepředešel."
                    "Danteho tedy pustíš napřed."
                    menu: 
                        "Chceš čekat na Mimoně, nebo odjet autobusem?"

                if j.love_points.get(a.name, 0) > 3:
                    "Chvíli šplháte společně všichni tři."
                    "A bavíte se pro změnu tím, jaká obuv je na Fuji nejlepší."
                    "Samozřejmě, že sandály a vy blbci jste si vzali bevnou obuv."
                    "Ale po chvíli vám začne Dante, docela utíkat."
                    show d fuji
                    d "Hele tak když vy dva jdete spolu a máte podobné tempo, tak já doženu Sučana."
                    hide d fuji
                    show a fuji
                    a "Jo běž, sejdeme se nahoře a nebo u autobusu."
                    hide a fuji
                    "Zůstala jsi tedy s Adrianem."
                    show a fuji
                    a "Mám ti vzít nějaké věci? Nemáš ten batoh těžký?"
                    hide a fuji
                    j "Nene v pohodě, to unesu."
                    j "Spíš mi to dost klouže, tak jestli mi nepomůžeš, na těch větších kamenech."
                    show a fuji 
                    a "Rád."
                    hide a fuji
                    "Pomalu postupujete s Adrianem nahoru."
                    "U větších kamenů a v nebezpečných místech ti pomáhá, takže postupujete velmi úspěšně vstříc vrcholu Fuji."
                    "Aby byla šance, že stihnete autobus zpátky, napočítali jste, že vrcholu musíte dosáhnout před čtvrtou hodinou."

                else:
                    "hh"
            "Počkat na Mimoně":
                "bbg"
    else:
        menu:
            "Sučan vám utekl, chceš jít s Dantem a Adrianem nebo počkáš na Mimoně?"
            "S Dantem a Adrianem pokořit top v mírnějším tempu.":
                "gfdhgd"
            "Počkat na Mimoně":
                "gfdhg"



    jump titulky #provizorně
    #return






