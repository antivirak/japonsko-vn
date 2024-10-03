label akt8:
    scene hotel kjoto
    "Dneska vás čeká přejezd do Kóbe, ale po cestě jste se rozhodli, že si zajedete do Nary"
    "Park v Naře je vyhlášený volně pobíhajícími jelínky, branami a svatyněmi."
    "Ráno jste společně vstáli, pobalili jste se. Mimoň jako vždy vstal prdelí napřed - jak se někdy říká."
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
    s "Já určitě chci a můžou jet až 3. Ten systém je teda uplně blbý, tak uvidíme zda mi odepíšou."
    s "Asi bychom se měli nasnídat a vyrazit, máme dneska dlouhý přejezd a večer chceme ten wague steak - luxusní hovezí maso, které je charakteristické svým tukovým mramorováním. Tito býčci jsou pravidelně masýrování a je jim dopřávána jen ta nejkvalitnější péče."
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
    scene kjoto ulice
    "Řídit bude Sučan."
    menu:
        "Kam si chceš sednout?"
        "Spolujezdec":
            if j.love_points.get(s.name, 0) > 4:
                "Sučan ti otevře dveře a pustí tě sednout."
            else:
                "Sedneš si na místo spolujezdce."
            "Podle vašich zvyklostí, má spolujezdec na starosti navigaci a hudbu."
            "Připojíš tedy mobil k autu, spustíš tedy playlist který jste si připravili před odjezdem."
            
        "Do zádu":
            if j.hate_points.get(n.name, 0) > 3 and j.love_points.get(a.name, 0) < 4:
                "Adrian si sedl za řidiče Mimoň dostředu a na tebe zbylo místo za spolujezdcem."
                "Dante si sedl k Sučanovi dopředu. A nastavuje navigaci a pustí playlist, který jste si připravili před odjezdem."
                "Mimoň napresoval tyč z Fuji mezi vás, takže musíš sedět zkrčená."
                j "Nechceš tu tyč opravdu vyhodit? Dost tu překáží."
                show m mask angry
                m "Nikdy, tu si pošlu poštou."
                hide m mask angry
                j "Tak jí pošli co nejdříve, takhle se nedá sedět."
            else: 
                "Sedla sis za spolujezdce, prostřední místo schytal Adrian a za řidiče si sedl Mimoň."
                "Který"






