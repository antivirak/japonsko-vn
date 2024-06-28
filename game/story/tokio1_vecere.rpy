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
            "Vstoupila jsi v botech na bambusové rohože."
            "Získáváš dva GP"
            $ j.gaijin_points += 2
            "[show_all_points()]"
            jump vecere
        "Pořádně se rozhlédnete.":
            "Všimnete si, že jsou vedle stolů úhledně seskládané boty."
            "Stoly stojí na bambusových rohožích."
            "Jentak tak stihnete Mimoně zastavit, aby v botech nešlápl na narohože."
    label vecere
        "Zujete se, boty vyskládáte na stranu a sednete si."
        "Číšník vám donese jídelní lístky."
        "Samosebou v japonštině a bez obrázků."
        "Naštěstí se můžete spolehnout na překladače v mobilu."
        







    


