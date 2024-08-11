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
    "Po chvíli se Sučan na Mimoně dobouchá a můžete tedy vyrazit na snídani."
    scene bg hotel fuji jidelna
    "Snídaně je v komceptu 'Švédských stolů' v japonském stylu."
    "Takže si můžete vybírat z rýže, rybí polévky, řas, smažených chobotnic a mnoha dalšího. "
    "Ale na své si příjdou i zastánci evropské kuchyně. Jsou zde saláty, vajíčka, slanina, pečivo..."
    if j.love_points.get(d.name , 0) > 5:
        "Když se zastavíš u nápojů, přitočí se k tobě Adrian, který se rozhlídne, a když usoudí, že ho nikdo neslyší. Začne na tebe mluvit."
        show a fujihs
        a "Doufám, že jste spolu ještě nespali."
        hide a fujihs
        j "Co?"
        show a fujihs
        a "[j.name_5p], vím že jsem ten poslední, kdo by ti měl radit, ale drž se od Danteho dál."
        a "Bere holky jako spotřební zboží, jestli mi rozumíš. Byla by tě škoda."
        hide a fujihs
        "Ještě se rozhlídne, aby se ujistil, že ho nikdo další neslyšel a než stihneš zareagovat, tak se přesune k jinému pultu."
        "Pochopíš, že tímto ukončil debatu. Jak s touto 'akward' informací naložíš je na tobě."
    "Ulovili jste si každý, na co jste měli chuť a zasedli jste ke stolu pro šest."
    "Po včerejšku jste všichni unavení, takže konverzace moc neplyne. Každý se věnujete své snídani."
    scene bg fuji pokoj
    "Po snídani se přesunete do pokojů, sraz u auta jste si dali na jedenáctou."
    if j.love_points.get(d.name, 0) > 5:
        "Chvíli po té co se dostaneš na pokoj slyšíš klepání."
        "Jdeš otevřít a za dveřmi stojí Dante. Usmívá se a v rukách drží složené tvé oblečení."
        show d fujihs
        d "Tak co Šípková Růženko? Něco jsem ti přinesl."
        hide d fujihs
        j "Děkuji."
        menu:
            "Chceš nějak rozmazávat rozhovor s Adrianem?"
            "Ano":
                j "Prosímtě, u snídaně mi Adrian naznačoval nějaké věci."
                show d fujihs
                d "Co ti říkal? To je vlastně jedno určitě si vymýšlí."
                hide d fujihs
            "Ne":
                "Vezmeš si věci. Dante se usměje"
                show d fujihs
                d "Tak v jedenáct u auta."
                hide d fujihs
                "Řekl a rozejde se ke svému pokoji."
                "Jdeš tedy do pokoje a zbalíš se, pak se natáhneš na postel a ješzě chvíli odpočíváš."
    elif j.love_points.get(a.name, 0) > 5:
        "Přijdeš do pokoje, natáhneš se na postel a slyšíš klepání."
        j "Jdu!"
        "Otevřeš dveře a za dveřmi nervózně přešlapuje Adrian."
        "Přes rameno tvojí pláťenou tašku."
        show a fujihs
        a "Nesu ti to oblečení. Je to vyprané a usušené."
        hide a fujihs
        j "Děkuji, Adri..ane"
        "Začínáš zjišťovat, že pokud chceš Adrianovi poděkovat, je jeho jméno neprakticky dlouhé."
        "Ale po včerejším rozhovoru se snažíš, zkrácené verzi vyvarovat."
        "Ačkoliv jsi zareagovala velmi rychle, a pauza v jeho jméně byla opravdu mikrosekundová."
        "Adrian se tak nějak smutně usmál, přešlápl z jedné nohy na druhou. Podal ti tašku."
        show a fujihs
        a "Tak já půjdu sraz v jedenáct u auta."
        hide a fujihs
        "Zůstala si stát zaraženě ve dveřích s taškou v ruce."
        "Adrian ti totiž nedal šanci na další rozhovor a odešel do pokoje."
        "Jdeš tedy do pokoje a zbalíš se, pak se natáhneš na postel a ješzě chvíli odpočíváš."
    elif j.love_points.get(s.name, 0) > 5:
        "Než stihneš zabouchnout dveře, tak ti Sučan strčí do dveří nohu."
        show s fujihs
        s "Tak co ještě se zlobíš? Nezabouchávej, přinesu ti ty věci."
        hide s fujihs
        "Zajde do pokoje naproti a vrací se s tvou plátěnou taškou."
        j "Díky. Už se nezlobím, ale přehnal jsi to."
        show s fujihs
        s "Ale, ale tak nebuď labuť! Neříkej, že si budeš hrát na uraženou."
        hide s fujihs
        j "Jo budu!"
        show s fujihs
        s "No prr holčičko! Já ti vyperu, ponocuju kvůli tomu a ty si budeš hrát na uraženou?"
        hide s fujihs
        "Ani nevíš jak se to stalo, ale Sučan je u tebe v pokoji a zabouchl za sebou dveře."
        "Instinktivně jsi trochu couvla, když se k tobě rozešel."
        "Sevřeli se ti vnitřnosti a o něco hůře se ti dýchá. Ale není to pocit nepříjemného strachu."
        "Sučan k tobě udělá ještě krok, ty zase poodstoupíš a narazíš zády do stěny."
        "Zvedne levou ruku a opře jí o stěnu. Vedle tvé hlavy. Čím ti odpadá možnost utéct do pokoje."
        show s fujihs
        s "Tak se koukej pěkně rychle odurazit."
        hide s fujihs
        j "Nebo co?"
        "Cítíš jak se ti hrne krev do obličeje a jak jsi nervózní."
        show s fujihs
        s "Jinak tě políbím."
        hide s fujihs
        menu:
            "Chceš si dál hrát na uraženou?"
            "Ano":
                j "Tak to neuděláš a vlastně tomu teď vůbec nepomáháš!Takhle nevychladnu nikdy."
                "Sučan se usměje. Pravou rukou tě ukazováčkem a palcem chytne za bradu a jemně ti jí přidrží zvedlou."
                "Začne se k tobě sklánět a ty stuhneš. On to myslel vážně? Zavřeš oči a jemně pootevřeš ústa."
                "Samým napětím snad ani nedýcháš."
                "Ale najednou uslyšíš jeho dech u svého ucha."
                show s fujihs
                s "Ještě nejsi připravená."
                hide s fujihs
                "Zašeptá, pustí tě, otevře dveře a zmizí."
                "Tobě vypadne tažka z ruky a sesuneš se zády po zdi na zem."
                "Cítíš hněv, očekávání, vzrušení, zklamání, smutek."
                "Chvíli se z této situace vzpamatováváš."
                "Zůstane ti na mysli jen zklamání, že tě vážně nepolíbil."
            "Ne":
                j "Dobře, dobře odpuštěno, přestávám být uražená."
                show s fujihs
                s "Škoda, mohla být zábava. Holt mi tvůj výraz zděššení, když jse řekl, že tě políbím musí stačit."
                hide s fujihs
                "Pustí tě a odejde."
                "Zůstala jsi na pokoji sama."

    else:
        "Zašla jsi do pokoje."
    "Pobalíš si věci, natáhneš se na posteli a ještě chvíli odpočíváš."
    scene bg hotel fuji parking
    "V jedenáct se sejdete u auta, kupodivu i Mimoň přišel včas."
    "Naskládali jste věci do auta a Sučan vám oznámil, že domluvil, že tam auto může ještě tak hodinku stát."
    "A že za rohem je park, tak že byste se před cestou mohli projít."
    scene bg hotel fuji park1
    "Souhlasíte a vyrazíte do přilehlého parku. Cestou si začneš uvědomovat, jak moc tě bolí všechny svaly."
    "Ale jsi rozhodlá, že když jsi jediná holka ve skupině, tak nebudeš fňukat."
    "Zatneš zuby a snažíš se předstírat, že ti cesta pěšky vůbec nedělá žádné problémy."
    scene bg hotel fuji parking
    "Po té co jste se pokochali parčíkem, je čas vyzvednout auto a přesunout se do dalšího hotelu."
    if j.driver:
        "Protože jsi druhý řidič a Sučan řídil včera na Fuji a z ní, je dnes řada na tobě."
        "Sedla jsi si tedy na místo řidiče. Natsavila jsis zrcátka na sebe a koukáneš do zádu."
    else:
        "Jako vždy řídí Sučan. Kluci tě gentlemansky pustili na místo spolujezdce."
        "A když se usadíš otočíš se do zádu."
    "Kde jsou naskládaní Dante, Adrian, Mimoň a jeho dřevěná tyč z Fuji."
    j "Tu tyč snad nepovezeme? Vždyť se tam nevejdete."
    show m mask angry
    m "To teda povezeme!"
    hide m mask angry
    j "Ale vždyť ti jí nevezmou do letadla, to nemá smysl jí vozit."
    show m mask angry
    m "Já si jí pošlu do čech poštou."
    hide m mask angry
    j "No dobře."
    "Dneska vás čeká jeden z delších přejezdů a rozhodli jste se jej absolvovat podél pobřeží."
    "A protože je vedro hledáte nějaké místo na koupání."
    "Po chvíli hledání, Adrian a Dante něco nalezli, zadali jste to do navigace a vyrazili."
    scene bg cesta nagoja3
    "Rozhodli jste se po cestování po dálnici jinak by přesun zabral 2x tolik času. Vjeli jste nejbližším nájezdem a dokonce jste i trefili správně mýtnou bránu."
    "Povolená rychlost je 80 km/h. V Čechách nepředstavitelné, že by se na dálnici jelo jen osmdesát."
    "Po chvíli, ale vypozurujete, že všichni Japonci jedou přesně o 20 km/h více."
    "Odvodíte si z toho, že v Japonsku je základní výbava auta tempomat a po chvíli googlení zjistíte, že se na dálnici dává pokuta až při překročení rychlosti o 20 km/h."
    "Zasmějete se nad myšlenkou jak striktně japonci dodržují pravidla a pak na dálnicích jedou o 20 km/h více."
    "Sice jste snídali až v děvet, ale vyráželi jste od hotelu až chvíli po dvanácté hodině."
    "Takže po chvíli jízdy začínáte mít všichni hlad."
    "Navíc je nutné natankovat, takže sjedete k nějaké benzínce po cestě."
    "Jedná se o velké odstavné parkoviště, kde zaparkujete a vydáte se do přilehlé budovy."
    "První kam zamíříte jsou záchody."
    "Roplývat se znovu nad luxusem a čistotou toalet nemá smysl, takže tuto část přeskočíme."
    scene bg benzinka kare
    "Budova má více částí kromě pokladny k benzínce, je zde obchod a jídelna."
    "Zamíříte tedy do části s jídelnou. I zde je typiccký objednávkový automat."
    "A jídlo si můžete prohlednout vedle ve vytrýnce, kde jsou plastové atrapy."
    "Zjistíte, že tato 'restarace' se specializuje na karé."
    "Takže si každý objednáte karé a sednete si ke stolům, které lze rozdělit přepážkami."
    if j.love_points.get(a.name, 0) > 5:
        "Adrian si položil tác vedle tebe a došel vám pro pití."
    elif j.love_points.get(d.name, 0) > 5:
        "Dante si položil tác vedle tebe a došel vám pro pití."
    elif j.love_points.get(s.name, 0) > 5:
        "Sučan si položil tác vedle tebe a došel ti pro pití."
    else:
        "Položila jsis tác ke stolu a došla si pro pití."
    "Když jste se všichni usadili ke svému jídlu, popřáli si dobrou chuť a začali jíst."
    scene bg benzinka kare televize
    "Zaujme vás televize která je kousek od vás."
    "Nejdříve je tam počasí, kde si z čísel a červené barvy odvodíte, že bude vedro."
    "Ale po chvíli je tam reportáž z Fuji, kde varují jak je Fuji zrádná a jak si mají dát pozor na vybavení."
    "A jako odstrašující případy je tam záběr na lidi, kteří něco nesplňují."
    "Kdo si myslíš, že to je? Ano, cizinci!"
    "Všichni si vybavíte Mimoně, a mlčíte. A děláte, že vaše jídlo je nejzajímavější věc v místnosti."
    "Když dojíte odnesete táci."
    "Dojdete si do krámku koupit nějakou vodu na cestu a přesunete se do auta."
    scene bg benzinka kare
    "Přejeli jste k benzínce, vystoupil Sučan s Adrianem."
    "Sučan tankuje, a Adrian s ním pak jde jako opora platit."
    "Když se vrátí do auta, vyrazíte dál s plnou nádrží."
    scene bg cesta nagoja3
    "Asi po další půlhodině sjíždíte, z dálnice, i zde jste trefili mýtnou bránu s budkou ve které seděl Japonec."
    "Podali jste mu lísteček a bankovku a on vám vrací na tácu účtenku a drobné nazpátek."
    scene bg cesta nagoja
    "Sjeli jste na úzkou cestičku mezi rýžovými poli a za chvíli, jste zajeli někam do takového háje který je lemován travnatými pláněmi a minijezírky."
    scene bg cesta nagoja2
    "Vypadá to trošku jako golfové hřiště."
    scene bg parkoviste ocean
    "Nakonec jste zastavili na parkovišti, které je tak pro 40 aut. Ale je v podstatě prázdné."
    scene bg ocean1
    "Před vámi je val se schody. A s velkou cedulí 'Nebezpečí Tsunami'."
    scene bg parkoviste ocean
    menu:
        "Chceš jít plavat?"
        "Jasně, je vedro.":
            "Pomocí ručníku se převlíkneš do plavek, Adrian, Dante a Sučan, to udělají stejně."
            scene bg ocean2
            "A vyrazíte směr schody když přelezete val, otevře se vám výhled na oceán s pěknou písečnou pláží."
            "Pláž je naprosto prázdná sem tam je vidět nějaký rybář. Ale rozhodně se nikdo nekoupe."
            "Chcete si sundat boty, ale zjistíte, že písek je strašně horký."
            "Takže dojdete v botech až skoro k oceánu, zde se zujete a jdete si zaplavat."
            "Jsou, ale strašně velké vlny, takže máš co dělat aby tě nejaká nepodsekla."
            "Japonci se koupou jen na vyznačených plážích s plavčíkem, nejlépe v zátočinách mimo otevřený oceán."
            "Takže jste jediní, kteří si uživají vodních radovánek."
            "Nejsou zde bójky, takže plaveš jen kousek, aby si měla jistotu, že kdyby tě chytila křeč do nohy po včerejšku, že zvládneš doplavat zpět."
            "Když se vracíš, tak vlny jsou snad ještě větší, než byly když jsi lezla do vody."
            "Jedna taková větší tě spláchne, takže cítíš jak sis o písek odřela nohy a jak se ti dostal do plavek. Dokonce sis dala hlavou o zem."
            "Do toho sis lokla i slané vody, jak jsi nečekala, že tě vlna vezme zezadu."
            if j.love_points.get(a.name, 0) > 5:
                "Cítíš jak tě někdo chytil za ruku. A vytáhl tě na nohy."
                "Když si protřeš oči a rozkoukáš se vidíš, jak tě drží Adrian za zapěstí."
                show a plavky worried
                a "Jsi v pořádku?!"
                hide a plavky worried
                j "Jo díky, jen jsem se trošku lekla, tak jsem si lokla vody."
                show a plavky worried
                a "Vypadalo to děsivě. Strašně jsem se o tebe bál."
                hide a plavky worried
                j "Jsem v pohodě, ale už asi půjdu na břeh."
                show a plavky worried
                a "Půjdu raději s tebou, ty vlny jsou strašně silné."
                hide a plavky worried
                j "Dobře díky."
                "Sučana a Dante si ještě plavou."
                show a plavky worried
                a "Počkej tady, donesu ti ručník a boty ať si nespálíš nohy o písek."
                hide a plavky worried
                j "Díky."
                "Adrian vyleze ven z vody úplně a rychle dojde pro svůj a tvůj ručník a boty."
                "Podá ti ho. Začnete se sušit."
                j "Adriane? Asi mi dlužíš nějaké odpovědi."
                show a plavky worried
                a "Dobře na jednu otázku ti odpovím, tak si rozmysli co chceš slyšet, než kluci příjdou."
                call adrian_otazky
                "Nastalo ticho, oba mlčíte."
                "Obula ses a naštěstí už z vody leze Dante a Sučan."
                "Otřou se a přesunete se k autu."
            elif j.love_points.get(d.name,0) > 5:
                "Cítíš jak tě někdo chytil za ruku. A vytáhl tě za ní z vody."
                "Následně tě chytí za pas a vyzvedl tě nahoru do náruče."
                "Konečně máš možnost si protřít oči a otevřít je. V náruči tě svírá Dante."
                "Až teď sis uvědomila že si nesundal tričko a plaval v něm."
                show d plavky
                d "Jsi v pohodě? Spláchlo tě to jako nic. Měla bys sis na sebe dávat větší pozor."
                d "Já nemusím být vždy po ruce."
                hide d plavky
                j "Vždyť mi nic není a dostala bych se z vody sama."
                show d plavky
                d "No když myslíš, já jsem viděl jak tě vyválela v písku, pěkně sis odřela nohy, a netřískla jsi hlavou o zem?"
                hide d plavky
                j "Jak to můžeš vědět? Vždyť já ani sama nevím, co se stalo. A pusť mě. Už si dám pozor."
                show d plavky
                d "Nene, donesu tě na břeh."
                hide d plavky
                j "Pusť mě, tohle není vážně potřeba!"
                "Snažíš se mu vysmeknout, bohužel tě drží velmi pevně."
                j "A proč máš vlastně na sobě to tričko?!"
                show d plavky
                d "A chceš pravdu nebo lež?"
                hide d plavky
                menu:
                    "Co odpovíš?"
                    "Pravdu.":
                        show d plavky
                        d "Tak důvody jsou dva, za prvé mám tetování a to japonci spojují s yakuzou."
                        d "A ten druhý je, že mám spoustu jizev. Takže se na veřejnosti moc neukazuju."
                        hide d plavky
                        j "Tetování? Jaký? A jizvy z čeho?"
                        show d plavky
                        d "Nezdá se ti, že jsi nějaká zvědavá, na to že se v podstatě neznáme?"
                        d "Pokud takhle budeš pokračovat, tak tě buď budu muset zabít nebo si tě vzít."
                        hide d plavky
                    "No samozřejmě, že lež, proto se ptám.":
                        show d plavky
                        d "No tak jsem kybork a bez trička je to poznat."
                        hide d plavky
                        j "Ovšem tak to je kvalitní práce, protože mě držíš v náruči už podruhé a nic jsem nepoznala."
                        show d plavky
                        d "Jo vzkážu svému technikovi, tvou poklonu."
                        hide d plavky
                        j "Já jsem docela fanynka technologických pokroků, takže mohla bych se podívat?"
                        show d plavky
                        d "To bych do tebe neřekl, že mě budeš takhle rafinovaně chtít svlíknout."
                        hide d plavky
                        "Totálně zrudneš, protože, jsi to brala, že vtipkujete."
                        j "Néé, tak to není, jen jsem pokračoval v tvém vtipu."
                        "To už jste na břehu a Dantě tě pokládá u tvých bot na zem."
                        show d plavky
                        d "Škoda. Hele pravda je taková že za prvé mám tetování a to si japonci spojují s yakuzou."
                        d "A taky mám spoustu nehezkých jizev. Takže se na veřejnosti moc neukazuju."
                        hide d plavky
                        j "Tetování? Jaký? A jizvy z čeho?"
                        show d plavky
                        d "Nezdá se ti, že jsi nějaká zvědavá, na to že se v podstatě neznáme?"
                        d "Pokud takhle budeš pokračovat, tak tě buď budu muset zabít nebo si tě vzít."
                        hide d plavky
                j "Jo tak to už jsme si vysvětlili, že si děláš jen srandu, že by si nikoho nezabil."
                show d plavky
                d "Když tomu věříš. Ale myslím, že by si se mnou už nikdy nepromluvila, kdyby si znala pravdu. Jako všechny."
                "Chceš na to reagovat, ale od vody přichází Adrian a Sučan."
                "Usušila ses obula ses, kluci udělali to samé a přesunuli jste se k autu."
            elif j.love_points.get(s.name,0) > 5:
                "Cítíš jak tě někdo chytil za ruku. A vytáhl tě na nohy."
                "A pak si tě přitáhl k sobě a jednou rukou tě drží kolem pasu."
                "Rukama si protřeš oči a koukáš na Sučana."
                show s plavky
                s "Seš v pohodě? Docela tě to sejmulo."
                hide s plavky
                j "Jo, díky. Docela mi ta vlna dala na frak, myslím že mám písek až ve vlasech."
                show s plavky
                s "Vypadáš trošku jako mořská panna, to je pravda."
                hide s plavky
                j "Tak mokře?"
                show s plavky
                s "Myslel jsem tak krásně, ale když nad tím tak přemýšlím, tak i mokře, to máš pravdu."
                hide s plavky
                "Pustí ruku z tvého pasu, ale chytí tě za ruku."
                show s plavky
                s "Pojď!"
                hide s plavky
                "A rozběhne se ke břehu. Máš co dělat aby si mu v té vodě a přívalu vln stačila."
                "Ani sis nevšimla kdy, ale Dante i Adrian už jsou u věci a suší se."
                "Sučan tě u břehu pustí."
                show s plavky
                s "Počkej přinesu ti boty a ručník."
                hide s plavky
                "Během pár vteřin je Sučan s věcmi zpátky."
                "Usušíš se nazuješ si boty a vyrazíte všichni k autu."
            else:
                "Otočíš se na čtyři a postavíš se, když se ti dostane hlava nad hladinu tak se nadechneš."
                "Protřeš si oči a rozhlídneš se. Spláchlo tě to blíže ke břehu."
                "Sedneš si na bobek a opláchneš si písek ze sebe."
                "A vydáš se ke břehu, boty jste si nechali až kousek dál od vody. Aby vám je nevzala nějaká vlna"
                "Takže musíš do toho rozpáleného písku, chvíli jen hřeje, ale když se voda z nohou vsákne do písku a odpaří. Začne nepříjemně pálit."
                "K botám přímo doposkakuješ. Ometeš si písek z nohou rukou a obuješ si boty."
                "Pak si vezmeš ručník a osušíš se. Kluci mezitím doplavali a vydali se taktéž ke břehu."
                "Adriana jedna větší vlna, také spláchla, když se dostal na nohy, vapadal jak vyvoraná myš."
                "Všichni se mu začnete smát a po chvíli se začne smát i Adrian."
                "Uděláš pár fotek a kluci se mezitím dostali ke břehu."
                "Obuli se osušili a vyrazili jste k autu."
            "Mimoň spí v otevřeném autě, ještě že se v japonsku nekrade."    
            "U parkoviště je kohoutek se sladkou vodou, takže se u něj vystřídáte."
            "Každý se pak jdete oblíknout za auto, kde se kryjete ještě i ručníkem."
        "Ne, nechci pak jet slaná další 2h v autě, ale k vodě půjdu.":
            "Adrian, Dante a Sučan se převlíkli do plavek a vyrazili jste společně k vodě."
            "Přelezli jste val, otevře se vám výhled na oceán s pěknou písečnou pláží."
            "Pláž je naprosto prázdná sem tam je vidět nějaký rybář. Ale rozhodně se nikdo nekoupe."
            "Chcete si sundat boty, ale zjistíte, že písek je strašně horký."
            "Takže dojdete v botech až skoro k oceánu, zde se kluci zujou a jdou si zaplavat."
            "Zůstala jsi na břehu tedy sama, uděláš pár fotek, pak si chvíli stavíš z větších kamínků a mušlí na písku."
            if j.love_points.get(s.name, 0) > 5:
                "Po chvíli, se Sučan oddělí od ostatních a zamíří k tobě."
                "Kousek od tebe křikne."
                show s plavky
                s "Pojď také do vody, je to tady super!"
                hide s plavky
                j "Není se tu kde osprchovat, nechci být slaná. Pojedeme ještě docela dlouho autem."
                "Mezitím došel Sučan až na vzdálenost pár kroků."
                show s plavky
                s "Tak aspoň přátelské objetí!"
                hide s plavky
                "Rozpřáhne ruce v naznačení objetí a rozejde se k tobě."
                j "Tak na to zapomeň, to bych pak rovnou mohla do vody, podívej se jak z tebe teče!"
                "Ale když zjistíš, že jsi ho nepřesvědčila a objetí myslí vážně."
                "Dáš se do běhu od vody a Sučan za tebou."
                "Už už tě skoro doběhl."
                show s plavky
                "Au, au, sakryš to pálí!"
                hide s plavky
                "Nechá tě být a běží zpátky k vodě kde si chladí spálená chodidla."
                "Vyhrála, jsi. Začneš se mu smát."
                j "Kdo jinému jámu kopá sám do ní padá a karma je zdarma!"
                if j.driver:
                    show s plavky
                    s "Moc se nesměj, kdyby si mi neutekla, tak se to nestalo. Co když teď nebudu moct řídit?"
                    hide s plavky
                "Po chvíli se na chodidla podívá, má je červená. Ale vypadá to, že jinak jsou v pohodě."
                "To už se vracejí Dante a Adrian. Takže se společně přesunou ke věcem obují, usuší a vyrazíte k autu."
            elif j.love_points.get(d.name, 0) > 5:
                "Po chvíli se Dante oddělí od ostatních a zamíří k tobě." 
                "Když se ve vodě postaví, všimneš si, že se koupal v triku."
                "Proč? Vždyť všichni kluci jsou normálně v plavkách. A na pláži nikdo není v dálce je sem tam nějaký rybář."
                show d plavky
                d "Co je na mě špatně, že na mě zase tak zíráš?"
                hide d plavky
                "Vyruší tě z myšlení Dante, který se dostal až k tobě."
                j "Chceš slyšet pravdu nebo si mám vymýšlet?"
                show d plavky
                d "Takže je na mě něco špatně, jasně že pravdu. Já ti také nelžu."
                hide d plavky
                j "Přemýšlela jsem proč se koupeš v triku, když tu kromě nás nikdo není."
                show d plavky 
                d "Jo aha a já myslel, že mí narostli rohy, nebo tak něco. Že sis mě tak zkoumavě prohlížela."
                d "Dám ti na výběr ze čtyř... pěti možností vyber si, co je podle tvého pravda."
                d "Takže na veřejnosti se nesvlékám, protože se za a) stydím, za b) víc na to letí holky, c) z náboženského přesvědčení,"
                d "d) mám tetování, které by se v japonsku na veřejnosti nemělo ukazovat a za e) mám tělo samoou jizvu, tak nechci nikoho děsit."
                hide d plavky
                "Možností máš na výběr opravdu hodně, možnost a) a nebo b) z nich z ní nejlépe, ale také nejméně pravděpodobně."
                j "V japonsku, se na veřejnosti nesmí ukazovat tetování?"
                show d plavky
                d "Ne no. Japonci mají tetování spojené s yakuzou."
                hide d plavky
                j "Aha."
                show d plavky
                d "Proč si vlastně nešla také do vody?"
                hide d plavky
                j "Nechtěla jsem být celá od soli a písku, když je odsud hotel ještě dvě hodiny autem."
                show d plavky
                d "Všiml jsem si že u toho parkovistě byl kohoutek, plánuju se opláchnout tam."
                hide d plavky
                "Jen co domluví připojí se k vám Adrian a Sučan, osušej se ručníkem, obují se a vyrazíte k autu."
            elif j.love_points.get(a.name, 0) > 5:
                "Po chvíli se oddělí Adrian od ostatních."
                "A rozejde se k tobě. Když má vodu asi do pasu, přijde větší vlna a zezadu ho překlopí a smete."
                "Trochu tě zamrazí, ale když se Adrian v pořádku vynoří, tak tě to rozesměje."
                "Dojde k tobě."
                show a plavky
                a "Proč jsi také nešla? Ta voda je osvěžující."
                hide a plavky 
                j "Aby mě ty vlny smetly, jako tebe?"
                show a plavky
                a "Přiznávám, že mě ta vlna překvapila. Možná proto se tu nikdo nekoupe."
                hide a plavky
                j "Nechtěla jsem strávit další dvě hodiny v autě slaná. Proč nejsi ještě s klukama ve vodě?"
                show a plavky
                a "Nechtěl jsem tě nechávat čekat dlouho samotnou na břehu."
                hide a plavky
                j "To je od tebe milé. Takže mi teď vysvětlíš všechny ty věci?"
                show a plavky
                a "Všechny asi ne, dneska ti odpovím na jednu otázku."
                hide a plavky
                call adrian_otazky
                "Adrian si všimne, že se kluci už vracejí a zmlkne."
                "Ty také nevíš jak na jeho odpověď reagovat tak raději mlčíš."
                "Kluci se usuší a obují a vyrazíte k autu."
        "Mimoň spí v otevřeném autě, ještě že se v japonsku nekrade."    
        "U parkoviště je kohoutek se sladkou vodou, takže se u něj kluci vystřídají."
        "Ty si sedneš na obrubník dál od auta a kohoutku a koukáš se do mobilu."
        "Každý se pak jde oblíknout za auto, kde se kryje ještě i ručníkem."
        "Ne, zůstanu u auta.":
            "Adrian, Dante a Sučan se převlíkli do plavek a vyrazili k vodě."
            "Ty jsi zůstala na parkovišti s Mimoněm."
            "Mimoň sedí rozvaléný přes zadní sedačky auta a vyndal si Danteho nintendo swich."
            show m mask
            m "Vždyť tu vůbec nemá žádný dobrý hry, proč to vůbec vozí?"
            m "Tak to musím změnit... "
            hide m mask 
            j "Vážně, chceš instalovat nějaké hry na cizí zařízení a vůbec půjčil ti ho?"
            show m mask
            m "Bral ho kvůli mně, mám ho u sebe už od letadla."
            hide m mask
            "Aha."
            "No docela drahá hračka, no snad Dante nebude litovat, že mu ho půjčil."
            "Sedneš si tedy na místo spolujezdce, nandáš si sluchátka, aby si nemusela poslouchat Mimoně."
            "Pustíš si svůj oblíbený playlist."
            "Vzbudí tě až to že se kluci vrací od vody."
        "Všimneš si že Mimoň také spí, ale nechal otevřené zadní dveře, ještě že se v japonsku nekrade."    
        "U parkoviště je kohoutek se sladkou vodou, takže se u něj kluci vystřídají."
        "Každý se pak jdete oblíknout za auto, kde se kryjete ještě i ručníkem."
        "Pak přijdou k autu a vypadají, že se chtějí převlíknout."
        "Rozespale tedy vylezeš a deš si stoupnout dál od auta."
        "Každý se pak jde oblíknout za auto, kde se kryje ještě i ručníkem."
    "Když jste přichystaní na odjezd vzbudíte Mimoně."
    show m mask angry
    "Co je?"
    hide m mask angry
    show d fujihs
    d "Pojedeme, skoro po cestě je ten Gibli park sice se nám nepodařilo koupit lístky dovnitř, alr mají i nějakou volně přístupnou část."
    d "Tak bychom se tam mohli zastavit."
    hide d fujihs
    show a fujihs
    a "Je úterý, mají zavřeno."
    show d fujihs
    d "Ajo, ale ono je stejně docela pozdě."
    hide d fujihs
    show s fujihs
    s "Sjel bych někam do lékárny, pro pantenol, spálil jsem se a všimli jsem si, že jste všichni spálený."
    s "Jsem za koupit jeden a podělíme se o něj."
    hide s fujihs
    "S tím souhlasíte."
    scene bg nagojapoliklinika
    "Pomocí map najdete něco co podle názvu připomíná lékárnu."
    "Zaparkujete u takového malého domečku s parkovišťátkem."
    "Adrian a Sučan vystoupí, vlezou dovnitř a za pár minut vychází."
    show a fujihs
    a "Je to nějaká poliklinika, ale doporučili nám nějaký velký obchoďák s drogerií."
    a "Že tam by mohli mít to co chceme."
    hide a fujihs
    "Vyrazíte tedy na doporučené místo."
    "Vypadá to trošku jako u nás globus nebo tesko, velký 'hangár' s parkovištěm."
    if j.driver:
        "Protože se nechcete zdržovat a dovnitř stejně nepůjdete všichni. Přibrzdíš u vchodu a kluci vyskáčou a jdou do obchoďáku."
        "A ty jedeš zaparkovat."
        menu:
            "Budeš parkovat po předu nebo po zádu?"
            "Po předu.":
                "Zajela jsi na místo jako po másle, kola se ti zastavili o betonovou zarážku."
                "Za pár minut se kluci vracejí s dvěmi tubami přípravku."
                "Naskákali do auta a ty začneš vycouvávat, ozve se hodně divný zvuk."
                "Dření plastů o beton."
                "Asi jak se zatížilo auto tak vám kleslo těžiště a odřeli jste kryt motoru o betonovou zarážku."
                "Na jízdních vlastnostech se nic nezměnilo, takže jsi vyrazila."
                "Ale ujeli jste pár metrů mimo parkoviště."
                "A na křižovatce auto začíná vydávat opravdu děsivé zvuky."
                "Projedeš křižovatkou."
                show a fujihs
                a "Asi bychom měli zastavit, ti japonci na nás divně koukají."
                hide a fujihs
                j "Jo také se mi to nelíbí."
                scene bg opravaauta
                "Zastavíš u prvního vězdu do baráku, kde se zastavit dá."
                "Vylezete ven a zjistíte."
                "Že vám z auta ve předu visí plasty."
                "Jak jsi vyjížděla ven z místa na parkovišti, zachytila jsi o betonovou zarážku krytku motoru a část podběhů."
                "Sučan jako milovník aut, jako první leze pod auto."
                show s fujihs
                s "Hmmm... Urvala jsi takové ty plastové nýty, teda ne všechny, ale nedrží tam, takže se nám to chytá do kol."
                s "Bez nářadí to neopravím."
                hide s fujihs
                show d fujihs
                d "Ukaž?"
                hide d fujihs
                "Dante se vymění se Sučanem pod autem."
                show d fujihs
                d "Jo souhlasím, to bez nářadí asi nedáme, nevím kde sehnat nýty nebo aspoň šrouby v japonsku."
                hide d fujihs
                "Zatímco poskakujete kolem auta všimnete si, že vedle vás nějaká rodina japonců se balí asi na dovolenou."
                show s fujihs
                s "Navrhuji ty plasty sundat a vyřešit to později."
                hide s fujihs
                show d fujihs
                d "Jo souhlasím, ale i tak by se nám hodilo nějaký nářadí."
                hide d fujihs
                show a fujihs
                a "A co byste chtěli, za nářadí? Zkusím se zeptat těch Japonců."
                show s fujihs
                s "Hele asi osmičku klíč a kleště."
                hide s fujihs
                "Adrian chvíli kouká do mobilu, asi do slovníku a pak se rozejde k rodině."
                "Chvíli s nimi mluví."
                "Poté se od rodiny oddělí starší japonec asi dědeček, jde přes ulici do nějaké garáže."
                "Za chvíli se vrací s nějakými nástroji, které podal Adrianovi."
                show a fujihs
                a "Tak mi půjčili tohle, bude to stačit?"
                hide a fujihs
                show s fujihs
                s "Uka? Jo to by mohlo stačit."
                hide s fujihs
                "Dante se mezitím vysoukal z pod auta a pustil Sučana zpět."
                "Sučan tedy zalezl pod auto, chvíli to tam morduje a za chvíli podává první plast."
                show s fujihs
                s "Ten velkéj nějak přichytím, ale ten menší sundám i na druhé straně."
                hide s fujihs
                "Zatím co Sučan sundává druhý plast, japonská rodina se mezitím nasoukala do auta a vypadá nervózně. Že by chtěla jet a vy stále máte jejich nářadí."
                hide s fujihs
                "Naštěsí během chvíle, Sučan podává i druhý plast."
                show s fujihs
                s "Hele není to ideální, ale asi s tím můžeme jet."
                hide s fujihs
                "Začne vylízat z pod auta, a podává nářadí Adrianovi."
                "Ten si jej převzal a rozejde se k Japoncům, na nich je vidět, že jsou se rádi, že brzy vypadnete."
                "Plasty jste dali na podlahu ke spolujezdci."
                "Sedla jsi zase za volant a vyrážíte směr hotel."
            "Po zádu.":
                "Pomocí párkovacích kamer si na první dobrou krásně zaparkovala."
                "Za pár minut se kluci vracejí s dvěmi tubami přípravku."
                "Naskládali se do auta. A vyrazíte směr hotel."
    else:
        "Sučan zaparkoval po zádu pomocí parkovacích asistentů. A jde s Adrianem a Dantem do obchoďáku."
        "Pomocí párkovacích kamer si na první dobrou krásně zaparkovala."
        "Za pár minut se kluci vracejí s dvěmi tubami přípravku."
        "Naskládali se do auta. A vyrazíte směr hotel."
    scene bg mapanagoja
    "Kolem šesté přijíždíte do Nagoji."
    "Najdete váš hotel, ale nevíte jak je to s parkováním, tak zastavíte na blikačky."
    show s fujihs
    s "Hotel má mít nějaké vlastní parkoviště, ale nevím kde."
    hide s fujihs
    "Takže Sučan s Adrianem vyrazí na recepci, vy čekáte v autě."
    show s fujihs
    s "Tak jsem dostal nějakou mapku a lísteček na slevu, je to nějaký parkoviště, kde mají zákazníci hotelu slevu."
    hide s fujihs
    "Parkoviště, je někde za vámi, takže musíte objet blok a nakonec parkoviště trefíte."
    "Vyndáte kufry a vyrazíte zpátky k hotelu."
    "Máte tři pokoje, dva dvojlůžáky a jeden jednolůžák."
    "Jednolůžák dostaneš ty, dokonce to tak očekávájí na recepci. Dante si bere pokoj s Adrianem."
    "A Sučan tedy schytal Mimoně."
    "Dáte si sraz za hodinku před pokoji, že půjdete společně na večeři."
    "Dala sis věci na pokoj a proběhneš sprchou."
    "Dáš vědět domů. Převlíkneš se přebalíš si věci s sebou a je akorát čas srazu."
    "Vylezeš před pokoj a tam už čekají Adrian, Dante a Sučan."
    show s nagoja
    s "Není tu Ichiran? Ten mi chutnal."
    hide s nagoja
    show a nagoja
    a "Jo, pobočka v Nagoji je, kouknu jestli je to někde blízko."
    a "..."
    a "Jo, tak je odsud asi 3 ulice."
    hide a nagoja
    show s nagoja
    s "Tak super za mě Ichiran."
    hide s nagoja
    show d nagoja
    d "Jo já jsem za."
    hide d nagoja
    "Vypadá to, že je rozhodnuto."
    show s nagoja
    "Hmmm. Ten Mimoň asi nepřijde, dojdu se na něj podívat."
    hide s nagoja
    "Zajde do pokoje a za cvíli vychází s Mimoněm."
    show m mask angry
    m "Mám hlad! Dal bych si normální suši."
    hide m mask angry
    show d nagoja
    d "Jde se na Ichiran, jak jsme byli první den v Tokiu."
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
    m "Sám nejdu, tak jdu teda s vámi."
    hide m mask angry
    show s nagoja
    s "Takže ikimašó."
    "Jdete tedy pár ulic a najdete pobočku Ichiranu."
    "Moc se neliší od Tokijské pobočky."
    "Zakrouškujete si, co si chcete dát, zaplatíte u automatu a během chvíle si už vychutbáváte každý svůj rámen."
    "Po jídle se jdete po Nagoje ještě projít."
    scene bg pachinko
    "Zaujme vás herna s Pachinkem."
    "V japonsku je totiž zakázaný hazard, takže nenajdete v něm typické herny."
    "Ale samozřejmně i Japonci jsou vynalézavý, takže mají pachinko herny."
    "Což je hra s kovovými kuličkami, něco na styl pinballu."
    "A jako výhru množíte kuličky a kuličky se dají vyměnit za hračky, nebo za speciální krabičku."
    "Která se na 'černém' trhu za pěníze."
    "Vlezli jste tedy dovnitř a jdete k jednomu automatu."
    "Sučan se posadil k jednomu automatu a vy jste se rozestavili kolem něho."
    "Vytáhli jste překladač a snažíte se přijít na to jak to funguje."
    "Po chvíli přijde Japonec, který se vás zeptá jestli chcete pomoc v japonštině."
    "Adrian odpoví v japonštině, že ano. Tak japonec spustí v japonštině. Tak mu řeknete anglicky jestli by to nemohl říct anglicky."
    "Tak to se viděsí a uteče?"
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
    Japonka "So now, give the card here. And you can start."
    hide japonkaherna
    "A tak Sučan vložil kartu do stroje a navolil první hru."
    "Když zmáčkl start, tak začnou lítat kuličky do stroje."
    show japonkaherna
    Japonka "Oh, you must, oh the button... Sorry."
    hide japonkaherna
    "Japonka pochopila že Sučan vůbec netuší, tak mu chytla ruku a snaží se ho navést."
    "Ale skoro všechny kuličky padají mimo výherní místo."
    "Když přestanou kuličky létat. Tak se Japonka zasměje a řekne."
    show japonkaherna
    Japonka "Ups, gameover, you lost five hundred yen. So you know how to play, in other part of room is automat where you pay one yen per ball."
    Japonka "Bye."
    hide japonkaherna
    "A zmizela"
    show s nagoja
    s "Hm, tak jsem prohrál pět set yenů a už chápu proč ti japonci u toho sedí ruku v jedné pozici."
    s "Jestli si to chcete někdo zkusit, jsem za vyndat tu kartu a jít na ten druhý automat."
    hide s nagoja
    "Ukončili jste tedy hru vyndali kartu a přesunuli se k automatu, kde se platí za jednotlivé míčky."
    "Každý jste si to vyzkoušeli."
    "Takže jste získali i nějaké kuličky zpět, ale po chvíli jste neměli žádné."
    "Takže jste odcházeli o 1000 yenů lehčí, ale nabytí nových zkušeností."
    "Ještě jste udělali malý okruh a vrátili jste se na hotel."
    "Druhý den se plánujete přesunout do Kjóta s tím, že část z vás pojede Šinkanzenem."
    "A protože zítřek je ve znamení přejezdu, rozhodnete se, že si ještě ráno Nagoju projdete za světla."
    "Rozejdete se do svých pokojů, proběhneš koupelnou, nařídíš budíka a do pár minut jsi tuhá."

    return

label adrian_otazky:
    menu:
        "Tak na kterou otázku chceš nejvíce znát odpověď?"
        "Proč nechce, aby Dante věděl o jeho omdlení?":
            show a plavky worried
            "Po tom, co jsem utekl z domu a neměl jsem nic, zvládl jsem si sbalit jen pár osobních věcí, na který jsem si vidělal potají na brigádě."
            hide a plavky worried
            j "Utekl z domu, bez věcí proč?"
            show a plavky worried
            a "Řekl jsem, že ti odpovím jen na jednu otázku a útěk z domova je jiný příběh."
            a "Neměl jsem tedy vlastně vůbec nic, neměl jsem ke komu jít, kde spát."
            a "Tenkrát v noci u mě zastavil Dante v autě, strašně pršelo já jsem byl promrzlý na kost."
            a "Řekl, že mi vezl narozeninový dárek a zjistil, že nejsem doma. A jestli nechci jít k němu, že na bytě má volný pokoj."
            a "S díky jsem to přijal, myslel jsem, že jen na pár dní, než se z toho svrabu vyhrabu."
            a "Teď to bylo 5 let, díky jeho podpoře jsem dostudoval a vlastně díky němu mám tak dobrou práci."
            a "Ale nechci být na něm tak závislý, vždycky moje problémy řeší, ale já po zkušenostech s otcem, nechci být na nikom závislý."
            a "A rozhodně nechci, aby si myslel, že jsem taková padavka, kterou skolí, první výšlap na horu."
            a "Když on je zvyklí běhat na sněžku s plnou polní."
            hide a plavky worried
        "Jak je to s jeho maminkou?":
            "Adrian zesmutní."
            show a plavky worried
            a "Dobře, dal jsem slib tak ti to tedy řeknu."
            a "Moje máma je nejlepší žesnká kterou jsem kdy znal. Akorát jsem jí osm let neviděl. Strašně mi chybí."
            hide a plavky worried
            j "Cože? Jakto?"
            show a plavky worried
            a "Řekl jsem, že ti odpovím na jednu otázku, tak mi neklaď doplňující, já ti to vysvětlím."
            a "Za všechno může můj otec, je to strašný násilník a alkoholik."
            a "Když mi bylo čtrnáct, tak jsem se mu poprvé v životě postavil, abych před ním ochránil mámu."
            a "Skončil jsem se zlomenou rukou v nemocnici."
            a "To byla pro mamku poslední kapka a začala aktivně řešit rozvod a místo, kde by se mnou mohla bydlet."
            "To co ti říká se ti neposlouchá vůbec lehce, nevíš jak se tvářit, jak se chovat."
            a "Bohužel otec je velmi vlivný podnikatel a v podstatě všechno, co jsme měli patřilo jemu."
            a "Navíc měl strašně sviňskýho právníka, z mamky udělali socku neschopnou postarat se o sebe natož o dítě."
            a "A na vzdory mým protestům bylo 'V zájmu dítěte' rozhodnuto, že budu svěřen do opatrovnictví otci."
            a "A dokonce se mu podařilo zařídit, že 'v zájmu mé výchovy' se se mnou nesmí máma ani vídat."
            a "Takže jsem zažil tři nejhorší roky svého života a v osmnácti jsem utekl z domova."
            a "A mamku už pět let s Dantem hledáme, strašně mi chybí, navíc mám strach, jestli jí ten šmejd něco neudělal."
            a "Adri mi vždycky říkala ona, když mi tak někdo řekne, připomene mi jí to. Navíc jsi holka..."
            "Na chvíli se odmlčí."
            a "Stačí ti to jako odpověď?"
            "Jen přikývneš nevíš, co odpovědět. Možná ses neměla ptát."
    return