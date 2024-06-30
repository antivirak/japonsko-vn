label recepce:
    scene bg hoteltokio
    show s neutral at left
    show d black at right
    show a neutral at center
    "Ty, Sučan, Adrian a Dante se seskupíte u recepce."
    hide s neutral
    hide d black
    hide a neutral
    s "Tak jsme asi všichni; vypadá to, že Mimoň nejde, takže IKIMAŠÓ."
    hide s neutral
    hide d black
    hide a neutral
    show m neutral
    "Jen to dořekne, otevřou se dveře výtahu a v nich stojí Mimoň."
    m "Mám hlad, chci suši!"
    hide m neutral
    show s neutral
    s "No uvidíme, co najdeme. Na mapách v okolí toho moc není."
    s "Takže teď jsme opravdu všichni. Takže IKIMAŠÓ!"
    hide s neutral
    "Vylezete před hotel."
    scene bg tokio1 venek
    show a neutral
    a "Tak kam?"
    hide a neutral
    show s neutral
    s "Já bych šel třeba doleva a třeba na něco narazíme."
    hide s neutral
    "Chvíli tak bezmyšlenkovitě bloudíte."
    show d black
    d "Našel jsem tu za rohem podnik s vysokým hodnocením."
    hide d black
    show a neutral
    a "Já tu jeden také vidím. Ukaž."
    hide a neutral
    "Oba koukají do mobilů."
    "Pak se shodnou, že na obou portálech je velmi dobře hodnocený jeden podnik."
    "Takže vás tam dovedou."
    "Je to takový malý podnik."
    "Ale rozhodnete se, že už máte hlad a je čas večeře."
    scene bg veceretokio1
    "Takže vlezete dovnitř."
    "Pozdravíte. Ujme se vás jeden z obsluhy."
    "Pokyne vám, abyste si sedli ke stolu"
    menu:
        "Půjdete si sednout ke stolu rovnou.":
            "Vstoupila jsi v botách na tatami – bambusové rohože."
            "Získáváš dva GP"
            $ j.gaijin_points += 2
            "[show_all_points()]"
            jump vecere
        "Pořádně se rozhlédnete.":
            "Všimnete si, že jsou vedle stolů úhledně seskládané boty."
            "Stoly stojí na bambusových rohožích."
            "Jen tak tak stihnete Mimoně zastavit, aby v botách nešlápl na rohože – tatami."
            "Získáváš HP pro Mimoně."
            $ j.add_hate_points_for_person(m, 1)
            "[j.show_all_points()]"
            jump vecere

label vecere:
    "Zujete se, boty vyskládáte na stranu a sednete si."
    "Číšník vám donese jídelní lístky."
    show menicko
    "Samo sebou v japonštině a bez obrázků."
    "Naštěstí se můžete spolehnout na překladače v mobilu."
    "Chvíli vybíráte. Když máte vybráno, tak odložíte jídelní lístek."
    hide menicko
    "Přijde číšník a Adrian objedná."
    "Chvíli konverzujete a už se vám nese jídlo."
    "V syrovém stavu. Obsluha položí talíře a misky před vás a zapne 'gril' zapuštěný do stolu."
    "Když vidí váš překvapený výraz, vysype obsah asi tří misek na plotýnku."
    "A pomocí špachtlí před vámi vytvoří okonomijaki, které ještě ozdobí přelitím majonézy a posype tuňákovými vločkami umeboši."
    "Poté placku rozkrájí pomocí špachtlí na pět dílů."
    $ narrator("どぞ ('Dozo').", what_font="fonts/mikachan.ttf")
    "Řekne a odejde ke svému pultíku."
    "Rozdělíte si okonomijaki mezi sebe."
    "Umyjete si ruce vlhčenými ručníčky, které jste dostali."
    "Naskládáte na gril maso, brambory a zeleninu."
    "Pomocí hůlek se pustíte do večeře."
    "Mimoň jídlo spíše napichuje, než že by jedl hůlkami."
    "Když dojíte okonomijaki, maso, brambory a zeleninu,"
    "číšník všechno odnese, otře gril a přinese ještě nudle se zeleninou a chobotnicí."
    "I toto jídlo před vámi připraví."
    $ narrator("どぞ ('Dozo').", what_font="fonts/mikachan.ttf")
    "Řekne a odejde ke svému pultíku."
    "Když dojíte a dopijete, domluvíte se, že zaplatíte všechno najednou, a pak si to rozpočítáte."
    "Zaplatit jde Adrian."
    "Slyšíte asi 10 x arigató z obou stran; jak od čístníka, tak od Adriana."
    "Sbalíte se obujete a vyjdete ven."
    scene bg tokio1 venek noc
    "Nebyli jste na večeři dlouho, ale přesto se venku už setmělo."
    "Protože jste všichni značně unavení, rozhodnete se zastavit v nějakém kombini pro snídani na další den, a pak se vrátit na hotel"
    "Po cestě je 7eleven, tak do něj zajdete."
    scene bg 7eleven
    "Koupíš si k snídani lívance plněné vanilkovým krémem, kávu a nějakou ochucenou vodu."
    "Přijdeš k prodavači, ten věci namarkuje a rovnou ti je narovná do tašky."
    "Ukážeš kartu a on pokyne k přístroji s obrazovkou na pultu. Zaplatíš a vyjdeš ven."
    scene bg tokio1 venek noc
    "Ostatním to trvá o něco déle."
    "Nakonec se postupně objeví."
    show s neutral at left
    show d black at right
    show a neutral:
        xalign 0.3
        yalign 1.0
    show m neutral:
        xalign 0.6
        yalign 1.0
    s "Máme všechno? Navrhuji, abychom se zítra sešli v osm ráno a vyrazili na poznávačku po Tokiu."
    "Zatím, co řešíte zítřek, vyrazíte směr hotel."
    m "Já nikam nechci a v osm stávat nebudu!"
    d "Taky nemusíš, zůstaň na hotelu."
    s "Takže, kdo chce, sraz ráno v osm na recepci. Jo, koukal jsem, že hotel má nějaké vlastní lázně."
    s "Plánuju tak za hodinku jít. To bude..."
    "Koukne na mobil na čas."
    s "Tak v půl desáté. Tak kdo se chce přidat, může."
    hide s neutral
    hide d black
    hide a neutral
    hide m neutral
    scene bg hoteltokio
    "Dojdete na hotel a jdete do pokojů."
    scene bg hoteltokio
    menu:
        "Chceš jít do hotelového Onsenu?"
        "Ano":
            "Přijdeš na pokoj, odložíš si věci a vyrazíš do hotelových onsenů."
            "Samozřejmě jsou striktně rozděleny na ženské a mužské."
            scene bg onsen
            menu:
                "Půjdeš doleva nebo doprava?"
                "Vlevo":
                    "Správně si zvolila dámský onsen. V místnosti před samotnou lázní se svlékneš donaha a své věci odložíš do jedné z proutěných krabic v regálu u stěny."
                    "Osprchuješ se a vlezeš si do horké lázně. Máš štěstí, nikdo jiný zde není."
                    "Po chvíli se rozhodneš, že je čas jít spát."
                "Vpravo":
                    "Vlezla si do pánské sekce!"
                    "Úchyláku!"
                    "Hra zde končí."
                    jump titulky
        "Ne":
            "Dojdeš si vyčistit zuby, převlíkneš se do pyžama a jdeš spát."
    return
