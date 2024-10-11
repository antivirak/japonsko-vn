label akt8:
    scene bg hotel kjoto
    "Dneska vás čeká přejezd do Kóbe, ale rozhodli jste se, že se po cestě stavíte v Naře."
    "Park v Naře je vyhlášený volně pobíhajícími jelínky, branami a svatyněmi."
    "Ráno jste společně vstali, pobalili jste se. Mimoň jako vždy vstal prdelí napřed – jak se někdy říká."
    show m mask angry
    m "Já nikam jet nechci, já chci zpátky do Tokia do gamecenter!"
    hide m mask angry
    show d kjoto
    d "Byl jsi u toho plánování, nikdo tě nenutil s námi absolvovat poznávací výlet po Japonsku."
    d "Kdykoliv se od nás můžeš odpojit, šinkanzenem jseš v Tokiu do dvou hodin, letenky zpět máš."
    hide d kjoto
    show m mask angry
    m "Sám nikam nepojedu!"
    hide m mask angry
    show s kjoto
    s "Tak asi budeš muset s námi absolvoval zbytek plánu."
    s "Jo to mi připomíná, že jsem se snažil zarezervovat to driftTaxi, rozmyslete se, kdo se přidáte."
    s "Já určitě chci a můžou jet až 3. Ten systém je teda úplně blbý – tak uvidíme, zda mi odepíšou."
    s "Asi bychom se měli nasnídat a vyrazit, máme dneska dlouhý přejezd a večer chceme ten wagyu steak."
    hide s kjoto
    show m mask angry
    m "Mám poslední tričko."
    hide m mask angry
    j "To už si vyprat nestihneš, chceme za chvíli vyrazit, cyklus pračky hodina a sušička tak půl."
    show m mask angry
    m "Ale já mám poslední tričko! Můžeš za to ty, řekla si, že si jich mám vzít jen 7, že si budeme prát."
    hide m mask angry
    j "No všichni jsme redukovali počet oblečení a my jsme si prali po Fuji."
    show m mask angry
    m "Mně si nevyprala."
    hide m mask angry
    show d kjoto
    d "A proč by to dělala? Pojďme snídat."
    hide d kjoto
    "Vyndali jste si tedy jídlo z ledničky a sedli jste si společně ke stolečku, který je typicky nízký musíte si sednout na takové minifutony."
    "Po snídani jste se pobalili, kufry jste naskládali ke dveřím a trošku po sobě poklidili. A vyrazili jste k autu."
    scene bg kjoto ulice
    "Řídit bude Sučan."
    menu:
        "Kam si chceš sednout?"
        "Spolujezdec":
            if j.love_points.get(s.name, 0) > 4:
                "Sučan ti otevře dveře a pustí tě sednout. Mrkne na tebe a mile se usměje."
                "Teprve poté přejde na stranu řidiče."
                "Vzadu se rozjela hádka, kvůli tyči z Fuji."
                show a kjoto
                a "Musí ta tyč vážně jet s námi? Tady se nedá sedět."
                hide a kjoto
                show m mask angry
                m "Musí, já si ji pošlu do Čech poštou!"
                hide m mask angry
                show d kjoto
                d "Už aby to bylo!"
                hide d kjoto
                "Sučan asi využívá situace, že se kluci věnují tyči a opře se levou rukou o tvou sedačku a nakloní se přes tebe."
                show s kjoto
                s "Promiň, nechal jsem si ve dveřích vodu."
                hide s kjoto
                "Říká, zatímco tě v podstatě uzamkl vlastním tělem k sedačce a pravou rukou šátrá ve dveřích."
                "Srdce ti snad přestalo na chvíli bít. Zadržela jsi dech, tak nějak istinktivně. Úzkost ti sevřela hrdlo a žaludek."
                show s kjoto
                s "Tady je, mrška!"
                hide s kjoto
                "Zahlásí za chvíli vítězoslavně a i s lahví se zase narovná na sedačce."
                show m mask angry
                "Ne a ne a ne! Ta tyč tady prostě zůstane a pak se pošle,"
                hide m mask angry
                "ozve se zezadu a tobě dojde, že vlastně nejste v autě sami."
                "Konečně se můžeš nadechnout a cítíš, že jsi úplně rudá."
                "Sučan je evidentně pobavený, protože se ti směje, zatímco se rovná na sedadle a zapíná pás."
                "Střelíš po něm pohledem a hodíš po něm balíčkem kapesníčků."
                show s kjoto
                s "No co? Měl jsem žízeň."
                hide s kjoto
                "Rozhodneš to více nerozpitvávat, protože i situace vzadu se uklidnila."

            else:
                "Sedneš si na místo spolujezdce."
                show a kjoto
                a "Musí ta tyč vážně jet s námi? Tady se nedá sedět."
                hide a kjoto
                show m mask angry
                m "Musí, já si ji pošlu do Čech poštou!"
                hide m mask angry
                show d kjoto
                d "Už aby to bylo!"
                hide d kjoto
                "Rozhovor vzadu utichne a vy vyjedete."
            "Podle vašich zvyklostí, má spolujezdec na starosti navigaci a hudbu."
            "Připojíš tedy mobil k autu a spustíš playlist, který jste si připravili před odjezdem."
        "Dozadu":
            if j.hate_points.get(n.name, 0) > 3 and j.love_points.get(a.name, 0) < 4:
                "Adrian si sedl za řidiče Mimoň do středu a na tebe zbylo místo za spolujezdcem."
                "Dante si sedl k Sučanovi dopředu. Nastavuje navigaci a pustí playlist, který jste si připravili před odjezdem."
                "Mimoň napresoval tyč z Fuji mezi vás, takže musíš sedět skrčená."
                j "Nechceš tu tyč opravdu vyhodit? Dost tu překáží."
                show m mask angry
                m "Nikdy, tu si pošlu poštou."
                hide m mask angry
                j "Tak ji pošli co nejdříve, takhle se nedá sedět."
                show m mask angry
                m "Tak až potkáme poštu..."
                hide m mask angry
                "Tímto Mimoň ukončil hovor, nasadil si sluchátka, do pár sekund usnul a chrápe na celé auto."
            else:
                "Sedla sis za spolujezdce, prostřední místo schytal Adrian a za řidiče si sedl Mimoň,"
                "který narval dřevěnou tyč z Fuji mezi sebe a Adriana. Takže Adrian je zase schoulený uprostřed."
                "Dante si sedl k Sučanovi dopředu. Nastavuje navigaci a pustí playlist, který jste si připravili před odjezdem."
                "Mimoň to zalomil, takže celou cestu spí."
    scene bg mapanara
    "Cesta do Nary je relativně krátká, takže po dvou hodinkách jízdy zastavujete na parkovišti."
    scene bg nara_jelinci1
    "Po zaparkování jste všichni vystoupili z auta, park je jen přes silnici."
    "Jen jste přešli na území parku, už se k vám žene stádo jelínků."
    "V parku se nachází několik stanovišť, kde se dají koupit takové speciální oplatky, kterými je povoleno jelínky krmit."
    "Adrian neodolá a hned si balíček asi za 100 yenů koupí."
    "Ve chvíli, kdy zaplatí a udělá od stánku asi 10 kroků, rozeběhne se k němu asi deset jelínků."
    "Jeden jelínek je dokonce tak netrpělivý, že než Adrian rozdělá balíček oplatek, tak Adriana začne okusovat."
    "Adrian začne instinktivně couvat, takže jde Adrian a s ním tlupa jelínků."
    "Když rozdá poslední oplatku, tak Adriana přestanou pronásledovat, rozhlídnou se a běží za dalším potenciálním krmičem."
    "Uprostřed jedné části parčíku jsou stromy, které vrhají stín. A ve stínu spí asi 20 jelínků."
    "Přesunete se tedy tam a využijete toho, že všichni odpočívají, takže se nechají pohladit a dá se s nimi vyfotit."
    "Všude kolem jsou bobky, takže je nutné dávat pozor, kam šlápnete."
    "Focením fotek a selfie strávíte dobrou hodinu a až poté si jdete projít zbytek parku."
    "Do chrámu se ale stojí fronta a rozhodnete se, že jste už chrámy viděli a před vámi je dlouhá cesta, takže jste chrám zkoukli jen zvenčí."
    "A po chvíli se již vracíte zpět. Kolem stánků se suvenýry."
    "Když přijdete do auta, sníte svačiny, které jste si s sebou nakoupili – toasty a káva."
    "Zjistíte, že už je po poledni, takže už nezbývá čas na Osaku, kterou jste chtěli taktéž dnes absolvovat."
    "Ale protože se nechcete svých plánů vzdát úplně, rozhodnete se, že alespoň projedete centrem města."
    "Do auta jste se naskládali ve stejném rozložení jako ráno a po zaplacení parkovného Sučan vyjíždí."
    "Adrian i Mimoň během pár minut usnou a i tebe jízda ukolíbá."
    "Vzbudí tě až to, že v Osace popojíždíte v koloně, navigace stále hlásí ať odbočíte vpravo, ačkoliv na všech křižovatkách je zákaz odbočení vpravo."
    "Po chvíli pochopíte, že si navigace myslí, že se nacházíte na jiné silnici, protože silnice v Osace je tříúrovňová."
    "Vy jste na pozemní komunikaci, je nad vámi vede okruh Osakou a nad ním ještě dálnice."
    "Popojíždíte kolonou, Sučan musí být stále ve střehu, protože auta přejíždějí z pruhu do pruhu, sem tam někdo na poslední chvíli zastaví."
    "Do toho navigace hlásí kraviny, takže si nejste jistí, že jedete správně."
    "Asi po hodině a půl jste konečně projeli centrem a situace se se malinko uklidnila."
    if j.driver:
        "Sučan po chvíli odbočí z hlavní a zastaví na takovém vyasfaltovaném plácku."
        show s kjoto
        s "Potřebuju vystřídat, bylo to náročnější, než jsem čekal."
        hide s kjoto
        j "Jo, jasně, já to dořídím."
        "Sučan vylezl z auta a jde si protáhnout nohy. Ty si zatím přendáš svoje věci na místo řidiče."
        "I zbytek posádky si jde trošku protáhnout nohy."
        show d kjoto
        d "Hmm... tak jsme toho moc neviděli, jsme asi klidně mohli po té dálnici horem."
        hide d kjoto
        show a kjoto
        a "Ale tak zase jsme ušetřili za poplatky za dálnici."
        hide a kjoto
        show d kjoto
        d "No, zase jsme spálili víc nafty a podívej se na Sučana, jak ho to vyšťavilo."
        hide d kjoto
        "Sučan se za chvíli vrací, vy se naskládáte do auta a vyrážíte směr Kóbe."
    else:
        show s kjoto
        "Kdyby mě měl kdo vystřídat, nebránil bych se. Naštěstí je to do Kóbe už jen kousek."
    scene bg mapakobe
    "Ani ne za hodinku už jste v Kóbe. Do Kóbe jste si naplánovali 4* hotel. Protože večer plánujete wagyu-steak."
    "Takže i podle toho jste si zvolili hotel."
    "Hotel jste trefili na první dobrou a autem jste zajeli přímo ke vchodu."
    "Vysypali jste se z auta a už vás u dveří odchytil Japonec s vozíčkem, kam jste naskládali kufry."
    "Sučan dostal lísteček s tím kam má zaparkovat auto, takže s Dantem odjeli auto zaparkovat."
    "Ty, Adrian a Mimoň jste zatím šli čekat do hotelu."
    "Rozhodně ale do interiéru s nedostatečným dresscodem nezapadáte, hotel je plný businessmanů a dam v kostýmcích."
    "A vy na sobě máte normální oblečení, jste splavení z cesty a Mimoň má dokonce svou liščí masku."
    "Naštěstí za chvíli přichází Sučan s Dantem. Sučanovi jste dali své pasy a on zamířil s Adrianem na recepci."
    "Za chvíli mají vyřešeno a vás se ujme Japonka, která naznačuje, že vás odvede na pokoj a začala tlačit vozíček k výtahům."
    "Vyjeli jste do šestého patra, zde jste vystoupili a následovali japonku do chodby."
    "U jednoho pokoje se zastavila, odemkla kartou a naznačila, že tam máte jít. Japonsky pak něco řekla, pravděpodobně k vybavení pokoje."
    "Pak otevřela další dva pokoje vedle a sundala zavazadla z vozíčku."
    "Poděkovali jste jí 'arigató', ona se usmála, uklonila se a s vozíčkem zamířila zpět k výtahům."
    "Vzala sis tedy svá zavazadla a zamířila do pokoje, který podle papírů má být tvůj."
    "Adrian s Dantem pak zabrali další a Sučan si vytáhl krátkou sirku a dostal k sobě Mimoně."
    "Ještě, než jste se v pokojích zabouchli, tak jste se domluvili, že se sejdete za cca hodinku v 17:00 a vyrazíte do města na večeři."
    "A že se obléknete slušně, když jste v takovém honosném hotelu a jdete na tak drahé jídlo."
    "Zalezeš tedy do pokoje, odložíš si pokojovou kartu na vstupní pultík, dáš si kufr do pokoje a vyndáš si věci na převlečení."
    "A přesuneš se do koupelny, je krásně prostorná, laděná do mramoru a zlata."
    "Užiješ si koupel ve vaně a umyješ si vlasy. Jako v ostatních hotelech v Japonsku koupelna obsahuje mýdla, šampón, kondicionér, koupací čepici, gumičky, hřeben, holítko, fén a mnoho dalšího."
    "Vlasy si vyfénuješ, učešeš se, nalíčíš a vezmeš si na sebe společenštější oblečení."
    "Zkontroluješ zprávy a zjistíš, že kluci dohadují místo pro večeři. Podle všech recenzí na internetu je ale do všech restaurací nutná rezervace, minimálně den předem."
    "To tě trošku znervózní, ale tak při nejhorším se jen projdete a koupíte večeři v kombini."
    "Napíšeš domů, že jsi v pořádku a jak se máte."
    "A mezitím ti přijde soukromá zpráva od Sučana"
    s "Neuvěříš! Mimoň si chce tady nechat vyprat. Cena podle ceníku je 600 yenů za kus. :D"
    "Za tu cenu se dá vyprat v japonsku celá pračka prádla..."
    j "Rozmluv mu to, je to blbost."
    s "Pracuju na tom."
    "Zkoukneš ještě sociální sítě. A už je pomalu čas vyrazit."
    "Sbalíš si věci, doladíš účes a jdeš čekat na chodbu."
    "Všichni kluci tam už čekají a všichni jsou učesaní, navonění a velmi vkusně oblečení."
    "Jen teda Mimoň vypadá pořád stejně. Vyrazíte tedy směr výtah."
    if j.love_points.get(a.name, 0) > 4:
        "Po cestě se k tobě přimotá Adrian."
        show a kobe
        a "Moc ti to sluší, [j.name_5p]!"
        hide a kobe
    elif j.love_points.get(d.name, 0) > 4:
        "Po cestě se k tobě přimotá Dante."
        show d kobe
        d "Moc ti to sluší, [j.name_5p]!"
        hide d kobe
    elif j.love_points.get(s.name, 0) > 4:
        "Po cestě se k tobě přimotá Sučan."
        show s kobe
        s "Moc ti to sluší, [j.name_5p]!"
        hide s kobe
    else:
        "Nikdo z kluků si tě nějak extra nevšímá."
    "Výtahem sjedete dolů a vyrazíte směr metro, protože do centra to jsou asi 4 km."
    "Ke stanici to naštěstí je jen kousek, takže do čtvrt hodinky už kupujete lístek v automatu."
    "Podle mapy na zdi jste odvodili, za kolik lístek potřebujete. Do automatu jste nasypali drobné, odmáčkli příslušnou cenu, a z automatu vypadl malý papírek."
    "Ten jsi pak vložila do příslušné díry v turniketu, na druhé straně ti lístek vyjel a turniket tě pustil."
    "Lístek sis tedy vzala a křečovitě jsi ho dalších šest stanic svírala, abys ho neztratila."
    "V cílové stanici jste všichni vystoupili a rovnou jste zamířili k východu."
    "Vložila jsi lístek zase do turniketu, ten se otevřel, prošla jsi, ale lístek ti to už nevydalo."
    "Kluci poznamenali, že je to jako s lístkem na šinkanzen. Také si ho nemohli nechat."
    "Přidala ses k čekajícímu Dantemu, turniketem prošli i Adrian a Sučan."
    "Mimoň, tam ale začne tak divně pochodovat a nakonec se rozběhne a snaží se turniketem proběhnout."
    "Samozřejmě se před ním dost razantně zavře."
    show d kobe
    d "Co dělá?"
    hide d kobe
    show a kobe
    a "Nevím, asi ztratil lístek?"
    hide a kobe
    show s kobe
    s "Tak proč si nekoupí nový, nebo si neřekne v té budce?"
    hide s kobe
    show d kobe
    d "Protože takhle na sebe upoutá pozornost všech a dělá blbce i z nás. Adriane zařídíš to?"
    hide d kobe
    show s kobe
    s "Co to děláš, Mimoni?!"
    hide s kobe
    "Křikne Sučan na Mimoně."
    show m mask angry
    m "Nemůžu najít lístek!"
    hide m mask angry
    show s kobe
    s "Tak jdi k té budce a nesnaž se probíhat! Adrian ti to vykomunikuje."
    hide s kobe
    "Adrian, ačkoliv evidentně nerad, došel k hlídací buňce a Japonci za přepážkou vysvětlil, že Mimoň ztratil lístek a že my jsme všichni v pořádku prošli."
    "Na Japonci bylo znát pohoršení z toho jak gaijini neumí jezdit metrem, ale Mimoně pustil."
    $ j.add_hate_points_for_person(m, 2)
    "Sice se tato situace dala řešit daleko lépe a s menší ostudou, nakonec jste v centru Kóbe."
    show a kobe
    a "Hele, našel jsem jeden podnik s fakt vysokým hodnocením, ale místo se tam má rezervovat asi týden dopředu."
    hide a kobe
    show s kobe
    s "Já bych to stejně zkusil."
    hide s kobe
    show d kobe
    d "Já jsem také za to, to zkusit. Jo Mimoňi, nechceš se jít najíst někam jinam? Říkal jsi, že na účtu už nemáš peníze a zatím jsme za tebe krom šinkanzenu všechno platili."
    d "Takže nám už teď dohromady dlužíš tak deset tisíc a ten steak vyjde minimálně na pět tisíc na osobu."
    hide d kobe
    show m mask angry
    m "Ne, na steak rozhodně půjdu. Nevidím důvod abych někam chodil sám."
    hide m mask angry
    show d kobe
    d "No, možná by tě teda měli založit rodiče, aby si tu nežil na naše náklady."
    hide d kobe
    show m mask angry
    m "Vždyť já vám to všechno dám!"
    hide m mask angry
    show a kobe
    a "Tady to má být po pravé straně,"
    hide a kobe
    "vstoupí do rozhovoru Adrian."
    "Chvíli se rozhlížíte a nikde nevidíte restauraci s příslušným názvem."
    "Nakonec se Adrian, zeptá Japonky, která dělá reklamu na nějakou jinou restauraci."
    "A ta mu ukáže na výtah za ní. Teprve teď si všimnete, že u patra číslo 4 je napsaný název té restaurace."
    "Vlezete do výtahu a vyjedete nahoru. Objevíte se v místnosti, kde jsou dva pultíky, pár barových stoliček a jeden Japonec."
    show chef
    Chef "Konbanwa!"
    hide chef
    show a kobe
    a "Konbanwa. Do you have a place for diner?"
    hide a kobe
    show chef
    Chef "Do you have reservation?"
    hide chef
    show d kobe
    d "No we don't."
    hide d kobe
    show chef
    Chef "How many people?"
    hide chef
    show d kobe
    d "Five."
    show chef
    Chef "Hmm, okay come in. And sit here."
    hide chef
    show d kobe
    d "To bylo nějaké snadné."
    hide d kobe
    "Posadili jste se tedy k pultíku, kam vám kuchař naznačil."
    "Dostali jste meníčko z kterého si máte vybrat."
    show chef
    Chef "Do you want testing menu? Soup, rice and the meat of your choice?"
    hide chef
    show d kobe
    d "That sounds great, and which meat do you recommend?"
    hide d kobe
    show chef
    Chef "Haha, it's obvious that this one, which is served only in restaurant with Kobe gold placket."
    Chef "But you can try this one, which is cheaper and make desicion which one is better."
    Chef "Of course I can distribute the meat euqally between you."
    hide chef
    show d kobe
    d "Oh, that sounds good, give us a minute."
    d "Fajn, pojďme se domluvit, kolik si objednáme kterého masa. Dal bych to s tím ochutnávkovým menu."
    "Chvíli jste se dohadovali a nakonec rozhodnete, že 600 g dražšího a 300 g levnějšího. Plus si k tomu dáte ten set."
    "Nadiktujete to kuchaři a on na chvíli odběhne pryč. Vrátí se zpět s mokrými nahřátými ručníky."
    show chef
    Chef "Anything for drink?"
    hide chef
    show d kobe
    d "Sake? It could be fine with meat, isn't it?"
    hide d kobe
    show chef
    Chef "Good taste, young man, whole bottle?"
    hide chef
    show d kobe
    d "Of course, and a glass for everyone. Thanks."
    hide d kobe
    show m mask angry
    m "Já chci džus!"
    hide m mask angry
    show d kobe
    d "A jaký?"
    hide d kobe
    show m mask angry
    m "Třeba pomerančový."
    hide m mask angry
    show d kobe
    d "Sumimasen, Sorry, can we get one orange juice, please?"
    hide d kobe
    show chef
    Chef "No problem, here it is."
    hide chef
    "Šéfkuchař vám tedy rozdal pohárky a rozlil saké. Mimoňovi dal džus, všem vám přinesl malou mističku se salátem ze skleněných nudlí"
    "a poté nanosil objednané maso a pochutiny na pult. Nechal vás udělat si fotografii a mezitím odnesl mističky od salátku a přinesl mističky s miso polévkou."
    "Zatímco jste jedli polívku, z výtahu vystoupilo asi šest lidí. Japonec se jim omluvil, že dneska mají už plno a poslal je do jiné restaurace."
    show chef
    Chef "You are lucky, we don't have any reservation today, because my colleague's wife has given birth to a child today. So I am here alone and I will close early."
    hide chef
    show s kobe
    s "Really? So Kanpai for the child!"  # TODO učili jsme ho děkuji a vyslovovat ř. Taky jsme se bavili o další cestě a doporučil nám loď-muzeum v Hirošimě
    hide s kobe
    show kobe_movie
    "Kuchař zase odběhl s nádobím a vrací se zpět s rýží. A začne si připravovat grill."
    "Varnou kovovou desku, zapuštěnou do pultu s plynovým hořákem."
    "Začne připravovat zeleninku a masíčko."
    "Můžeš se následujících pár minut kochat anebo pokračovat v příběhu."
    hide kobe_movie
    "Poté co jste všechno snědli a dopili saké, jste se rozloučili poděkovali popřáli hezký večer a vyrazili do víru velkoměsta."
    "Venku to mezitím ožilo, nějaká klučičí kapela tu měla koncert, a o kus dál hrála nějaká pouliční zpěvačka."
    "Prošli jste se nočním Kóbe a vyrazili na metro."
    "Tentokrát, jste si ohlídali, že Mimoň má lístek, a vystoupili jste společně na zastávce poblíž hotelu."
    "U zastávky byl Lawson, takže jste si v něm mohli koupit věci na snídani."
    "Se snídaňkou v taškách jste vyrazili na váš super-ultra přepychivý hotel. Na chodbě jste se rozloučili, sraz jste si dali ráno na osmou a zamířili jste každý do svého pokoje."
    "Odlíčila ses a převlékla do věcí na spaní. Asi v devět večer někdo klepe na dveře."
    menu:
        "Kdo to asi je?"
        "Adrian":
            if j.love_points.get(a.name, 0) > 6:
                "Je to Adrian."
                call kobe_adrian_love
                return
            "Je to Sučan."
            call kobe_sucan_nolove
            return
        "Dante":
            if j.love_points.get(d.name, 0) > 4 and d.duvera:
                "Je to Dante."
                call kobe_Dante_love
                return
            if j.love_points.get(d.name, 0) > 4 and d.onenight:
                "Je to Dante. Nenechá tě nic říct, protože se prosmýkne dveřmi, přitlačí tě ke zdi a začne tě líbat."
                call kobe_dante_onenight
                return
            "Je to Sučan."
            call kobe_sucan_nolove
            return
        "Sučan":
            if j.love_points.get(s.name, 0) > 4:
                "Je to Sučan."
                call kobe_sucan_love
                return
            "Je to Mimoň."
            call kobe_mimon
            return
        "Mimoň":
            if j.hate_points.get(m.name, 0) > 4:
                "Je to Mimoň."
                call kobe_mimon
                return
            "Naštěstí je to Sučan."
            call kobe_sucan_nolove
            return
        "Je to jedno, stejně neotevřu.":
            if j.love_points.get(d.name, 0) > 4 and d.onenight:
                "Za chvíli slyšíš otevírání dveří. Zaklaply a cvakl zámek."
                "Krve by se tě teď nedořezal, pokud je to sériový vrah."
                call kobe_dante_onenight
                return

            "Za chvíli se ozve ještě jedno zaklepání a pak už je klid, takže můžeš jít spát."

    return


label kobe_dante_onenight:
    # TODO spicy mode will not be included in the competition verion of the game
    "Zatímco tě dychtivě líbá, tak nahmatal konec tvého trička na spaní. A začíná ti ho vyhrnovat nahoru."
    menu:
        "Zachytit mu ruce":
            show d kobe
            d "To ani nezkoušej. Byla si to ty, kdo mi dal tuhle nabídku,"
            hide d kobe
            "sykne jedovatě, zatímco ti zvládl evidentně nějakým chmatem obě ruce chytit, dát nad hlavu a uzamknout v jedné ruce."
            "Druhou rukou pokračuje ve vyhrnování trička. Zatímco od polibků normálních přechází do pusinkování tvého krku a šíje."
            menu:
                "Oddat se.":
                    "Pevný stisk tvých rukou mírně povolí. Když se mu podaří tričko vyhrnout na úroveň tvých ramen."
                    "Poté ti tričko přetáhl přes hlavu a zahodil."
                    "Pravou rukou ti šáhl za záda a podprsenka se bez odmlouvání rozepla snad ještě dříve, než se jí Dante stihl dotknout."
                    "Mezitím se stále líbáte a ty se mu snažíš rozepnout košili. Když se ti to podaří, zajedeš rukama po jeho holé kůži a vypracovaných svalech až na záda."
                    "A i přes všechno to vzrušení jasně cítíš, že na zádech má velké množství jizev."
                    "Mezitím tě Dante začal líbat na šíjí, chytil tě rukama za boky a jednoduchým pohybem, jako kdybys byla pírko, si tě nadhodil do výšky."
                    "Necháš se jím vést. Nasměroval si tě tak, že máš nohy okolo jeho pasu, drží tě za zadek a vyrazil s tebou směr postel."
                    "Hodí tě na postel, ale na chvíli nemáš obavu, že by se ti s ním mohlo něco stát."
                    "18+"
                "Začít křičet o pomoc.":
                    j "Dante nech toho! Pomoc! Nech mě!"
                    "Dante ti urychleně, zacpe rukou pusu, abys nemohla křičet."
                    show d kobe
                    d "Co blbneš? Já myslel cituji: že si chceš tuhle dovolenou užít se vším všudy."
                    hide d kobe
                    "Pustí ti ruce a sundá ruku z tvých úst a vypadá velmi zmateně."
                    j "Tak to jsme si nerozuměli. Byla bych ráda, kdybys teď odešel."
                    show d kobe
                    d "Jasně, jak si přeješ. Promiň."
                    hide d kobe
                    $ j.add_hate_points_for_person(d.name, 5)
                    "Sebere se, odemkne dveře a vypadne na chodbu. Zůstaneš na pokoji sama."

        "Nechat ho":
            "Během chvilky ti tričko vyhrnul k hlavě, Na chvilku tě přestal líbat, aby tričko mohl přetáhnout a zahodit."
            "Pravou rukou ti šáhl za záda a podprsenka se bez odmlouvání rozepla snad ještě dříve, než se jí Dante stihl dotknout."
            "Mezitím se stále líbáte a ty se mu snažíš rozepnout košili. Když se ti to podaří, zajedeš rukama po jeho holé kůži a vypracovaných svalech až na záda."
            "A i přes všechno to vzrušení jasně cítíš, že na zádech má velké množství jizev."
            "Mezitím tě Dante začal líbat na šíjí, chytil tě rukama za boky a jednoduchým pohybem, jako kdybys byla pírko, si tě nadhodil do výšky."
            "Necháš se jím vést. Nasměroval si tě tak, že máš nohy okolo jeho pasu, drží tě za zadek a vyrazil s tebou směr postel."
            "Hodí tě na postel, ale na chvíli nemáš obavu, že by se ti s ním mohlo něco stát."
            "18+"

    return


label kobe_sucan_nolove:
    show s kobe
    s "Jdu se jen zeptat, jestli je všechno v pořádku."
    s "A domluvit se s tebou na to drift-taxi, už mi odepsali a budeme muset trošku překopat plány."
    s "Mají volný termín jen o den dříve."
    hide s kobe
    j "Jasně, plán upravíme. Nějakou vůli jsme si nechali, ne?"
    show s kobe
    s "Jo, nechali, jen se jdu s tebou poradit, než to půjdu probrat s ostatními."
    s "Přeci jen mi na tvém názoru záleží."
    s "Takže mám s tebou počítat na driftTaxi?"
    menu:
        "Jo jasně, jsem pro každou špatnost.":
            $ j.driftaxi = True
            s "Super, bude to bomba!"
        "Ne, tohle není pro mě.":
            $ j.driftaxi = False
            s "Jo, jasný, nenutím tě. Nabídnu to klukům."
    s "Takže domluveno, jdu to ještě prodiskutovat s klukama, ale uděláme delší přejezdy a vyjde nám o den více na Tokio před odletem."
    hide s kobe
    j "Jo, den navíc v Tokiu na suvenýry asi všichni oceníme."
    show s kobe
    s "Jojo, také jsem si říkal, že to bude lepší a na tom severu jsme stejně neměli moc míst, co chceme vidět."
    s "Tak to je všechno, co jsem chtěl. Dobrou, [j.name_5p]."
    hide s kobe
    "Rozloučí se Sučan a jde klepat na vedlejší dveře."
    "Zavřeš za ním a připravíš se na spaní. Během pár minut spíš."
    return

label kobe_mimon:
    show m mask angry
    m "Přišel jsem ti jen oznámit, že nemám nic na sebe."
    hide m mask angry
    j "No dobře a čekáš, že udělám co?"
    show m mask angry
    m "Že mi vypereš."
    hide m mask angry
    j "Tady asi těžko a hotelová služba takhle v noci už také nebude přijímat objednávky."
    j "Můžeš si to přeprat ručně a vyfénovat a nebo holt budeš mít nějaké tričko podruhé."
    show m mask angry
    m "No to je skvělý."
    hide m mask angry
    "Ještě něco mrmlá a odešel od tvých dveří směr svůj pokoj."
    "S velkou úlevou zavíráš dveře. A jdeš si lehnout. Příště snad budeš radši klepání ignorovat."
    return

label kobe_adrian_love:
    show a kobe
    a "Promiň, chtěl jsem se ujistit, že je vše v pořádku a poděkovat ti za včerejšek."
    hide a kobe
    j "Jo, všechno je v pořádku, pojď dál. Dáš si čaj?"
    show a kobe
    a "Jo, rád."
    hide a kobe
    "Dáš vařit vodu a zaliješ dva čaje."
    menu:
        "Chceš nabídnout Adrianovi přespání?"
        "Ano.":
            j "Nechceš přespat dneska tady? Je tu manželská postel a byla bych klidnější mít tě pod dohledem."
            show a kobe
            a "Ale mně je vážně dobře... počkej... cože? Jo, vlastně mi není úplně nejlépe."
            a "Ale je ti jasné, jak si to vyloží Dante?"
            hide a kobe
            j "Já jsem si vědoma následků svých činů."
            show a kobe
            a "Myslíš to vážně?"
            hide a kobe
            j "Neptej se pořád tak hloupě na všechno. Pozval si mě na rande, ne?"
            j "A nejsme malý, abychom chodili kolem horké kaše. Jestli o mě máš vážně zájem tak u sebe přespávat asi budeme."
            show a kobe
            a "Aha, tak to si musíme ujasnit jednu podstatnou věc."
            menu:
                a "Chceš se mnou chodit?"
                "Ano.":
                    a "Tak teď si přijdu, jako kdybys přijala žádost o ruku."
                    a "Dobře dojdu si pro nějaké věci k Dantemu a vrátím se."
                    hide a kobe
                    "Za chvíli někdo zase klepe."
                    "Otevřeš a ve dveřích stojí Adrian. Usmívá se od ucha k uchu."
                    show a kobe
                    a "Tak mě tu máš, [j.name_5p]"
                    hide a kobe
                    j "Tak pojď dál, co Dante?"
                    show a kobe
                    a "K tomu bych se nevyjadřoval. Nechci si kazit večer s tebou."
                    hide a kobe
                    "Pustíš ho dovnitř, zavře za sebou a zamkne zevnitř."
                    "Položí tašku, co si přinesl, na pult u dveří, obmotá levou ruku kolem tvých zad. A dlouze tě políbí."
                    "Ještě, že tě drží, protože ačkoliv příměrům z románů určitě nevěříš, přirovnání že se ti z polibku podlomili kolena není daleko od pravdy."
                    "Byl to opravdu krásný, jemný, romantický a dlouhý polibek."
                    "Poté se na tebe moc mile usměje, vezme si věci z poličky a zamíří do pokoje."
                    "Vybere si tu část postele, kde nemáš věci."
                    show a kobe
                    a "Přijdu si dneska jak ve snu. Mám fotky s jelínky, ochutnal jsem wagyuu steak a holka mých snů souhlasila, že se mnou bude chodit."
                    hide a kobe
                    "Mluví o tobě tak hezky. Adrian je hodný kluk, udělala jsi dobře, že jsi se vztahem souhlasila."
                    j "Tak se hlavně neštípej, ať se neprobudíme."
                    "Dojdeš si umýt hrnečky od čaje a vyčistit si zuby."
                    "Adrian leží v posteli a čeká na tebe."
                    "Zalezeš si teda na svou polovinu a lehneš si na bok."
                    "Adrian se k tobě zezadu přitulí a odhrne ti vlasy z krku a políbí tě na šíji."
                    show a kobe
                    a "Dobrou, [j.name_5p]."
                    hide a kobe
                    "Zhasne lampičku a do pár minut spíte."
                "Ne.":
                    a "Pak asi přespání není vhodné."
                    hide a kobe
                    "Adrian urychlině dopil čaj, umyl hrnek a bezeslova vypadl."
                    "Takže jsi také dopila, umyla hrnek, vyčistila si zuby a hurá spát."
        "Ne.":
            "Chvíli jste si s Adrianem u čaje povídali."
            "Když dopil, umyl po sobě hrnek, popřál ti dobrou noc a šel spát a ty za chvíli také."
    return

label kobe_sucan_love:
    show s kobe
    s "Přišel jsem se zeptat, zda je všechno v pořádku."
    s "Přišla jsi mi při večeři taková smutná, btw strašně ti to slušelo."
    hide s kobe
    j "Děkuji, ale přemýšlela jsem nad tím Mimoněm, že jsem si toho, že ztratil ten lístek, měla všimnout."
    show s kobe
    s "To si tak neber. Já tu popravdě nejsem kvůli tomu, že by mě zajímalo, jak se máš."
    s "I když to mě samozřejmě také zajímá, ale že Mimoň pouští televizi na plný pecky a do toho si chrápe, tak mě napadlo, zda bych nemohl najít azyl u tebe."
    hide s kobe
    menu:
        "Necháš Sučana u sebe přespat?"
        "Ano.":
            j "Jo, jasně, je tu manželská postel, to se v pohodě vyspíme oba."
            show s kobe
            s "Díky, ani nevíš, jak jsem ti vděčný, jen těch pár hodin s ním na pokoji jsou hotový očistec."
            s "Dojdu si tedy pro nějaké věci a vyčistit zuby a za chvíli jsem tady."
            hide s kobe
            j "Jasný."
            "Ty si se poté, co Sučan odešel, také finálně připravíš do postele a za chvilinku se ozve klepání."
            "Jdeš otevřít a ve dveřích stojí Sučan. Tak ho pustíš dovnitř zavřeš dveře a zamkneš."
            "Sučan s taškou zamíří do pokoje, dá si mobil na nabíječku a oba si zalezete do postele."
            "Je mezi vámi takové zvláštní napětí a ani jeden nemluvíte."
            "Poté co oba ležíte v posteli tak zhasneš."
            s "To je ale klid. Jak ti chutnal wagyu steak?"
            j "Jo, chutnal. Je to velký rozdíl od normálního hovězího."
            s "Jo, to souhlasím."
            menu:
                s "Hele, [j.name_5p], rozmyslela ses, co ke mně vlastně cítíš?"
                "Ráda jako bratra.":
                    j "Stále jsi pro mě jako brácha."
                    s "Chápu, tak dobrou [j.name_5p]."
                    "Pochopila jsi, že tímto váš rozhovor ukončil a jdete spát."
                "Dát mu šanci.":
                    j "Stále jsem trošku zmatená, ale myslím, že tě začínám vidět jako Sučana a ne brášku co mě vždycky zachrání."
                    "S touhle větou se z boku přetočíš na záda, aby k němu obsah věty došel."
                    "Obsah tvých slov k němu bezpochyby doputoval, protože během chvilky nad tebou klečí tak, že kolena má v úrovni tvých boků."
                    "Instinktivně zvedneš obě ruce, abys ho mohla odstrčit jako v době dětských válek."
                    "Tvé ruce tak spočinou na Sučanově vypracované hrudi, ale tvá snaha ho odstrčit se zdá být lichou."
                    "Po chvíli ti dá ruce na stranu, skloní se k tobě a dlouze tě políbí."
                    "Přestaneš se bránit a polibek mu opětuješ. Využiješ toho, že během polibku je svolnější."
                    "Podaří se ti ho ze sebe shodit a prohodit si pozici. A políbíš ty jeho."
                    "Po chvíli tě ale Sučan chytne za rameno a jemně, ale razantně tě odstrčí."
                    j "Co se děje? Tobě se to nelíbí?"
                    s "Líbí a moc, ale takhle to nechci. Chci mít jistotu, že se mnou chceš být, a ne že jsem pobláznění na jednu noc nebo nějaký převozník po tvém ex."
                    "Tohle se tě dotkne, uraženě z něj slezeš, lehneš si na bok zády k němu a rozhodneš se usnout."
        "Ne.":
            j "Promiň, to mi nepřijde jako vhodné."
            show s kobe
            s "Jo jasný, sem to jen zkoušel. Půjdu k sobě, dobrou noc [j.name_5p]."
            hide s kobe
            "Sučan se s tebou rozloučil a vyrazil do svého pokoje. Ty se také připravíš do postele a za pár minut spíš."
    return

label kobe_Dante_love:
    show d kobe
    d "Přišel jsem dokončit náš rozhovor ohledně toho, kdo jsem."
    hide d kobe
    j "Tak asi pojď dál?"
    "Dante vstoupí do pokoje s černým kufříkem v ruce. Zavře za sebou dveře a zamkne."
    "Zamíří do pokoje a na postel položí kufřík. Na číselném zámku navolí kombinaci a ozve se klapnutí."
    show d kobe
    d "Přišlo mi, že mi věříš, tak ten kufřík otevři."
    hide d kobe
    "Dojdeš k posteli, kde leží onen odemčený kufřík a otevřeš ho. Uvnitř je automatická pistole se zásobníkem a tlumičem."
    "Instinktivně odskočíš."
    j "To je jen atrapa, že?"
    show d kobe
    d "Jestli atrapou lze zastřelit několik desítek lidí, tak je to atrapa."
    hide d kobe
    j "Pár desítek...?"
    "Opakuješ nevěřícně, možná s nadějí, že odpoví, že jsi špatně slyšela."
    show d kobe
    d "Fajn, takže teď už mi opravdu věříš. Rozhodni se, jak s tím naložíš."
    hide d kobe
    "Dante zaklapne kufřík, zatočí číselným zámkem a vyrazí směr dveře."
    menu:
        "Chceš ho zastavit?"
        "Ano, takhle odejít nemůže.":
            j "Dante, počkej, takhle odejít nemůžeš!"
            "Dante se zastavil a smutně se na tebe otočí."
            j "Já vím, že ses mi to snažil naznačit už několikrát, ale pochop, že je to pro mě strašně těžké."
            show d kobe
            d "No hlavně jsem vůl, teď riskuju tvůj život a ty se mě určitě ještě bojíš."
            d "Tak teď aspoň rozumíš, proč pracuju sám a nenavazuju vztahy."
            d "Další zklamání, dobrou noc, [j.name_5p]!"
            hide d kobe
            "Otočí se na 'podpatku' a rozejde se rychle ke dveřím."
            "Je ti jasné, že pokud něco neuděláš, tak tímto váš vztah/přátelství definitivně skončí."
            j "Dante! Počkej!"
            "Voláš, zatímco se za ním rozeběhneš."
            "Odemykání zámku dveří ho naštěstí zdrželo, takže ho doběhneš a zezadu obejmeš."
            "Dante úplně ztuhne. když se k tobě otočí, máš pocit, že se mu v očích zaleskly slzy."
            j "Možná to budu chvíli zpracovávat, ale vím, že pro mě si důležitý, tak nedělej blbosti."
            j "A doufám, že i já jsem pro tebe důležitá, když si mi řekl pravdu."
            show d kobe
            d "Jsi pro mě důležitá. Víc, než bych si přál."  # než bych ti přál?
            hide d kobe
            "Během své věty se vymaní z tvého obětí a vyklouzne z pokoje."
            "Když vzápětí otevřeš dveře na chodbu, tak tam Dante už není."
            "Rozhodneš se, že si půjdeš lehnout."
        "Ne, ať si jde, vrah.":
            "Odemkl dveře, ještě se na tebe smutně ohlédl a pak za sebou zabouchl."
            "Trošku otřesená dojdeš zamknout a jdeš spát."

    return
