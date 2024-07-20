label hotel_fuji:
    scene bg hotel fuji parking
    "Po příjezdu na hotel zaparkujete na hotelovém parkovišti, vyndáte si kufry"
    scene bg fuji recepce
    "a úplně zničení zamíříte na recepci."
    "Na recepci ukážete své pasy a rozhodnete se přikoupit si pozdější checkout a snídani."
    "Dostanete každý svou kartu od pokoje, tentokrát Sučan zařídil jednolůžkový pokoj pro každého a hotel nikdo nehacknul."
    "Ty navíc dostáváš kód od zámku do dámského onsenu. Pánské nejsou zamčené."
    "Když Mimoň zjistí, že máte každý vlastní pokoj, tak vypadá že se vztekne."
    show m fuji
    m "No já sám na pokoji nebudu! Ne a ne a ne!"
    hide m fuji
    j "Všichni jsme na pokoji sami, navíc je podle čísel máme vedle sebe."
    show s fuji
    s "Pojďme, vyřešíme to nahoře, nemusíme si tu dělat ostudu."
    hide s fuji
    "Jdete tedy společně do výtahu a vyjedete do čtvrtého patra."
    "Mimoň se mezitím vyvztekal a asi pochopil, že nikdo neustoupí."
    "Tvůj pokoj je nejblíže k výtahu."
    "Vedle tebe má pokoj Dante, vedle Danteho Adrian."
    "Sučan má pokoj naproti tobě a Mimoň pak vedle něho."
    scene bg fuji pokoj
    "Zapadneš do pokoje. Pokoj se nijak extra neliší od pokoje, ve kterém jste spali v Tokiu."
    "Zamkneš se, odložíš si kufr, vybalíš si věci na převlečení a zalezeš do koupelny."
    "Jsi celá ulepená a černá od sopečného prachu."
    "Dopřeješ si tedy pořádnou koupel. Oblékneš se."
    "Pak si vyčistíš zuby a přesuneš se do pokoje."
    "Zase si opíšeš heslo z kartičky na wifi a natáhneš se do postele."
    "Otevřela jsi 'socky' a asi za 10 minut někdo klepe."
    menu:
        "Kdo si přeješ, aby to byl?"
        "Adrian":
            if j.love_points.get(a.name, 0) > 4:
                jump adrian_fuji
                # TODO if really jump, then we can unindent this one level
            else:
                "Vstaneš."
                j "Už jdu!"
                "Otevřeš dveře a jsi zklamaná."
                jump sucan_fuji_nolove
        "Dante":
            if j.love_points.get(d.name, 0) > 4:
                jump dante_fuji
            else:
                "Vstaneš."
                j "Už jdu!"
                "Otevřeš dveře a jsi zklamaná."
                jump sucan_fuji_nolove

        "Mimoň":
            jump mimon_fuji
        "Sučan":
            if j.love_points.get(s.name, 0)>4:
                jump sucan_fuji
            else:
                "Vstaneš."
                j "Už jdu!"
                "Otevřeš dveře a jsi zklamaná."
                jump mimon_fuji
        "Budeš předstírat, že spíš.":
            jump spanek_fuji

label adrian_fuji:
    "K tvému milému překvapení za dveřmi opravdu stojí Adrian."
    "Mile se na tebe usmívá."
    show a fujihs
    a "Promiň, že ruším, ale jdu dát prát věci sobě a Dantemu. Napadlo mě, jestli mi nechceš dát i svoje. Máme toho málo na naplnění pračky."
    hide a fujihs
    j "Tady je pračka? A stihne to do rána uschnout?"
    show a fujihs
    a "Jo, dole v předsíňce u onsenů a je tam i sušička. Cyklus stojí 600 yenů a sušička pak 200 yenů. Prášek se fasuje na recepci."
    hide a fujihs
    j "No a nebude to hodinu prát a tak hodinu sušit?"
    show a fujihs
    a "S Dantem se u toho vystřídáme, klidně mi dej věci a běž spát."
    hide a fujihs
    j "Tak pojď dovnitř a nestůj na chodbě."
    "Uhneš ze dveří a zamíříš ke kufru, kde máš naházené věci z dnešního výšlapu."
    j "A není to blbé ti takhle dát svoje špinavé věci na vyprání?"
    show a fujihs
    a "Tak ty naše jsou určitě špinavější. Jestli ti je blbé mi dávat spodní prádlo, pochopím to, a dej mi jen kalhoty, triko a mikinu."
    hide a fujihs
    "Teď ti dojde, že v té hromadě špíny samozřejmě máš zahrabané i spodní prádlo."
    j "Hele, jsem vykoupaná, a spodní prádlo je zamotané v tom. Dám ti to tak."
    j "Ale mám jednu podmínku, zastavíš se tu až půjdeš od pračky zpátky na pokoj."
    show a fujihs
    a "..."
    hide a fujihs
    "Jenom zamrká a zčervenají mu tváře."
    j "Počkej, nemyslím to tak, na co teď asi myslíš... Chci si promluvit o tom, co se dneska nahoře stalo."
    show a fujihs
    a "Dobře."
    hide a fujihs
    "Podáš mu plátěnou tašku se svými věcmi na vyprání."
    show a fujihs
    a "Děkuji."
    hide a fujihs
    j "Ne, já děkuji. Nemám sílu si jít prát sama."
    "Adrian odejde z tvého pokoje."
    "Trošku pokoj poklidíš a uděláš dva čaje, které na pokoji jsou v rámci klasické výbavy japonských hotelů."
    "Za chvíli někdo klepe."
    j "Už běžím, Adri."
    "Otevřeš dveře a tam Adrian."
    show a fujihs
    a "Jak si mi to řekla?"
    hide a fujihs
    j "Adri?"
    show a fujihs
    a "Tak mi tak, prosím, neříkej."
    hide a fujihs
    j "Proč?"
    show a fujihs
    a "Tak mi říkala máma... Co si chtěla probrat?"
    hide a fujihs
    "Říkala?! Proč sakra použil minulý čas? Nechceš úplně šlapat do vosího hnízda, zeptáš se na to jindy až bude lepší příležitost."
    j "Tak pojď dovnitř, dáš si čaj? Udělala jsem dva."
    "Přikývne. Vstoupí tedy do pokoje, zavře za sebou a ty mu naznačíš ať jde s tebou dál."
    "Ukážeš mu, aby si sedl na postel."
    "A podáš mu hrneček s čajem."
    j "Chci vědět, zda si v pohodě. Nahoře si byl dobrou minutu v bezvědomí a ještě nechceš, abych o tom někomu říkala. Takže mi asi dlužíš vysvětlení."
    show a fujihs
    a "Jo, je mi dobře, jen nejsem zvyklý na tak vysoké nadmořské výšky."
    hide a fujihs
    j "Dobře, ale kdyby cokoliv, tak to někomu řekneš. Mně nebo Dantemu."
    show a fujihs
    a "Dantemu ne. Jestli na tom trváš a nevadí ti to, tak bych teda radši zvolil tebe."
    hide a fujihs
    j "Dobře, ale myslím, že mi dlužíš vysvětlení, proč tak nechceš, aby to Dante věděl."
    show a fujihs
    a "Jenou ti to třeba řeknu, ale teď mě prosím nenuť."
    a "Co ty, nejsi moc pomlácená?"
    hide a fujihs
    j "Pomlácená asi trošku, ale spálila jsem se. Přišlo mi, že sluníčko v podstatě nesvítilo, ale jsem spálená."
    show a fujihs
    a "Jo, já jsem se také spálil. Zítra najdeme lékárnu a koupíme něco na spáleniny."
    hide a fujihs
    "Adrian dopije čaj."
    show a fujihs
    a "Asi bych už měl jít. Věci ti dám zítra po snídani."
    hide a fujihs
    "Sice by sis ráda s Adrianem ještě povídala a dostala z něho, jak je to s jeho mámou a s Dantem."
    "Ale zároveň seš strašně unavená."
    j "Asi bych měla jít spát, tak ráno v devět na snídani?"
    "Adrian vstane a zamíří s hrníčkem do koupelny"
    show a fujihs
    a "Tak já tě vyzvednu?"
    hide a fujihs
    j "Jo, to by bylo super. Ten hrníček tam nech, já ho umeju."
    show a fujihs
    a "V žádném případě."
    hide a fujihs
    "Zajde do koupelny, hrneček umyje a vrátí ho na tác u vstupu."
    show a fujihs
    a "Tak dobrou, [j.name_5p]."
    hide a fujihs
    "Nečeká na odpověď a jde ke dveřím."
    j "Dobrou, Adri..ane."
    "Dveře otevře a vyjde ven, zabouchne za sebou."
    "Dojdeš zamknout, nařídíš si budíka a jdeš spát."
    return

label dante_fuji:
    "Otevřeš dveře a k tvému milému překvapení to doopravdy je Dante."
    show d fujihs
    d "Jdu dát prádlo sobě a Adrianovi. V pračce je ještě místo."
    if j.hoodie == d.name:
        d "A já mám u tebe svou mikinu."
        hide d fujihs
        j "Jé, promiň, to mi vůbec nedošlo. Moc díky za půjčení."
        j "Neměla bych ti ji spíše vyprat já?"
        show d fujihs
        d "To je dobrý, stejně potřebuju vyprat zbytek oblečení z Fuji."
    d "Nechceš si tam dát i to svoje?"
    d "Pračka je dost velká, jen do sušičky to budeme muset dát na víckrát."
    hide d fujihs
    j "No a nebude ta pračka dobrou hodinu prát a sušička další hodinu sušit?"
    show d fujihs
    d "Vzali jsme si na to s Adrianem služby. Tak co, bereš nabídku?"
    hide d fujihs
    j "No jasně, že přijmu možnost si nechat vyprat to špinavé oblečení z Fuji."
    j "Jen teda si z toho vyndám spodní prádlo."
    show d fujihs
    d "Tvoje kalhotky jsem už viděl, vypereme to všechno. Dej to sem. Nejsme malý, ne?"
    d "Nebo na tvém spodním prádle uvidím něco, co jsem ještě neviděl? Máš ho s vodotryskem? Či s GPS?"
    d "Vlastně, to jsem už taky viděl."
    hide d fujihs
    "Dante mluví od dveří, zatímco jsi zašla dále do pokoje a bereš plátěnou tašku, do které jsi naskládala ty špinavé věci z Fuji."
    j "Ne, nic takového nevedu. Na."
    "Podáš Dantemu celou tašku."
    show d fujihs
    "Mám službu na pračku, takže budu čekat, než dopere. Plánuju si číst, mám přijít sem a zase ti předčítat?"
    menu:
        "Máš zájem o předčítání?"
        "Ano":
            j "Jsem docela unavená, ale pohádka na dobrou noc zní dobře."
            show d fujihs
            d "No, pohádka... Zapomněla jsi, že máme rozečtený thriller?"
            # TODO make sure that this path is only available if D. already read the book to her
            hide d fujihs
            j "Vím, to byl vtip."
            show d fujihs
            d "Dobře, odnesu to prádlo do pračky a přijdu s knihou."
            hide d fujihs
            j "Domluveno."
            "Dante se sebere a odejde z pokoje."
            "Trošku v pokoji poklidíš a dáš vařit vodu, kdyby chtěl Dante čaj nebo kávu."
            "Nařídíš si budíka a dáš si nabíjet mobil."
            "Neuběhne ani čtvrt hodiny a někdo klepe na dveře."
            j "Běžím, Dante!"
            "zavoláš a jdeš mu otevřít."
            "Dante stojí za dveřmi s knížkou a plechovkou 'Strong Zero'"
            show d fujihs
            d "Dáš si?"
            hide d fujihs
            menu:
                "Dáš si s Dantem trošku ovocné vodky?"
                "Ano":
                    j "Tak trošku na ochutnání."
                    "Dante tedy rozlije obsah plechovky do hrnečků na tácku u varné konvice."
                    "Jeden si vezmeš a jdeš první dál do pokoje."
                "Ne":
                    j "Ne, ne, jsem unavená, ale můžu ti nabídnout čaj."
                    show d fujihs
                    d "To je dobrý, ta vodka mi stačí."
                    hide d fujihs
                    "Pokyneš Dantemu, že má jít za tebou a jdete dále do pokoje."
            "Teď ti ale dojde, že vlastně v pokoji je jen postel a noční stolek. Žádná další židle nebo jiné místo k sezení."
            j "Ups, to jsme nedomysleli. Kde budeš sedět?"
            show d fujihs
            d "Teď jsme spolu spali tři noci v jedné posteli a ty řešíš, kde tady budu sedět?"
            # TODO make sure that this path is only available if Hracka spent Tokio nights on the same room with D.
            d "Normálně si zalez do postele a já si sednu k tobě na kraj."
            hide d fujihs
            "No, asi není vhodné ho teď vyhazovat, a navíc tě zajímá ta knížka."
            "Takže si lehneš do postele a Dante se posedí k tobě na okraj, někam na úroveň tvých boků."
            "Otevře knihu a dá se do čtení"
            "Ani nevíš, kdy jsi usnula a kdy Dante odešel. Ráno tě vzbudil budík na mobilu a Dante v pokoji není."
            "Na nočním stolečku najdeš na bločku s papíry s hlavičkou hotelu napsáno:"
            "Dobrou noc, [j.name_5p]. Probdělou noc si necháme na jindy. D."
        "Ne":
            j "Ne, jsem unavená půjdu spát."
            show d fujihs
            d "Tak já si beru to oblečení, sejdeme se tak v devět ráno na snídani, ale to si ještě napíšeme."
            hide d fujihs
            "Dante odejde a zavře za sebou. Dojdeš se zamknout a jdeš spát"
    return

label sucan_fuji:
    "Otevřeš dveře a k tvému milému překvapení to doopravdy je Sučan."
    show s fujihs
    s "Dvě věci, nechceš si dát prát věci z Fuji? A nechceš si chvíli ještě povídat?"
    hide s fujihs
    "Vybalí na tebe."
    j "Vyprat oblečení? Jo, to by bylo asi super. Povídat? Moc ráda."
    j "Tady je nějaká pračka?"
    show s fujihs
    s "Jo, dole v předsíňce onsenu je za 600 yenů pračka a asi za 200 yenů sušička. Mám v podstatě jen věci z Fuji a z letu a ta pračka je velká."
    hide s fujihs
    j "Oki, hodím si tam také věci."
    if j.hoodie == s.name:
        "Navíc mám tvoji mikinu, tak aspoň ti ji vrátím čistou."
    j "Počkej, hodím si něco přes pyžamo a jdu s tebou."
    show s fujihs
    s "To není nutné. Prát umím obstojně a ta pračka moc jiná, než pračky v Čechách, nebude."
    s "Spíš jsem si říkal, zda si nechceš povídat, než ta pračka dopere."
    hide s fujihs
    j "No jo, ta pračka bude prát tak hodinu a něco a cyklus sušičky je také minimálně na půl hodiny."
    j "Já dvě hodiny vzhůru nevydržím. Hmm, ale ta postel je tak stodvacítka, ne?"
    j "Tak si vem přikrývku a polštář sem, můžeme si povídat. A když usneme, vzbudí nás budík."
    j "A jeden nebo druhý tam dojde."
    show s fujihs
    s "Domluveno, přijdu za chvíli."
    hide s fujihs
    "Sučan odejde, nastavíš si budík na ráno a mobil si dáš nabíjet."
    "Poklidíš trošku pokoj."
    "A během chvíle někdo klepe."
    "Otevřeš a Sučan stojí za dveřmi s polštářem a peřinou."
    show s fujihs
    s "Tak mě tady máš, pračka dopere za hodinu a 10 minut. Budík nastaven."
    hide s fujihs
    "Sedneš si na postel a zády se opřeš o zeď, Sučan si sedne na druhý konec postele."
    j "Hele, Sučane. To, co se dělo dneska nahoře... víš... já tě mám ráda... celý život jsme jako bratr a sestra."
    j "Jsem z toho nějak zmatená."
    show s fujihs
    s "Nevlastní sourozenci. A já rád počkám, než si to v hlavě srovnáš."
    s "Ale nechceš řešit nějaké příjemnější téma?"
    hide s fujihs
    j "Děkuji, jsem ti za to vděčná."
    show s fujihs
    s "Chtěl jsem zarezervovat to drift taxi, ale ty jejich stránky jsou strašně userUNfriendly. Takže jsem jim napsal e-mail."
    s "A prý se nám brzy ozvou, jestli mají volno v termínu, co budeme projíždět kolem."
    hide s fujihs
    j "Tak to je super. Hele, já jsem vážně dost unavená. Nechceme si oba lehnout a prostě si povídat, než usneme?"
    show s fujihs
    s "Dobře."
    hide s fujihs
    "Natáhnete se vedle sebe. Sice to není klasické jednolůžko, ale manželská postel to také není."
    "Sučan tě chytne za ruku dál od něj a donutí tě přetočit se na bok obličejem k němu. Pak ti dá ruku pod hlavu."
    "A našteluje si tě tak, že máš teď hlavu na jeho ramenu."
    show s fujihs
    s "Tak je to lepší než se drcat rameny."
    hide s fujihs
    j "Sučane? Proč to děláš?"
    show s fujihs
    s "Spi, vypadáš unaveně."
    hide s fujihs
    "Chceš mu odporovat, vysmeknout se z objetí. Ale jsi strašně unavená už nemáš sílu. Navíc ti drží ruku a hladí tě ve vlasech."
    j "Tak moc unavená nejsem, pust mě,"
    "špitneš. Cítíš jeho teplo a kolínskou, ale jen tak lehce. Dopadla na tebe únava, tvé tělo je těžké a odmítá se hnout."
    "Víčka se ti zavírají a je strašně těžké je nechat otevřené. Spíš."
    "Vzbudí tě zvuk budíku. Stále jsi ve stejné pozici, v jaké jsi usnula."
    "Sučan se z pod tebe vysouká a típne budík."
    show s fujihs
    s "Spi, jdu dát prádlo z pračky do sušičky."
    hide s fujihs
    "Mžouráš na něj. Konečně ses doprobrala a došlo ti, kde jsi a která bije."
    j "Půjdu já, ty ho pak vyndej ze sušičky."
    show s fujihs
    s "To nepůjde, musím já. Ta pračka se sušičkou jsou v pánském onsenu."
    hide s fujihs
    j "Počkej, ty si mě podvedl? Takže já tě tu nechala spát, abychom se vystřídali u pračky, a já k ní nemůžu?"
    show s fujihs
    s "Nenazval bych to podvodem, spíše využitím situace."
    s "Ale netvrď mi, že se ti to nelíbilo. Usla si dřív, než si dolehla."
    hide s fujihs
    j "Ale to protože si mě uhnal na Fuji."
    show s fujihs
    s "Dobře, jdu přehodit to prádlo, a pak půjdu spát k sobě. Spokojená?"
    hide s fujihs
    j "Jo, tak běž, ty podvodníku."
    "Sučan si posbírá svoje věci a odejde."
    "Zamkneš za ním a usneš."
    return

label mimon_fuji:
    "Za dveřmi srojí Mimoň, stále špinavý a ve stejném oblečení v kterém byl na Fuji."
    show m fuji
    m "Přišel jsem ti oznámit, že už mi zbývají jen 3 čistá trička."
    hide m fuji
    j "Dobře a mně to říkáš proč?"
    show m fuji
    m "Že by se měli vyprat."
    hide m fuji
    "To chce, abych mu vyprala? Tak to ne, jestli po mě něco chce tak by mohl aspoň poprosit."
    j "By se měli? No to asi jo. A ty by si se měl vykoupat, převlíknout a jít spát."
    "Chceš zabouchnout, ale pak si to rozmyšlíš a ustoupíš."
    j "Dobře, to co chceš vyprat, tak přines ráno v sedm ke mě. Koukala jsem, že tu pračku na hotelu mají."
    show m fuji
    m "V sedm vstávat nebudu!"
    hide m fuji
    j "Ber jak je, v sedm tu bude tvé prádlo a nebo máš smůlu."
    "Zavřeš dveře, zamkneš a jdeš spát."
    "Ráno ti zvoní budík před sedmou, vstaneš převlíkneš vezmeš si své špinavé prádlo."
    "Vylezeš před pokoj je 6:59, čekáš jestli se neobjeví Mimoň. Po deseti minutách to vzdáš a sjedeš výtahem dolů."
    scene bg fuji pradelna
    "Večer sis totiž na recepci všimla, že inzerují že mají pračku. Najdeš ji v dámském onsenu. V předcíňce jsou pračky dokonce dvě a dvě sušičky."
    "Naházíš věci do pračky, pomocí překladače se dozvíš, že cyklus stojí 600 yenů a že si na recepci můžeš koupit prací kapsli za 60 yenů."
    "Vezmeš si tedy propozice s sebou a na racepci ukážeš na příslušný odstavec."
    "Za chvíli odcházíš s vítězným výrazem zpátky s kapslý na prádlo a o 60 yenů lehčí."
    "Hodíš ji k prádlu, zavřeš naházíš 600 jenů do pračky a navolíš program. Pračka se pustila."
    "Na displeji se ukážou čísla a nějaké znaky, odvodíš z toho, že cyklus skončí."
    "Nařídíš si budíka, a jdeš zpátky do pokoje. A ještě usneš."
    "Když ti zazvoní budík, sejdeš dolů a věci přendáš do susičky."
    "A je pomalu čas na snídani po chatu jste se domluvili, že se sejtede před pokoji, takže vyjedeš zpátky do patra."
    return

label sucan_fuji_nolove:
    "Za dveřmi stojí Sučan."
    show s fujihs
    s "Nechceš si dát prát věci z Fuji?"
    hide s fujihs
    "Vybalí na tebe."
    j "Vyprat oblečení? Jo, to by bylo asi super. Tady je nějaká pračka?"
    show s fujihs
    s "Jo, dole v předsíňce onsenu je za 600 yenů pračka a asi za 200 yenů sušička. Mám v podstatě jen věci z Fuji a z letu a ta pračka je velká."
    hide s fujihs
    j "Oki, hodím si tam také věci."
    j "Počkej, hodím si něco přes pyžamo a jdu s tebou."
    show s fujihs
    s "To není nutné. Prát umím obstojně a ta pračka moc jiná, než pračky v Čechách, nebude."
    s "Jen mi dej co chceš vyprat běž klidně spát zařídím to."
    hide s fujihs
    j "No jo, ta pračka bude prát tak hodinu a něco a cyklus sušičky je také minimálně na půl hodiny."
    j "Jseš si tím jistý? Nemám ti nějak pomoc?"
    show s fujihs
    s "Ne budu si prát svoje věci, tak mi je jedno jestli je tam o tričko a kalhoty víc."
    hide s fujihs
    j "Tak dobře moc díky."
    "Dojdeš do pokoje do pláťené tašky naházíš věci na vyprání a dáš je Sučanovi."
    show s fujihs
    s "Super, dám ti to zpátky ráno po snídani?"
    hide s fujihs
    j "Jo, ještě jednou díky a dobrou noc."
    "Odejde, nastavíš si budík na ráno a mobil si dáš nabíjet."
    "A během pár minut usneš."
label spanek_fuji:
    "Rozhodla ses, že na nikoho nemáš náladu a že budeš předstírat, že spíš."
    "A za pár minut už to ani není předstírání."
    "Ráno ti zvoní budík, vstaneš, oblékneš se a vezmeš si špinavé prádlo dolů."
    scene bg fuji pradelna
    "Večer sis totiž na recepci všimla, že inzerují že mají pračku. Najdeš ji v dámském onsenu. V předcíňce jsou pračky dokonce dvě a dvě sušičky."
    "Naházíš věci do pračky, pomocí překladače se dozvíš, že cyklus stojí 600 yenů a že si na recepci můžeš koupit prací kapsli za 60 yenů."
    "Vezmeš si tedy propozice s sebou a na racepci ukážeš na příslušný odstavec."
    "Za chvíli odcházíš s vítězným výrazem zpátky s kapslý na prádlo a o 60 yenů lehčí."
    "Hodíš ji k prádlu, zavřeš naházíš 600 jenů do pračky a navolíš program. Pračka se pustila."
    "Na displeji se ukážou čísla a nějaké znaky, odvodíš z toho, že cyklus skončí."
    "Nařídíš si budíka, a jdeš zpátky do pokoje. A ještě usneš."
    "Když ti zazvoní budík, sejdeš dolů a věci přendáš do susičky."
    "A je pomalu čas na snídani po chatu jste se domluvili, že se sejtede před pokoji, takže vyjedeš zpátky do patra."
    return
