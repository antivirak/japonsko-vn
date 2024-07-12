label akt3:
    scene bg hoteltokio
    "Druhý den ráno jste zase měli sraz na osmou hodinu u recepce."
    "A i tentokrát se vedení ujal Dante."
    scene bg tokio1 day1
    "Stejně jako předchozí den jste vyrazili pěšky na metro."
    scene bg 7eleven
    "Po cestě jste si koupili pití a svačinku."
    scene bg metro
    "Adrian došel koupit 5 celodenních lístků. A vyrazili jste ke svatyni Senso-ji."
    scene bg senso_ji0
    "Senso-ji je starodávný budhistický chrám v Asakuse."
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
    "A protože je čas obědu a Mimoň stále otravuje se suši, rozhodli jste se mu vyjít vstříc."
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
    "Mimoň chvíli zkoumá svoji porci, zatímco vy se sborovým Itadakimas začínáte ochutnávat první kousky."  # TODO Mimoň si tam přines vlastní hůlky
    show m mask
    m "{\b} A jsem v prdeli, já nejím ryby! {\b}"
    hide m mask
    "Všichni na něj zůstanete nechápavě zírat."
    "Doufáte, že to je pouze vtip."
    "Ale podle toho, že Mimoň ryby začne sundávat."
    "Začnete všichni jíst, ryby od Mimoně si rozdělí kluci mezi sebe."
    "Po obědě vyrazíte si Šibuju přejít a šáhnout si na psa pro štěstí."
    "Ze Šibuji se metrem přesouváte na Šinziku na křižovatku vyhlášenou velkou obrazovkou s Kočičkou."
    "Zde vyčkáte asi dva reklamní bloky (15cti minutové) abyste viděli alespoň dva celé spoty s kočičkou."
    "Poté se si jdete do vedlejší ulice vyfotit obchodní centrum s godzilou."
    "A protože, Mimonň toho moc nesnědl začne otravovat, že má hlad."
    show m mask
    "Mekáč!"
    hide m mask
    "Protože jste toho už dost nachodili, tak i vám vyhládlo, takže přistoupíte na to, že je čas jídla."
    "Adrian našel nějaké doporučení na restauraci na nagi ramen - rybičkový rámen"
        menu: 
            "Půjdeš s Mimoněm do mekáče? Nebo s klukama na nagi rámen?"
            "Mekáč":
                "Takže protože, Mimoň za žádnou cenu nemůže jít sám, a nebo prostě nemáš chuť na rybičkový rámen."
                "Zůstal ti na ktrku Mimoň"
                "Adrian ti ještě předá přenosnou wifi, abyste si pak mohli napsat, kde se sejdete a oddělí se odvás."
                "Mimoň stále otravuje s Mekáčem."
                "Bohužel ten co najdete, je strašně plný a navíc nemá samoobsužné objednávkové půltíky. A protože pospícháte, a vysvětlování v angličtině, co chcete je horor, jak pro vás, tak pro prodavače."
                "Tak přemluvíš Mimoně, že půjdete do vedlejšího KFC, kde je méně lidí a je vidět, že má samoobjednávkový pult pro objednání v angličtině."
                "Nakonec Mimoň i když neochotně souhlasí, objednávku udělate společně a ty zaplatíš."
                "Když Mimoň dostane své hranolky a masové nugetky, tak přestane být tak protivný a je s ním i řeč."
                "Po tom co dojíte, tak Mimoň chce do gamecentra, které jste po cestě potkali."
                "Takže se přesunete do gamecentra a klukům napíšeš, že jste tam."
            "Rámen":
                show m mask
                m "Já ale nechci jít sám! Někdo se mnou musí jít!"
                m "Sám nikam nejdu!"
                hide m mask
                show s neutral
                s "Nekřič, koukají se na nás."
                s "Tak já s tebou půjdu."
                hide s neutral
                "Sučan tedy odchází s naštvaným Mimoněm a vy vyrážíte na rámen."
                "Takže jdeš s Adrianem a Dantem."
                "Nejdříve vás Adrian na místo, kde měl rámen být, bohužel pobočka je zavřená."
                "Ale nezoufáte během chvíle má Adrian náhradu."
                "Adrian vás provede malými uličkami, až k takovým zapadlým dveřím."
                "Vlezete dovnitř a po úzkém schodišti, smrdí to tam rybinou."
                "U vstupu stojí objednávkový automat."
                if j.love_points.get(a.name, 0) > 2:
                    show a neutral
                    "Adrian se na tebe usměje."
                    a "Pomůžu ti."
                    "Pomocí Adriana a mobilního překladače, si obejdnáš rámen podle své představy."
                    "Zaplatíš a přesuneš se na 'bar', vyvýšený stůl oddělující místnost od koutu s kuchyní."   
                else:
                    "Pomocí překladače v mobilu si objedáš co chceš"        
                if j.love_points.get(d.name, 0) > 2:
                    "Adrian si sedne z jedné strany a Dante z druhé."
                    show d black at left
                    show a neutrar at right
                    "Takže jsi obklopena oběma muži."
                    "Předáš lísteček s objednávkou obsluze."
                    "To samé udělají i Dante s Adrianem"
                    "Začnete si spolu povídat, lépe řečeno konverzaci otevře Adrian."
                    a "Tak já vám nevím, ale já jsem asi v prdeli já nejím rámen."
                    "To vás všechny rozesměje a násdledná konverzace plyne sama od sebe."
                    "Během toho dostanete rámen, se sborovým Arigantó, jej převezmete a pustíte se do jídla."
                    "Na to jak zapadlý podnik a na první pohled pochybný to je, rámen je výborný."
                else:  
                    show a neutral at center
                    show d black at right  
                    "Adrian si sedne vedle tebe a Dante až vedle něj."
                    "Adrian se na tebe moc mile usmívá."
                    "Předáš lísteček s objednávkou obsluze."
                    "To samé udělají i Dante s Adrianem"
                    "Najednou Adrianovi zasvítí oči a zahlásí"
                    a "Tak já vám nevím, ale já jsem asi v prdeli já nejím rámen."
                    "To tě odrovná. A začneš se smát."
                    j "Tak hlavně, že aspoň ty ryby jíš, když je to rybí rámen."
                    a "No vlastně ne."
                    "To už se směješ tak, že skoro brečíš, protože se snažíš, nesmát se nahlas, neb je to v Japonku neslušné."
                "Během toho dostanete rámen, se sborovým Arigantó, jej převezmete a pustíte se do jídla."
                "Na to jak zapadlý podnik a na první pohled pochybný to je, rámen je výborný."
                "Dojíte, poděkujete a jdete hledat druhou část skupiny."
                "Od Sučana jste dostali zprávu, že jsou v gamecentru."
    "Když se všichni najdete v gamecentru. Mimoň hraje už asi pátou rytmickou hru. A odmítá odejít."
    #TODO další kolo minihry
    "Asi po hodině se vám podaří Mimoně přesvědčit, že už půjdete."
    "V nižším patře si ještě projdete ufocatchery."
    "Dante se u jednoho zastaví, hodí tam 100 yenů, pomačkal čudlíky a už 'jeřáb' svírá plyšáka s velkou hlavou."
    "A plyšák kupodivu nespadl a dojel až k výdejní díře."
    "Celý automat hraje a bliká."
    "Dante vytahuje plyšáka s velkou hlavou."
    show d plysak
    d "Na vem si ho, já jsem si to chtěl jen zkusit."
    d "Můžeš to brát jako pouťovou růži z papíru."
    hide d plysak
    "Gratulujeme získáváš plyšáka, budeš ho teď muset tahat 3 týdny s sebou :D"
    "Po té jste vyrazili na Tokijskou Eiffelovu věž, Tokia tower, která měří 333 m, takže je o 13 m vyšší než její model Eiffelova věž."
    "Dojeli jste na nejblizší zastávku metra a zbytek cesty došli. Jako všude jinde i zde se stojí dvě fronty, nejdříve fronta na nákup lístků a pak fronta na příslušný výtah."


                


    jump titulky #provizorně

