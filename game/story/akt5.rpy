label akt5:
    scene bg hotel fuji chodba
    show s fujihs at left
    show d fujihs at center
    show a fujihs at right
    "Na chodbě před pokoji už všichni čekají až na..."
    "Mimoně. Žádné překvapení, co?"
    hide s fujihs
    hide d fujihs
    hide a fujihs
    "Po chvíli se Sučan na Mimoně dobouchá, a můžete tedy vyrazit na snídani."
    scene bg hotel fuji jidelna
    "Snídaně je v konceptu 'Švédských stolů' v japonském stylu."
    "Takže si můžete vybírat z rýže, rybí polévky, řas, smažených chobotnic a mnoha dalšího."
    "Ale na své si přijdou i zastánci evropské kuchyně. Jsou zde saláty, vajíčka, slanina, pečivo... Prvky kontinentální i Anglické snídaně."
    "Jen nejméně sladké pečivo má sladkost asi jako evropský toastový chléb nebo hamburgerová žemle."
    if j.love_points.get(d.name, 0) > 5:
        "Když se zastavíš u nápojů, přitočí se k tobě Adrian, rozhlédne se, a když usoudí, že ho nikdo neslyší, začne na tebe mluvit."
        show a fujihs
        a "Doufám, že jste spolu ještě nespali."
        hide a fujihs
        j "Co?"
        show a fujihs
        a "[j.name_5p], vím že jsem ten poslední, kdo by ti měl radit, ale drž se od Danteho dál."
        a "Bere holky jako spotřební zboží, jestli mi rozumíš. Byla by tě škoda."
        hide a fujihs
        "Ještě se rozhlédne, aby se ujistil, že ho nikdo další neslyšel. A než stihneš zareagovat, přesune se k jinému pultu."
        "Pochopíš, že tímto ukončil debatu. Jak s touto 'awkward' informací naložíš, je na tobě."
    "Ulovili jste si každý, na co jste měli chuť a zasedli jste ke stolu pro šest."
    "Po včerejšku jste všichni unavení, takže konverzace moc neplyne. Každý se věnujete své snídani."
    scene bg fuji pokoj
    "Po snídani se přesunete do pokojů, sraz u auta jste si dali na jedenáctou."
    if j.love_points.get(d.name, 0) > 5:
        "Chvíli poté, co se dostaneš na pokoj, slyšíš klepání."
        "Jdeš otevřít a za dveřmi stojí Dante. Usmívá se a v rukách drží složené tvé oblečení."
        show d fujihs
        d "Tak co, Šípková Růženko? Něco jsem ti přinesl."
        hide d fujihs
        j "Děkuji."
        menu:
            "Chceš nějak rozmazávat rozhovor s Adrianem?"
            "Ano":
                j "Prosím tě, u snídaně mi Adrian naznačoval nějaké věci."
                show d fujihs
                d "Co ti říkal? To je vlastně jedno, určitě si vymýšlí."
                hide d fujihs
            "Ne":
                "Vezmeš si věci. Dante se usměje"
                show d fujihs
                d "Tak v jedenáct u auta,"
                hide d fujihs
                "řekl a vyrazil ke svému pokoji."
                "Jdeš tedy do pokoje a sbalíš se, pak se natáhneš na postel, a ještě chvíli odpočíváš."
    elif j.love_points.get(a.name, 0) > 5:
        "Přijdeš do pokoje, natáhneš se na postel a slyšíš klepání."
        j "Jdu!"
        "Otevřeš dveře a za dveřmi nervózně přešlapuje Adrian."
        "Přes rameno tvoji plátěnou tašku."
        show a fujihs
        a "Nesu ti to oblečení. Je to vyprané a usušené."
        hide a fujihs
        j "Děkuji, Adri..ane"
        "Začínáš zjišťovat, že pokud chceš Adrianovi poděkovat, je jeho jméno neprakticky dlouhé."
        "Ale po včerejším rozhovoru se snažíš zkrácené verzi vyvarovat."
        "Ačkoliv jsi zareagovala velmi rychle, a pauza v jeho jméně byla opravdu mikrosekundová."
        "Adrian se tak nějak smutně usmál, přešlápl z jedné nohy na druhou. Podal ti tašku."
        show a fujihs
        a "Tak já půjdu, sraz v jedenáct u auta."
        hide a fujihs
        "Zůstala si stát zaraženě ve dveřích s taškou v ruce."
        "Adrian ti totiž nedal šanci na další rozhovor a odešel do pokoje."
        "Jdeš tedy do pokoje a sbalíš se, pak se natáhneš na postel, a ještě chvíli odpočíváš."
    elif j.love_points.get(s.name, 0) > 5:
        "Než stihneš zabouchnout dveře, tak ti Sučan strčí do dveří nohu."
        show s fujihs
        s "Tak co, ještě se zlobíš? Nezabouchávej, přinesu ti ty věci."
        hide s fujihs
        "Zajde do pokoje naproti a vrací se s tvou plátěnou taškou."
        j "Díky. Už se nezlobím, ale přehnal jsi to."
        show s fujihs
        s "Ale, ale tak nebuď labuť! Neříkej, že si budeš hrát na uraženou."
        hide s fujihs
        j "Jo, budu!"
        show s fujihs
        s "No prr holčičko! Já ti vyperu, ponocuju kvůli tomu a ty si budeš hrát na uraženou?"
        hide s fujihs
        "Ani nevíš, jak se to stalo, ale Sučan je u tebe v pokoji a zabouchl za sebou dveře."
        "Instinktivně jsi trochu couvla, když k tobě vyrazil."
        "Sevřely se ti vnitřnosti a o něco hůře se ti dýchá. Ale není to pocit nepříjemného strachu."
        "Sučan k tobě udělá ještě krok, ty zase poodstoupíš a narazíš zády do stěny."
        "Zvedne levou ruku a opře ji o stěnu. Vedle tvé hlavy. Čímž ti odpadá možnost utéct do pokoje."
        show s fujihs
        s "Tak se koukej pěkně rychle odurazit."
        hide s fujihs
        j "Nebo co?"
        "Cítíš, jak se ti hrne krev do obličeje a jak jsi nervózní."
        show s fujihs
        s "Jinak tě políbím."
        hide s fujihs
        menu:
            "Chceš si dál hrát na uraženou?"
            "Ano":
                j "Tak to neuděláš a vlastně tomu teď vůbec nepomáháš! Takhle nevychladnu nikdy."
                "Sučan se usměje. Pravou rukou tě ukazováčkem a palcem chytne za bradu a jemně ti ji přidrží zvedlou."
                "Začne se k tobě sklánět a ty ztuhneš. On to myslel vážně? Zavřeš oči a jemně pootevřeš ústa."
                "Samým napětím snad ani nedýcháš."
                "Ale najednou uslyšíš jeho dech u svého ucha."
                show s fujihs
                s "Ještě nejsi připravená,"
                hide s fujihs
                "zašeptá, pustí tě, otevře dveře a zmizí."
                "Tobě vypadne taška z ruky a sesuneš se zády po zdi na zem."
                "Cítíš hněv, očekávání, vzrušení, zklamání, smutek."
                "Chvíli se z této situace vzpamatováváš."
                "Zůstane ti na mysli jen zklamání, že tě vážně nepolíbil."
            "Ne":
                j "Dobře, dobře odpuštěno, přestávám být uražená."
                show s fujihs
                s "Škoda, mohla být zábava. Holt mi tvůj výraz zděšení, když jsem řekl, že tě políbím, musí stačit."
                hide s fujihs
                "Pustí tě a odejde."
                "Zůstala jsi na pokoji sama."

    else:
        "Zašla jsi do pokoje."
    "Pobalíš si věci, natáhneš se na posteli, a ještě chvíli odpočíváš."
    scene bg hotel fuji parking
    "V jedenáct se sejdete u auta, kupodivu i Mimoň přišel včas."
    "Naskládali jste věci do auta a Sučan vám oznámil, že domluvil, že tam auto může ještě tak hodinku stát."
    "A že za rohem je park, tak že byste se před cestou mohli projít."
    scene bg hotel fuji park1
    "Souhlasíte a vyrazíte do přilehlého parku. Cestou si začneš uvědomovat, jak moc tě bolí všechny svaly."
    "Ale jsi rozhodnutá, že když jsi jediná holka ve skupině, tak nebudeš fňukat."
    "Zatneš zuby a snažíš se předstírat, že ti cesta pěšky vůbec nedělá žádné problémy."
    scene bg hotel fuji parking
    "Poté, co jste se pokochali parčíkem, je čas vyzvednout auto a přesunout se do dalšího hotelu."
    if j.driver:
        "Protože jsi druhý řidič a Sučan řídil včera na Fuji a z ní, je dnes řada na tobě."
        "Sedla sis tedy na místo řidiče. Nastavila sis zrcátka na sebe a koukneš dozadu,"
    else:
        "Jako vždy řídí Sučan. Kluci tě gentlemansky pustili na místo spolujezdce."
        "A když se usadíš, otočíš se dozadu,"
    "kde jsou naskládaní Dante, Adrian, Mimoň a jeho dřevěná tyč z Fuji."
    j "Tu tyč snad nepovezeme? Vždyť se tam nevejdete."
    show m mask angry
    m "To teda povezeme!"
    hide m mask angry
    j "Ale vždyť ti ji nevezmou do letadla, to nemá smysl ji vozit."
    show m mask angry
    m "Já si ji pošlu do Čech poštou."
    hide m mask angry
    j "No dobře."
    "Dneska vás čeká jeden z delších přejezdů a rozhodli jste se jej absolvovat podél pobřeží."
    "A protože je vedro, hledáte nějaké místo na koupání."
    "Po chvíli hledání Adrian a Dante něco nalezli, zadali jste souřadnice do navigace a vyrazili."
    scene bg cesta nagoja3
    "Rozhodli jste se pro cestu po dálnici, jinak by přesun zabral 2x tolik času. Vjeli jste nejbližším nájezdem, a dokonce jste i trefili správně mýtnou bránu."
    "Povolená rychlost je 80 km/h. V Čechách nepředstavitelné, že by se na dálnici jelo jen osmdesát."
    "Po chvíli ale vypozorujete, že všichni Japonci jedou přesně o 20 km/h více."
    "Odvodíte si z toho, že v Japonsku je základní výbava auta tempomat a po chvíli googlení zjistíte, že se na dálnici dává pokuta až při překročení rychlosti o 20 km/h."
    "Zasmějete se nad myšlenkou, jak striktně Japonci dodržují pravidla a pak na dálnicích jedou o 20 km/h více."
    "Snídali jste až v devět, od hotelu vyrážíte až chvíli po dvanácté hodině."
    "Takže po chvíli jízdy začínáte mít všichni hlad."
    "Navíc je nutné natankovat, takže sjedete k nějaké benzínce po cestě."
    "Jde o velké odstavné parkoviště, kde zaparkujete a vydáte se do přilehlé budovy."
    "Nejprve zamíříte na záchody."
    "Rozplývat se znovu nad luxusem a čistotou toalet nemá smysl, takže tuto část přeskočíme."
    scene bg benzinka kare
    "Budova má více částí – kromě pokladny je zde také obchod a jídelna."
    "Zamíříte tedy do části s jídelnou. I zde je typický objednávkový automat."
    "A jídlo si můžete prohlédnout vedle ve vitrínce, kde jsou plastové atrapy."
    "Zjistíte, že tato 'restaurace' se specializuje na karé."
    "Takže si každý objednáte karé a sednete si ke stolům, které lze rozdělit přepážkami."
    # TODO minigame?
    if j.love_points.get(a.name, 0) > 5:
        "Adrian si položil tác vedle tebe a došel vám pro pití."
    elif j.love_points.get(d.name, 0) > 5:
        "Dante si položil tác vedle tebe a došel vám pro pití."
    elif j.love_points.get(s.name, 0) > 5:
        "Sučan si položil tác vedle tebe a došel ti pro pití."
    else:
        "Položila sis tác ke stolu a došla si pro pití."
    "Když jste se všichni usadili ke svému jídlu, popřáli jste si dobrou chuť a začali jíst."
    scene bg benzinka kare televize
    "Zaujme vás televize, která je kousek od vás."
    "Nejdříve je tam počasí, kde si z čísel a červené barvy odvodíte, že bude vedro."
    "Ale po chvíli je tam reportáž z Fuji, kde varují, jak je Fuji zrádná a jak si návštěvníci mají dát pozor na vybavení."
    "A jako odstrašující případy je tam záběr na lidi, kteří něco nesplňují."
    "Kdo si myslíš, že to je? Ano, cizinci!"
    "Všichni si vybavíte Mimoně, a mlčíte. A děláte, že vaše jídlo je nejzajímavější věc v místnosti."
    "Když dojíte, odnesete tácy."
    "Dojdete si do krámku koupit nějakou vodu na cestu a přesunete se do auta."
    scene bg benzinka kare
    "Přejeli jste k benzínce, vystoupil Sučan s Adrianem."
    "Sučan tankuje, a Adrian s ním pak jde jako opora platit."
    "Když se vrátí do auta, vyrazíte dál s plnou nádrží."
    scene bg cesta nagoja3
    "Po další asi půlhodině sjíždíte z dálnice. I zde jste trefili mýtnou bránu s budkou, ve které seděl Japonec."
    "Podali jste mu lísteček a bankovku a on vám vrací na tácku účtenku a drobné nazpátek."
    scene bg cesta nagoja
    "Sjeli jste na úzkou cestičku mezi rýžovými poli a za chvíli jste zajeli do háje lemovaného travnatými pláněmi a minijezírky."
    scene bg cesta nagoja2
    "Vypadá to trošku jako golfové hřiště."
    scene bg parkoviste ocean
    "Nakonec jste zastavili na parkovišti, které je tak pro 40 aut. Ale je v podstatě prázdné."
    scene bg ocean1
    "Před vámi je val se schody. A s velkou cedulí 'Nebezpečí Tsunami'."
    scene bg parkoviste ocean
    menu:
        "Chceš jít plavat?"
        "Jasně, je vedro.":
            "Pomocí ručníku se převlíkneš do plavek, Adrian, Dante a Sučan to udělají stejně."
            scene bg ocean2
            "Vyrazíte směr schody. Když přelezete val, otevře se vám výhled na oceán s pěknou písečnou pláží."
            "Pláž je naprosto prázdná; sem tam je vidět nějaký rybář. Ale rozhodně se nikdo nekoupe."
            "Chcete si sundat boty, ale zjistíte, že písek je strašně horký."
            "Takže dojdete v botech až skoro k oceánu, zde se zujete a jdete si zaplavat."
            "Jsou ale strašně velké vlny, takže máš co dělat, aby tě nějaká nepodsekla."
            "Japonci se koupou jen na vyznačených plážích s plavčíkem, nejlépe v zátočinách mimo otevřený oceán."
            "Takže jste jediní, kteří si užívají vodních radovánek."
            "Nejsou zde bójky, takže plaveš jen kousek, abys měla jistotu, že kdyby tě chytila křeč do nohy po včerejšku, zvládneš doplavat zpět."
            "Při návratu na břeh dosahují vlny snad ještě větší amplitudy, než jaké byly, když jsi lezla do vody."
            "Jedna taková větší tě spláchne, takže cítíš, jak sis o písek odřela nohy a jak se ti dostal do plavek. Dokonce sis dala hlavou o zem."
            "Do toho sis lokla i slané vody, jak jsi nečekala, že tě vlna vezme zezadu."
            if j.love_points.get(a.name, 0) > 5:
                "Cítíš, jak tě někdo chytil za ruku. A vytáhl tě na nohy."
                "Když si protřeš oči a rozkoukáš se, vidíš, jak tě drží Adrian za zapěstí."
                show a plavky worried
                a "Jsi v pořádku?!"
                hide a plavky worried
                j "Jo, díky, jen jsem se trošku lekla, tak jsem si lokla vody."
                show a plavky worried
                a "Vypadalo to děsivě. Strašně jsem se o tebe bál."
                hide a plavky worried
                j "Jsem v pohodě, ale už asi půjdu na břeh."
                show a plavky worried
                a "Půjdu raději s tebou, ty vlny jsou strašně silné."
                hide a plavky worried
                j "Dobře, díky."
                "Sučan a Dante si ještě plavou."
                show a plavky worried
                a "Počkej tady, donesu ti ručník a boty, ať si nespálíš nohy o písek."
                hide a plavky worried
                j "Díky."
                "Adrian vyleze ven z vody úplně a rychle dojde pro svůj a tvůj ručník a boty."
                "Podá ti ho. Začnete se sušit."
                j "Adriane? Asi mi dlužíš nějaké odpovědi."
                show a plavky worried
                a "Dobře, na jednu otázku ti odpovím, tak si rozmysli, co chceš slyšet, než kluci přijdou."
                call adrian_otazky
                "Nastalo ticho, oba mlčíte."
                "Obula ses a naštěstí už z vody leze Dante a Sučan."
                "Otřou se a přesunete se k autu."
            elif j.love_points.get(d.name, 0) > 5:
                "Cítíš, jak tě někdo chytil za ruku. A vytáhl tě za ni z vody."
                "Následně tě chytí za pas a vyzvedne nahoru do náruče."
                "Konečně máš možnost si protřít oči a otevřít je. V náruči tě svírá Dante."
                "Až teď sis uvědomila, že si nesundal tričko a plaval v něm."
                show d plavky
                d "Jsi v pohodě? Spláchlo tě to jako nic. Měla bys jsi na sebe dávat větší pozor."
                d "Já nemusím být vždy po ruce."
                hide d plavky
                j "Vždyť mi nic není a dostala bych se z vody sama."
                show d plavky
                d "No když myslíš, já jsem viděl jak tě vyválela v písku, pěkně sis odřela nohy a netřískla jsi hlavou o zem?"
                hide d plavky
                j "Jak to můžeš vědět? Vždyť já ani sama nevím, co se stalo. A pusť mě. Už si dám pozor."
                show d plavky
                d "Nene, donesu tě na břeh."
                hide d plavky
                j "Pusť mě, tohle vážně není potřeba!"
                "Snažíš se mu vysmeknout, bohužel tě drží velmi pevně."
                j "A proč máš vlastně na sobě to tričko?!"
                show d plavky
                d "A chceš pravdu nebo lež?"
                hide d plavky
                menu:
                    "Co odpovíš?"
                    "Pravdu.":
                        show d plavky
                        d "Tak důvody jsou dva: za prvé mám tetování, a to Japonci spojují s yakuzou."
                        d "A ten druhý je, že mám spoustu jizev. Takže se na veřejnosti moc neukazuju."
                        hide d plavky
                        j "Tetování? Jaký? A jizvy z čeho?"
                        show d plavky
                        d "Nezdá se ti, že jsi nějaká zvědavá na to, že se v podstatě neznáme?"
                        d "Pokud takhle budeš pokračovat, tak tě buď budu muset zabít nebo si tě vzít."
                        hide d plavky
                    "No samozřejmě, že lež, proto se ptám.":
                        show d plavky
                        d "No tak jsem kyborg, a bez trička je to poznat."
                        hide d plavky
                        j "Ovšem tak to je kvalitní práce, protože mě držíš v náruči už podruhé a nic jsem nepoznala."
                        show d plavky
                        d "Jo, vzkážu svému technikovi tvou poklonu."
                        hide d plavky
                        j "Já jsem docela fanynka technologických pokroků, takže... mohla bych se podívat?"
                        show d plavky
                        d "To bych do tebe neřekl, že mě budeš takhle rafinovaně chtít svlíknout."
                        hide d plavky
                        "Totálně zrudneš, protože jsi to brala jako vtipkování."
                        j "Néé, tak to není, jen jsem pokračovala v tvém vtipu."
                        "To už jste na břehu a Dante tě pokládá u tvých bot na zem."
                        show d plavky
                        d "Škoda. Hele, pravda je taková že za prvé: mám tetování, a to si Japonci spojují s yakuzou."
                        d "A taky mám spoustu nehezkých jizev. Takže se na veřejnosti moc neukazuju."
                        hide d plavky
                        j "Tetování? Jaký? A jizvy z čeho?"
                        show d plavky
                        d "Nezdá se ti, že jsi nějaká zvědavá na to, že se v podstatě neznáme?"
                        d "Pokud takhle budeš pokračovat, tak tě buď budu muset zabít nebo si tě vzít."
                        hide d plavky
                j "Jo, tak to už jsme si vysvětlili, že si děláš jen srandu, že bys nikoho nezabil."
                show d plavky
                d "Když tomu věříš. Ale myslím, že bys se mnou už nikdy nepromluvila, kdybys znala pravdu. Jako všechny."
                "Chceš na to reagovat, ale od vody přichází Adrian a Sučan."
                "Usušila ses a obula. Kluci udělali to samé a přesunuli jste se k autu."
            elif j.love_points.get(s.name, 0) > 5:
                "Cítíš, jak tě někdo chytil za ruku a vytáhl tě na nohy."
                "Pak si tě přitáhl k sobě a jednou rukou tě drží kolem pasu."
                "Rukama si protřeš oči a koukáš na Sučana."
                show s plavky
                s "Seš v pohodě? Docela tě to sejmulo."
                hide s plavky
                j "Jo, díky. Docela mi ta vlna dala na frak, myslím že mám písek až ve vlasech."
                show s plavky
                s "Vypadáš trošku jako mořská panna, to je pravda."
                hide s plavky
                j "Tak mokře?"
                show s plavky
                s "Myslel jsem tak krásně, ale když nad tím tak přemýšlím, tak i mokře, to máš pravdu."
                hide s plavky
                "Pustí ruku z tvého pasu, ale chytí tě za ruku."
                show s plavky
                s "Pojď!"
                hide s plavky
                "A rozběhne se ke břehu. Máš co dělat, abys mu v té vodě a přívalu vln stačila."
                "Ani sis nevšimla kdy, ale Dante i Adrian už jsou u věcí a suší se."
                "Sučan tě u břehu pustí."
                show s plavky
                s "Počkej, přinesu ti boty a ručník."
                hide s plavky
                "Během pár vteřin je Sučan s věcmi zpátky."
                "Usušíš se, nazuješ si boty a vyrazíte všichni k autu."
            else:
                "Otočíš se na všechny čtyři a postavíš se. Nadechneš se, jakmile se ti dostane hlava nad hladinu."
                "Protřeš si oči a rozhlédneš se. Spláchlo tě to blíže ke břehu."
                "Sedneš si na bobek, opláchneš ze sebe písek a vydáš se ke břehu."
                "Boty jste si nechali až kousek dál od vody, aby vám je nevzala nějaká vlna."
                "Takže musíš do toho rozpáleného písku. Chvíli jen hřeje, ale když se voda z nohou vsákne do písku a odpaří, začne nepříjemně pálit."
                "K botám doslova doposkakuješ. Ometeš si rukama písek z nohou a obuješ si boty."
                "Pak si vezmeš ručník a osušíš se. Kluci mezitím doplavali a vydali se taktéž ke břehu."
                "Adriana jedna větší vlna také spláchla a když se dostal na nohy, vypadal jak vyoraná myš."
                "Všichni se mu začnete smát a po chvíli se začne smát i Adrian."
                "Uděláš pár fotek a kluci se mezitím dostali ke břehu."
                "Obuli jste se, osušili a vyrazili jste k autu."
            scene bg parkoviste ocean
            "Mimoň spí v otevřeném autě. Ještěže se v Japonsku nekrade."    
            "U parkoviště je kohoutek se sladkou vodou, takže se u něj vystřídáte."
            "Každý se pak jdete oblíknout za auto, kde se kryjete ještě i ručníkem."
        "Ne, nechci pak jet slaná další 2 h v autě. Ale k vodě půjdu.":
            "Adrian, Dante a Sučan se převlíkli do plavek a vyrazili jste společně k vodě."
            scene bg ocean2
            "Přelezli jste val, otevře se vám výhled na oceán s pěknou písečnou pláží."
            "Pláž je naprosto prázdná sem tam je vidět nějaký rybář. Ale rozhodně se nikdo nekoupe."
            "Chcete si sundat boty, ale zjistíte, že písek je strašně horký."
            "Takže dojdete v botech až skoro k oceánu, zde se kluci zují a jdou si zaplavat."
            "Zůstala jsi na břehu tedy sama, uděláš pár fotek, pak si chvíli stavíš z větších kamínků a mušlí na písku."
            if j.love_points.get(s.name, 0) > 5:
                "Po chvíli se Sučan oddělí od ostatních a zamíří k tobě."
                "Kousek od tebe křikne."
                show s plavky
                s "Pojď také do vody, je to tady super!"
                hide s plavky
                j "Není se tu kde osprchovat, nechci být slaná. Pojedeme ještě docela dlouho autem."
                "Mezitím došel Sučan až na vzdálenost pár kroků."
                show s plavky
                s "Tak aspoň přátelské objetí!"
                hide s plavky
                "Rozpřáhne ruce v naznačení objetí a rozejde se k tobě."
                j "Tak na to zapomeň, to bych pak rovnou mohla do vody. Podívej se, jak z tebe teče!"
                "Ale když zjistíš, že jsi ho nepřesvědčila a objetí myslí vážně,"
                "dáš se do běhu od vody. Sučan tě pronásleduje."
                "Už tě skoro doběhl."
                show s plavky
                "Au, au, sakryš, to pálí!"
                hide s plavky
                "Nechá tě být a běží zpátky k vodě, kde si chladí spálená chodidla."
                "Vyhrála jsi. Začneš se mu smát."
                j "Kdo jinému jámu kopá, sám do ní padá. A karma je zdarma!"
                show s plavky
                s "Moc se nesměj, kdybys mi neutekla, tak se to nestalo. Co když teď nebudu moct řídit?"
                hide s plavky
                "Po chvíli se na chodidla podívá, má je červená. Ale vypadá to, že jinak jsou v pohodě."
                "To už se vracejí Dante a Adrian. Takže se společně přesunou ke věcem, obují se, usuší a vyrazíte k autu."
            elif j.love_points.get(d.name, 0) > 5:
                "Po chvíli se Dante oddělí od ostatních a zamíří k tobě." 
                "Když se ve vodě postaví, všimneš si, že se koupal v triku."
                "Proč? Vždyť všichni kluci jsou normálně v plavkách. A na pláži nikdo není; v dálce je sem tam nějaký rybář."
                show d plavky
                d "Co je na mně špatně, že na mě zase tak zíráš?"
                hide d plavky
                "Vyruší tě z myšlení Dante, který se dostal až k tobě."
                j "Chceš slyšet pravdu nebo si mám vymýšlet?"
                show d plavky
                d "Takže je na mě něco špatně; jasně, že pravdu. Já ti také nelžu."
                hide d plavky
                j "Přemýšlela jsem proč se koupeš v triku, když tu kromě nás nikdo není."
                show d plavky 
                d "Jo aha, a já myslel, že mi narostly rohy, nebo tak něco. Že sis mě tak zkoumavě prohlížela."
                d "Dám ti na výběr ze čtyř... pěti možností a vyber si, co je podle tvého pravda."
                d "Takže na veřejnosti se nesvlékám, protože se: za a) stydím, za b) víc na to letí holky, c) z náboženského přesvědčení,"
                d "d) mám tetování, které by se v Japonsku na veřejnosti nemělo ukazovat a za e) mám tělo samou jizvu, tak nechci nikoho děsit."
                hide d plavky
                "Možností máš na výběr opravdu hodně, možnost a) anebo b) z nich zní nejlépe, ale také nejméně pravděpodobně."
                j "V Japonsku se na veřejnosti nesmí ukazovat tetování?"
                show d plavky
                d "Ne, no. Japonci mají tetování spojené s yakuzou."
                hide d plavky
                j "Aha."
                show d plavky
                d "Proč si vlastně nešla také do vody?"
                hide d plavky
                j "Nechtěla jsem být celá od soli a písku, když je odsud hotel ještě dvě hodiny autem."
                show d plavky
                d "Všiml jsem si, že u toho parkoviště byl kohoutek. Plánuju se opláchnout tam."
                hide d plavky
                "Jen co domluví, připojí se k vám Adrian a Sučan, osuší se ručníkem, obují se a vyrazíte k autu."
            elif j.love_points.get(a.name, 0) > 5:
                "Po chvíli se oddělí Adrian od ostatních."
                "A rozejde se k tobě. Když má vodu asi do pasu, přijde větší vlna a zezadu ho překlopí a smete."
                "Trochu tě zamrazí, ale když se Adrian v pořádku vynoří, rozesměje tě to."
                "Dojde k tobě."
                show a plavky
                a "Proč jsi také nešla? Ta voda je osvěžující."
                hide a plavky 
                j "Aby mě ty vlny smetly, jako tebe?"
                show a plavky
                a "Přiznávám, že mě ta vlna překvapila. Možná proto se tu nikdo nekoupe."
                hide a plavky
                j "Nechtěla jsem strávit další dvě hodiny v autě slaná. Proč nejsi ještě s klukama ve vodě?"
                show a plavky
                a "Nechtěl jsem tě nechávat čekat dlouho samotnou na břehu."
                hide a plavky
                j "To je od tebe milé. Takže mi teď vysvětlíš všechny ty věci?"
                show a plavky
                a "Všechny asi ne, dneska ti odpovím na jednu otázku."
                hide a plavky
                call adrian_otazky
                "Adrian si všimne, že se kluci už vracejí, a zmlkne."
                "Ty také nevíš, jak na jeho odpověď reagovat, tak raději mlčíš."
                "Kluci se usuší a obují a vyrazíte k autu."
            scene bg parkoviste ocean
            "Mimoň spí v otevřeném autě, ještěže se v Japonsku nekrade."    
            "U parkoviště je kohoutek se sladkou vodou, takže se u něj kluci vystřídají."
            "Ty si sedneš na obrubník dál od auta a kohoutku a koukáš se do mobilu."
            "Každý se pak jde obléknout za auto, kde se kryje ještě i ručníkem."
        "Ne, zůstanu u auta.":
            "Adrian, Dante a Sučan se převlíkli do plavek a vyrazili k vodě."
            "Ty jsi zůstala na parkovišti s Mimoněm."
            "Mimoň sedí rozvalený přes zadní sedačky auta a vyndal si Danteho Nintendo Switch."
            show m mask
            m "Vždyť tu vůbec nemá žádný dobrý hry, proč to vůbec vozí?"
            m "Tak to musím změnit..."
            hide m mask 
            j "Vážně, chceš instalovat nějaké hry na cizí zařízení? A vůbec, půjčil ti ho?"
            show m mask
            m "Bral ho kvůli mně, mám ho u sebe už od letadla."
            hide m mask
            "Aha."
            "No, docela drahá hračka, snad Dante nebude litovat, že mu ho půjčil."
            "Sedneš si tedy na místo spolujezdce, nandáš si sluchátka, abys nemusel['a' if j.gender == 'f' else ''] poslouchat Mimoně."
            "Pustíš si svůj oblíbený playlist."
            "Vzbudí tě až to, že se kluci vrací od vody."

            "Všimneš si, že Mimoň také spí, ale nechal otevřené zadní dveře. Ještě že se v Japonsku nekrade."    
            "U parkoviště je kohoutek se sladkou vodou, takže se u něj kluci vystřídají."
            "Pak přijdou k autu a vypadají, že se chtějí převlíknout."
            "Rozespale tedy vylezeš a jdeš si stoupnout dál od auta."
            "Každý se pak jde obléknout za auto, kde se kryje ještě i ručníkem."
    "Když jste přichystaní na odjezd, vzbudíte Mimoně."
    show m mask angry
    "Co je?"
    hide m mask angry
    show d fujihs
    d "Pojedeme, skoro po cestě je ten Ghibli park. Sice se nám nepodařilo koupit lístky dovnitř, ale mají i nějakou volně přístupnou část."
    d "Tak bychom se tam mohli zastavit."
    hide d fujihs
    show a fujihs
    a "Je úterý, mají zavřeno."
    hide a fujihs
    show d fujihs
    d "Ajo, ale ono je stejně docela pozdě."
    hide d fujihs
    show s fujihs
    s "Sjel bych někam do lékárny pro Pantenol, spálil jsem se a všiml jsem si, že jste všichni spálený."
    s "Jsem za koupit jeden a podělíme se o něj."
    hide s fujihs
    "S tím souhlasíte."
    scene bg nagojapoliklinika
    "Pomocí map najdete něco, co podle názvu připomíná lékárnu."
    "Zaparkujete u takového malého domečku s parkovišťátkem."
    "Adrian a Sučan vystoupí, vlezou dovnitř a za pár minut vychází."
    show a fujihs
    a "Je to nějaká poliklinika, ale odkázali nás na velký obchoďák s drogerií."
    a "Že tam by mohli mít to, co chceme."
    hide a fujihs
    "Vyrazíte tedy na doporučené místo."
    "Vypadá to trošku jako u nás Globus nebo Tesco; velký 'hangár' s parkovištěm."
    if j.driver:
        "Protože se nechcete zdržovat a dovnitř stejně nepůjdete všichni, přibrzdíš u vchodu, kluci vyskáčou a jdou do obchoďáku."
        "Ty jedeš zaparkovat."
        menu:
            "Budeš parkovat popředu nebo pozadu?"
            "Popředu.":
                "Zajela jsi na místo jako po másle, kola se ti zastavila o betonovou zarážku."
                "Za pár minut se kluci vracejí s dvěma tubami přípravku."
                "Naskákali do auta a ty začneš vycouvávat, ozve se hodně divný zvuk."
                "Dření plastů o beton."
                "Asi jak se zatížilo auto, tak vám kleslo těžiště a odřeli jste kryt motoru o betonovou zarážku."
                "Na jízdních vlastnostech se nic nezměnilo, takže jsi vyrazila."
                "Ale ujeli jste pár metrů mimo parkoviště a na křižovatce auto začíná vydávat opravdu děsivé zvuky."
                "Projedeš křižovatkou."
                show a fujihs
                a "Asi bychom měli zastavit, ti Japonci na nás divně koukají."
                hide a fujihs
                j "Jo, také se mi to nelíbí."
                scene bg opravaauta
                "Zastavíš u prvního vjezdu do baráku, kde se zastavit dá."
                "Vylezete ven a zjistíte,"
                "že vám z auta vepředu visí plasty."
                "Jak jsi vyjížděl['a' if j.gender == 'f' else ''] ven z místa na parkovišti, zachytil['a' if j.gender == 'f' else ''] jsi o betonovou zarážku kryt motoru a část podběhů."
                "Sučan – milovník aut jako první leze pod auto."
                show s fujihs
                s "Hmmm... Urval['a' if j.gender == 'f' else ''] jsi takové ty plastové nýty. Teda ne všechny, ale nedrží tam, takže se nám to chytá do kol."
                s "Bez nářadí to neopravím."
                hide s fujihs
                show d fujihs
                d "Ukaž?"
                hide d fujihs
                "Dante se vymění se Sučanem pod autem."
                show d fujihs
                d "Jo, souhlasím, to bez nářadí asi nedáme. Nevím kde sehnat nýty nebo aspoň šrouby v Japonsku."
                hide d fujihs
                "Zatímco poskakujete kolem auta, všimnete si, že vedle vás postává nějaká rodina Japonců, asi se balí na dovolenou."
                show s fujihs
                s "Navrhuji ty plasty sundat a vyřešit to později."
                hide s fujihs
                show d fujihs
                d "Jo, souhlasím, ale i tak by se nám hodilo nějaký nářadí."
                hide d fujihs
                show a fujihs
                a "A co byste chtěli za nářadí? Zkusím se zeptat těch Japonců."
                show s fujihs
                s "Hele asi osmičku klíč a kleště."
                hide s fujihs
                "Adrian chvíli kouká do mobilu, asi do slovníku, a pak se rozejde k rodině."
                "Chvíli s nimi mluví."
                "Poté se od rodiny oddělí starší Japonec, asi dědeček, a jde přes ulici do nějaké garáže."
                "Za chvíli se vrací s nějakými nástroji, které podal Adrianovi."
                show a fujihs
                a "Tak mi půjčili tohle, bude to stačit?"
                hide a fujihs
                show s fujihs
                s "Uka? Jo, to by mohlo stačit."
                hide s fujihs
                "Dante se mezitím vysoukal z pod auta a pustil Sučana zpět."
                "Sučan tedy zalezl pod auto, chvíli to tam morduje a za chvíli podává první plast."
                show s fujihs
                s "Ten velkej nějak přichytím, ale ten menší sundám i na druhé straně."
                hide s fujihs
                "Zatímco Sučan sundává druhý plast, Japonská rodina se nasoukala do auta a vypadá nervózně. Že by chtěli jet a vy stále máte jejich nářadí?"
                hide s fujihs
                "Naštěstí během chvíle Sučan podává i druhý plast."
                show s fujihs
                s "Hele, není to ideální, ale asi s tím můžeme jet."
                hide s fujihs
                "Začne vylézat z pod auta a podává nářadí Adrianovi."
                "Ten si jej převzal a rozejde se k Japoncům. Na nich je vidět, že jsou se rádi, že brzy vypadnete."
                "Plasty jste dali na podlahu ke spolujezdci."
                scene bg cesta nagoja3
                "Sedla jsi zase za volant a vyrážíte směr hotel."
            "Pozadu.":
                "Pomocí parkovacích kamer jsi 'na první dobrou' krásně zaparkovala."
                "Za pár minut se kluci vracejí s dvěma tubami přípravku."
                scene bg cesta nagoja3
                "Naskládali se do auta. A vyrazíte směr hotel."
    else:
        "Sučan zaparkoval pozadu pomocí parkovacích asistentů. A jde s Adrianem a Dantem do obchoďáku."
        "Za pár minut se kluci vracejí s dvěma tubami přípravku."
        scene bg cesta nagoja3
        "Naskládali se do auta. A vyrazíte směr hotel."
    scene bg mapanagoja
    "Kolem šesté přijíždíte do Nagoji."
    scene bg nagoja vecer1
    "Najdete váš hotel, ale nevíte, jak je to s parkováním. Tak zastavíte na blikačky."
    show s fujihs
    s "Hotel má mít nějaké vlastní parkoviště, ale nevím kde."
    hide s fujihs
    "Takže Sučan s Adrianem vyrazí na recepci, vy čekáte v autě."
    show s fujihs
    s "Tak jsem dostal nějakou mapku a lísteček na slevu, je to nějaké parkoviště, kde mají zákazníci hotelu slevu."
    hide s fujihs
    "Parkoviště je někde za vámi, takže musíte objet blok, a nakonec parkoviště trefíte."
    "Vyndáte kufry a vyrazíte zpátky k hotelu."
    "Máte tři pokoje: dva dvojlůžáky a jeden jednolůžák."
    # TODO if j.gender == 'f'?
    scene bg nagoja hotel
    "Jednolůžák dostaneš ty, dokonce to tak očekávají na recepci. Dante si bere pokoj s Adrianem."
    "A Sučan tedy schytal Mimoně."
    "Dáte si sraz na společnou večeři za hodinku před pokoji."
    "Dala sis věci na pokoj a proběhneš sprchou."
    "Dáš vědět domů. Převlékneš se, přebalíš si věci s sebou a je akorát čas srazu."
    scene bg chodba
    "Vylezeš před pokoj a tam už čekají Adrian, Dante a Sučan."
    show s nagoja
    s "Není tu Ichiran? Ten mi chutnal."
    hide s nagoja
    show a nagoja
    a "Jo, pobočka v Nagoji je. Kouknu, jestli je to někde blízko."
    a "..."
    a "Je odsud asi 3 ulice."
    hide a nagoja
    show s nagoja
    s "Tak super, za mě Ichiran."
    hide s nagoja
    show d nagoja
    d "Jo, já jsem za."
    hide d nagoja
    "Vypadá to, že je rozhodnuto."
    show s nagoja
    s "Hmmm. Ten Mimoň asi nepřijde, dojdu se na něj podívat."
    hide s nagoja
    "Zajde do pokoje a za chvíli vychází s Mimoněm."
    show m mask angry
    m "Mám hlad! Dal bych si normální suši."
    hide m mask angry
    show d nagoja
    d "Jde se na Ichiran, jak jsme byli první den v Tokiu."
    hide d nagoja
    show m mask angry
    m "Nechci!"
    hide m mask angry
    show s nagoja
    s "Tak zůstaň na hotelu, nebo si někam zajdi sám."
    hide s nagoja
    show m mask angry
    m "Sám nikam nejdu, ať se mnou jde [j.name]."
    hide m mask angry
    j "Já jdu se zbytkem na Ichiran."
    show m mask angry
    m "Sám nejdu, tak jdu teda s vámi."
    hide m mask angry
    show s nagoja
    s "Takže ikimašó."
    show nagoja vecer
    "Jdete tedy pár ulic a najdete pobočku Ichiranu."
    "Moc se neliší od Tokijské pobočky."
    "Zakroužkujete si, co si chcete dát, zaplatíte u automatu a během chvíle si už vychutnáváte každý svůj ramen."
    "Po jídle se jdete po Nagoje ještě projít."
    scene bg pachinko
    "Zaujme vás herna s Pachinkem."
    "V Japonsku je totiž zakázaný hazard, takže tam nenajdete typické herny."
    "Ale samozřejmě, i Japonci jsou vynalézaví, takže mají pachinko herny."
    "Což je hra s kovovými kuličkami, něco na styl pinballu."
    "A jako výhru množíte kuličky, které se dají vyměnit za hračky nebo za speciální trofej."
    "Která se na černém trhu dá směnit za peníze."
    "Vlezli jste tedy dovnitř a jdete k jednomu z automatů."
    "Sučan se posadil k automatu a vy jste se rozestavili kolem něho."
    "Vytáhli jste překladač a snažíte se přijít na to, jak to funguje."
    show japonecherna
    "Po chvíli přijde Japonec, který se vás japonsky zeptá, jestli chcete pomoct."
    "Adrian odpoví v japonštině, že ano. Japonec spustí v japonštině. Tak mu řeknete anglicky jestli by to nemohl říct anglicky."
    hide japonecherna
    "Tak to se vyděsí a uteče."
    "Za chvíli přijde Japonka, která na vás začne mluvit anglicky."
    show japonkaherna
    Japonka "Do you need help?"
    hide japonkaherna
    show d nagoja
    d "Maybe yes? We want to try it."
    hide d nagoja
    show japonkaherna
    Japonka "Ok, so give the money here and you get card. One thousand is minimum."
    hide d nagoja
    "Tak Sučan vyndá peníze, a strčí je do ukázané dírky."
    "Vypadla mu zlatá karta."
    show japonkaherna
    Japonka "So now, put the card here. And you can start."
    hide japonkaherna
    "A tak Sučan vložil kartu do stroje a navolil první hru."
    "Když zmáčkl start, tak začnou lítat kuličky do stroje."
    show japonkaherna
    Japonka "Oh, you must hold the button... Sorry."
    hide japonkaherna
    "Japonka pochopila že Sučan vůbec netuší, tak mu chytla ruku a snaží se ho navést."
    "Ale skoro všechny kuličky padají mimo výherní místo."
    "Když přestanou kuličky létat. Tak se Japonka zasměje a řekne."
    show japonkaherna
    Japonka "Ups, gameover, you lost five hundred yen. So, you know how to play. In other part of room there is automat where you pay one yen per ball."
    Japonka "Bye."
    hide japonkaherna
    "A zmizela"
    show s nagoja
    s "Hm, tak jsem prohrál pět set yenů a už chápu proč ti Japonci, co u toho sedí, mají ruku v jedné pozici."
    s "Jestli si to chcete někdo zkusit, jsem za vyndat tu kartu a jít na nějaký z těch levnějších přístrojů."
    hide s nagoja
    "Ukončili jste tedy hru, vyndali kartu a přesunuli se k automatu, kde se platí za jednotlivé míčky."
    "Každý jste si to vyzkoušeli."
    "Takže jste získali i nějaké kuličky zpět, ale po chvíli jste neměli žádné."
    "Odcházíte o 1000 yenů lehčí, ale plni nových zkušeností."
    scene nagoja vecer
    "Ještě jste udělali malý okruh a vrátili jste se na hotel."
    "Druhý den se plánujete přesunout do Kjóta s tím, že část z vás pojede Šinkanzenem."
    "A protože zítřek je ve znamení přejezdu, rozhodnete se, že si ještě ráno Nagoju projdete za světla."
    scene nagoja hotel
    "Rozejdete se do svých pokojů, proběhneš koupelnou, nařídíš budíka a do pár minut jsi tuhá."

    return

label adrian_otazky:
    menu:
        "Tak na kterou otázku chceš nejvíce znát odpověď?"
        "Proč nechce, aby Dante věděl o jeho omdlení?":
            show a plavky worried
            a "Po tom, co jsem utekl z domu a neměl jsem nic, zvládl jsem si sbalit jen pár osobních věcí, na který jsem si vydělal potají na brigádě."
            hide a plavky worried
            j "Utekl jsi z domu bez věcí, proč?"
            show a plavky worried
            a "Řekl jsem, že ti odpovím jen na jednu otázku a útěk z domova je jiný příběh."
            a "Neměl jsem tedy vlastně vůbec nic, neměl jsem ke komu jít, kde spát."
            a "Tenkrát v noci u mě zastavil Dante v autě, strašně pršelo a já jsem byl promrzlý na kost."
            a "Řekl, že mi vezl narozeninový dárek a zjistil, že nejsem doma. A jestli nechci jít k němu, že na bytě má volný pokoj."
            a "S díky jsem to přijal, myslel jsem, že to bude jen na pár dní, než se z toho svrabu vyhrabu."
            a "Teď to bylo 5 let, díky jeho podpoře jsem dostudoval a vlastně díky němu mám tak dobrou práci."
            a "Ale nechci být na něm tak závislý, vždycky moje problémy řeší, ale já po zkušenostech s otcem, nechci být na nikom závislý."
            a "A rozhodně nechci, aby si myslel, že jsem taková padavka, kterou skolí, první výšlap na horu."
            a "Když on je zvyklý běhat na Sněžku s plnou polní."
            hide a plavky worried
        "Jak je to s jeho maminkou?":
            "Adrian zesmutní."
            show a plavky worried
            a "Dobře, dal jsem slib tak ti to tedy řeknu."
            a "Moje máma je nejlepší ženská kterou jsem kdy znal. Akorát jsem jí osm let neviděl. Strašně mi chybí."
            hide a plavky worried
            j "Cože? Jak to?"
            show a plavky worried
            a "Řekl jsem, že ti odpovím na jednu otázku, tak mi neklaď doplňující, já ti to vysvětlím."
            a "Za všechno může můj otec, je to strašný násilník a alkoholik."
            a "Když mi bylo čtrnáct, tak jsem se mu poprvé v životě postavil, abych před ním ochránil mámu."
            a "Skončil jsem se zlomenou rukou v nemocnici."
            a "To byla pro mamku poslední kapka a začala aktivně řešit rozvod a místo, kde by se mnou mohla bydlet."
            "To co ti říká se ti neposlouchá vůbec lehce. Nevíš, jak se tvářit, jak se chovat."
            a "Bohužel, otec je velmi vlivný podnikatel a v podstatě všechno, co jsme měli, patřilo jemu."
            a "Navíc měl strašně sviňskýho právníka, z mamky udělali socku neschopnou postarat se o sebe natož o dítě."
            a "A na vzdory mým protestům bylo 'v zájmu dítěte' rozhodnuto, že budu svěřen do opatrovnictví otci."
            a "A dokonce se mu podařilo zařídit, že 'v zájmu mé výchovy' se se mnou nesmí máma ani vídat."
            a "Takže jsem zažil tři nejhorší roky svého života a v osmnácti jsem utekl z domova."
            a "A mamku už pět let s Dantem hledáme. Strašně mi chybí, navíc mám strach, jestli jí ten šmejd něco neudělal."
            a "Adri mi vždycky říkala ona, když mi tak někdo řekne, připomene mi jí to. Navíc jsi holka..."
            "Na chvíli se odmlčí."
            a "Stačí ti to jako odpověď?"
            "Jen přikývneš, nevíš, co odpovědět. Možná ses neměla ptát."
    return
