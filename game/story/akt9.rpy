label akt9:
    "Po vydařeném večeru jste ráno vstali a pobalili jste si věci, pokoj jste měli opustit do desíti."
    "Protože vás čeká přejezdový den a víte, že před devátou nemá v Japonsku smysl chodit na jakékoliv památky,"
    "tak jste se domluvili, že sraz u recepce bude tentokrát až v devět, abyste u hradu Himedži byli přibližně na desátou."
    "Poté, co jste se sešli u recepce, zavelel Sučan s velkým elánem 'Ikimašó' a vyrazili jste k autu."
    if j.driver:
        menu:
            "Chceš dneska řídit?"
            "Ano":
                "Protože hodně řídí Sučan, nabídneš se, že dneska budeš řídit ty."
                "Měl by vás dnes čekat menší přejezd. Konečně mimo větší města."
                "Sučan si sedl na místo spolujezdce, aby obstaral navigaci, playlist a občerstvení."
                scene bg mapahimedzi
                "Bez větších obtíží parkujete na parkovišti k Himedži hradu."
            "Ne":
                "Ačkoliv větší část cesty řídil Sučan, rozhodla jsi se, že si ještě chvíli odpočineš."
                "Na severu vás čekají dva dlouhé přejezdy. Takže si ještě zařídíš dostatečně."
                "Pustila jsi tedy Sučana na místo řidiče a sama sis sedla na čestné místo spolujezdce."
                "Kluci vzadu se kroutí s Mimoněm a jeho pitomou tyčí – žádné překvápko."
                "Jako vždy je tvým úkolem, obstarat navigaci, playlist a občerstvení pro Sučana."
                scene bg mapahimedzi
                "Cesta naštěstí rychle uteče a bez obtíží parkujete na parkovišti u hradu Himedži."
    else: 
        "Sučan, si sedne za volant, ty na místo spolujezdce."
        "A pánové s dřevěnou tyčí z Fuji se kroutí vzadu."
        "Jako vždy je tvým úkolem, obstarat navigaci, playlist a občerstvení pro Sučana."
        scene bg mapahimedzi
        "Cesta naštěstí rychle uteče a parkuje na parkovišti u hradu Himedži."
    "Himedži castle, neboli Himedži hrad jste zvolili, protože je jeden s nejstarších dochovaných hradů v Japonsku."
    "V Japonsku je hradů velké množství, ale protože jsou převážně dřevěné, tak během let lehly popelem a jsou jen rekonstruovány."
    "U vstupu jste za pomoci Adriana koupili pět lístků a prošli turniketem."
    "Dle očekávání je hrad na kopci. Takže se táhnete po cestičce a schodech směrem vzhůru."
    "U vstupu jsou lavičky a igelitové sáčky."
    menu:
        "Proč si myslíš, že tomu tak je?"
        "a) Do hradu je zakázáno nosit vodu a jídlo. Takže máte obsah batohů vyprázdnit do sáčků.":
            "Špatně, v hradě se sice jíst nesmí, ale jídlo v uzavřené tašce nikomu nevadí a čistou vodu naopak hlídači doporučují."
            $ j.increment_gaijin_points(1)
        "b) Do hradu se nesmí v botách. Do igelitek máte umístit obuv.":
            "Správně, igelitové sáčky jsou myšleny na obuv, kterou si musíte s sebou nést až k východu."
        "c) Igelitku si máte vzít jako sedátko pod sebe, abyste nezašpinili vybavení hradu.":
            "Špatně, z původního vybavení v hradě moc nezůstalo, lavičky je možné normálně využívat. Sáčky jsou na obuv."
            $ j.increment_gaijin_points(2)
        "d) Sáček je určen pro osoby s dlouhými vlasy – mají si jej umístit na hlavu, aby všude nezanechávali vlasy.":
            "Špatně, kdyby tomu tak bylo, měli by Japonci k dispozici spíše koupací čepice, sáčky jsou na obuv."
            $ j.increment_gaijin_points(1)
        "e) Před vstupem do místností hradu, musíte projít kontrolou, do sáčku se má vysypat obsah tašek, aby se hlídači nemuseli hrabat v taškách návštěvníků.":
            "Špatně, kdyby bylo potřeba projít kontrolou stalo by se tak již při vstupu do areálu, navíc hlídači nemají problém nakouknout do zavazadel. Sáčky jsou na obuv."
            $ j.increment_gaijin_points(1)
    "Poté, co se všichni zujete a umístíte obuv do igelitek, které si budete muset vzít s sebou,"
    "protože výlez z hradu je jinde nežli vstup,"
    "se vydáte ve směru šipek na obhlídku hradu. Přístupných je 7 pater."
    "Jsou to převážně prázdné dřevěné místnosti s informačními tabulemi v japonštině, či velmi špatné angličtině."
    "Po cestě najdete držáky na katany, či malý model hradu."
    $ dictionary.add_item("katana", "Japonský meč.")
    "Výhled malými okénky je hezký, ale nepraktický. Je zvláštní, že nimi byl někdo schopný zpozorovat nepřítele."
    "Schodiště jsou úzká, stropy nízké, takže pohyb pro Evropana je značně komplikovaný."
    "Poté, co jste si prošli hrad, jste vyšli na nádvoří, kde jste si mohli udělat společnou fotku s hradem."
    "Uprostřed nádvoří totiž stojí pultík na nastavení chytrých telefonů."
    "Poté jste se přesunuli do blízké budovy, kde je výstava vybavení samurajů,"
    $ dictionary.add_item("samuraj", "Japonský rytíř. Cvičený v boji, ale i ve vystupování.")
    "nějaké povídání o pokladech, kimonech atd."
    $ dictionary.add_item("kimono", "Typické japonské oblečení, připomínající evropský župan.")
    "Poté jste se zahradou přesunuli ještě k hradbám hradu, na rozdíl od evropských je to taková dřevěná řadovka."

    return
