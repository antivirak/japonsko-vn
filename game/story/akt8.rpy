label akt8:
    scene bg hotel kjoto
    "Dneska vás čeká přejezd do Kóbe, ale po cestě jste se rozhodli, že si zajedete do Nary"
    "Park v Naře je vyhlášený volně pobíhajícími jelínky, branami a svatyněmi."
    "Ráno jste společně vstali, pobalili jste se. Mimoň jako vždy vstal prdelí napřed - jak se někdy říká."
    show m mask angry
    m "Já nikam jet nechci, já chci zpátky do Tokia do gamecenter!"
    hide m mask angry
    show d kjoto
    d "Byl jsi u toho plánování, nikdo tě nenutil s námi absolvovat poznávací výlet po Japonsku."
    d "Kdykoliv se od nás můžeš odpojit, šinkanzenem jseš v Tokiu do dvou hodin, letenky zpět máš."
    hide d kjoto
    show m mask angry
    m "Sám, nikam nepojedu!"
    hide m mask angry
    show s kjoto
    s "Tak asi budeš muset s námi absolvoval zbytek plánu."
    s "Jo to mi připomíná, že jsem se snažil zarezervovat to driftaxi, rozmyslete se kdo se přidáte."
    s "Já určitě chci a můžou jet až 3. Ten systém je teda úplně blbý, tak uvidíme zda mi odepíšou."
    s "Asi bychom se měli nasnídat a vyrazit, máme dneska dlouhý přejezd a večer chceme ten wague steak."
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
    d "Proč by to dělala? Pojďme snídat."
    hide d kjoto
    "Vyndali jste si tedy jídlo z ledničky a sedli jste si společně ke stolečku, který je typicky nízký musíte si sednou na takové minifutony."
    "Po snídani jste se pobalili, kufry jste naskládali ke dveřím a trošku po sobě poklidili. A vyrazili jste k autu."
    scene bg kjoto ulice
    "Řídit bude Sučan."
    menu:
        "Kam si chceš sednout?"
        "Spolujezdec":
            if j.love_points.get(s.name, 0) > 4:
                "Sučan ti otevře dveře a pustí tě sednout. Mrkne na tebe a mile se usměje."
                "Teprve poté přejde na stranu řidiče."
                "V zádu se rozjela hádka, kvůli tyči z Fuji."
                show a kjoto
                a "Musí ta tyč vážně jet s námi? Tady se nedá sedět."
                hide a kjoto
                show m mask angry
                m "Musí, já si jí pošlu do Čech poštou!"
                hide m mask angry
                show d kjoto
                d "Už, aby to bylo!"
                hide d kjoto
                "Sučan, asi využívá situace, že se kluci věnují tyči a opře se levou rukou o tvou sedačku a přes tebe se nakloní."
                show s kjoto
                s "Promiň, nechal jsem si ve dveřích vodu."
                hide s kjoto
                "Říká zatímco tě v podstatě uzamkl vlastním tělem k sedačce a pravou rukou šátrá ve dveřích."
                "Srdce ti snad přestalo na chvíli bít a i dech si zadržela, tak nějak intuitivně. Úzkost ti sevřela hrdlo a žaludek."
                show s kjoto
                s "Tady je mrška!"
                hide s kjoto
                "Zahlásí za chvíli vítězoslavně a i s lahví se zase narovná na sedačce."
                show m mask angry
                "Ne a ne a ne! Ta tyč tady prostě zůstane a pak se pošle."
                hide m mask angry
                "Ozve se ze zadu a tobě dojde, že vlastně nejste v autě sami."
                "Konečně se můžeš nadechnout, a cítíš jak jsi úplně rudá."
                "Sučan je evidentně pobavený, protože se ti směje zatímco se rovná na sedadle a páše se."
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
                m "Musí, já si jí pošlu do Čech poštou!"
                hide m mask angry
                show d kjoto
                d "Už, aby to bylo!"
                hide d kjoto
                "Rozhovor vzadu utichne a vy vyjedete."
            "Podle vašich zvyklostí, má spolujezdec na starosti navigaci a hudbu."
            "Připojíš tedy mobil k autu, spustíš tedy playlist který jste si připravili před odjezdem."
        "Do zádu":
            if j.hate_points.get(n.name, 0) > 3 and j.love_points.get(a.name, 0) < 4:
                "Adrian si sedl za řidiče Mimoň do středu a na tebe zbylo místo za spolujezdcem."
                "Dante si sedl k Sučanovi dopředu. A nastavuje navigaci a pustí playlist, který jste si připravili před odjezdem."
                "Mimoň napresoval tyč z Fuji mezi vás, takže musíš sedět skrčená."
                j "Nechceš tu tyč opravdu vyhodit? Dost tu překáží."
                show m mask angry
                m "Nikdy, tu si pošlu poštou."
                hide m mask angry
                j "Tak jí pošli co nejdříve, takhle se nedá sedět."
                show m mask angry
                m "Tak až potkáme poštu..."
                hide m mask angry
                "Tímto Mimoň ukončil hovor, nasadil si sluchátka a do pár sekund usnul a chrápe na celé auto."
            else: 
                "Sedla sis za spolujezdce, prostřední místo schytal Adrian a za řidiče si sedl Mimoň."
                "Který narval dřevěnou tyč s Fuji mezi sebe a Adriana. Takže Adrian je zase schoulený uprostřed."
                "Dante si sedl k Sučanovi dopředu. A nastavuje navigaci a pustí playlist, který jste si připravili před odjezdem."
                "A Mimoň to zalomil, takže celou cestu spí."
    scene bg mapanara
    "Cesta do Nary, je relativně krátká, takže po dvou hodinkách jízdy zastavujete na parkovišti."
    scene bg nara jelinci1
    "Po zaparkování, jste všichni vystoupili z auta, park je jen přes silnici."
    "Jen jste přešli na území parku už se k vám, žene stádo jelínků."
    "V parku se nachází několik stanovišť, kde se dají koupit takové speciální oplatky, kterými je povoleno jelínky krmit."
    "Adrian neodolá a hned si balíček asi za 100 yenů koupí."
    "Ve chvíli kdy zaplatí a udělá od stánku asi 10 kroků rozeběhne se k němu. Asi deset jelínků."
    "Jeden jelínek je dokonce tak netrpělivý, že než Adrian rozdělá balíček oplatek, tak Adriana začne okusovat."
    "Adrian začne instinktivně couvat, takže jde Adrian a s ním tlupa jelínků."
    "Když rozdá poslední oplatku, tak Adriana přestanou pronásledovat, rozhlídnou se a běží za dalším potenciálním krmičem."
    "Uprostřed jedné části parčíku jsou stromy, které vrhají stín. A ve stínu spí asi 20 jelínků."
    "Přesunete se tedy tam, a využijete toho, že všichni odpočívají, takže se nechají pohladit a dá se s nimi vyfotit."
    "Focením fotek a selfií strávíte dobrou hodinu a až poté si jdete projít zbytek parku."
    "Do chrámu, se ale stojí fronta a rozhodnete se, že jste už chrámy viděli a před vámi je dlouhá cesta, takže jste chrám zkoukli z venčí."
    "A po chvíli se již vracíte zpět. Kolem stánků se suvenýry."
    "Když přijdete do auta sníte svačiny, které jste si s sebou nakoupili - toasty a káva."
    "Zjistíte, že už je pokročilý čas po poledni, takže už nezbývá čas na Osaku, kterou jste chtěli, taktéž dnes absolvovat."
    "Ale protože, se nechcete svých plánů vzdát úplně, rozhodnete se, že alespoň projedete centrem města."
    "Do auta jste se naskládali ve stejném rozložení jako ráno a Sučan, po zaplacení parkovného s vámi vyjíždí."
    "Adrian i Mimoň během pár minut usnou a i tebe jízda ukolíbá."
    "Vzbudí tě až to, že v Osace popojíždíte v koloně, navigace stále hlásí ať odbočíte vpravo, ačkoliv na všech křižovatkách je zákaz odbočení v pravo."
    "Po chvíli pochopíte, že si navigace myslí, že se nacházíte na jiné silnici, protože silnice v Osace je tříúrovňová."
    "Vy jste na pozemní komunikaci, je nad vámi vede okruh osakou a nad ním ještě dálnice."
    "Popojíždíte kolonou, Sučan musí být stále ve střehu, protože auta přejíždějí z pruhu do pruhu, sem tam někdo na poslední chvíli zastaví."
    "Do toho navigace hlásí kraviny, takže si nejste jistí, že jedete správně."
    "Asi po hodině a půl jste konečně projeli, centrem a situace se se malinko uklidnila."
    if j.driver:
        "Sučan po chvíli, odbočí z hlavní a zastaví na takovém vyasfaltovaném plácku."
        show s kjoto
        s "Potřebuju vystřídat, bylo to náročnější než jsem čekal."
        hide s kjoto
        j "Jo jasně, já to dořídím."
        "Sučan zatím vylezl z auta a jde si protáhnout nohy. Ty si zatím přendáš svoje věci na místo řidiče."
        "I zbytek posádky, si jde trošku protáhnout nohy."
        show d kjoto
        d "Hmm... tak jsme toho moc neviděli, jsme asi klidně mohli po té dálnici horem."
        hide d kjoto
        show a kjoto
        a "Ale tak zase jsme ušetřili, za poplatky za dálnici."
        hide a kjoto
        show d kjoto
        d "No, zase jsme spálili víc nafty a podívej se na Sučana, jak ho to vyšťavilo."
        hide d kjoto
        "Sučan se za chvíli vrací, vy se naskládáte do auta a vyrážíte směr Kóbe."
    else:
        show s kjoto
        "Kdyby mě měl kdo vystřídat, nebránil bych se. Naštěstí je to do Kóbe už jen kousek."
    scene bg mapakobe
    "Ani ne za hodinku už jste v Kóbe. Do Kobe jste si naplánovali 4* hotel. Protože večer plánujete wague-steak."
    "Takže i podle toho jste si zvolili hotel."
    "Hotel jste trefili na první dobrou a autem jste zajeli přímo ke vchodu."
    "Vysypali jste se z auta a už vás u dveří odchytil Japonec s vozíčkem, kam jste naskládali kufry."
    "Sučan dostal lísteček s tím kam má zaparkovat auto, takže s Dantem odjeli auto zaparkovat."
    "Ty, Adrian a Mimoň jste zatím šli čekat do hotelu."
    "Rozhodně, ale do interiéru a dresscodu nezapadáte, hotel je plný businessmanů a dam v kostýmcích."
    "A vy na sobě máte normální oblečení, jste splavený z cesty a Mimoň má dokonce svou liščí masku."
    "Naštěstí za chvíli přichází Sučan s Dante, Sučanovi jste dali své pasy a on zamířil s Adrianem na recepci."
    "Za chvíli mají vyřešeno a vás se ujme Japonka, která naznačuje že vás odvede na pokoj a začala tlačit vozejček k výtahům."
    "Vyjeli jste do šestého patra, zde jste vystoupili a následovali japonku do chodby."
    "U jednoho pokoje se zastavila odemkla kartou, naznačila že tam máte jít, japonsky pak něco řekla, pravděpodobně k vybavení pokoje."
    "Pak otevřela další dva pokoje vedle a sundala zavazadla z vozíčku."
    "Poděkovali jste jí 'arigató', ona se usmala uklonila se a s vozíčkem zamířila zpět k výtahům."
    "Vzala sis tedy svá zavazadla a zamířila do pokoje, který podle papírů má být tvůj."
    "Adrian s Dantem, pak zabrali další a Sučan si vytáhl kratkou sirku a dostal k sobě Mimoně."
    "Ještě než jste se v pokojích zabouchli, tak jste se domluvili, že se sejdete tak za cca hodinku a půl v 18:30 a vyrazíte do města na večeři."
    "A že se oblíknete slušně, když jste v takovém honosném hotelu a jdete na tak drahé jídlo."
    "Zalezeš tedy do pokoje, odložíš si vstupní kartu na vstupní pultík, dáš si kufr do pokoje a vyndáš si věci na převlečení."
    "A přesuneš se do koupelny, je krásná prostorná, laděná do mramoru a zlata."
    "Užiješ si koupel ve vaně a umyješ si vlasy. Jako všechny hotely v japonsku koupelna obsahuje mýdla, šampón, kondicioner, koupací čepici, gumičky, hřeben, holítko, fén a mnoho dalšího."
    "Vlasy si vyfénuješ, učešeš se, nalíčíš a vezmeš si na sebe společenskejší oblečení."
    "Zkontroluješ zprávy a zjistíš, že kluci dohadují místo pro večeři. Podle všech recenzí na internetu, je ale do všech restaurací nutná rezervace, minimálně den předem."
    "To tě trošku znervózní, ale tak při nejhorším se jen projdete a koupíte večeři v kombini."
    "Napíšeš domů, že jsi v pořádku a jak se máte."
    "A mezitím ti přijde soukromá zpráva od Sučana"
    s "Neuvěříš! Mimoň si chce tady nechat vyprat. Cena podle ceníku je 600 yenů za kus. :D"
    "Za tu cenu se dá vyprat v japonsku celá pračka prádla..."
    j "Rozmluv mu to, je to blbost."
    s "Pracuju na tom."
    "Zkoukneš ještě sociální sítě. A už je pomalu čas vyrazit."
    "Sbalíš si věci doladíš, účes a jdeš čekat na chodbu."
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
    "Výtahem sjedete tedy dolů, vyrazíte směr metro. Protože do centra to jsou asi 4 km."
    











