label akt7:
    "Když se ráno probudíš asi 10 minut před budíkem, zjistíš, že Dante je oblečený a leží na svém futonu s knížkou."
    "Sučan je také připravený s batohem, takže vystřelíš z postele, vypneš nadcházející budík, aby neřval na celou místnost a zamíříš do koupelny."
    "Když vylezeš, tak Sučan už čeká u dveří a Dante se také zvedá. A k tvému zděšení zjistíš, že frontu na koupelnu stojí Mimoň a také vypadá sbaleně."
    j "Stalo se tu něco?"
    show s kjoto
    s "Jdu napřed."
    hide s kjoto
    "Odejde za dveře."
    show d kjoto
    d "Ještě si nejdla, nasnídej se a pak vyrazíme."
    hide d kjoto
    j "Něco jste si provedli se Sučanem?"
    show d kjoto
    d "Adrianovi není stále dobře, takže zůstává na ubytování. Ale Mimoň s námi prý půjde."
    hide d kjoto
    "To vážně ignoruje, co mu říkáš?"
    if j.love_points.get(a.name,0)>5:
        "Počkat, Adrianovi ještě nění dobře?"
        menu:
            "Chceš zůstat s Adrianem na ubytování, když mu není dobře?"
            "Ano, radši s ním zůstaneš.":
                call osetrovani_Adriana
            "Ne, chci vidět Kjoto, snad by si řekl o pomoc kdyby bylo třeba.":
                call Kjoto
    return
label osetrovani_Adriana:
    j "Zůstanu s Adrianem."
    show d kjoto
    d "Cože?"
    hide d kjoto
    j "Zůstanu, tady s Adrianem, jestli mu pořád nění dobře, tak by asi neměl celý den zůstat sám."
    show d kjoto
    d "Tak s ním zůstanu já, není důvod, aby si tu zůstávala ty."
    hide d kjoto
    "Vzpomeneš, jak tě Adrian zapřisáhl, aby si o jeho slabosti neříkala Dantemu a rozhodneš se, že by Adrian asi Danteho na pokoji nechtěl."
    j "Hele já jsem také unavená z Fuji. Včera jsem si také moc neodpočinula."
    j "Chci tu zůstat hlavně kvůli sobě. Adrian je spíš výmluva."
    "Pochybovačně si tě změří pohledem, naštěstí na to Mimoň vychází z koupelny."
    show d kjoto
    d "Odchod!"
    hide d kjoto
    "Zavelí doslova Dante, takže Mimoň si sebere batoh a odcházejí."
    "Zůstala jsi tedy na Apartmánu jenom sama s Adrianem."
    "Dojdeš si do ledničky pro snídani, sníš si ji u stolečku, který je tak nízký, že u něho sedět na zemi."
    "Po snídani po sobě uklidíš, přerovnáš si věci v kufru a rozhodneš se, že se podíváš na balkón."
    "Po chvíli přemýšlení jak to funguje, se ti podaří soupačky otevřít"
    "Otevře se ti výhled na Tokio, sálající vedro ti ihned vykouzlí krůpěje potu na čele."
    "Vykloníš se přes zábradlí aby sis užila výhled."
    "Užíváš si chvilku, kterou sis vytvořila a od začátku pobytu si snad poprvé můžeš užívat atmosféry japonska."
    "Bez pocitu naprosté vyčerpanosti, nebo s klukama za prdelí."
    "Z rozmínání, tě vytrhne Adrianův hlas, teda spíše zasténání."
    if j.love_points.get(a.name, 0) > 5:
        menu:
            "Poběžíš k Adrianovi, nebo si přivřeš dveře a užiješ si chvilku pro sebe?"
            "Pomoc Adrianovi":
                "Ihned se rozeběhneš do pokoje."
                show a kjoto sleeping
                "Adrian, leží na posteli a vypadá v bolestech. Když k němu přijdeš zjistíš, že má horečku."
                hide a kjoto sleeping
                "Celé tělo mu vybruje. Super, takže to vypadá na svalovou horečku."
                j "Adriane, Adriane, slysíš mě?"
                show a kjoto sleeping
                a "Mm, [j.name5p]"
                hide a kjoto sleeping
                "Zamumlá, zatímco mu drkotají zuby o sebe."
                "Pochopíš, že má momentálně zimnici, rozhodneš se tedy nejdříve ho zahřát a až zimnice polevý tak stáhnout horečku."
                "Pořádně ho zabalíš do jeho peřiny a ještě přineseš svojí přikrývku, kterou přes něj přehodíš."
                "Z kufru vyndáš cestovní lékáničku a z ní paralen. Dojdeš do přecíňky dáš vařit vodu a uděláš čaj."
                "Ten doředíš trochu studenou vodou tak aby se dal rovnou pít."
                "S čajem a paralenem se vrátíš k Adrianovi."
                j "Adri, musíš si vzít prášek, máš štrašnou horečku."
                show a kjoto sleeping
                a "Mami?"
                hide a kjoto sleeping
                "Evidentně vůbec nezvládá vnímat, ale po chvíli se ti ho podaří dostat do polosedu."
                "Dáš mu prášek a hrníček mu přiložíš k ústům."
                j "Adri, potřebuju od tebe trošku spolupráce, spolkni to a napij se."
                "Ani neotevře oči, ale nakonec prášek spolkne a trochu ho zapije."
                "Podaří se ti ho zase uložit a pořádně přikrýt."
                "Chytíš ho pod dekami za ruku, která hřeje víc jak ohříváček rukou v zimě."
                j "Adri, snaž se usnout. Za chvíli ti bude teplo."
                "Ještě chvíli vybruje, ale asi za pět minut usne a svaly trochu poleví."
                "Pustíš mu ruku a dojdeš do koupelny pro ručník, ten nemočíš ve vlažné vodě a dojdeš ho dát Adrianovi na čelo."
                "Pak si vzpomeneš, že máš v kufru asi 15 balíčků kapesníčků, protože Mimoňovi balila maminka a asi trochu neodhadla počet balení."
                "A Mimoň když to zjistil, chtěl je vyhodit. Vyndáš jeden balíček namočíš je taktéž ve vlažné vodě a přiložíš je Adrianovi na zápěstí a kotníky."
                "Všineš si, že má Adrian na pravé noze jizvu."
                "Dojdeš ještě asi dvakrát zchladit ručník, co si dala Adrianovi na čelo."
                "Mezitím asi začne působit prášek, který si do něj dostala, takže horečka evidentně klesla."
                "Odneseš a vyházíš mokré kapesníčky a ručník, sundáš z něho svojí peřinu a natáneš se u sebe."
                "Adrian vypadá, že konečně vklidu spí. Po chvíli začneš mít hlad a dojde ti, že Adrian také nic nesnědl."
                "Vezmmeš si tedy, věci a vyrazíš do obchodu koupit vám něco k jídlu."
                "Než odejdeš tak ještě jemně probudíš Adriana a donutíš ho dopít, ten čaj."
                "V krámě chvíli rozmýšlíš, co vlastně vzít, v čechách by si zašla do restaurace koupit vývar, nebo by si ho sama uvařila, ale tady?"
                "Nakonec se rozhodneš pro dva instantní rámeny, kolu, čaj, kafe, čokoládu. Zaplatíš a vracíš se zpět."
                "Adrian spí, když mu šáhneš na čelo už tolik nesálá, takže horečka klesla, to je dobré znamení."
                "Dáš vařit vodu, nudle rozlámeš na kousíčky a zaliješ jeden z rámenů. Sice jsi v krámě dostala celou výbavu, ale hůlky ti ve vašem stavu přijdou nepoužitelné."
                "Naštěstí si vezeš cestovní lžíci. Necháš rámen chvíli stát a mezitím napíše klukům jak jsou na tom."
                "Zrovna jsou v nějakém opičím parku. Kde je to prý opačně než jinde, lidé jsou v klecích při krmení a opice volně běhají."
                "Když rámen trošku vychladne, vezmeš si ho i s lžící k Adrianovi."
                "Sedneš si k němu na kraj a pokusíš se ho probudit."
                j "Adriane musíš, něco sníst."
                "Otevře oči a trošku zděšeně a zahambeně se na tebe podívá"
                show a kjoto openeyes
                a "[j.name5p]?"
                hide a kjoto openeyes
                j "Sedni si musíš něco sníst, jestli se to nezlepší, měli bychom tě vzít do nemocnice."
                show a kjoro openeyes
                a "To nebude nutné, nic mi není, děkuji za jídlo."
                hide a kjoto openeyes
                "Velmi obtížně, se posadí na posteli i když se snaží hrát na hrdinu jak mu nic není."
                j "Adriane, já tady jsem s tebou celý dopoledne, nehraj tu na mě, že ti nic není!"
                j "Měl si tak vysokou horečku, že si snad i blouznil, tohle není prdel, podle mě máš svalovou horečku, protože jsi přepískl tu Fuji."
                "Řekneš možná trošku až moc ostře."
                show a kjoto openeyes
                a "Ale mě vážně už nic není."
                hide a kjoto openeyes
                j "O tom si povíme až se najíš."
                "Nabereš trošku rámenu na lžíci a dáš mu jí před pusu."
                "Adrian zrudne."
                show a kjoto openeyes
                a "Já se můžu najíst sám, tohle je trošku ponižující."
                hide a kjoto openeyes
                j "Tak mám napsat Dantemu, ať tě přijde nakrmit on?"
                show a kjoto openeyes
                a "Ne to ne, já to ale vážně zvládnu sám. A jakto, že tu jsme jen samy?"
                hide a kjoto openeyes
                j "Jeli si udělat okruh po Kjotu. Dante tu chtěl s tebou zůstat, ale vypakovala jsem ho."
                j "Stačí ti to jako odpověď? Koukej teda jíst když to zvládneš sám. Dantemu o tomhle nic neřeknu."
                show a kjoto openeyes
                a "Děkuji, vážím si toho, všeho co pro mě děláš."
                hide a kjoto openeyes
                "Vezme si od tebe lžíci a začne opravdu pomalu jíst."
                "Když vidíš, že to ale teda zvládne, položíš mu ramen do klína a jdeš si udělat svůj."
                j "Hele, mamka ti hodně chybí co?"
                show a kjoto openeyes
                a "Jo chybí, byla to skvělá ženská. Proč?"
                hide a kjoto openeyes
                j "Když s měl horečku, tak jsi mumlal moje jméno, ale když jsem na tebe promluvila, řekl jsi mi mami."
                show a kjoto openeyes
                a "Promiň, to mě mrzí. A strašně mě štve, že zase zachraňuješ ty mě."
                hide a kjoto openeyes
                j "To nestojí za řeč, až dojíš ten rámen, tak sníš ještě čokoládu a koupila jsem kolu."
                j "Potřebuješ do sebe dostat nějakou energii. Nechápu proč si tu Fuji nevzdal."
                show a kjoto openeyes
                a "..."
                hide a kjoto openeyes
                "Nic ti neřekne, dělá, že ho momentálně polívka před ním zajímá nejvíce ze všeho, zároveň působí tak nějak smutně a vesele zároveň."
                "Sníš si svůj oběd, doneseš Adrianovi ještě tu čokoládu a kolu, dopočítáš kolik hodin uběhlo od toho co si do něj dostala paralen a rozhodneš, že je čas na další."
                "Adrian sní asi půlku té čokolády, vezme si od tebe paralen zapije ho kolou. A přes to, že v kole je kofein, během pár minut zase usne."
                "Uklidíš tedy po obědě a jdeš se také natáhnout, dopadla na tebe také únava z Fuji a během pár minut spíš."
                "Vzbudíš se asi ve tři odpoledne, dojdeš di do koupelny, daš si i rychlou sprchu na probuzení."
                "A dojde vzbudit Adriana aby se napil."
                j "Adriane, měl by ses napít."
                show a kjoto openeyes
                a "Jo, jasně."
                hide a kjoto openeyes
                "Řekne ještě malinko rozespale. Napije se koli, kterou si mu přinesla z ledničky."
                show a kjoto openeyes
                a "Děkuji, už mi je vážně lépe. Šel bych se vykoupat a pak bychom se mohli připojit ke klukům."
                hide a kjoto openeyes
                j "Není to trošku narychlo? No dobře, dojdi se vykoupat a když se i pak budeš cítit, tak se k nim můžeme připojit."
                "Adrian si vyndá věci a vyrazí do koupelny."
                j "Nech si pootevřeno."
                show a kjoto openeyes
                a "Cože?"
                hide a kjoto openeyes
                j "Nech si pootevřené dveře prosím, mám o tebe strach, kdyby se ti udělalo hůř, tak ať se k tobě dostanu."
                j "Nepolezu ti tam, věř, že kdybych tě chtěla očumovat, měla jsem k tomu dneska celé dopoledne a ani by si to nevěděl."
                show a kjoto openeyes
                a "Dobře. Asi děkuji?"
                hide a kjoto openeyes
                "Úplně nervozní a rudý zaleze do koupelny, dveře sice zabouchne ale zámek neslyšíš klapnout."
                "Převlíkneš se tedy do věcí na ven, sbalíš si věci a napíšeš klukům kde jsou a kde budou tak za hodinu."
                "Adrian vyleze asi za půl hodiny a vypadá tak o 100% lépe."
                j "Tak jak ti je?"
                show a kjoto openeyes
                a "Myslím, že se citím na drobnou procházku."
                hide a kjoto openeyes
                j "No moc se mi to nelíbí, ale když myslíš. Kluci jsou teď v nějaké sojovkárně, máme se s nimi sejít v nějaké tržnici."
                j "Jseš si jistý, že to zvládneš? ještě před pár hodinami jsi vypadal, že na svalovou horečku v nejlepším jen zemřeš."
                show a kjoto openeyes
                a "Vážně mi je dobře, asi ta tvá péče."
                hide a kjoto openeyes
                j "Ale jestli mi po cestě někde zkolabuješ, tak všechno Dantemu řeknu. A po tom co tě vlastnoručně zabiju. Tak mi budeš dlužit minimálně jedno pozvání na večeři."
                show a kjoto openeyes
                a "Nezkolabuju a na tu večeři tě pozvu i bez toho abys mě musela zabít co ty na to?"
                hide a kjoto openeyes
                menu:
                    "Mám to brát jako pozvání na rande?":
                        show a kjoto openeyes
                        a "Ano."
                        hide a kjoto openeyes
                        $ j.add_love_points_for_person(a.name, 2)
                        "Wow, tak tady to začíná být zajímavé. Adrian tě právě pozval na rande."
                        "Tak nějaké náznaky tu byly i dříve, ale tady jde do tuhého. Ale asi by bylo lepší, kdyby to nebylo tak okaté."
                        "Přeci jen nechceš dělat dusno v partě, navíc Sučan tě možná až přehnaně brání, takže by bylo lepší, být opatrní."
                        j "Dobře beru tě za slovo, jen bych byla opatrnější před ostaníma, nebo bych to odložila až po návratu z Japonska."
                        "Tvá odpověď se evidentně Adrianovi moc nelíbí. Protože si povzdechne a jde si balit věci."
                    "To jsem jen tak plácla, není třeba.":
                        show a kjoto openeyes
                        a "Tak se asi se pobalíme a vyrazíme."
                        hide a kjoto openeyes
                        $ j.add_love_points_for_person(a.name, 0.5)
            "Užít si výhled":
                "Další zasténání se neozve, takže si užíváš výhled a jemný vítr který si pohrává s tvými vlasy."
                "V pokoji je ticho, tak se ti možná něco jen zdálo."
                "Po chvíli zaslouženého oddechu se vrátíš do pokoje."
                "Adrian spí, když ho dojdeš zkontrolovat, zjistíš že má horečku."
                "Uvaříš čaj, z cestovní lékarničky vytáhneš paralen. Adriana vzbudíš a donutíš ho sníst prášek."
                "Adrian zase usne a ty se věnuješ také svým věcem, kolem polednícho se rozhodneš vyrazit koupit něco k obědu."
                "Před odchodem ještě vzbudíš Adriana aby se napil a aby věděl, že jdeš pryč."
                "V nejbližším kombiny, koupíš dva rámeny a něco k pití."
                "Vrátíš se na ubytko a oba rámeny zaleješ horkou vodou. Když trošku schladnou vzbudíš Adriana."
                "Ten se vysouká z podpeřiny dojde si do koupelny a po chvíli se k tobě připojí u nízkého stolu na zemi."
                "U kterého musíte sedět na takových 'podesedácívh' taktéž na zemi."
                "Jídlo po chvíli sníte, Adrian ti poděkuje a jde si zase lehnout."
                "Uklidíš odpadky, a natáhneš se. Napíšeš klukům jak jsou na tom."
                "Podle všeho akorát jsou z nějakého parku s opicemi taktéž na oběd. Pak plánují nějakou sojovkárnu."
                "Domluvíte se, že by ses večer připojila. Po té také usneš."
                "Vzbudíš se asi ve tři, dojdeš tedy do koupelny. Po rychlé sprše se sbalíš."
                "Vzbudíš Adriana a řekneš mu že se plánuješ připojit ke klukům."
                show a kjoto openeyes
                a "Už mi je lépe, počkej, vysprchuju se a půjdu také."
                hide a kjoto openeyes
                j "No když myšlíš."
                "Adrian si vezme věci a zamíří do koupelny, ty mezitím vykomunikuješ místo setkání."
                "Adrianovi to naštěstí dlouho netrvá a za chvíli už vycházíte na metro."
    "Další zasténání se neozve, takže si užíváš výhled a jemný vítr který si pohrává s tvými vlasy."
    "V pokoji je ticho, tak se ti možná něco jen zdálo."
    "Po chvíli zaslouženého oddechu se vrátíš do pokoje."
    "Adrian spí, když ho dojdeš zkontrolovat, zjistíš že má horečku."
    "Uvaříš čaj, z cestovní lékarničky vytáhneš paralen. Adriana vzbudíš a donutíš ho sníst prášek."
    "Adrian zase usne a ty se věnuješ také svým věcem, kolem polednícho se rozhodneš vyrazit koupit něco k obědu."
    "Před odchodem ještě vzbudíš Adriana aby se napil a aby věděl, že jdeš pryč."
    "V nejbližším kombiny, koupíš dva rámeny a něco k pití."
    "Vrátíš se na ubytko a oba rámeny zaleješ horkou vodou. Když trošku schladnou vzbudíš Adriana."
    "Ten se vysouká z podpeřiny dojde si do koupelny a po chvíli se k tobě připojí u nízkého stolu na zemi."
    "U kterého musíte sedět na takových 'podesedácívh' taktéž na zemi."
    "Jídlo po chvíli sníte, Adrian ti poděkuje a jde si zase lehnout."
    "Uklidíš odpadky, a natáhneš se. Napíšeš klukům jak jsou na tom."
    "Podle všeho akorát jsou z nějakého parku s opicemi taktéž na oběd. Pak plánují nějakou sojovkárnu."
    "Domluvíte se, že by ses večer připojila. Po té také usneš."
    "Vzbudíš se asi ve tři, dojdeš tedy do koupelny. Po rychlé sprše se sbalíš."
    "Vzbudíš Adriana a řekneš mu že se plánuješ připojit ke klukům."
    show a kjoto openeyes
    a "Už mi je lépe, počkej, vysprchuju se a půjdu také."
    hide a kjoto openeyes
    j "No když myšlíš."
    "Adrian si vezme věci a zamíří do koupelny, ty mezitím vykomunikuješ místo setkání."
    "Adrianovi to naštěstí dlouho netrvá a za chvíli už vycházíte na metro."
    return
label Kjoto:
    "Pochopila jsi, že odpovědi se nedočkáš, pobalíš si věci a mezitím Mimoň vyjde z koupelny."
    "Z ledničky si vyndáš věci na snídani a rychle je sníš. Mimoň se mezití také sbalil, takže můžete vyrazit."
    "Dole se potkáte se Sučanem. Ozve se jeho oblíbené Ikimašó a vyrazíte."
    if j.love_points.get(s.name,0)>5:
        "Připojíš se k Sučanovi a po cestě na metro si povídáte."
        "Protože, Dantemu s Mimoněm malinko utečete, usoudíš, že vás nemůžou slyšet a položiš Sučanovi otázku, která ti už nějakou dobou vrtá v hlavě."
        j "Hele, Sučane můžu se tě na něco zeptat?"
        show s kjoto
        s "Samozřejmě, [j.name5p], ty můžeš vždycky."
        hide s kjoto
        "Co tak najednou? Vždyť se známe od mala, to sis uvědomil, že ke mě něco citíš až teď?"
        show s kjoto
        s "Ne já to vím dlouho, párkrát sem se ti to snažil naznačit."
        s "Jen ty si to asi nevnímala, protože mě prostě bereš jen jako pozorného bratra. No a pak si byla ve vztahu."
        s "Rozhodně sem nechtěl být ten, co ti bude kazit vztah. Na to nemám právo."
        s "Ale strašně mě ničilo, jak byl tvůj ex strašnej, zasloužíš si někoho lepšího."
        hide s kjoto
        j "Nikdy jsem si toho nevšimla, promiň. Chovala jsem se trošku jako kráva, co?"
        show s kjoto
        s "Takhle o sobě nemluv. A nekaž mi ten krásný pocit, že jsem teď s tebou."
        hide s kjoto
        j "No o tom se sní každýmu jít se mmnou v Kjótu na autobus"
        "Mezitím jste došli k zastávce autobusu, zastavili jste a Dante s Mimoněm vás došli."


    elif j.love_points.get(d.name,0)>5:
        "Připojíš se do dvojice s Dantem, Sučan jde tedy napřed s Mimoněm."
        "Kráčíte mlčky vedle sebe."
        j "Myslíš, že Adrian bude v pohodě? Nevypadal moc dobře."
        show d kjoto
        d "Jo vyspí se a bude mu dobře, asi jsme to s tou Fuji přehnali."
        hide d kjoto
        j "Hmm... Taky nejsem úplně v pohodě. "
        show d kjoto
        d "Bylo to náročné pro všechny a díky některým i psychicky."
        hide d kjoto
        "Přikývneš a nastane zase ticho. Sbíráš odvahu ke své nasledující otázce."
        j "Hele, Dante, nechceš si přestat se mnou hrát?"
        show d kjoto
        d "Co? Asi nerozumím tvé otázce."
        hide d kjoto
        j "Ubijíjí mě to, že nevím na čem jsem. Takže by si mi možná mohl říct jak to se mnou máš."
        j "Takže holka na jednu noc, vztah, nebo si to všechno blbě vykládám?"
        show d kjoto
        d "A co by si chtěla odemne slyšet?"
        hide d kjoto
        menu:
            "Že si tuhle dovolenou užiju se vším všudy.":
                show d kjoto
                d "Tak to nemůžu sloužit. Holky na jednu noc sice sbírám, ale vždy se ujistím, že si nebudou kromě luxusního sexu nic pamatovat." #TODO co si myslíte? nebo mám nechat možnost sexu na jednu noc?
                d "Rozhodně ne jméno a obličej, uspokojila má odpověď tvoji dušičku?"
                d "Ale kdo ví? Třeba se ti podaří, přesvědčit mě, abych udělal vyjímmku."
                hide d kjoto
                $ j.add_love_points_for_person(d.name,1)
            "Že máš nějaké morální standardy.":
                show d kjoto
                d "Dost vysoké. Ale taky dost nebezpečné povolání."
                $ j.add_love_points_for_person(d.name,2)
                d "Takže pokud se mnou někdy nějaká holka bude chtít být, tak si mě musí vzít. A počítat s tím, že rozvod nepřipadá v úvahu."
                d "Pouze její smrt, ale ta jí může potkat i bez rozvodu."
                hide d kjoto
                j "Jojo to už jsem slyšela, opakovaný vtip není vtipem."
                show d kjoto
                d "Myslíš, že žertuju? Veř tomu, že bych rád našel holku, která by byla ochotná akceptovat můj divoký, smrtí nasáklý život."
                hide d kjoto
                j "Tohle mě vážně nebaví, asi mi budeš muset říct o sobě víc, tohle mě unavuje."
                j "Pořád jen mluvíš o svatbě, nebezpečí a smrti. Buď to vůbec nevytahuj a nebo mluv na rovinu."
                show d kjoto
                d "Jsem vládní agent, nejsem tady na dovolené,což si asi pochopila, ale mám se zúčastnit jedné předávky drog."
                d "Aby to nebylo jednoduché, tak jsem nastrčená krysa v evropské odnoži yakuzi (yakuza - je japonská mafie)"
                d "Vztahům se raději vyhybám, protože mě můžou oslabit a navíc všichni v mé blízkosti jsou automaticky ve smrtelném nebezpečí."
                d "Do teď můj jedniný přítel byl a je Adrian, který si kvůli mně už pár únosy prošel. Byl jsem rozhodlý, že holku si nikdy nenajdu."
                d "Ale tebe nějak nemůžu dostat z hlavy."
                hide d kjoto
                "Tak to je šílené to si musel všechno vymyslet, tak yakuza v Japonsku samozřejmě stále úřaduje."
                "Ale její evropská větev? Blbost. Vladní agent? Nejsme v Americe."
                j "Ještě mi řekni, že máš s sebou zbraň. Ať je to kompletní."
                show d kjoto
                d "Teď ne, ale na apartmánu, mám dvě automatické pistole."
                hide d kjoto
                j "Není možné, neprošel by si přes letiště."
            "Že si to blbě vykládám.":
                show d kjoto
                d "Pravděpodobně ano, jen se snažím být milý, když spolu máme strávit tolik času."
                hide d kjoto
                $ j.add_love_points_for_person(d.name,-2)
    elif j.hate_points.get(m.name,0)>5:
        "Z nějakého důvodu se na tebe nalepil Mimoň, a aktivně s tebou drží krok."
    else:
        "Všichni společně vyrazíte na metro"