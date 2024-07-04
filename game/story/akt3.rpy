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
    "A během pár minut se vám vaše menu nese. Nejsou to typické 'maki' suši rolky tak, jak je znáte z Česka."
    scene bg susi
    "Jde o Tokijské 'nigiri' suši. Na hromádce rýže je plátek syrové ryby."
    "Číšník postaví před vás tácy."
    "Mimoň chvíli zkoumá svoji porci, zatímco vy se sborovým Itadakimas začínáte ochutnávat první kousky."  # TODO Mimoň si tam přines vlastní hůlky
    show m mask
    m "{\b} A jsem v prdeli, já nejím ryby! {\b}"
    hide m mask

    jump titulky #provizorně

