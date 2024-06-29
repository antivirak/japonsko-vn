label recepce:
    scene bg hoteltokio
    show s neutral at left
    show d black at right
    show a neutral at center
    "Ty, Sučan, Adrian a Dante se seskupíte u recepce."
    hide s neutral
    hide d black
    hide a neutral
    s "Tak jsme asi všichni, vypadá to, že Mimoň nejde, takže IKIMAŠÓ."
    hide s neutral
    hide d black
    hide a neutral
    show m neutral
    "Jen to dořekne, otevřou se dveře výtahu a v nich stojí Mimoň. "
    m "Mám hlad, chci suši!"
    hide m neutral
    show s neutral
    s "No uvidíme, co najdeme, na mapách v okolí toho moc není."
    s "Takže teď jsme opravdu všichni. Takže IKIMAŠÓ!"
    hide s neutral
    "Vylezete před hotel."
    scene bg tokio1 venek
    show a neutral
    a "Tak kam?"
    hide a neutral
    show s neutral
    s "Já bych šel třeba do leva a třeba na něco narazíme."
    hide s neutral
    "Chyvíli tak bezmyšlenkovitě bloudíte."
    show d black
    d "Našel jsem tu za rohem podnik s vysokým hodnocením."
    hide d black
    show a neutral
    a "Já tu jeden také vidím. Ukaž."
    hide a neutral
    "Oba koukají do mobilů."
    "Pak se shodnou, že na obou portálech, je velmi dobře hodnocený jeden podnik."
    "Takže vás tam dovedou."
    "Je to takový malý podnik."
    "Ale rozhodnete se, že už máte hlad a je čas večeře."
    scene bg veceretokio1
    "Takže vlezete dovnitř."
    "Pozdravíte. Ujme se vás jeden z obsluhy."
    "Pokyne vám abyste si sedli ke stolu"
    menu:
        "Půjdte si sednout ke stolu rovnou.":
            "Vstoupila jsi v botech na tatami – bambusové rohože."
            "Získáváš dva GP"
            $ j.gaijin_points += 2
            "[show_all_points()]"
            jump vecere
        "Pořádně se rozhlédnete.":
            "Všimnete si, že jsou vedle stolů úhledně seskládané boty."
            "Stoly stojí na bambusových rohožích."
            "Jentak tak stihnete Mimoně zastavit, aby v botech nešlápl na rohože - tatami."
            "Získáváš HP pro Mimoně."
            $ j.add_hate_points_for_person(m, 1)
            "[show_all_points()]"
            jump vecere

    label vecere:
        "Zujete se, boty vyskládáte na stranu a sednete si."
        "Číšník vám donese jídelní lístky."
        show menicko 
        "Samosebou v japonštině a bez obrázků."
        "Naštěstí se můžete spolehnout na překladače v mobilu."
        "Chvíli vybíráte, když máte vybráno. Tak odložíte jídelní lístek."
        hide menicko
        "Přijde číšník a Adrian objedná."
        "Chvíli konverzujete a už se vám nese jídlo."
        "V syrovém stavu. Položí talíře misky před vás a zapne 'gril' zapuštěný do stolu."
        "Když vidí váš překvapěný výraz, vysype opsah asi tří misek na plotýnku."
        "A pomocí špachtlí před vámi vytvoří okonomiaky, které ještě ozdobí přelitím majonézy a posype tuňákovými vločkami."
        "Poté to rozkrájí pomocí špachtlí na pět dílů."
        "どぞ ('Do zo'). Řekne a odejde ke svému půltíku."
        "Rozdělíte si okonomiaky mezi sebe."
        "Umyjete si ruce, vlhcěnými ručníčky, které jste dostali."
        "Naskládáte na gril maso, brambory a zeleninu."
        "Pomocí hůlek se pustíte do večeře."
        "Mimoň jídlo spíše napichuje, než že by jedl hůlkami."
        "Když dojíte okonomiaky, maso, brambory a zeleninu"
        "Číšník všechno odnese, otře gril a přinese ještě nudle se zeleninou a chobotnicí."
        "I toto jídlo před vámi připraví."
        "どぞ ('Do zo'). Řekne a odejde ke svému půltíku."
        "Když dojíte a dopijete, domluvíte se že zaplatíte všechno najdenou a pak si to rozpočítáte."
        "Zaplatit jde Adrian."
        "Slyšíte asi 10 x arigató z obou stran jak od čístníka, tak od Adriana."
        "Sbalíte se obujete a vyjdete ven."
        scene bg tokio1 venek noc
        "Nebyli jste na večeři dlouho, ale přesto se venku už setmělo."
        "Protože jste všichni značně unavený, rozhodnete se zastavit v nějakém kombini pro snídani a pak se vrátit na hotel"
        "Po cetě jedna večerka je, tak do ní zajdete."
        scene bg konbini
        "Koupíš si k snídani lívance plněné vanilkovým krémem, kávu a nějakou ochucenou vodu."
        "Přijdeš k prodavači, věci namarkuje rovnou ti je narovná do tašky."
        "Ukážeš kartu a on pokyne k přístroji s obrazovkou na pultu, zaplatíš a vyjdeš ven."
        scene bg tokio1 venek noc
        "Ostatním to tvá o něco déle."
        "Nakonec se postupně objeví."
        show s neutral at left
        show d black at right
        show a neutral:
            xalign 0.3
            yalign 1.0
        show m neutral:
            xalign 0.6
            yalign 1.0
        s "Máme všechno? Navrhuji, abychom se zítra sešli v osm ráno a vyrazili na poznávačku po Tokiu."
        "Zatím, co řešíte zítřej vyrazíte směr hotel."
        m "Já nikam nechci a v osm stávat nebudu!"
        d "Taky nemusíš, zůstaň na hotelu."
        s "Takže, kdo chce, sraz ráno v osm na recepci. Jo, koukal jsem že hotel má nějaké vlastní lázně."
        s "Plánuju tak za hodinku jít. To bude..."
        "Koukne na mobil na čas."
        s "Tak v půl desáté. Tak kdo se chce přidat, může."
        hide s neutral
        hide d black
        hide a neutral
        hide m neutral
        scene bg hoteltokio
        "Dojdete na hotel a jdete do pokojů."

