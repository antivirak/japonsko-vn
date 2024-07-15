label akt2:
    scene bg hoteltokio
    "Druhý den ráno se v osm potkáte na recepci. Mimoň má jako vždy asi 10 minut zpoždění."
    "Plán dne má na starosti Dante."
    "Po městě se musíte pohybovat po spolu, protože internet má pouze Sučan a Adrian."
    "Tak abyste si mohli dát vědět. Kdyby se něco dělo."
    scene bg tokio1 day1
    "Vyrazíte pěšky na metro, které je asi 10 minut od hotelu."
    scene bg 7eleven
    "Po cestě se stavíte v 7eleven pro něco k pití a nějakou svačinku."
    scene bg metro
    "V metru jdete k automatům na lístky, kde si plánujete zřídit ‚suiku‘ nebo ‚pasmo‘; něco na styl české lítačky."
    "Podle informací na netu se dá sehnat v automatu v metru. Ale žádný automat, který by vydával karty jste nenašli."
    "Jdete k informačnímu okénku. Tam posíláte Adriana, jako nejvíce zběhlého v japonštině."
    "U okénka se dozvídáte, že kvůli nedostatku čipů lze tyto karty vyzvednout jen na vybraných vlakových nádražích."
    "Ale náhradou vám prodavačka nabídne celodenní lístek na metro. Koupíte jej 5x."
    scene bg akimetro
    "Vaše první cesta směřuje na Akihabaru, do jedné nejvíce barevných čtvrtí Tokia."
    scene bg akihabara2
    "Nejdříve jste zašli do obchodního centra Yodobashi akiba, kde jste prolezli všechna patra."
    scene bg yodobashi elektronika
    "Přes první patro, kde byla různá elektronika."
    scene bg yodobashi elektronika2 
    "Myši, mobily, počítače, powerbanky..."
    scene bg yodobashi starwars
    "Až do třetího patra, kde byla sekce figurek,"
    scene bg yodobashi plysaci
    "hraček, plyšáků, gachaponů i nějakých herních automatů."
    "Ani nevíte jak, ale najednou je čas oběda."
    "Po krátké diskuzi se rozhodnete navštívit Ichiran ramen."
    scene bg akihabara
    "Pobočka je sice asi 3 km od nákupního centra, ale zatím jste dostatečně fresh, takže tam vyrazíte pěšky."
    "Po cestě potkáte nějaké gamecentrum, tak se domluvíte, že se tam zastavíte po cestě zpět."
    scene bg ichiran  # sehnat lepší ichiran z venčí
    "Dorazíte k pobočce Ichiranu, ale je před vámi dlouhá fronta asi 15 lidí."
    "Avšak jeden z Japonců vám pro urychlení podává meníčko pro zakroužkování správného ramenu na míru."
    call ichiran_selection_minigame_main
    scene bg ichiran2 # sehnat lepší ichiran
    "Poté, co jste zakroužkovali, jak by váš Ichiran ramen měl vypadat, jste ještě chvíli čekali."
    "Než jste se dostali dovnitř budovy, u vstupu byl automat, kam jste museli zadat, jestli chcete jen ramen nebo například vajíčko navíc."
    "Když jste zaplatili a posunuli se ještě ve frontě, všimli jste si, že do 'jídelny' vedou 4 vstupy."
    show ichiran_led at truecenter
    "A na zdi visí panel s ledkami, které svítí červeně, oranžově a zeleně."
    "Po chvíli přemýšlení dojdete k závěru, že zelená značí volno, červená obsazeno a oranžová úklid stolu."
    "Když se vás Japonec, který usazuje ke stolům, zeptá, kolik vás je."
    show a neutral
    "Adrian hbitě odpoví"
    a "Go."
    hide a neutral
    "Číšník se strašně zděsí, ale pomocí rukou, nohou, japonštiny a angličtiny mu vysvětlíte, že je v pořádku, když budete sedět odděleně."
    hide ichiran_led
    "Sice se mu tato informace nezamlouvá, ale po chvíli se mu podaří vás všechny usadit do kóje."
    "Obsluha za stěnou vytáhne roletku u vašich míst. Ty jí předáš svoje vyplněné meníčko a lísteček o zaplacení. Poděkují a zase stáhnou roletku."
    "A aby sis ukrátil['a' if j.gender == 'f' else ''] čekání na svůj rámen, tak si ho v minihře vytvoř."
    # TODO minihra ichiran
    "Poté, co jsi získal['a' if j.gender == 'f' else ''] svůj rámen, tak si jej rychle snědl['a' if j.gender == 'f' else ''],"
    "aby na tebe ostatní dlouho nečekali."
    "Vylezeš před Ichiran, kde už čekají Adrian, ['Dante' if j.gender == 'f' else 'Hana'] a Sučan. Mimoň je stále uvnitř."
    j "Mimoň tu ještě není?"
    show a neutral
    a "Ne, seděl vedle mě. Myslím, že ještě zápasí s hůlkama."
    hide a neutral
    j "Aha."
    "Čekáte dalších dobrých deset minut, než konečně Mimoň vyleze."
    # TODO bg gamecentrum
    "Když jste všichni pohromadě, vyrazíte do gamecentra."
    "Gamecentrum projdete celé přes ufocatchery, gachapony, rytmické hry a závodní automaty."
    "U rytmických her se zasekne Mimoň a přesvědčuje vás, ať si s ním jdete někdo zahrát."
    menu:
        "Chceš si s Mimoněm zahrát na bubínky?"
        "Jasně!":
            call rhytm_game_main
            # TODO we can have a winner say if player has at least 90 % or something
        "Nemám zájem.":
            "Mimoň se na chvíli zamračí, ale pak se rozhodne, že si zahraje sám."

    scene bg zavodky
    "Sučan zapadne k závodním automatům a rozjíždí velký závod s místními Japonci."
    "Asi po hodině se vám podaří Mimoně a Sučana odtud dostat."
    scene ueno1
    "A vyrážíte do parčíku. Zde narazíte na památníku bojovníků ve válce Ueno, někdy označované jako válka Shogi-tai."
    scene ueno2
    "Bitva zde proběhla roku 1868 v období Meidži."
    scene ueno3
    "V této válce byli na jedné straně konfliktu služebníci, leníci staré vlády Tokugawa a obyvatelé z okolních provincií. Říkali si Shogi-tai."
    scene ueno4
    "Ti čelili armádě nové vlády a tento boj prohráli."
    scene ueno5
    "Okisato Ogawa a jeho společníci, přeživší z Shogi-tai, dostali v roce 1874 povolení"
    scene ueno6
    "od nové vlády Meidži, aby postavili hrobku mrtvým vojákům."
    scene ueno7
    "Od roku 2003 má památné místo na starost Tokio."
    "Zatímco jdete po parčíkové magistrále, Adrian začne nahrávat video do svého blogu o Japonsku."
    "Do naprostého ticha, které ruší jen zvuk cikád, zahlásí."
    show a neutral
    a "Nemaj tady cikány, zato tu jsou cikády."
    hide a neutral
    scene bentendo
    "Parčíkem jste se dostali až k Benten-do svatyni, kterou nechal vystavět na začátku sedmnáctého století Mizunoya Katsutka."
    scene bg metro
    "Dále jste se rozhodli navštívit císařské zahrady, takže se přiblížíte metrem."
    # TODO scene zahrady a park
    "Ale k zahradám přicházíte až v půl sedmé a zahrady mají otevřeno jen do šesti."
    scene bg park
    "Zamířili jste ještě na chvíli do blízkého parčíku, ale už je v podstatě tma."
    scene bg park2
    show d black
    d "Asi bychom se měli stavit někde na jídle."
    hide d black
    show m neutral
    m "Já chci suši!"
    hide m neutral
    show d black
    d "Tak já jsem za to se přiblížit k hotelu metrem a najít něco v okolí."
    hide d black
    scene bg metro
    "Všichni souhlasíte, takže se přiblížíte k hotelu metrem."
    scene bg tokio1 venek noc
    "Na ulici se zeptáte jednoho z Japonců na doporučení suši restaurace nebo nějaké jiné."
    "Nějakou vám doporučil, ale když jste k ní přišli, tak už zavírala. Protože už bylo půl deváté."
    "Po chvíli bloudění jste zjistili, že otevřenou restauraci už asi nenajdete."
    show d neutral
    d "Navrhuji si koupit nějaké hotové jídlo v 7eleven."
    hide d black
    show a neutral
    a "Jsem pro, jsem úplně mrtvej."
    hide a neutral
    show s neutral
    s "Já taky."
    hide s neutral
    show m neutral
    m "Ne! Já chci suši!"
    hide m neutral
    scene bg 7eleven
    "Vyhlídli jste si (na Japonských veřejných prostranstvích poměrně vzácné) lavičky v nějakém vnitrobloku kanceláří a v 7eleven jste si koupili každý svoji 'hotovku'."
    scene bg vecereday2
    "Prodavači vám ji ohřáli, přibalili ubrousky a dali na výběr mezi hůlkami a plastovým příborem."
    "Po jídle jste sesbírali všechen odpad (který se musel vyhodit až na hotelu, venku nejsou koše) a vyrazili jste pěšky na hotel." 
    return
