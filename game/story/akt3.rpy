label akt3:
    scene bg hoteltokio
    "Druhý den ráno jste zase měli sraz na osmou hodinu u recepce."
    "A i tentokrát se vedení ujal Dante."
    scene bg tokio1 day1
    "Stejně jako předchozí den jste vyrazili pěšky na metro."
    scene bg 7eleven
    "Po cestě jste si koupili pití a svačinku."
    scene bg metro
    "Adrian došel koupit 5 celodenních lístků. A vyrazili jste ke svatyni Sensódži."
    scene bg senso_ji0
    "Sensódži je starodávný budhistický chrám v Asakuse."
    "Jde o jednu z ikonických památek Tokia, kterou ročně navštíví přes 30 miliónů lidí."
    scene bg senso_ji1
    "Svatyně byla zničena během druhé světové války při bombovém útoku na Tokio."
    scene bg senso_ji2
    "Svatyni začali rekonstruovat asi 6 let po útoku a pracovali na ní celých 7 let."
    "Svatyně je pro Japonce symbolem míru."
    scene bg senso_jitrziste
    "Hlavní vstup ke svatyni je lemován stánky."
    "Rozhodli jste se projít si tuto uličku."
    scene bg senso_jitrziste2
    "Avšak toto místo je opravdu velmi populární, takže jste se museli vmísit do davu."
    "Pomalu procházíte a kocháte se suvenýry a náboženskými předměty, když tu si všimneš, že s vámi není Mimoň."
    j "Kde je Mimoň?"
    show s neutral
    s "Nevím, teď tu byl."
    hide s neutral
    show a neutral
    a "Jo, zrovna před chvílí remcal, že je tu moc lidí."
    hide a neutral
    show d black
    d "Pojďte někam, kde můžete počkat, a já ho najdu."
    hide d neutral
    "Došli jste tedy na křižovatku, kde bylo trochu volněji a Dante odešel."
    scene bg senso_jimaska
    "Za chvíli se vrací s Mimoněm, který má na sobě nasazenou liščí masku a úsměv od ucha k uchu."
    show m mask at left
    show d black at right
    d "Kupoval si jen masku, byl támhle za rohem."
    hide m mask
    hide d black
    "Když jste zase všichni, oddechnete si a jdete si koupit zmrzlinu,"
    scene bg senso_jiicecream
    "kterou si musíte sníst v boční uličce. Protože v Japonsku je neslušné chodit s jídlem. A ani chůze se zmrzlinou není přijatelná."
    scene bg metro
    "Pak jste se přesunuli na Šibuju, na jednu z největších křižovatek v Tokiu, co do počtu chodců, kteří ji denně používají."
    scene bg sibuja
    "A protože je čas oběda a Mimoň stále otravuje se suši, rozhodli jste se mu vyjít vstříc."
    "V obchodním centru jste našli suši restauraci."
    scene bg susirestaurace
    "Chvíli jste procházeli meníčko a nakonec jste se rozhodli, že si každý objednáte ochutnávkové menu."
    "Pak jste se chvíli bavili vláčkem, který rozvážel přídavky k jednotlivým stolům."
    "Když tu si Dante všimne, že Mimoň vytáhl svoje hůlky, které si dopoledne koupil spolu s maskou."
    show d black
    d "Nebudeš tady s nimi jíst, že ne?"
    hide d black
    show m mask
    m "Proč ne?"
    hide m mask
    show d black
    d "Copak si do hospody nosíš vlastní příbor?"
    hide d black
    "A během pár minut se vám vaše menu nese. Nejsou to typické 'maki' suši rolky tak, jak je znáte z Česka."
    scene bg susi
    "Jde o Tokijské 'nigiri' suši. Na hromádce rýže je plátek syrové ryby."
    "Číšník postaví před vás tácy."
    "Mimoň chvíli zkoumá svoji porci, zatímco vy se sborovým Itadakimas začínáte ochutnávat první kousky."
    show m mask udiv
    m "{\b} A jsem v prdeli, já nejím ryby! {\b}"
    hide m mask udiv
    "Všichni na něj zůstanete nechápavě zírat."
    "Doufáte, že to je pouze vtip."
    "Ale asi není, podle toho, že Mimoň začne ryby sundávat."
    "Začnete všichni jíst, ryby od Mimoně si rozdělí kluci mezi sebe."
    scene bg sibuja
    "Po obědě vyrazíte přejít Šibuju a šáhnout si na psa pro štěstí."
    scene bg metro
    "Ze Šibuji se metrem přesouváte na Šindžuku, křižovatku vyhlášenou velkou obrazovkou s kočičkou."
    scene bg sindzuku
    "Zde vyčkáte asi dva reklamní bloky (15minutové), abyste viděli alespoň dva celé spoty s kočičkou."
    scene bg godzila
    "Poté se si jdete do vedlejší ulice vyfotit obchodní centrum s godzilou."
    "A protože Mimoň toho moc nesnědl, začne otravovat, že má hlad."
    show m mask
    "Mekáč!"
    hide m mask
    "Protože jste toho už dost nachodili, tak i vám vyhládlo, takže přistoupíte na to, že je čas jídla."
    "Adrian našel nějaké doporučení na restauraci na nagi ramen – s ančovičkami"
    menu: 
        "Půjdeš s Mimoněm do mekáče? Nebo s ostatními na nagi rámen?"
        "Mekáč":
            "Protože Mimoň za žádnou cenu nemůže jít sám, nebo prostě nemáš chuť na rybičkový rámen,"
            "zůstal ti na krku Mimoň."
            "Adrian ti ještě předá přenosnou wifi, abyste si pak mohli napsat, kde se sejdete, a oddělí se od vás."
            "Mimoň stále otravuje s Mekáčem."
            "Bohužel, ten, co najdete, je strašně plný, a navíc nemá samoobslužné objednávkové pultíky. A protože pospícháte, a objednávání v angličtině je horor jak pro vás, tak pro prodavače,"
            "přemluvíš Mimoně, že půjdete do vedlejšího KFC. Tam je méně lidí a je vidět, že má samoobslužný pult pro objednání v angličtině."
            "Nakonec Mimoň (i když neochotně) souhlasí, objednávku uděláte společně a ty zaplatíš."
            "Když Mimoň dostane své hranolky a masové nugetky, tak přestane být tak protivný a je s ním i řeč."
            "Po tom, co dojíte, tak Mimoň chce do gamecentra, které jste po cestě potkali."
            "Takže se přesunete do gamecentra a klukům napíšeš, že jste tam."
        "Ramen":
            show m mask angry
            m "Já ale nechci jít sám! Někdo se mnou musí jít!"
            m "Sám nikam nejdu!"
            hide m mask angry
            show s neutral
            s "Nekřič, koukají na nás lidi."
            s "Tak já s tebou půjdu."
            hide s neutral
            "Sučan tedy odchází s naštvaným Mimoněm a vy vyrážíte na rámen."
            "Jdete tedy ve třech, s Adrianem a Dantem."
            "Nejdříve vás Adrian dovede na místo, kde měl rámen být. Pobočka je však bohužel zavřená."
            "Ale nezoufáte a během chvíle má Adrian náhradu."
            "Procházíte malými uličkami, až k takovým zapadlým dveřím."
            "Vlezete dovnitř po úzkém schodišti, do nosu váš udeří odér rybí polévky."
            scene bg nagi
            "Na konci schodiště visí na zdi objednávkový automat."
            if j.love_points.get(a.name, 0) > 2:
                show a neutral
                "Adrian se na tebe usměje."
                a "Pomůžu ti."
                "S pomocí Adriana a mobilního překladače si objednáš ramen podle své představy."
                "Zaplatíš a přesuneš se na 'bar', vyvýšený stůl rozdělující místnost do kuchyňské a jídelní části."   
            else:
                "Pomocí překladače v mobilu si objednáš, co chceš"
            "Z automatu vyjede vytištěný lísteček s objednávkou."       
            if j.love_points.get(d.name, 0) > 2:
                "Adrian si sedne z jedné strany a Dante z druhé."
                show d black at left
                show a neutral at right
                "Takže jsi obklopena oběma muži."
                "Předáš lísteček s objednávkou obsluze."
                "To samé udělají i Dante s Adrianem"
                "Začnete si spolu povídat; lépe řečeno konverzaci otevře Adrian."
                a "Tak já vám nevím, ale já jsem v prdeli já nejím rámen."
                "To vás všechny rozesměje a následná konverzace plyne sama od sebe."
            else:  
                show a neutral at center
                show d black at right  
                "Adrian si sedne vedle tebe a Dante až vedle něj."
                "Adrian se na tebe moc mile usmívá."
                "Předáš lísteček s objednávkou obsluze."
                "To samé udělají i Dante s Adrianem"
                "Najednou Adrianovi zasvítí oči a zahlásí"
                a "Tak já vám nevím, ale já jsem v prdeli já nejím rámen."
                "To tě odrovná. A začneš se smát."
                j "Tak hlavně, že aspoň ty ryby jíš, když je to rybí rámen."
                a "No, vlastně ne."
                "To už se směješ tak, že skoro brečíš, protože se snažíš nesmát se nahlas, neb je to v Japonku neslušné."
            "Během toho dostanete ramen, se sborovým Arigató jej převezmete a pustíte se do jídla."
            "Na to, jak zapadlý a na první pohled pochybný podnik to je, se během vašeho pobytu v podniku vystřídá dost Japonců."
            "Čemuž ale vůbec nerozumíte, rámen je z ančoviček nebo čeho, takže je dost slaný a cítit rybinou."
            "Dojíte, poděkujete a jdete hledat druhou část skupiny."
            "Od Sučana jste dostali zprávu, že jsou v gamecentru."
    scene bg plysak
    "Všichni se sejdete v gamecentru. Mimoň hraje už asi pátou rytmickou hru a odmítá odejít."
    # TODO další kolo minihry
    "Asi po hodině se vám podaří Mimoně přesvědčit, že už půjdete."
    "V nižším patře si ještě projdete ufocatchery."
    # TODO ufo catcher minigame
    "Dante se u jednoho zastaví, hodí tam 100 yenů, pomačká čudlíky a 'jeřáb' už svírá plyšáka s velkou hlavou."
    "A plyšák kupodivu nespadl a dojel až k výdejnímu otvoru."
    "Celý automat hraje a bliká."
    "Dante vytahuje plyšáka."
    show d plysak at left
    d "Na, vem si ho, já jsem si to chtěl jen zkusit."
    d "Můžeš to brát jako pouťovou růži z papíru."
    hide d plysak
    "Gratulujeme, získáváš plyšáka, budeš ho teď muset tahat 3 týdny s sebou :D"
    scene bg metro
    "Poté jste vyrazili na Tokijskou Eiffelovu věž, Tokio tower, která měří 333 m. Je tedy o 13 m vyšší než její pařížská předloha."
    "Nejbližší stanice metra je na jedné z linek, na které neplatí vaše celodenní jízdenky."
    scene bg tokiotower
    "Dojeli jste na nejbližší možnou zastávku metra a zbytek cesty došli. Jako všude jinde, i zde se stojí dvě fronty. Nejdříve fronta na nákup lístků, a pak fronta na příslušný výtah."
    "Vyjedete nahoru a můžete si užívat výhled na noční Tokio."
    "Tohle je poslední zastávka dnešního dne."
    scene bg metro
    "Vyrazíte zpátky metrem do hotelu a po cestě se zastavíte ještě v 7eleven."
    scene bg 7eleven
    "Potřebujete si udělat nákup na zítřejší výstup na Fuji."
    "Zatímco nakupujete, všimnete si, že si Mimoň plánuje koupit pouze půllitrovku coly."
    "Přitom si musíte nakoupit jídlo a pití na celý den, na Fuji si jídlo nekoupíte."
    j "Mimoňi, půllitrovka coly ti na výstup na Fuji stačit nebude, vem si aspoň dvojlitrovku vody k tomu."
    j "A nějaké jídlo; tam asi nebude možnost si něco koupit."
    j "Takže si musíš něco koupit na snídani, oběd i večeři."
    show m mask angry
    m "Nechci! Nebudu. Nevím co si mám koupit! Kup to!"
    hide m mask angry
    "Tohle tě naštve."
    j "Tak dost, já nejsem tvoje matka nebo sestra, abych se o tebe starala. Jsi dospělý. Dávám ti jen radu, zařiď se podle toho sám!"
    "A jdeš si sama najít jídlo a pití na další den."
    "S nákupem vyrazíte na hotel."
    scene bg tokio1 venek noc
    show s neutral
    s "Tak výstup nahoru a dolů trvá asi 10 h, my tam pojedeme necelé dvě hodiny. Jel bych tak, abychom v osm byli na parkovišti u páté stanice Fujinomiya trail."
    s "Takže sraz v šest ráno na recepci."
    s "Souhlas?"
    hide s neutral
    "Všichni souhlasíte až na..."
    show m mask angry
    m "Tak brzo vstávat nebudu! Nikam nejedu."
    hide m mask angry
    show d black
    d "Tak s námi nejezdi, zaplať si tu hotel na 3 týdny, letenky máš. Nikdo tě nenutí s námi absolvovat 3 týdenní poznávací zájezd. Jen jsi to mohl říct už před odletem, nemuseli jsme rezervovat ty další hotely."
    hide d black
    show m mask angry
    "Já sám nebudu!!! Nechci!!"
    hide m mask angry
    show s neutral
    s "Tak v tom případě buď ráno v šest na recepci."
    hide s neutral
    scene bg hoteltokio
    "Dojdete na hotel a rozejdete se do svých pokojů."




    return
