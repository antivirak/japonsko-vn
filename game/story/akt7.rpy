label akt7:
    scene bg hotel kjoto
    "Když se ráno probudíš asi 10 minut před budíkem, zjistíš, že Dante je oblečený a leží na svém futonu s knížkou."
    scene bg kjoto koupelna
    "Sučan je také připravený s batohem, takže vystřelíš z postele, vypneš nadcházející budík, aby neřval na celou místnost a zamíříš do koupelny."
    scene bg hotel kjoto
    "Když vylezeš, Sučan už čeká u dveří a Dante se také zvedá. A k tvému zděšení zjistíš, že frontu na koupelnu stojí Mimoň a také vypadá sbaleně."
    j "Stalo se tu něco?"
    show s kjoto
    s "Jdu napřed."
    hide s kjoto
    "Odejde za dveře."
    show d kjoto
    d "Ještě si nejedla, nasnídej se a pak vyrazíme."
    hide d kjoto
    j "Něco jste si provedli se Sučanem?"
    show d kjoto
    d "Adrianovi není stále dobře, takže zůstává na ubytování. Ale Mimoň s námi prý půjde."
    hide d kjoto
    "To vážně ignoruje, na co se ho ptáš?"
    if j.love_points.get(a.name, 0) > 4:
        "Počkat, Adrianovi ještě není dobře?"
        menu:
            "Chceš zůstat s Adrianem na ubytování, když mu není dobře?"
            "Ano, radši s ním zůstaneš.":
                call osetrovani_Adriana
            "Ne, chci vidět Kjóto, snad by si řekl o pomoc, kdyby bylo třeba.":
                call Kjoto
    jump Kjoto

label osetrovani_Adriana:
    j "Zůstanu s Adrianem."
    show d kjoto
    d "Cože?"
    hide d kjoto
    j "Zůstanu, tady s Adrianem, jestli mu pořád není dobře, tak by asi neměl celý den zůstat sám."
    show d kjoto
    d "Tak s ním zůstanu já, není důvod, abys tu zůstávala ty."
    hide d kjoto
    "Vzpomeneš, jak tě Adrian zapřisáhl, aby jsi o jeho slabosti neříkala Dantemu a rozhodneš se, že by Adrian asi Danteho na pokoji nechtěl."
    j "Hele, já jsem taky unavená z Fuji. Včera jsem si také moc neodpočinula."
    j "Chci tu zůstat hlavně kvůli sobě. Adrian je spíš výmluva."
    "Pochybovačně si tě změří pohledem, naštěstí na to Mimoň vychází z koupelny."
    show d kjoto
    d "Odchod!"
    hide d kjoto
    "Doslova zavelí Dante, takže si Mimoň sebere batoh a odcházejí."
    "Zůstala jsi tedy na apartmánu jenom sama s Adrianem."
    "Dojdeš si do ledničky pro snídani, sníš si ji u stolečku, který je tak nízký, že u něho sedíš na zemi."
    "Po snídani po sobě uklidíš, přerovnáš si věci v kufru a rozhodneš se, že se podíváš na balkón."
    "Po chvíli přemýšlení, jak to funguje, se ti podaří šoupačky otevřít"
    scene bg kjoto vyhled hotel
    "Otevře se ti výhled na Kjóto. Sálající vedro ti ihned vykouzlí krůpěje potu na čele."
    "Vykloníš se přes zábradlí, aby sis užila výhled."
    "Užíváš si chvilku, kterou sis vytvořila a od začátku pobytu si snad poprvé můžeš užívat atmosféry Japonska."
    "Bez pocitu naprosté vyčerpanosti, nebo s klukama za prdelí."
    "Z rozjímání tě vytrhne Adrianův hlas, tedy spíše zasténání."
    if j.love_points.get(a.name, 0) > 4:
        menu:
            "Poběžíš k Adrianovi, nebo si přivřeš dveře a užiješ si chvilku pro sebe?"
            "Pomoc Adrianovi":
                scene bg hotel kjoto
                "Ihned se rozeběhneš do pokoje."
                show a kjoto sleeping
                "Adrian leží na posteli a vypadá to, že je v bolestech. Když k němu přijdeš, zjistíš, že má horečku."
                hide a kjoto sleeping
                "Celé tělo se mu klepe. Super, takže to vypadá na svalovou horečku."
                j "Adriane, Adriane, slyšíš mě?"
                show a kjoto sleeping
                a "Mm, [j.name_5p]"
                hide a kjoto sleeping
                "Zamumlá, zatímco mu drkotají zuby o sebe."
                "Pochopíš, že má momentálně zimnici, rozhodneš se tedy nejdříve ho zahřát a až zimnice poleví, tak stáhnout horečku."
                "Pořádně ho zabalíš do jeho peřiny, a ještě přineseš svoji přikrývku, kterou přes něj přehodíš."
                "Z kufru vyndáš cestovní lékárničku a z ní paralen. Dojdeš do předsíňky, dáš vařit vodu a uděláš čaj."
                "Ten doředíš trochou studené vody tak, aby se dal rovnou pít."
                "S čajem a paralenem se vrátíš k Adrianovi."
                j "Adri, musíš si vzít prášek, máš strašnou horečku."
                show a kjoto sleeping
                a "Mami?"
                hide a kjoto sleeping
                "Evidentně vůbec nezvládá vnímat, ale po chvíli se ti ho podaří dostat do polosedu."
                "Dáš mu prášek a hrníček mu přiložíš k ústům."
                j "Adri, potřebuju od tebe trošku spolupráce, spolkni to a napij se."
                "Ani neotevře oči, ale nakonec prášek spolkne a trochu ho zapije."
                "Podaří se ti ho zase uložit a pořádně přikrýt."
                "Chytíš ho pod dekami za ruku, která hřeje víc jak ohříváček rukou v zimě."
                j "Adri, snaž se usnout. Za chvíli ti bude teplo."
                "Ještě chvíli vibruje, ale asi za pět minut usne a svaly trochu poleví."
                "Pustíš mu ruku a dojdeš do koupelny pro ručník, ten namočíš ve vlažné vodě a dojdeš ho dát Adrianovi na čelo."
                "Pak si vzpomeneš, že máš v kufru asi 15 balíčků kapesníčků, protože Mimoňovi balila maminka a asi trochu neodhadla počet balení."
                "A Mimoň když to zjistil, tak je chtěl vyhodit. Vyndáš jeden balíček, namočíš kapesníčky ve vlažné vodě a přiložíš je Adrianovi na zápěstí a kotníky."
                "Všimneš si, že má Adrian na pravé noze jizvu."
                "Dojdeš ještě asi dvakrát zchladit ručník, co jsi dala Adrianovi na čelo."
                "Mezitím asi začne působit prášek, který si do něj dostala, takže horečka evidentně klesla."
                "Odneseš a vyházíš mokré kapesníčky a ručník, sundáš z Adriana svoji peřinu a natáhneš se u sebe."
                "Vypadá to, že konečně v klidu spí. Po chvíli začneš mít hlad a dojde ti, že Adrian také nic nesnědl."
                "Vezmeš si tedy věci a vyrazíš do obchodu koupit něco k jídlu."
                "Než odejdeš, tak ještě jemně probudíš Adriana a donutíš ho dopít čaj."
                scene bg kjoto ulice
                "V krámě chvíli rozmýšlíš, co vlastně vzít. V Čechách bys zašla do restaurace koupit vývar, nebo by jsi ho sama uvařila, ale tady?"
                "Nakonec se rozhodneš pro dva instantní rameny, kolu, čaj, kafe, čokoládu. Zaplatíš a vracíš se zpět."
                scene bg hotel kjoto
                "Adrian spí. Když mu šáhneš na čelo, už tolik nesálá, takže horečka klesla. To je dobré znamení."
                "Dáš vařit vodu, nudle rozlámeš na kousíčky a zaliješ jeden z ramenů. Sice jsi v krámě dostala celou výbavu, ale hůlky ti ve vašem stavu přijdou nepoužitelné."
                "Naštěstí si vezeš cestovní lžíci. Necháš ramen chvíli stát a mezitím napíšeš klukům, jak jsou na tom."
                "Zrovna jsou v nějakém opičím parku, kde je to prý opačně než jinde. Lidé jsou při krmení v klecích a opice volně běhají."
                "Když ramen trošku vychladne, vezmeš si ho i se lžící k Adrianovi."
                "Sedneš si k němu na kraj a pokusíš se ho probudit."
                j "Adriane, musíš něco sníst."
                "Otevře oči a trošku zděšeně a zahanbeně se na tebe podívá."
                show a kjoto openeyes
                a "[j.name_5p]?"
                hide a kjoto openeyes
                j "Sedni si, musíš něco sníst. Jestli se to nezlepší, měli bychom tě vzít do nemocnice."
                show a kjoto openeyes
                a "To nebude nutné, nic mi není, děkuji za jídlo (itadakimas)."
                hide a kjoto openeyes
                "Velmi obtížně se posadí na posteli, i když se před tebou snaží hrát na hrdinu, jak mu nic není."
                j "Adriane, já tady jsem s tebou celý dopoledne. Nehraj tu na mě, že ti nic není!"
                j "Měl si tak vysokou horečku, že si snad i blouznil. Tohle není prdel. Podle mě máš svalovou horečku, protože jsi přepískl tu Fuji."
                "Řekneš možná trošku až moc ostře."
                show a kjoto openeyes
                a "Ale mně vážně už nic není."
                hide a kjoto openeyes
                j "O tom si povíme, až se najíš."
                "Nabereš trošku ramenu na lžíci a dáš mu ji před pusu."
                "Adrian zrudne."
                show a kjoto openeyes
                a "Já se můžu najíst sám, tohle je trošku ponižující."
                hide a kjoto openeyes
                j "Tak mám napsat Dantemu, ať tě přijde nakrmit on?"
                show a kjoto openeyes
                a "Ne, to ne. Já to ale vážně zvládnu sám. A jak to, že tu jsme jen my dva sami?"
                hide a kjoto openeyes
                j "Jeli si udělat okruh po Kjótu. Dante tu chtěl s tebou zůstat, ale vypakovala jsem ho."
                j "Stačí ti to jako odpověď? Koukej teda jíst, když to zvládneš sám. Dantemu o tomhle nic neřeknu."
                show a kjoto openeyes
                a "Děkuji, vážím si toho všeho, co pro mě děláš."
                hide a kjoto openeyes
                "Vezme si od tebe lžíci a začne opravdu pomalu jíst."
                "Když vidíš, že to ale teda zvládne, položíš mu ramen do klína a jdeš si udělat svůj."
                j "Hele, mamka ti hodně chybí co?"
                show a kjoto openeyes
                a "Jo chybí, byla to skvělá ženská. Proč?"
                hide a kjoto openeyes
                j "Když si měl horečku, tak jsi mumlal moje jméno, ale když jsem na tebe promluvila, řekl jsi mi mami."
                show a kjoto openeyes
                a "Promiň, to mě mrzí. A strašně mě štve, že zase zachraňuješ ty mě."  # TODO zase - use variable?
                hide a kjoto openeyes
                j "To nestojí za řeč, až dojíš ten rámen, tak sníš ještě čokoládu. A koupila jsem kolu."
                j "Potřebuješ do sebe dostat nějakou energii. Nechápu, proč si tu Fuji nevzdal."
                show a kjoto openeyes
                a "..."
                hide a kjoto openeyes
                "Nic ti neřekne, dělá, že ho momentálně polévka před ním zajímá nejvíce ze všeho na světě. K tomu působí tak nějak smutně a vesele zároveň."
                "Sníš si svůj oběd, doneseš Adrianovi ještě čokoládu a kolu, dopočítáš, kolik hodin uběhlo od toho, co jsi do něj dostala paralen a rozhodneš, že je čas na další."
                "Adrian sní asi půlku čokolády, vezme si od tebe paralen a zapije ho kolou. A přes to, že v kole je kofein, během pár minut zase spí."
                "Uklidíš tedy po obědě a jdeš se také natáhnout. I na tebe dopadla únava z Fuji a během pár minut spíš."
                "Vzbudíš se asi ve tři odpoledne, dojdeš si do koupelny, dáš si i rychlou sprchu na probuzení."
                "A dojdeš vzbudit Adriana, aby se napil."
                j "Adriane, měl by ses napít."
                show a kjoto openeyes
                a "Jo, jasně."
                hide a kjoto openeyes
                "Řekne ještě malinko rozespale. Napije se koly, kterou jsi mu přinesla z ledničky."
                show a kjoto openeyes
                a "Děkuji, už mi je vážně lépe. Šel bych se vykoupat a pak bychom se mohli připojit ke klukům."
                hide a kjoto openeyes
                j "Není to trošku narychlo? No dobře, dojdi se vykoupat, a když se i pak budeš cítit, tak se k nim můžeme připojit."
                "Adrian si vyndá věci a vyrazí do koupelny."
                j "Nech si pootevřeno."
                show a kjoto openeyes
                a "Cože?"
                hide a kjoto openeyes
                j "Nech si pootevřené dveře, prosím, mám o tebe strach. Kdyby se ti udělalo hůř, tak ať se k tobě dostanu."
                j "Nepolezu ti tam, věř, že kdybych tě chtěla očumovat, měla jsem k tomu dneska celé dopoledne a ani bys to nevěděl."
                show a kjoto openeyes
                a "Dobře. Asi děkuji?"
                hide a kjoto openeyes
                "Úplně nervózní a rudý zaleze do koupelny. Dveře sice zabouchne ale zámek neslyšíš klapnout."
                "Převlékneš se tedy do oblečení na ven, sbalíš si věci a napíšeš klukům, kde jsou, a kde budou tak za hodinu."
                "Adrian vyleze asi za půl hodiny a vypadá o 100 \% lépe."
                j "Tak jak ti je?"
                show a kjoto openeyes
                a "Myslím, že se cítím na drobnou procházku."
                hide a kjoto openeyes
                j "No, moc se mi to nelíbí, ale když myslíš. Kluci jsou teď ve zdejší výrobně sójovky, máme se s nimi sejít v nějaké tržnici."
                j "Jseš si jistý, že to zvládneš? Ještě před pár hodinami jsi vypadal, že na svalovou horečku v nejlepším jen zemřeš."
                show a kjoto openeyes
                a "Vážně mi je dobře, to asi ta tvá péče."
                hide a kjoto openeyes
                j "Ale jestli mi po cestě někde zkolabuješ, tak všechno Dantemu řeknu. Potom, co tě vlastnoručně zabiju. Tak mi budeš dlužit minimálně jedno pozvání na večeři."
                show a kjoto openeyes
                a "Nezkolabuju a na tu večeři tě pozvu i bez toho, abys mě musela zabít, co ty na to?"
                hide a kjoto openeyes
                menu:
                    "Mám to brát jako pozvání na rande?":
                        show a kjoto openeyes
                        a "Ano."
                        hide a kjoto openeyes
                        $ j.add_love_points_for_person(a, 2)
                        "Wow, tak tady to začíná být zajímavé. Adrian tě právě pozval na rande."
                        "Tak nějaké náznaky tu byly i dříve, ale tady jde do tuhého. Ale asi by bylo lepší, kdyby to nebylo tak okaté."
                        "Přeci jen nechceš dělat dusno v partě, navíc Sučan tě možná až přehnaně brání, takže by bylo lepší být opatrná."
                        j "Dobře, beru tě za slovo. Jen bych byla opatrnější před ostaníma, nebo bych to odložila až po návratu z Japonska."
                        "Tvá odpověď se evidentně Adrianovi moc nelíbí. Protože si povzdechne a jde si balit věci."
                        scene bg kjoto ulice
                        "Adrianovi to naštěstí dlouho netrvá a za chvíli už vycházíte na metro."
                        return
                    "To jsem jen tak plácla, není třeba.":
                        show a kjoto openeyes
                        a "Tak se asi pobalíme a vyrazíme."
                        hide a kjoto openeyes
                        $ j.add_love_points_for_person(a, 0.5)
            "Užít si výhled":
                "Další zasténání se neozve, takže si užíváš výhled a jemný vítr, který si pohrává s tvými vlasy."
                "V pokoji je ticho, tak se ti možná něco jen zdálo."
                "Po chvíli zaslouženého oddechu se vrátíš do pokoje."
                scene bg hotel kjoto
                "Adrian spí. Když ho dojdeš zkontrolovat, zjistíš, že má horečku."
                "Uvaříš čaj, z cestovní lékárničky vytáhneš paralen. Adriana vzbudíš a donutíš ho sníst prášek."
                "Adrian zase usne a ty se věnuješ také svým věcem. Kolem poledne se rozhodneš vyrazit koupit něco k obědu."
                "Před odchodem ještě vzbudíš Adriana, aby se napil a aby věděl, že jdeš pryč."
                scene bg kjoto ulice
                "V nejbližším kombini koupíš dva rameny a něco k pití."
                "Vrátíš se na apartmán a oba rameny zaleješ horkou vodou. Když trošku zchladnou, vzbudíš Adriana."
                "Ten se vysouká zpod peřiny, dojde si do koupelny a po chvíli se k tobě připojí u nízkého stolu na zemi."
                "U kterého musíte sedět na takových 'podsedácích' taktéž na zemi."
                "Jídlo po chvíli sníte, Adrian ti poděkuje a jde si zase lehnout."
                "Uklidíš odpadky a natáhneš se. Napíšeš klukům, jak jsou na tom."
                "Podle všeho akorát jdou z nějakého parku s opicemi taktéž na oběd. Pak plánují místní sójovkárnu."
                "Domluvíte se, že by ses večer připojila. Poté také usneš."
                scene bg kjoto koupelna
                "Vzbudíš se asi ve tři, dojdeš tedy do koupelny. Po rychlé sprše se sbalíš."
                scene bg hotel kjoto
                "Vzbudíš Adriana a řekneš mu, že se plánuješ připojit ke klukům."
                show a kjoto openeyes
                a "Už mi je lépe, počkej, vysprchuju se a půjdu také."
                hide a kjoto openeyes
                j "No když myslíš."
                "Adrian si vezme věci a zamíří do koupelny, ty mezitím vykomunikuješ místo setkání."
                scene bg kjoto ulice
                "Adrianovi to naštěstí dlouho netrvá a za chvíli už vycházíte na metro."

    return


label Kjoto:
    "Pochopila jsi, že odpovědi se nedočkáš. Pobalíš si věci a mezitím Mimoň vyjde z koupelny."
    "Z ledničky si vyndáš věci na snídani a rychle je sníš. Mimoň se mezitím také sbalil, takže můžete vyrazit."
    "Dole se potkáte se Sučanem. Ozve se jeho oblíbené Ikimašó a vyrazíte."
    scene bg kjoto ulice
    if j.love_points.get(s.name, 0) > 4:
        "Připojíš se k Sučanovi a po cestě na metro si povídáte."
        "Protože Dantemu s Mimoněm malinko utečete, usoudíš, že vás nemůžou slyšet, a položíš Sučanovi otázku, která ti už nějakou dobou vrtá v hlavě."
        j "Hele, Sučane, můžu se tě na něco zeptat?"
        show s kjoto
        s "Samozřejmě, [j.name5p], ty můžeš vždycky."
        hide s kjoto
        j "Co tak najednou? Vždyť se známe od mala, to sis uvědomil, že ke mně něco cítíš až teď?"
        show s kjoto
        s "Ne, já to vím dlouho, párkrát sem se ti to snažil naznačit."
        s "Jen ty si to asi nevnímala, protože mě prostě bereš jen jako pozorného bratra. No a pak si byla zadaná."
        s "Rozhodně sem nechtěl být ten, co ti bude kazit vztah. Na to nemám právo."
        s "Ale strašně mě ničilo, jak byl tvůj ex strašnej. Zasloužíš si někoho lepšího."
        hide s kjoto
        j "Nikdy jsem si toho nevšimla, promiň. Chovala jsem se trošku jako kráva, co?"
        show s kjoto
        s "Takhle o sobě nemluv. A nekaž mi ten krásný pocit, že jsem teď s tebou."
        hide s kjoto
        j "No o tom se sní každýmu, jít se mnou v Kjótu na autobus"
        scene bg kjoto bus
        "Mezitím jste došli k zastávce autobusu, zastavili jste a Dante s Mimoněm vás došli."
        "Takže Sučan ti neodpověděl."

    elif j.love_points.get(d.name, 0) > 4:
        "Připojíš se do dvojice s Dantem, Sučan jde tedy napřed s Mimoněm."
        "Kráčíte mlčky vedle sebe."
        j "Myslíš, že Adrian bude v pohodě? Nevypadal moc dobře."
        show d kjoto
        d "Jo, vyspí se a bude mu dobře. Asi jsme to s tou Fuji přehnali."
        hide d kjoto
        j "Hmm... Taky nejsem úplně v pohodě."
        show d kjoto
        d "Bylo to náročné pro všechny a kvůli některým i psychicky."
        hide d kjoto
        "Přikývneš a nastane zase ticho. Sbíráš odvahu ke své následující otázce."
        j "Hele, Dante, nechceš si přestat se mnou hrát?"
        show d kjoto
        d "Co? Asi nerozumím tvé otázce."
        hide d kjoto
        j "Ubíjí mě to, že nevím, na čem jsem. Takže by si mi možná mohl říct, jak to se mnou máš."
        j "Takže holka na jednu noc, vztah, nebo si to všechno blbě vykládám?"
        show d kjoto
        d "A co by si chtěla ode mne slyšet?"
        hide d kjoto
        menu:
            "Že si tuhle dovolenou užiju se vším všudy.":
                "Mrkneš na něj."
                show d kjoto
                d "Tak to nemůžu sloužit. Holky na jednu noc sice sbírám, ale vždy se ujistím, že si nebudou kromě luxusního sexu nic pamatovat." 
                "Co Betatesteři měla by být možnost sexu na jednu noc?"
                d "Rozhodně ne jméno a obličej. Uspokojila má odpověď tvoji dušičku?"
                d "Ale kdo ví? Třeba se ti podaří přesvědčit mě, abych udělal výjimku."
                hide d kjoto
                $ j.add_love_points_for_person(d.name, 1)
            "Že máš nějaké morální standardy.":
                show d kjoto
                d "Dost vysoké. Ale taky dost nebezpečné povolání."
                $ j.add_love_points_for_person(d.name, 2)
                d "Takže pokud se mnou někdy nějaká holka bude chtít být, musí si mě vzít. A počítat s tím, že rozvod nepřipadá v úvahu."
                d "Jediný akceptovatelný rozvod je smrt jednoho z nás."
                hide d kjoto
                j "Jojo, to už jsem slyšela, opakovaný vtip není vtipem."
                show d kjoto
                d "Myslíš, že žertuju? Věř tomu, že bych rád našel holku, která by byla ochotná akceptovat můj divoký, smrtí nasáklý život."
                hide d kjoto
                j "Tohle mě vážně nebaví, asi mi budeš muset říct o sobě víc. Tohle mě unavuje."
                j "Pořád jen mluvíš o svatbě, nebezpečí a smrti. Buď to vůbec nevytahuj anebo mluv na rovinu."
                show d kjoto
                d "Jsem vládní agent. Nejsem tady na dovolené, což si asi pochopila, ale mám se zúčastnit jedné předávky drog."
                d "Aby to nebylo jednoduché, tak jsem nastrčená krysa v Evropské odnoži yakuzy (yakuza – Japonská mafie)"
                d "Vztahům se raději vyhýbám, protože mě můžou oslabit, a navíc všichni v mé blízkosti jsou automaticky ve smrtelném nebezpečí."
                d "Doteď můj jediný přítel byl a je Adrian, který si kvůli mně už pár únosy prošel. Byl jsem rozhodlý, že holku si nikdy nenajdu."
                d "Ale tebe nějak nemůžu dostat z hlavy. To je tak ve zkratce vše."
                hide d kjoto
                "Tak to je šílené. To si musel všechno vymyslet. Yakuza v Japonsku samozřejmě stále úřaduje, ale její Evropská větev?"
                "Blbost. Vládní agent? Nejsme v Americe. Únosy v dnešní době a bez medializace?"
                "Plky, plky, plky. Jestli je tohle pravda, tak ty jsi panenka Mariánská"
                j "Ještě mi řekni, že máš s sebou zbraň. Ať je to kompletní."
                show d kjoto
                d "Teď ne, ale na apartmánu mám dvě automatické pistole."
                hide d kjoto
                j "Není možné, neprošel by si přes letiště."
                show d kjoto
                d "Ti říkám, že jsem vládní agent a člen mafie. Opravdu si myslíš, že je takový problém zařídit si tu zbraně?"
                hide d kjoto
                menu:
                    "Budeš této fanfikci věřit?"
                    "Ano":
                        $ d.duvera = True
                    "Ne":
                        $ d.duvera = False
                "Dante zmlkne, protože přicházíte na doslech Sučana s Mimoněm. Zastavili se totiž u autobusové zastávky."
            "Že si to blbě vykládám.":
                show d kjoto
                d "Pravděpodobně ano. Jen se snažím být milý, když spolu máme strávit tolik času."
                hide d kjoto
                $ j.add_hate_points_for_person(d.name, 2)
                j "Tak to jsem chtěla slyšet, jsem ráda, že jsme si to vyjasnili."
                "Přidáš trošku do kroku, dojdeš Sučana s Mimoněm a během chvíle jste na autobusové zastávce."
    elif j.hate_points.get(m.name, 0) > 5:  # TODO větší nebo menší?
        "Z nějakého důvodu se na tebe nalepil Mimoň, a aktivně s tebou drží krok."
        "Když zrychlíš, zrychlí, když zpomalíš, zpomalí."
        show m mask angry
        m "Tak já nevím, co chci vidět."
        hide m mask angry
        j "Tak plán má Dante a na preference jsme se tě ptali před odjezdem a naposledy včera."
        show m mask angry
        m "No ty kokot, tak to je hustý, to si musím vyfotit."
        hide m mask angry
        j "Nemáš ten plakát vyfocený už z Tokia?"
        show m mask angry
        m "Ne takhle!"
        hide m mask angry
        j "Jo, jasně, vyfoť si ho ještě z více úhlů."
        show m mask angry
        m "V pondělí budu vstávat ve tři ráno, je premiéra poníků."
        hide m mask angry
        j "Co prosím?"
        show m mask angry
        m "No v pondělí je release nového dílu My little pony a my to na discordu sledujeme společně."
        m "A je posun času, budu muset kvůli tomu vstát v noci."
        hide m mask angry
        j "Jasně, poníci, no tak to určitě vstaň. To si nemůžeš nechat ujít."
        "Z této šílené situace tě vysvobodí to, že Dante se Sučanem zastavili u autobusové zastávky."
        "Takže jste k nim došli a tento divný hovor se přirozeně ukončil."
    else:
        "Všichni společně vyrazíte na autobus. A během pár minut stojíte na zastávce."
    scene bg kjoto bus
    "Podle jízdních řádů, a hlavně aplikací v mobilu vyčtete, jakým autobusem chcete jet."
    "Máte štěstí, má jet za pět minut, takže jste přišli tak akorát."
    "Čekáte 5 minut, 10 minut. Začíná to být divné. Trošku znervózníte, zda nestojíte na špatné zastávce."
    "Ale po chvíli naštěstí přijíždí autobus s vaším číslem. Pochopili jste, že vlaky sice jezdí na vteřinu přesně,"
    "ale autobusy mají běžně zpoždění, Nějaké náznaky jste pochytili už v Tokiu, ale teď jste si to potvrdili."
    scene bg kjoto autobus
    "Výstupní stanici jste si z Japonských znaků přečetli jako 'skříňka pod sprchou, domeček, lampička' a další znaky."
    "Lístek na autobusy a metro koupili kluci včera po příjezdu do Kjóta na nádraží. Celodenní na metro i na autobusy najednou."
    "Řidič celou cestu nezavřel pusu; po chvíli jste pochopili, že hlásí 'Budeme zastavovat', 'Rozjíždíme se', 'Zatáčíme doprava', 'Zatáčíme doleva'."
    "Mimoň se Sučanem v autobuse usli, Dante si čte a ty se kocháš výhledem z okna."
    scene bg kjoto zahrady
    "První zastávka byli zahrady Tenrjúdži, zde jste se pokochali nádhernou přírodou, Japonským chrámem a zenovou zahradou."
    "Taková malá botanická."
    scene bg kjoto bambushaj
    "Z této zahrady jste se volně přesunuli do bambusového háje."
    "Tím jste prošli takovým větším okruhem zpátky na hlavní silnici a zjistili jste, že kousek od vás je zahrada s vyhlídkou a opicemi."
    scene bg kjoto reka
    "Rozejdete se tedy po hlavní cestě, směr vyhlídka. Přejdete most a za chvíli už platíte vstupné do areálu."
    "Je těsně před polednem, takže začíná být nesnesitelné vedro. A to jste ve stínu stromů."
    scene bg kjoto cesta bez opic
    "Cesta je udržovaná, takže výstup nahoru vám nečiní zas takové obtíže."
    "Vlastně po Fuji je to procházka růžovou zahradou. I když samozřejmě sem tam ještě cítíš, že tě bolí svaly."
    "Po cestě je spousta, poučných tabulí, samozřejmě jen v japonštině."
    "A pár výstražných, ty jsou i s nedokonalým anglickým překladem."
    "Závěr? Máte se chovat ohleduplně, opice nekrmit mimo krmící budku. Všechny drobné věci máte mít uklizené ve vnitřních kapsách tašek."
    "Opice nerozčilovat, raději si udržovat odstup, podle všeho hodně koušou."
    scene bg kjoto cesta opice
    "Už začínáš pochybovat, že vůbec nějaké opice uvidíte, ale když už je vyhlídka na dohled, začnou se po cestě objevovat."
    "Jsou normálně volně, takže opičí samec leží jen 2 m od cesty, po které přecházíte."
    "A o pár metrů dále si hrají dvě mláďata."
    "Je to opravdu jiný pocit, jít takto v přírodě a koukat na volně pobíhající zvířata."
    scene bg vyhled na kjoto
    "Po chvíli dorážíte na otevřené prostranství – vyhlídka na Kjoto."
    "A u vyhlídky stojí budova s klecovým přístavkem."
    "Nejdříve se pokocháte výhledem na Kjóto, taková Praha."
    scene bg kjoto krmeni opic
    "A následně zamíříte do budovy. Zjistíte, že jde o zmíněné krmící místo."
    "U obsluhy asi za 50 yenů koupíte balíček s ořechy, jablky a jiným ovocem a přijdete k mříži. "
    "Za ní už čeká asi 10 opic, které se těší na dobrůtky."
    "Podáš jednomu opičákovi jablko a on si ho vezme do tlapek."
    "Je to vážné kouzelný systém, že v kleci jsou lidé a opice volně."
    "Shodnete se na tom, že už máte hlad, a vyrazíte tedy zpět."
    scene bg kjoto reka
    "Cesta dolů vám uteče velmi rychle, přejdete most přes řeku zpět a ocitnete se na hlavní ulici, která je lemovaná různými restauracemi."
    "Všechny jsou dost plné a stojí se na ně fronta, nebo nemají menu v angličtině."  # TODO menu v japonštině ale může být levnější
    scene bg kjoto nudle
    "Nakonec se zastavíte u nějaké restaurace se soba nudlemi."
    "Inzerovali venku, že mají anglické menu, ale dostali jste normálně japonské."
    "Číšník evidentně neumí ani slovo anglicky, protože vedle u stolu se posadila rodina pravděpodobně Američanů,"
    "a ti se na něj snaží mluvit anglicky, ale on si říká svou v japonštině."
    "Vy si ale zvládnete objednat, sice se číšník na něco Japonsky doptával, ale nevíte na co."
    "Ale s objednávkou odkráčel a za chvíli vám přinesl 4 skleničky a konvici se soba čajem."
    "Pohankový čaj à la výplach popelníku. Je jeden z nejoblíbenějších nápojů k jídlu. No, aspoň je zdarma."
    "Jídlo vám donesli a Mimoň dostal malou mističku a pidi talířek."
    "V mističce je rozkleplé syrové vajíčko a na talířku jsou tři masové kuličky o velikosti hopíku."
    "Podíváte se tedy znovu do jídelního lístku a zjistíte, že si Matěj objednal jídlo ze sekce předkrmy."
    "Cena bohužel odpovídala ceně hlavního jídla. Mimoň by si ale stejně nic jiného nevybral."
    "Sníte tedy své bukkake soba, Mimoň svůj drahý předkrm, zaplatíte a vyrazíte dále."
    scene bg kjoto centrum
    "V této části Kjóta, jste se ale hodně zdrželi, takže se musí malinko upravit plán."
    "Proto stříbrný a zlatý chrám zkouknete jen při projíždění okolo autobusem. Vystoupíte někde v centru města."
    scene bg kjoto sojovkarna
    "A Dante vás proplete uličkami až k nějaké zapadlé rodinné sójovkárně, na kterou dostal tip od kolegy v práci."
    "V krámě je mlaďoulinká Japonka, která je z vaší početné návštěvy dost nervózní."
    "Ale pomocí překladače jí na mobilu ukážete,"
    "že byste chtěli od ní doporučení na nějakou sójovku."
    "Za chvíli se k ní přidá nějaký starší Japonec a dostanete doporučení na sójovku, kterou vyrábějí přímo u nich."
    "v součtu si koupíte asi 5 litrů."
    "Takže Japonec je spokojený, dokonce vás nechá nakouknout do vedlejší místnosti, kde má sudy se zrající černou kapalinou."
    scene bg kjoto trh
    "Ze sójovkárny jste zamířili někam na tržiště, kde jste si dali sraz s Adrianem."
    scene bg kjoto chobotnicky
    "Na tržišti někteří z vás ochutnali takojaki – chobotnicové koule či smažené chobotničky na špejli."
    "Takto odvážný byl i Adrian a vypadá, že už mu je dobře, sláva."
    scene bg kjoto gejsi
    "Z tržiště jste zamířili do Červené čtvrti – ulice Gejš."
    "Bohužel jste jsem dorazili až po šesté hodině, takže v ulici již není ani jedna Gejša. Japonci opravdu končí den brzy."
    "Ale i tak jste si uličku prošli. Následoval další přesun, a to do Fušimi Inari-taiša k chrámu, kde je celý vstup lemovaný tori, rumělkovými posvátnými branami."
    scene bg kjoto
    "K úpatí kopce, kde se svatyně nachází, jste ale dorazili až po sedmé hodině. Tudíž se začalo rychle stmívat."
    "Ale dole byl krásný červeno zlatý chrám, který nasvícený vypadal opravdu kouzelně."
    scene bg kjoto brany
    "Dokonce tori brány se po nasvícení skvostně vyjímají."
    "Prošli jste jimi první část, ale po zkontrolování času a jízdních řádů jste usoudili, že až nahoru nepůjdete, neboť byste se nedostali na hotel."
    "Takže při první odbočce z trasy se odpojíte a zamíříte směr zastávka."
    scene bg kjoto liska
    show m mask angry at right
    m "To si děláte prdel, no ty vole. Tady je socha lišky."
    hide m mask angry
    "??? Cože? To nemůže myslet vážně."
    show s kjoto at left
    s "Nekřič tady a klidni výrazy."
    hide s kjoto
    show m mask angry at right
    m "Ale to jste mi neřekli, že tu jsou sochy lišek."
    hide m mask angry
    show d kjoto at left
    d "Protože, jsme to nevěděli?"
    show m mask angry at right
    m "Jste mi to udělali schválně, šli jsme sem až nakonec, abych si nemohl vyfotit lišky."
    hide m mask angry
    show d kjoto
    d "Říkám ti, že jsem podrobně nezkoumal, co je kde k vidění. Udělal jsem plán na základě turistických míst v Kjótu a GPT."
    hide d kjoto
    show a kjoto at left
    a "Tak si měl říct včera, když to Dante plánoval, že sem chceš za světla."
    hide a kjoto 
    show m mask angry at right
    m "Ale to jste mi neřekli, že tu budou lišky."
    hide m mask angry
    "Usoudíte, že to asi nemá smysl řešit, prostě jste to špatně naplánovali."
    "Ty jsi zvolil['a' if j.gender == 'f' else ''] blbou cestu na Fuji a nechal['a' if j.gender == 'f' else ''] ho odejít v sandálech a s šesti litry vody."
    "Sučan zarezervoval blbé auto. Dante špatně plánuje 'tour de city'."
    "Adrian odletěl jako člověk navíc. Původní plán byl odletět jen ve čtyřech,"
    "Prostě všichni tu dovolenou kazíte, ale on je brouček."
    j "Tak si to vyfoť a měli bychom jít, jinak nám odjede poslední bus a budeme muset jít asi pět kilometrů pěšky."
    show m mask angry
    m "Tak to teda nejdu!"
    hide m mask angry
    show s kjoto
    s "Tak pohni kostrou. Je to ještě kus na tu zastávku."
    hide s kjoto
    "Za pár minut už stojíte na zastávce, jste tu o chvíli dříve. Překvapivě je tu prostor k sezení."
    show m mask angry
    m "Jsem si tu lišku mohl vyfotit ještě líp, kdybychom tak nepospíchali. Teď tu čekáme!"
    hide m mask angry
    "Autobus přijel na čas a úspěšně jste se přesunuli do blízkosti apartmánu."
    "Zatavili jste se jako vždy v 7eleven pro hotovku k večeři a pro snídani."
    scene bg hotel kjoto
    "A s nákupem jste se přesunuli do apartmánu."
