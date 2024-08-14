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
    scene bg ichiran venek  
    "Dorazíte k pobočce Ichiranu, ale je před vámi dlouhá fronta asi 30 lidí."
    "Avšak jeden z Japonců vám pro urychlení podává meníčko pro zakroužkování správného ramenu na míru."
    call ichiran_selection_minigame_main
    scene bg ichiran venek  # TODO sehnat jeste lepší ichiran
    "Poté, co jste zakroužkovali, jak by váš Ichiran ramen měl vypadat, jste ještě chvíli čekali."
    "Než jste se dostali dovnitř budovy, u vstupu byl automat, kam jste museli zadat, jestli chcete jen ramen nebo například vajíčko navíc."
    "Když jste zaplatili a posunuli se ještě ve frontě, všimli jste si, že do 'jídelny' vedou 4 vstupy."
    show ichiran_led at truecenter
    "A na zdi visí panel s ledkami, které svítí červeně, oranžově a zeleně."
    "Po chvíli přemýšlení dojdete k závěru, že zelená značí volno, červená obsazeno a oranžová úklid stolu."
    "Když se vás Japonec, který usazuje ke stolům, zeptá, kolik vás je."
    show a neutral
    "Adrian hbitě odpoví"
    a "Gonin."
    hide a neutral
    "Číšník se strašně zděsí, ale pomocí rukou, nohou, japonštiny a angličtiny mu vysvětlíte, že je v pořádku, když budete sedět odděleně."
    hide ichiran_led
    scene bg ichiran2
    "Sice se mu tato informace nezamlouvá, ale po chvíli se mu podaří vás všechny usadit do kóje."
    "Obsluha za stěnou vytáhne roletku u vašich míst. Ty jí předáš svoje vyplněné meníčko a lísteček o zaplacení. Poděkují a zase stáhnou roletku."
    "A aby sis ukrátil['a' if j.gender == 'f' else ''] čekání na svůj rámen, tak si ho v minihře vytvoř."
    # Minihra ramencatch
    $ ramencatch_target_amounts = IngredientsMapper.map_ingredients(ichiran_selection_result)
    call ramencatch_start

    label ramencatch_won:
        return
