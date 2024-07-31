label akt5:
    "Na chodbě před pokoji už všichni čekají až na..."
    "Mimoně. Žádné překvapení, co?"
    "Po chvíli se Sučan na Mimoně dobouchá a můžete tedy vyrazit na snídani."¨
    "Snídaně je v komceptu 'Švédských stolů' v japonském stylu."
    "Takže si můžete vybírat z rýže, rybí polévky, řas, smažených chobotnic a mnoha dalšího. "
    "Ale na své si příjdou i zastánci evropské kuchyně. Jsou zde saláty, vajíčka, slanina, pečivo..."
    if j.love_points.get(d , 0) > 5:
        "Když se zastavíš u nápojů, přitočí se k tobě Adrian, který se rozhlídne, a když usoudí, že ho nikdo neslyší. Začne na tebe mluvit."
        a "Doufám, že jste spolu ještě nespali."
        j "Co?"
        a "[j.name_5p], vím že jsem ten poslední, kdo by ti měl radit, ale drž se od Danteho dál."
        a "Bere holky jako spotřební zboží, jestli mi rozumíš. Byla by tě škoda."
        "Ještě se rozhlídne, aby se ujistil, že ho nikdo další neslyšel a než stihneš zareagovat, tak se přesune k jinému pultu."
        "Pochopíš, že tímto ukončil debatu. Jak s touto 'akward' informací naložíš je na tobě."
    "Ulovili jste si každý, na co jste měli chuť a zasedli jste ke stolu pro šest."
    "Po včerejšku jste všichni unavení, takže konverzace moc neplyne. Každý se věnujete své snídani."
    "Po snídani se přesunete do pokojů, sraz u auta jste si dali na jedenáctou."
    if j.love_points.get(d, 0) > 5:
        "Chvíli po té co se dostaneš na pokoj slyšíš klepání."
        "Jdeš otevřít a za dveřmi stojí Dante. Usmívá se a v rukách drží složené tvé oblečení."
        d "Tak co Šípková Růženko? Něco jsem ti přinesl."
        j "Děkuji."
        menu:
            "Chceš nějak rozmazávat rozhovor s Adrianem?"
            "Ano":
                j "Prosímtě, u snídaně mi Adrian naznačoval nějaké věci."
                d "Co ti říkal? To je vlastně jedno určitě si vymýšlí."
            "Ne":
                "Vezmeš si věci. Dante se usměje"
                d "Tak v jedenáct u auta."
                "Řekl a rozejde se ke svému pokoji."
    elif j.love_points.get(a, 0) > 5:
        "Přijdeš do pokoje, natáhneš se na postel a slyšíš klepání."
        j "Jdu!"
        "Otevřeš dveře a za dveřmi nervózně přešlapuje Adrian."
        "Přes rameno tvojí pláťenou tašku."
        a "Nesu ti to oblečení. Je to vyprané a usušené."
    elif j.love_points.get(s, 0) > 5:
        "Než stihneš zabouchnout dveře, tak ti Sučan strčí do dveří nohu."
        s "Tak co ještě se zlobíš? Nezabouchávej, přinesu ti ty věci."
        "Zajde do pokoje naproti a vrací se s tvou plátěnou taškou."
    else:
"Pobalíš si věci, natáhneš se na posteli a ještě chvíli odpočíváš."
""


     
    return