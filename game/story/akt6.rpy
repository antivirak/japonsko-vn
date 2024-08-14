label nagora_rano:
    scene bg hotel nagoja
    "Ráno jsi vstala a jste domluvení s Adrianem a Dantem, že si před odjezdem ještě projdete Nagoju."
    "Sučan si zase našel, že je ve městě nejaký obchod s modely aut. Takže vstal dříve a má se k vám připojit."
    "Sbalila sis věci, protože podle plánu, přijdete chvíli před checkoutem si vzít kufry a půjdete k autu."
    scene bg chodba
    "Před pokoji už čeká Adrian a Dante se snaží doklepat na Mimoně."
    "Kupodivu, Mimoň po chvíli otvírá a vypadá připraveně."
    "Vyrážíte tedy pěšky k nagojskému hradu."
    "Po cestě potkáváte nápis Nagoja, tak se u něj na střídačku vyfotíte."
    "U vstupu do hradních zahrad zjistíte, že jsou otevřeny až od devíti, a vy potřebujete do desíti vyklidit pokoje."
    "Proto se rozhodnete, že čekat u vstupu půl hodiny kvůli půlhodinové procházce po zahradách asi nemá smysl."
    "Navíc byste museli zaplatit celodenní vstupné."
    "Takže obejdete část zahrad která je zdarma a setkáte se se Sučanem."
    "Poté se vrátíte na hotel a vyzvednete si kufry odhlásíte se a vyrazíte do garáží k autu."
    "U auta naskládáte věci do auta. Dnes je v plánu přejezd do Kjóta šinkanzenem (japonským rychlovlakem)"
    if j.name = driver:
        "Jste jen dva aktivní řidiči, takže Šinkanzenem může jen jeden z vás."
        menu:
            "Budeš převážet auto, nebo pojedeš šinkanzenem?"
            "Převezu auto.":
                "Vytáhla jsi černého petra, nebo jsi jen moc hodná."
                "Zážitek z rychlovlaku přenecháš klukům a pojedeš autem úplně sama."
                "Převzala sis od Adriana přenosnou wifi, spojila si mobil s autem."
                "Nastavila navigaci a vyjíždíš."
                "Kluci mmezitím šli dolů k parkomatu zaplatit, takže když sjedeš k výjezdu, dostáváš zaplacený lísteček a vydáváš se na cestu."
                "Všichni ti popřejí šťastnou cestu a ty vyrážíš."
                "Provoz není zas tak extrémní a už ti ani nedělají problémy blinkry/stěrače."
                "Ale za chvíli najíždíš na městcký okruh Nagoji (most). A samozřejmě se zde vybírá mýto."
                "Zastavíš u budky, kde sedí japonec."
                "Na ceduli je asi pět cen v závislosti na velikosti auta a denní době."
                "Japonec ti v japonštině sdělí částku."
                "Samozřejmě mu nerozumíš, takže mu podáš 10 000 yenů, spolehlivě je to částka několíkanásobně přesahující všechny možnosti."
                "Japoncovi se pravděpodobně nelíbí, že mu podáváš tak velkou bankovku. Ceny na ceduli se pohybují mezi 700-1200 yenů."
                "Takže ti zopakuje co řekl před chvílí, samozřejmě mu nerozumíš."
                "Tak se jen usměješ a řekneš."
                j "Hai"
                "Což je japonsky Ano, a strčíš mu tu bankovku."
                "Sice ještě něco v japonštine mrmlá, ale pochopil, že mu je to k ničemu a na podnose podává účet a peníze na zpátek."
                "Správně přijmeš tác oběma rukama a peníze si nasypeš do ruky, teda spíše do auta, jak jsi nervozní."
                "Ale máš lísteček, takže můžeš pokračovat."
                "Během chvíle se dostaneš nakonec městckého okruhu, a musíš projet mýtnou bránou aby si najela na placenou dálnici."
                "Vjezd pro 'cash' poznáš na první dobrou od jiného japonce dostaneš kartičku na průjezd."
                "Následuje asi dvou hodinová jízda po dálnici, která jde hladce a bez větších potíží."
                "Po cestě bylo jedno křížení, takže jsi musela u automatu zaplatit lístek který si měla u sebe."
                "To znamená vložit lístek do automatu a nasypat peníze do příslušných přihrádek, automat si to sám spočítal a vrátil ti."
                "Pak si u jiného nájezdu u automatu vyfasovala nový lísteček a s tím ses dostala až do Kjóta."
                "Jenže při sjezdu na Kjóto, ti samozřejmně spadla navigace a cesty se různě větvili, takže jsi skončila na úplně blbé silnici."
                "Musíš tedy řešit jestli někde bude možnost se otočit, navíc to vypadá jako nájezd na další dálnici, takže ti hrozí, že budeš muset zaplatit za další úsek a pravděpodobně 2x."
                "Za cestu tam i zpět. Nakonec se ti jednou rukou podaří navigaci zprovoznit. Zatímco se snažíš udržet na silnici a nikoho neohrozit."
                "Navigace ti naznačuje otočení o 180°, zkontroluješ situaci, silnice v tomto místě není úplně široká, trošku připomíná české okresky."
                "Ale pro japonská úzká auta jsou to regulerní dva pruhy."
                "Vypadá to, že široko daleko nikdo nejede tak to ryskneš a otočíš to do protisměru, teda musíš si při otáčení i trošku couvnout, protože na otočení na jednou na silnici není místo."
                "V průběhu tvého manévru se kupodivu, žádné auto neobjevilo."
                "Až když se rozjíždíš, tak tě jedno auto dohání a předjíždí."
                "Navigace je také spokojná a stáhla tě do Kjóta."
                "Voláš tedy Sučanovi. Kde jsou."
                "Podle plánů mají být v Kjótu dřive jak ty. Protože šinkanzen jezdí asi tak 3x rychleji než auta."
                "Na nádraží v Nagoje to také měli jen půl hodiny a šinkanzen jezdí každou půl hodinu."
                "Strašně dlouho ti to nezvedá."
                "Tak zkoušíš volat Dantemu. Ten to zvedl."
                d "No?"
                j "Jsem v Kjótu, za 15 minut budu na místě."
                d "No my jsme teď koupili lístky na metro a budeme se k ubytování teprve přesouvat."
                j "No to je super, to tam budu asi dřive jak vy, tak snad najdu ubytování."
                d  "Promiň, zdrželi jsme se. Musím, řešit spoje promiň."
                "A položil ti to. Trošku tě to rozčílí, jedeš asi tři hodiny, takže jsi nejedla."
                "Navíc doprava se začíná hodně zhušťovat, takže musíš být pořát ve střehu."
                "Doufala jsi, že si tě u ubytování kluci odchytí a navedou tě kde zaparkovat."
                "Míjíš nádraží, kde je to opravdu překážková jízda, auta, taxíky, autobusy a lidé."
                "Po chvíli se konečně dostaneš na místo určení, takže projíždíš tou ulicí kde máte mít ubytování."
                "Ale vlastně nevíš jak přesně má vypadat a kluky také nevidíš."
                "'Váš cíl je v pravo' zahlásí navigace a vvypne se."
                "Kde? Super... Místo na zaparkování ani na zastavení nikde. Za tebou auta."
                "Jedeš tedy ulicí dál až na nějakou velkou křižovatku a silnici."
                "Odbočíš v pravo, ale zjistíš, že není tak snadné odbočit zase v pravo. Můžeš odbočit až na dalším semaforu, který je asi až o 4 ulice dále než si chtěla."
                "Podařilo se ti odbočit. A ulice je méně frekventovaná, takže jsi na chvíli zastavila na blikačky, znovu zadala navigaci cíl."
                "A napsala klukům, že doufáš, že už tam jsou, že odmítáš kroužit pořád dokola, jako blondýna na kruháči s třicítkou."
                "Rozjedeš se, a za chvíli píše Sučan, že na tebe čekají."
                "Navigace tě donaviguje, v ulici stojí na jedné straně Sučan a Dante a na druhé Adrian a Mimoň."
                "Sučan stojí na té z které jedeš, přibrzdíš tedy a dáš blikačky."
                show s nagoja
                s "Vyházíme tady kufry ať je nemusíme tahat a po cestě jsme viděli volné docela levné parkoviště. Na naviguju tě."
                "Otevře dveře s Dantem vyndají kufry a Sučan si sedne k tobě do auta."
                "A nanaviguje tě na parkoviště, na místo raději zajedeš po zádu."
                "Vezmeš si tašku s osobními věcmi a vyrazíte se Sučanem směr ubytování."
            "Pojedu šinkanzenem.":
                "Vyslovila jsi přání, zkusit si šinkanzen. A Sučan ti nebrání, souhlasí, že auto převeze."
                call sinkanzen
                

    else:
        "Protože jediný aktivní řidič z vaší skupiny je Sučan, tak on bude ten, co převeze auto."
        "A vy si můžete užít zážitek ze šinkanzenu."
        menu:
            "Chceš jet šinkanzenem anebo budeš dělat podporu Sučanovi?"
            "Šinkanzem, přeci si nenechám ujít takovou možnost.":
                call sinkanzen
            "Se Sučanem, ve dvou je ten přejezd lepší, vlak jako vlak.":
                "Rozhodneš se, že v tom Sučana nenecháš samotného."
                "Sučan se mezitím usadil na místo řidiče. A nastavuje si navigaci. Ale ještě si nechal otevřené dveře."
                j "Tak já pojedu s tebou, kdyby něco tak se nám to ve dvou bude lépe řešit."
                j "A myslím, že o tolik jiné než české vlaky to nebude."
                show s nagoja
                s "Jseš si jistá? V Čechách vlaky nejezdí třista. Abys toho nelitovala."
                hide s nagoja
                j "Jo jsem si jistá. Ty by si to pro mě také udělal."
                j "Hele je dobrý jezdit ve dvou, co kdyby i spadla navigace, nebobudeš potřebovat rychle něco přeložit?"
                "Nakloníš se k němu do dveří a tlumeným hlasem mu řekneš."
                j "Navíc asi nechci jet s klukama. Když můžu strávit čas s tebou."
                "Pak už nahlas aby tě ostatní slyšeli dodáš."
                j "Tak já jdu s klukama zaplatit k parkomatu a nastoupím dole."
                "Vyrazíte tedy napřed k parkomatu, po cestě k výtahu slyšíte jak Sučan zabouchl a nastartoval auto."
                "Sjedete dolů, zaplatíte a s lístečkem o zaplacení čekáš na Sučana."
                "Sučan během chvíle přijíždí. Rozloučíte se s ostatními, ty nasedneš a vyrazíte do Kjóta."
                "Když se dostanete z parkoviště na hlavní ulici. Tak se na tebe Sučan otočí."
                show s nagoja
                s "Udělala jsi mi radost."
                hide s nagoja
                j "A čím prosimtě?"
                show s nagoja
                s "Že si mi dala přednost, před žážitkem z rychlovlaku, nebo možná před klukama?"
                hide s nagoja
                j "To je jasné, sice neřídím, ale je mi jasné jak musí být nepříjemné řídit v cizím státě cizí auto a ještě na druhé straně než si zvyklý."
                j "To já bych sama auto odmítla řídit."
                show s nagoja
                s "Tak já takhle neřídím, poprvé vždyť to víš. Klidně si mohla jet."
                s "Ale asi bych pak trošku žárlil."
                hide s nagoja
                j "Jo máš, pravdu je pěkně debilní, že z nás máš jediný řidičák. Takže přicházíš o šinkanzen"
                show s nagoja
                s "O ten vlak nejde, žárlil bych na kluky, že můžou strávit čas s tebou."
                hide s nagoja
                j "Netlač tolik na pilu. Nebo začnu litovat, že jsem nezvolila vlak."
                j "Pustím nějaké písničky, co ty na to?"
                show s nagoja
                s "Jo pusť, co chceš, můj mobil ti je k dispozici. Jen mi nezruš propojení s navigací."
                hide s nagoja
                "Našla jsi u Sučana spotify a našla jsi tam nějaký použitelný playlist. Provoz není zas tak extrémní."
                "Za chvíli najíždíte na městcký okruh Nagoji (most). A samozřejmě se zde vybírá mýto."
                "Sučan zastaví u budky, kde sedí japonec."
                "Na ceduli je asi pět cen v závislosti na velikosti auta a denní době."
                "Japonec ti v japonštině sdělí částku."
                "Samozřejmě mu nerozumíte, takže s peněženky vylovíš 5000 yenů a podáš je Sučanovi a Sučan Japonci, spolehlivě je to částka přesahující všechny možnosti."
                "Japoncovi se pravděpodobně nelíbí, že mu podáváte tak velkou bankovku. Ceny na ceduli se pohybují mezi 700-1200 yenů."
                "Takže vám zopakuje, co řekl před chvílí, samozřejmě mu nerozumíte."
                "Sučan se ale usměje na Japince a řekne."
                show s nagoja
                s "Hai, arigató!"
                hide s nagoja
                "Což je japonsky Ano, a strčíš mu tu bankovku."
                "Sice Japonec ještě něco v japonštine mrmlá, ale pochopil, že mu je to k ničemu a na podnose podává účet a peníze na zpátek."
                "Sučan přijme tác oběma rukama a peníze ti nasype nastavených dlaní."
                "Tác vrátí, a vyrážíte dál."
                show s nagoja
                s "Nějak si nemůžu navyknout, jak ti Japonci, mluví jen v japonštině, že nezkusí tu angličtinu, když vidí cizince?"
                hide s nagoja
                j "Tebe to překvapuje, vždyť Češi jsou to samé i když v posledních letech se to malinko zlepšuje."
                "Po chvíli najíždíte na dálnici, správně svolíte nájezd pro auta bez ETC."
                "Od Japonce dostanete lísteček s místem nájezdu a pokračujete."
                "Cesta po dálnici docela rychle ubíhá, seš v kontaktu s druhou skupinou."
                "Sice měli být podle plánu v Kjótu dříve než vy. Protože vlakem to trvá jen půl hodiny a šinkanzen jezdí každou půl hodinu."
                "Ale podle informocí, jim cesta na nádraží trvala přes půl hodiny. Lístky si koupili až na ten pozdější, protože 15 minut na najití vlaku jim přišlo málo."
                "Navíc si byli koupit jídlo na cestu. A v Kjótu máte ubytování také pěkný kus od nádraží."
                "Takže podle všeho budete u ubytování se Sučanem první."
                show s nagoja
                s "Začínám mít hlad, myslíš, že by si mi z batohu mohla vyndat sendvič?"
                hide s nagoja
                j "Jo jasně."
                "Odpovíš natáhneš se dozádu na sedačky a podáš si Sučanův batoh."
                "Vyndáš sendvič, rozděláš ho a podáš ho Sučanovi."
                show s nagoja
                s "Díky, ten druhý si dej ty."
                hide s nagoja
                "Teprve teď ti dojde, že ses se Sučanem rozhodla jet na poslední chvíli a vlastně sis nekoupila, žádné jídlo na cestu."
                "A že máš hlad jak vlk, jak se hezky česky říká."
                j "Nebude ti chybět? Já kdyžtak vydržím do Kjóta."
                show s nagoja
                s "Nic sis s sebou nevzala, nepletu se? "
                s "V kjótu budeme až za hodinu, než se ubytujeme sejdeme s klukama, tak bude odpoledne. Klidně si dej tu druhou půlku."
                hide s nagoja
                j "Tak děkuji Sučane."
                "S chutí se zakousneš do plněného toastu. Když dojíte. Tak obal dáš do pytlíku do dveří, že to pak vezmeš vyhodit."
                show s nagoja
                s "Ještě mám v batohu kafe."
                hide s nagoja
                "Šáhneš tedy znovu pro batoh a vytáhneš asi sedmičku petlahev s kafem. Odšroubuješ uzávěr a podáš ji Sučanovi."
                "Sučan se napije a podá ti jí zpátky, předjede jedno auto a zase si po flašce šáhne."
                "Za chvíli ti jí vrací podruhé."
                show s nagoja
                s "Bych takový servis v autě potřeboval pořád. A klidně se taky napij, sedmička kafe je docela zabiják."
                hide s nagoja
                "Trošku na tebe doléhá unava, takže ani neprotestuješ a trochu kafe se napiješ."
                "Minete nějaké větší křížení dálnic, ale kupodivu jste nemuseli při sjezdu platit a znovu si vyzvedávat lísteček, asi patři i druhá část dálnice stejné společnosti."
                "Posloucháte písničky, koukáte z okna a povídáte si."
                "Před Kjótem sjíždíte z dálnice, u mýtné brány vyberete správný pruh."
                "Tentokrát u placení je automat. Sučan zastaví, u automatu, ale ty vylezeš ven a k automatu dojdeš."
                "Načteš lísteček, zobrazí se ti cena, zasuneš bankovky do autamatu a mince nasypeš do 'nálevky'. Vyjede ti účet."
                "Jdeš si sednou zpět do auta."
                show s nagoja
                s "Díky, připoutej se ať můžeme jet."
                hide s nagoja
                j "No jó mami!"
                show s nagoja
                s "Jak si mi to řekla?"
                hide s nagoja
                "Zeptá se tě zatímco se k tobě otočí a nakloní"
                j "Mami!"
                "Vybuchneš smíchy."
                show s nagoja
                s "Na to, že mě bereš jako bráchu na to už jsem si docela zvykl, ale máma? Tak to je jiný level."
                hide s nagoja
                "Zasměje se s tebou."
                show s nagoja
                s "Tak mě obejmi dcero."
                hide s nagoja
                "Nakloní se k tobě ještě blíže a rozpřáhne ruce. A obejme tě."
                j "Asi bychom měli jet, ať to tu neblokujeme."
                show s nagoja
                s "Takhle zkazit rodinou chvilku."
                hide s nagoja
                "Pustí tě, odmáčkne ručku, vypne výstražné světla a rozjede se."
                "Sjedete do Kjóta. A projíždíte centrem. Zde je doprava výrazně komplikovanější."
                "Musíte kličkovat mezi auty, autobusy, taxíky a lidmi."
                "Je to docela stresující, auta přejíždějí nahodně mezi pruhy. Míjíte se s nimi na centimetry."
                "Docela tě to znérvózňuje, ale Sučan to zvládá s naprostým klidem."
                "Spousta lidí by v jeho situaci nadávali a šíleli, jen on se na tebe stíhá v mezičase i usmívat."
                show s nagoja
                s "Neboj se tak, vím co dělám. Nic se nám nestane."
                hide s nagoja
                "Po pár minutách se konečně vymotáte, ze zasekaného centra a blížíte se k místu které udává navigace."
                show s nagoja
                s "Nevím, jak to bude s parkováním. Asi přibrzdím, vyndáme kufry, počkáš u nich a já sjedu zaparkovat."
                hide s nagoja
                j "Dobře, asi jiná možnost není."
                "V ulici kde máte bydlení, dle očekávání žádné místo na zastavení uplně není, Sučan přibrzdí kousek od adresy na přechodě."
                "Vyndáte kufry na ulici, teda spíše Šučan, moc tě totiž k práci nepustí."
                show s nagoja
                s "Tak já jedu zaparkovat, tak mi tu nezvlč."
                hide s nagoja
                "Rychle tě obejme, a než stihneš zareagovat už sedí v autě a odjíždí."
                "Protože stojíš u hromady kufrů, nemáš moc možností co dělat."
                "Položíš si tedy svůj kufr na zem a sedneš si na něj."
                "Ale Sučan odjel s internetem a kluci asi nejsou poblíž."
                "Takže si odsouzená následujících pár minut strávit, bez internetu čekáním na někoho kdo tě vysvobodí."

    return
label sinkanzen:
    "Takže jdete napřed zaplatit parkovné do parkomatu a Sučan mezitím sjede garážemi k výjezdu."
    "Protože je vaše auto na japonské poměry docela široké, místama to má opravdu tip ťop."
    "Zaplacený lístek jste načetli u výjezdu a Sučana to pustilo, popřáli jste mu šťastnou cestu a vyrážíte na nádraží."
    "Na nádraží u okénka Adrian objednal čtyři lístky na šinkanzen z Nagoji do Kjóta."
    "S odjezdem za tříčtvrtě hodiny, protože měl strach, že byste za 15 minut nestihli najít místo odjezdu a navíc si plánujete koupit bentobox."
    "Typická japonská obědová krabička na cesty."
    "Do části nádraží odkud jezdí šinkanzeny vás to pustí pouze s jízdenkou na šinkanzen."
    "Tu ale máte, takže projdete turniketem a zaplujete do obchodu s bentoboxy."
    "Každý si koupíte svůj bentobox na cesty."
    "A vyrazíte hledat nástupiště odkud vám jede váš vlak."
    "Podle šipek a barviček, nástupiště najdete docela snadno."
    "Na peróně, si najdete kde má zastavit váš vůz, abyste nemuseli přebíhat vnitřkem a postavíte se do fronty."
    "Zatímco čekáte na váš vlak, kocháte se výhledem na nádraží a vlaky."
    "Váš vlak samozřejmě přijede na čas, lidi vystoupí a vy nastoupíte."
    "Usednete na svá místa."
    if j.love_points.get(a.name,0) > 5:
        "Máš místo vedle Adriana, gentlemansky tě pustil k okýnku."
        "Mimoň se dí před vámi, a usl v podstatě ve chvíli kdy dosedl. Dante si vytáhl mobil s GPS, aby mohl měřit kolik vlak pojede."
        "Otevřel si svůj bentobox a dal se do jídla."
        "Adrian si vybalil svůj bentobox a ty svůj."
        "Každý jste si koupil něco jiného."
        show a nagoja
        a "Chceš ochutnat? Klidně si nabídni, co chceš, nejsem po té Fuji uplně fit. Takže to všechno asi nesním."
        hide a nagoja
        "Svou nabídku, doprovází i vřelým gestem."
        j "Děkuji."
        "Usěješ se na něj. A spíš tak zdvořilostně od něj ochutnáš."
        "Vybrala sis lepší bentobox."
        "Po chvíli se ti začne chtít na záchod a navíc jsi strašně zvědavá jak vypadají záchody v šinkanzenu."
        j "Dovolíš? Potřebuji si odskočit."
        show a nagoja
        a "Tak já půjdu radeji s tebou."
        hide a nagoja
        "Zvedne se pustí tě před sebe a vyrazíte k neblížším záchodům."
        "Když projdete uličkou mimo dohled ostaních."
        show a nagoja
        "Je těžké s tebou být chvíli osamotě."
        hide a nagoja
        j "Proč by si si se mnou chtěl být osamotě?"
        "Vylítne z tebe bezmyšlenkovitě."
        "Hned po vyslovení věty, toho začínáš litovat. Adrian má červené tváře a je dost nervozní."
        "Přemýšlíš, jak to napravit a pak si řekneš, že objetí nic nemůže zkazit."
        "Obejmeš Adriana, nejdříve zaraženě stojí, ale nakonec obmotá ruce kolem tebe a lehce si tě přitáhne."
        "Z těžka dýchá, trošku se od něj odkloníš a podíváš se mu do obličeje. Má strašně smutné oči. Přesto, že se na tebe usmál, když ses na něj podívala."
        "Pustíš ho a on pustí tebe, dojdeš si tedy na toaletu a Adrian tam na tebe čeká."
        j "Můžeš."
        show a nagoja
        a "Já jsem tě šel jen doprovodit."
        hide a nagoja
        j "Díky."
        "Vrátíte se tedy zpátky na svá místa."
        "Když míjíte Danteho, zvedne oči od knížky a změří si vás pohledem."
        "V podstatě ses usadila, dojedla bentobox a je čas se sbalit a připravit se k výstupu."
    elif j.love_points.get(d.name, 0) > 5:
        "Máš místo vedle Danteho, gentlemansky tě pustik k okýnku."
        "Adrian s Mimoněm sedí před vámi, ale oba v usli snad ještě než dosedli."
        "Vybalili jste si oba své bentoboxy a pustili se do jídla."
        "Na stoleček před sebe sis kromě bentoboxu postavila i mobil."
        "Užíváš si jídla a sem tam se díváš s okýnka na měnící se krajinu, i když převažuje oplocený koridor."
        "Nevíš jak se ti to podařilo, ale při nabírání rýže z boxu, ti box podjel a drcnul do tvého mobilu."
        "Který na hladkém povchu stolečku, dostal dostatečnou kinetickou energii a ihned si to zamířil k zemi."
        "Avšak Dante, který se snad nepodíval ani tvým směrem, tvůj mobil chytil ve vzduchu, těsně po tom co opustil stoleček."
        j "Díky, nechtěla bych ho tu lovit pod sedačkami, mezi cestujícími."
        "A natáhneš ruku směrem k mobilu, ale Dante ti s rukou uhne."
        show d nagoja
        d "No zadarmo to nebude."
        hide d nagoja
        j "Jak zadarmo to nebude?"
        show d nagoja
        d "Vyměním ho za objetí."
        hide d nagoja
        menu:
            "Chceš vyměnit svůj mobil za objetí?"
            "Ano":
                j "No dobře, to je asi férový obchod za to, že tu nemusím lézt po čtyřech a hledat mobil."
                "Otočíš se k němu, že ho obejmeš, ale uhne ti."
                show d nagoja
                d "Počkej, chci pořádné objetí, pojď do té části kde jsou dveře a záchody."
                hide d nagoja
                j "Nezneužíváš trošku situace?"
                show d nagoja
                d "Tak já ho můžu klidně upustit."
                hide d nagoja
                j "No dobře už jdu."
                "Vstane s tvým telefonem v ruce a pustí tě před sebe do uličky přesunute se do chodbičky k záchodům a dveřím."
                "Je zde výrazně více místa než v českých vlacích. A nikdo nikde."
                "Dante se zastaví na kraji. Kouká na tebe a mlčí."
                "Sevře se ti žaludek a citíš jak se ti do zváří hrne krev. A seš dost nervózní."
                "Chvíli naproti němu jen stojíš a skoro nedýcháš. Nejradši by si utekla někam hodně daleko, ale zároveň tě strašně zajímá jak tohle bude pokračovat."
                "Danteho přítomnost ti vůbec není nepříjemná, a ten jeho osobitý styl a tajemno kolem něj. Z něho dělají adepta na tvého přítele."
                "Zvedne tvůj mobil nad svojí hlavu a protože je vyšší než ty nezbývá ti, než se k němu přiblížit a pro mobil se natáhnout na špičkách."
                "Když už už mobil skoro držíš chytí tě druhou rukou kolem pasu a přitáhne si tě do objetí."
                "A jak si stála na špičkách, tak si samozřejmě stratila rovnováhu a 'spadla' si mu rukama kolem krku."
                "Když povolí sevření honem je sundáš, ale Dante tě nepustil úplně."
                "Udělá krok k tobě, takže je zase nebezpečně blízko intuitivně ustoupíš, o krok o dva."
                "Ale během tvého 'pádu' si tě Dante malinko pootočil."
                "Takže při svém třetím krůčku narážíš do stěny. A Dante tě samozřejmě celou dobu dvého couvání nepustil, ze svého dosahu."
                "Když narazíš zádama do zdi, tak se pousměje, evidentně to byl jeho plán."
                "Rukama se taktéž dotkneš zdi za sebou. Začínáš přemítat co dělat."
                "Když začneš křičet, tak zburcuješ celý vlak, o to asi nemáš zájem."
                "Když se pokusíš vyvléknout tak, že se snížíš pod jeho ruce a pak se pokusíš ze strany utéct, pravděpodobně nebudeš dost rychlá."
                "A vlastně docela pochybuješ, že by ti něco ve vlaku udělal. A poku si tě dostal do téhle pozice aby tě políbil."
                "Tak ti to vlastně asi nevadí. Zavřeš tedy oči a necháš rty mírně pootevřené."
                "Cítíš a slyšíš jak položil ruku svou pravou ruku těsně nad tvé levé ramono kousek od tvého ucha."
                "Skoro nedýcháš slyšíš jak se jeho dech k tobě přibližuje."
                "Ale místo polibku ti jen do pravého ucha zašeptá:"
                show d nagoja
                d "Měla by ses o své věci lépe starat."
                hide d nagoja
                "Vytřeštíš oči, tohle jsi nečekala, ale to už ti Dante strká tvůj mobil do ruky a během okamžiku jseš v místnosti sama."
                "Snažíš se nějak vstřebat co se stalo, když tu z druhé strany přichází nějaký Japonec."
                "Asi si myslí, že čekáš frontu na záchod."
                "A protože svítí, že záchod je volný začne na tebe mluvit japonsky a gestem ti dává přednost směr záchod."
                j "Ie, arigató"
                "Špitneš a vyrazíš směr tvé místo."
                "Japonec ještě něco mrmlá v japonštině, ale nejsi schopná ho vnímat."
                "Že by Dante věděl, že se ten Japonec blíží? Blbost. Nebo se mu nelíbíš? Nebo si s tebou jenom tak hraje?"
                "Mnohem radši by si dostala tu pusu jak se teď máš k Dantemu vrátit?"
                "Když se blížíš k místu, kde sedíte, Dante vyleze do uličky a pustí tě sednout."
                "Když se protahuješ kolem něho aby sis mohla sednout, tak na tebe mrkne."
                "Evidentně svoje jídlo už dojedl a stihl si vytáhnout notebook na něm datluje."
                "Dojíš si svůj bentobox a když se otočíš Danteho směrem, tak Dante klávesovou zkratkou přepne obrazovky,"
                "takže vidíš jen neutrální pozadí. A Dante přestane psát."
                j "Promiň, nemměla jsem v úmyslu koukat pod ruce, jen mě zaujalo jak si rychle psal."
                "Otočíš se a upřeně koukáš s okýnka ven."
                show d nagoja
                d "Já se nezlobím, ale jsou věci, které by si neměla vidět v tvém zájmu."
                hide d nagoja
                "Vlastně ani nevíš proč, ale jeho věta tě rozčílí."
                j "Už mě to unavuje. Nechceš si přestat hrát na důležitého, tajemného a že všechno děláš kvůli mému dobru?"
                show d nagoja
                d "Já si na nic nehraju. A nevím, čím jsem tě tak rozčílil."
                hide d nagoja
                j "Možná by si v rámci mého dobra měl příště sedět s Adrianem a nemámit ze mě objetí, když v zápětí utečeš."
                "Dante se rozeměje."
                show d nagoja
                d "Jo tak tohle tě naštvalo. A to si chtěla, abychom se líbali před tím Japoncem?"
                hide d nagoja
                j "Výmluvy, o něm si nemohl vědět. Počkej, takže si mě chtěl tedy políbit?"
                show d nagoja
                d "Kdo ví. Myslím, že solidně podceňuješ moje schopnosti. A za chvíli vystupujeme, měli bychom vzbudit kluky a sbalit se."
                hide d nagoja
                "Vstane a šťouchne do Adriana, aby ho probudil. Sbalí si věci a notebook do batohu, společně popženete Mimoně a jdete se připravit k výstupu."

            "Ne":
                j "Hele za to mi to nestojí, hoď ho klidně na zem."
                show d nagoja
                d "No když myslíš."
                hide d nagoja
                "Řekl a mobil upustil a ten zaplul někam pod vaše sedačky."
                "Zkusíš se sehnout a mobil nahmatat, ale nedaří se ti to."
                "Takže zavřeš bentobox, složíš stoleček, bentobox položíš na sedačku a klekneš si mezi sedačky."
                show d nagoja
                d "Kdybych tušil, že mi budeš klečet u nohou, ani bych se ho nepokusil chytit."
                hide d nagoja
                "Potřebuješ se sklonit pod sedačky, ale Dante tam má nohy."
                j "Jsem ráda, že se bavíš. Uhneš, potřebuju se dostat pod sedačky."
                show d nagoja
                d "A kouzelné slovíčko by nebylo?"
                hide d nagoja
                j "Abrakadabra? Neštvi mě stejně je to tvoje chyba, že spadl tak blbě."
                show d nagoja
                d "Jo tak ona to nakonec je moje chyba, že ti spadl telefon."
                hide d nagoja
                "Chytneš se levou rukou za Danteho koleno a pokusíš se napresovat pravým ramenem mezi něj a sedačku, aby si mohla pravou rukou šáhnout pod sedačku."
                show d nagoja
                d "Tady se to začíná přiostřovat, počkej, já ti teda uhnu. Ještě by si to mohli Japonci špatně vyložit."
                hide d nagoja
                "Vstane do uličky a ty se mužeš natáhnout pod sedačky pro mobil."
                "Mobil si vylovila, ale získáváš dva GP za nevhodné chování ve vlaku."
                $ j.increment_gaijin_points(2)
                "[j.show_all_points()]"
                "Mobil si raději uložíš do síťky na sedle, sedneš si sklopíš stoleček a položíš si na něj zpátky svůj bentobox."
                "Dante si sedne zpět. Když dojíš, je pomalu čas se balit a připravovat na výstup."
    else:
        "Mimoň a Adrian jen co dosednou tak usnou. Dante si vytáhl mobil s GPS, aby viděl kolik ten vlak jede."
        "Otevřela jsis svůj bentobox a dala si se do jídlo, u toho koukáš z okénka."
        "Po asi deseti minutách se vydáš na záchod, aby sis udělala obrázek jak vypadají záchody v šinkanzenu."
        "Když se vrátíš na místo rychle dojíš a je čas začít ce balit za chvíli vystupujete."
                
    return



