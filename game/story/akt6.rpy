label akt6:
    scene bg hotel nagoja
    "Ráno jsi vstala a jste domluvení s Adrianem a Dantem, že si před odjezdem ještě projdete Nagoju."
    "Sučan si zase vyhledal, že je ve městě nějaký obchod s modely aut. Takže vstal dříve a má se k vám připojit."
    "Sbalila sis věci, protože podle plánu si chvíli před checkoutem přijdete vzít kufry a půjdete k autu."
    scene bg chodba
    "Před pokoji už čeká Adrian a Dante se snaží doklepat na Mimoně."
    "Kupodivu, Mimoň po chvíli otvírá a vypadá připraveně."
    "Vyrážíte tedy pěšky k nagojskému hradu."
    "Po cestě potkáváte nápis Nagoja, tak se u něj na střídačku vyfotíte."
    "U vstupu do hradních zahrad zjistíte, že jsou otevřeny až od devíti, a vy potřebujete do desíti vyklidit pokoje."
    "Proto se rozhodnete, že čekat u vstupu půl hodiny kvůli půlhodinové procházce po zahradách asi nemá smysl."
    "Navíc byste museli zaplatit celodenní vstupné."
    "Takže obejdete část zahrad, která je zdarma, a setkáte se se Sučanem."
    "Poté se vrátíte na hotel a vyzvednete si kufry, odhlásíte se a vyrazíte do garáží k autu."
    "Naskládáte věci do auta. Dnes je v plánu přejezd do Kjóta šinkanzenem (japonským rychlovlakem)"
    if j.driver:
        "Jste se Sučanem jediní aktivní řidiči, takže šinkanzenem může jen jeden z vás."
        menu:
            "Budeš převážet auto, nebo pojedeš šinkanzenem?"
            "Převezu auto.":
                "Vytáhla sis černého Petra, nebo jsi jen moc hodná."
                "Zážitek z rychlovlaku přenecháš klukům a pojedeš autem úplně sama."
                "Převzala sis od Adriana přenosnou wifi, spojila jsi mobil s autem,"
                "nastavila navigaci a vyjíždíš."
                "Kluci mezitím šli dolů k parkomatu zaplatit, takže když sjedeš k výjezdu, dostáváš zaplacený lísteček a vydáváš se na cestu."
                "Všichni ti popřejí šťastnou cestu a ty vyrážíš."
                "Provoz není zas tak extrémní a už ti ani nedělají problémy blinkry/stěrače."
                "Ale za chvíli najíždíš na městský okruh Nagoji (most). A samozřejmě se zde vybírá mýto."
                "Zastavíš u budky, kde sedí Japonec."
                "Na ceduli je asi pět cen v závislosti na velikosti auta a denní době."
                "Japonec ti v japonštině sdělí částku."
                "Samozřejmě mu nerozumíš, takže mu podáš 10 000 yenů, spolehlivě je to částka několikanásobně přesahující všechny možnosti."
                "Japoncovi se pravděpodobně nelíbí, že mu podáváš tak velkou bankovku. Ceny na ceduli se pohybují mezi 700-1200 yeny."
                "Takže ti zopakuje, co řekl před chvílí, samozřejmě mu nerozumíš."
                "Tak se jen usměješ a řekneš."
                j "Hai."
                "Což je japonsky Ano, a strčíš mu tu bankovku."
                "Sice ještě něco v japonštině mrmlá, ale pochopil, že mu je to k ničemu a na podnose podává účet a peníze nazpátek."
                "Správně přijmeš tác oběma rukama a peníze si nasypeš do ruky, teda spíše do auta, jak jsi nervózní."
                "Ale máš lísteček, takže můžeš pokračovat."
                "Během chvíle se dostaneš nakonec městského okruhu, a musíš projet mýtnou bránou, abys najela na placenou dálnici."
                "Vjezd pro 'cash' poznáš na první dobrou a od jiného Japonce dostaneš kartičku na průjezd."
                "Následuje asi dvou hodinová jízda po dálnici, která jde hladce a bez větších potíží."
                "Po cestě bylo jedno křížení, takže jsi musela u automatu zaplatit lístek, který jsi měla u sebe."
                "To znamená vložit lístek do automatu a nasypat peníze do příslušných přihrádek, automat si to sám spočítal a vrátil ti."
                "Pak jsi u jiného nájezdu u automatu vyfasovala nový lísteček a s ním ses dostala až do Kjóta."
                "Jenže při sjezdu na Kjóto ti samozřejmě spadla navigace a cesty se různě větvily, takže jsi skončila na úplně blbé silnici."
                "Musíš tedy řešit, jestli někde bude možnost se otočit, navíc to vypadá jako nájezd na další dálnici, takže ti hrozí, že budeš muset zaplatit za další úsek, a to pravděpodobně 2x."
                "Za cestu tam i zpět. Nakonec se ti jednou rukou podaří navigaci zprovoznit. Zatímco se snažíš udržet na silnici a nikoho neohrozit,"
                "navigace ti naznačuje otočení o 180°. Zkontroluješ situaci, silnice v tomto místě není úplně široká, trošku připomíná české okresky."
                "Ale pro japonská úzká auta jsou to regulérní dva pruhy."
                "Vypadá to, že široko daleko nikdo nejede, tak to riskneš a otočíš to do protisměru; teda musíš si při otáčení i trošku couvnout, protože na otočení najednou na silnici není místo."
                "V průběhu tvého manévru se kupodivu žádné auto neobjevilo."
                "Až když se rozjíždíš, tak tě jedno auto dohání a předjíždí."
                "Navigace je také spokojená a stáhla tě do Kjóta."
                "Voláš tedy Sučanovi, kde jsou."
                "Podle plánu mají být v Kjótu dříve než ty. Protože šinkanzen jezdí asi tak 3x rychleji než auta."
                "Na nádraží v Nagoje to také měli jen půl hodiny a šinkanzen jezdí každou půlhodinu."
                "Strašně dlouho ti to nezvedá."
                "Tak zkoušíš volat Dantemu. Ten to zvedl."
                d "No?"
                j "Jsem v Kjótu, za 15 minut budu na místě."
                d "No my jsme teď koupili lístky na metro a budeme se k ubytování teprve přesouvat."
                j "No to je super, to tam budu asi dříve jak vy, tak snad najdu ubytování."
                d "Promiň, zdrželi jsme se. Musím řešit spoje, promiň."
                "A položil ti to. Trošku tě to rozčílí, jedeš asi tři hodiny, takže jsi nejedla."
                "Navíc doprava se začíná hodně zhušťovat, takže musíš být pořád ve střehu."
                "Doufala jsi, že si tě u ubytování kluci odchytí a navedou tě, kam zaparkovat."
                "Míjíš nádraží, kde je to opravdu překážková jízda. Auta, taxíky, autobusy a lidé."
                "Po chvíli se konečně dostaneš na místo určení, takže projíždíš ulicí, kde máte mít ubytování."
                "Ale vlastně nevíš, jak přesně má vypadat. Kluky také nevidíš."
                "'Váš cíl je vpravo,' zahlásí navigace a vypne se."
                "Kde? Super... Místo na zaparkování ani na zastavení nikde. Za tebou auta."
                "Jedeš tedy ulicí dál až na nějakou velkou křižovatku a silnici."
                "Odbočíš vpravo, ale zjistíš, že není tak snadné odbočit zase vpravo. Můžeš odbočit až na dalším semaforu, který je asi až o 4 ulice dále, než jsi chtěla."
                "Podařilo se ti odbočit. A ulice je méně frekventovaná, takže jsi na chvíli zastavila na blikačky a znovu zadala navigaci cíl."
                "Napsala jsi klukům, že doufáš, že už tam jsou. Že odmítáš kroužit pořád dokola, jako blondýna na kruháči s třicítkou."
                "Rozjedeš se, a za chvíli píše Sučan, že na tebe čekají."
                "Navigace tě donaviguje, v ulici stojí na jedné straně Sučan a Dante a na druhé Adrian a Mimoň."
                "Sučan stojí na té, ze které jedeš. Přibrzdíš tedy a zapneš blikačky."
                show s nagoja
                s "Vyházíme tady kufry, ať je nemusíme tahat. Po cestě jsme viděli volné a docela levné parkoviště. Nanaviguju tě."
                hide s nagoja
                "Otevře dveře, s Dantem vyndají kufry, Sučan si sedne k tobě do auta"
                "a nanaviguje tě na parkoviště. Na místo raději zajedeš pozadu."
                "Zakousneš rychle sušenku, co sis sbalila na cestu. Vezmeš si tašku s osobními věcmi a vyrazíte se Sučanem směr ubytování."
            "Pojedu šinkanzenem.":
                "Vyslovila jsi přání zkusit si šinkanzen. A Sučan ti nebrání, souhlasí, že auto převeze."
                call sinkanzen

    else:
        "Protože jediný aktivní řidič z vaší skupiny je Sučan, tak on bude ten, co převeze auto."
        "A vy si můžete užít zážitek ze šinkanzenu."
        menu:
            "Chceš jet šinkanzenem, anebo budeš dělat podporu Sučanovi?"
            "Šinkanzem, přeci si nenechám ujít takovou možnost.":
                call sinkanzen
            "Se Sučanem, ve dvou je ten přejezd lepší. Vlak jako vlak.":
                "Rozhodneš se, že v tom Sučana nenecháš samotného."
                "Sučan se mezitím usadil na místo řidiče. A nastavuje si navigaci. Ale ještě si nechal otevřené dveře."
                j "Tak já pojedu s tebou. Kdyby něco, tak se nám to ve dvou bude lépe řešit."
                j "A myslím, že o tolik jiné, než české vlaky, to nebude."
                show s nagoja
                s "Jseš si jistá? V Čechách vlaky nejezdí třista. Abys toho nelitovala."
                hide s nagoja
                j "Jo, jsem si jistá. Ty by si to pro mě také udělal."
                j "Hele, je dobrý jezdit ve dvou, co kdyby ti spadla navigace, nebo budeš potřebovat rychle něco přeložit?"
                if j.love_points.get(s.name, 0) > 4:
                    "Nakloníš se k němu do dveří a tlumeným hlasem mu řekneš:"
                    j "Navíc asi nechci jet s klukama. Když můžu strávit čas s tebou."
                    "Pak už nahlas aby tě ostatní slyšeli dodáš:"
                    j "Tak já jdu s klukama zaplatit k parkomatu a nastoupím dole."
                    "Vyrazíte tedy napřed k parkomatu, po cestě k výtahu slyšíte, jak Sučan zabouchl a nastartoval auto."
                    "Sjedete dolů, zaplatíte a s lístečkem o zaplacení čekáš na Sučana."
                    "Sučan během chvíle přijíždí. Rozloučíte se s ostatními, ty nasedneš a vyrazíte do Kjóta."
                    "Když se dostanete z parkoviště na hlavní ulici, Sučan se na tebe otočí."
                    show s nagoja
                    s "Udělala jsi mi radost."
                    hide s nagoja
                    j "A čím, prosimtě?"
                    show s nagoja
                    s "Že si mi dala přednost před zážitkem z rychlovlaku. Nebo možná před klukama?"
                    hide s nagoja
                    j "To je jasné. Sice neřídím, ale umím si představit, jak musí být nepříjemné řídit v cizím státě, cizí auto a ještě na druhé straně, než si zvyklý."
                    j "To já bych sama auto odmítla řídit."
                    show s nagoja
                    s "Tak já takhle neřídím poprvé, vždyť to víš. Klidně si mohla jet."
                    s "Ale asi bych pak trošku žárlil."
                    hide s nagoja
                    j "Jo, máš pravdu, je pěkně debilní, že z nás máš jediný řidičák. Takže přicházíš o šinkanzen"
                    show s nagoja
                    s "O ten vlak nejde, žárlil bych na kluky, že můžou strávit čas s tebou."
                    hide s nagoja
                    j "Netlač tolik na pilu. Nebo začnu litovat, že jsem nezvolila vlak."
                    j "Pustím nějaké písničky, co ty na to?"
                    show s nagoja
                    s "Jo, pusť, co chceš, můj mobil ti je k dispozici. Jen mi nezruš propojení s navigací."
                    hide s nagoja
                    "Našla jsi u Sučana Spotify a našla jsi tam nějaký použitelný playlist. Provoz není zas tak extrémní."
                    "Za chvíli najíždíte na městský okruh Nagoji (most). A samozřejmě se zde vybírá mýto."
                    "Sučan zastaví u budky, kde sedí Japonec."
                    "Na ceduli je asi pět cen v závislosti na velikosti auta a denní době."
                    "Japonec ti v japonštině sdělí částku."
                    "Samozřejmě mu nerozumíte, takže z peněženky vylovíš 5000 yenů, podáš je Sučanovi a Sučan Japonci. Spolehlivě je to částka přesahující všechny možnosti."
                    "Japoncovi se pravděpodobně nelíbí, že mu podáváte tak velkou bankovku. Ceny na ceduli se pohybují mezi 700-1200 yeny."
                    "Takže vám zopakuje, co řekl před chvílí. Samozřejmě mu stále nerozumíte."
                    "Sučan se ale usměje na Japonce a řekne."
                    show s nagoja
                    s "Hai, arigató!"
                    hide s nagoja
                    "Což je japonsky Ano, a strčí mu tu bankovku."
                    "Sice Japonec ještě něco mrmlá, ale pochopil, že mu je to k ničemu a na podnose podává účet a peníze nazpátek."
                    "Sučan přijme tác oběma rukama a peníze ti nasype nastavených dlaní."
                    "Tác vrátí a vyrážíte dál."
                    show s nagoja
                    s "Nějak si nemůžu navyknout, jak ti Japonci mluví jen japonsky. Že nezkusí tu angličtinu, když vidí cizince?"
                    hide s nagoja
                    j "Tebe to překvapuje, vždyť Češi jsou to samé, i když v posledních letech se to malinko zlepšuje."
                    "Po chvíli najíždíte na dálnici, správně svolíte nájezd pro auta bez ETC."
                    "Od Japonce dostanete lísteček s místem nájezdu a pokračujete."
                    "Cesta po dálnici docela rychle ubíhá, jsi v kontaktu s druhou skupinou."
                    "Sice měli být podle plánu v Kjótu dříve než vy, protože vlakem to trvá jen půl hodiny a šinkanzen jezdí každou půlhodinu."
                    "Ale podle informací jim cesta na nádraží trvala přes půl hodiny. Lístky si koupili až na ten pozdější, protože 15 minut na najití vlaku jim přišlo málo."
                    "Také si na nástupišti museli koupit bento box na cestu."
                    "A v Kjótu máte ubytování také pěkný kus od nádraží."
                    "Takže podle všeho budete u ubytování se Sučanem první."
                    show s nagoja
                    s "Začínám mít hlad. Myslíš, že bys mi z batohu mohla vyndat sendvič?"
                    hide s nagoja
                    j "Jo, jasně,"
                    "odpovíš a natáhneš se dozadu na sedačky pro Sučanův batoh."
                    "Vyndáš sendvič, rozděláš jej a podáš Sučanovi."
                    show s nagoja
                    s "Díky, ten druhý si dej ty."
                    hide s nagoja
                    "Teprve teď ti dojde, že ses se Sučanem rozhodla jet na poslední chvíli a vlastně sis nekoupila žádné jídlo na cestu."
                    "A že máš hlad jak vlk, jak se hezky česky říká."
                    j "Nebude ti chybět? Já kdyžtak vydržím do Kjóta."
                    show s nagoja
                    s "Nic sis s sebou nevzala, nepletu se? "
                    s "V kjótu budeme až za hodinu, než se ubytujeme a sejdeme s klukama, bude odpoledne. Klidně si dej tu druhou půlku."
                    hide s nagoja
                    j "Tak děkuji, Sučane."
                    "S chutí se zakousneš do plněného toastu. Když dojíte, dáš obal do pytlíku do dveří, že to pak vezmeš na ubytování vyhodit."
                    show s nagoja
                    s "Ještě mám v batohu kafe."
                    hide s nagoja
                    "Šáhneš tedy znovu pro batoh a vytáhneš asi sedmičku pet lahev s kafem. Odšroubuješ uzávěr a podáš ji Sučanovi."
                    "Sučan se napije a podá ti ji zpátky, předjede jedno auto a zase si po flašce šáhne."
                    "Za chvíli ti ji vrací podruhé."
                    show s nagoja
                    s "Bych takový servis v autě potřeboval pořád. A klidně se taky napij, sedmička kafe je docela zabiják."
                    hide s nagoja
                    "Trošku na tebe doléhá únava, takže ani neprotestuješ a trochu se kafe napiješ."
                    "Minete nějaké větší křížení dálnic, ale kupodivu jste nemuseli při sjezdu platit a znovu si vyzvedávat lísteček. Asi i druhá část dálnice patři stejné společnosti."
                    "Posloucháte písničky, koukáte z okna a povídáte si."
                    "Před Kjótem sjíždíte z dálnice, u mýtné brány vyberete správný pruh."
                    "Tentokrát je u placení automat. Sučan zastaví u automatu, ty vylezeš ven a k automatu dojdeš."
                    "Načteš lísteček, zobrazí se ti cena, zasuneš bankovky do automatu a mince nasypeš do 'nálevky'. Vyjede ti účet."
                    "Jdeš si sednou zpět do auta."
                    show s nagoja
                    s "Díky, připoutej se, ať můžeme jet."
                    hide s nagoja
                    j "No jó, mami!"
                    show s nagoja
                    s "Jak si mi to řekla?"
                    hide s nagoja
                    "zeptá se tě, zatímco se k tobě otočí a nakloní"
                    j "Mami!"
                    "Vybuchneš smíchy."
                    show s nagoja
                    s "Na to, že mě bereš jako bráchu, jsem si už docela zvykl. Ale máma? Tak to je jiný level."
                    hide s nagoja
                    "Zasměje se s tebou."
                    show s nagoja
                    s "Tak pojď na mou hruď, dcero."
                    hide s nagoja
                    "Nakloní se k tobě ještě blíže a rozpřáhne ruce. A obejme tě."
                    j "Asi bychom měli jet, ať to tu neblokujem."
                    show s nagoja
                    s "Takhle zkazit rodinou chvilku."
                    hide s nagoja
                    "Pustí tě, odmáčkne ručku, vypne výstražná světla a rozjede se."
                    "Sjedete do Kjóta. A projíždíte centrem. Zde je doprava výrazně komplikovanější."
                    "Musíte kličkovat mezi auty, autobusy, taxíky a lidmi."
                    "Je to docela stresující, auta přejíždějí náhodně mezi pruhy. Míjíte se s nimi na centimetry."
                    "Docela tě to znervózňuje, ale Sučan to zvládá s naprostým klidem."
                    "Spousta lidí by v jeho situaci nadávala a šílela, jen on se na tebe stíhá v mezičase i usmívat."
                    show s nagoja
                    s "Neboj se tak. Vím, co dělám. Nic se nám nestane."
                    hide s nagoja
                    "Po pár minutách se konečně vymotáte ze zasekaného centra a blížíte se k místu, které udává navigace."
                    show s nagoja
                    s "Nevím, jak to bude s parkováním. Asi přibrzdím, vyndáme kufry, počkáš u nich a já sjedu zaparkovat."
                    hide s nagoja
                    j "Dobře, asi jiná možnost není."
                    "V ulici, kde máte bydlení, dle očekávání žádné dobré místo na zastavení není. Sučan přibrzdí kousek od adresy na přechodě."
                    "Vyndáte kufry na ulici, teda spíše Šučan, moc tě totiž k práci nepustí."
                    show s nagoja
                    s "Já jedu zaparkovat, tak mi tu nezvlč."
                    hide s nagoja
                    "Rychle tě obejme a než stihneš zareagovat, už sedí v autě a odjíždí."
                    "Protože stojíš u hromady kufrů, nemáš moc možností, co dělat."
                    "Položíš si tedy svůj kufr na zem a sedneš si na něj."
                    "Ale Sučan odjel s internetem a kluci asi nejsou poblíž."
                    "Takže si odsouzená následujících pár minut strávit bez internetu čekáním na někoho, kdo tě vysvobodí."
                    "Ale nečekáš ani čtvrthodinu a Sučan přichází i s ostatními."
                    show s nagoja
                    s "Zaparkoval jsem a oni akorát přicházeli od zastávky."
                    hide s nagoja
                    "Rozebrali jste si každý svá zavazadla a vyrážíte na ubytko."
                    "Má to být nějaký luxusnější guesthouse, ve kterém máte strávit 2 noci."

                else:
                    j "Sejdeme se teda dole, dojdu s klukama zaplatit."
                    "Sešli jste dolů, v parkomatu jste zaplatili. A Sučan mezitím úspěšně sjel dolů."
                    "Se zaplaceným lístkem si sedáš do auta."
                    "Projedete závorou, zamáváte zbytku skupiny."
                    "Sučan zkušeně a s ledovým klidem brázdí ulice Nagoji."
                    j "Pustím nějaké písničky, co ty na to?"
                    show s nagoja
                    s "Jo, pusť, co chceš. Můj mobil ti je k dispozici. Jen mi nezruš propojení s navigací."
                    hide s nagoja
                    "Našla jsi u Sučana Spotify a našla jsi tam nějaký použitelný playlist. Provoz není zas tak extrémní."
                    "Za chvíli najíždíte na městský okruh Nagoji (most). A samozřejmě se zde vybírá mýto."
                    "Sučan zastaví u budky, kde sedí Japonec."
                    "Na ceduli je asi pět cen v závislosti na velikosti auta a denní době."
                    "Japonec ti v japonštině sdělí částku."
                    "Samozřejmě mu nerozumíte, takže z peněženky vylovíš 5000 yenů, podáš je Sučanovi a Sučan Japonci, spolehlivě je to částka přesahující všechny možnosti."
                    "Japonci se pravděpodobně nelíbí, že mu podáváte tak velkou bankovku. Ceny na ceduli se pohybují mezi 700-1200 yeny."
                    "Takže vám zopakuje, co řekl před chvílí. Samozřejmě mu nerozumíte."
                    "Sučan se ale usměje na Japonce a řekne."
                    show s nagoja
                    s "Hai, arigató!"
                    hide s nagoja
                    "Což je japonsky Ano, a strčí mu tu bankovku."
                    "Sice Japonec ještě něco japonsky mrmlá, ale pochopil, že mu je to k ničemu a na podnose podává účet a peníze nazpátek."
                    "Sučan přijme tác oběma rukama a peníze ti nasype nastavených dlaní."
                    "Tác vrátí, a vyrážíte dál."
                    show s nagoja
                    s "Nějak si nemůžu navyknout, jak ti Japonci mluví jen v japonštině. Že nezkusí tu angličtinu, když vidí cizince?"
                    hide s nagoja
                    j "Tebe to překvapuje, vždyť Češi jsou to samé, ikdyž v posledních letech se to malinko zlepšuje."
                    "Z městského okruhu sjedete na dálnici a projedete správnou mýtnou bránou."
                    "Posloucháte písničky a povídáte si."
                    "Cesta po dálnici docela rychle ubíhá, jsi v kontaktu s druhou skupinou."
                    "Sice měli být podle plánu v Kjótu dříve než vy, protože vlakem to trvá jen půl hodiny a šinkanzen jezdí každou půl hodinu."
                    "Ale podle informocí jim cesta na nádraží trvala přes půl hodiny. Lístky si koupili až na ten pozdější, protože 15 minut na najití vlaku jim přišlo málo."
                    "Navíc si byli koupit bento box na cestu. A v Kjótu máte ubytování také pěkný kus od nádraží."
                    "Takže podle všeho budete u ubytování se Sučanem první."
                    "Před Kjótem sjíždíte z dálnice, u mýtné brány vyberete správný pruh."
                    "Tentokrát je u placení automat. Sučan zastaví u automatu, ty vylezeš ven a k automatu dojdeš."
                    "Načteš lísteček, zobrazí se ti cena, zasuneš bankovky do automatu a mince nasypeš do 'nálevky'. Vyjede ti účet."
                    "Jdeš si sednou zpět do auta."
                    "Na okraji Kjóta vidíte 7eleven, tak u něj zastavíte a jdete si koupit něco k pití a k jídlu."
                    "Jídlo do sebe nasypete v autě, dojdete vyhodit odpadky do krámu a vyrazíte."
                    "V Kjótu je provoz o něco silnější, než byl dopoledne v Nagoje."
                    "Musíte kličkovat mezi auty, autobusy, taxíky a lidmi."
                    "Je to docela stresující, auta přejíždějí náhodně mezi pruhy. Míjíte se s nimi na centimetry."
                    "Docela tě to znervózňuje, ale Sučan to zvládá s naprostým klidem."
                    "Po chvíli se odpojíte z hlavní magistrály a blížíte se k ubytování."
                    show s nagoja
                    s "Nevím, jak to bude s parkováním. Asi přibrzdím, vyndáme kufry, počkáš u nich a já sjedu zaparkovat."
                    hide s nagoja
                    j "Dobře."
                    "V ulici, kde máte bydlení, dle očekávání žádné dobré místo na zastavení není. Sučan přibrzdí kousek od adresy na přechodě."
                    "Vyndáte kufry na chodník. Ty se k nim postavíš a Sučan zaleze do auta a odjede."
                    "Samozřejmě odjel i s internetem, takže čekáš sama na chodníku s kufry, bez internetu."
                    "Ale nečekáš ani čtvrthodinu a Sučan přichází i s ostatními."
                    show s nagoja
                    s "Zaparkoval jsem a oni akorát přicházeli od zastávky."
                    hide s nagoja
                    "Rozebrali jste si každý svá zavazadla a vyrážíte na ubytko."
                    "Má to být nějaký luxusnější guesthouse, ve kterém máte strávit 2 noci."

label sinkanzen:
    "Takže jdete napřed zaplatit parkovné do parkomatu a Sučan mezitím sjede garážemi k výjezdu."
    "Protože je vaše auto na japonské poměry docela široké, místy to má opravdu tip ťop."
    "Zaplacený lístek jste načetli u výjezdu a Sučana to pustilo, popřáli jste mu šťastnou cestu a vyrážíte na nádraží."
    "Na nádraží u okénka Adrian objednal čtyři lístky na šinkanzen z Nagoji do Kjóta"
    "s odjezdem za třičtvrtě hodiny, protože měl strach, že byste za 15 minut nestihli najít místo odjezdu. Navíc si plánujete na cestu koupit bento box."
    "Typickou japonskou obědovou krabičku na cesty."
    "Do části nádraží, odkud jezdí šinkanzeny, vás to pustí pouze s jízdenkou."
    "Tu ale máte, takže projdete turniketem a zaplujete do obchodu s bento boxy."
    "Každý si koupíte svůj bento box na cestu a vyrazíte hledat nástupiště, odkud vám jede vlak."
    "Podle šipek a barviček nástupiště najdete docela snadno."
    "Na peróně si najdete, kde má zastavit váš vůz, abyste nemuseli přebíhat vnitřkem, a postavíte se do fronty."
    "Zatímco čekáte na váš vlak, kocháte se výhledem na nádraží a vlaky."
    "Váš vlak samozřejmě přijede na čas. Cestující vystoupí a vy nastoupíte."
    "Usednete na svá místa."
    if j.love_points.get(a.name, 0) > 4:
        "Máš místo vedle Adriana, gentlemansky tě pustil k okýnku."
        "Mimoň sedí před vámi, a usnul v podstatě ve chvíli, kdy dosedl. Dante si vytáhl mobil s GPS, aby mohl měřit, jak rychle vlak pojede."
        "Otevřel si svůj bento box a dal se do jídla."
        "Adrian si vybalil svůj bento box a ty svůj."
        "Každý jste si koupil něco jiného."
        show a nagoja
        a "Chceš ochutnat? Klidně si nabídni, co chceš. Nejsem po té Fuji uplně fit. Takže to všechno asi nesním."
        hide a nagoja
        "Svou nabídku, doprovází i vřelým gestem."
        j "Děkuji."
        "Umsěješ se na něj. A spíše tak zdvořilostně od něj ochutnáš."
        "Zhodnotíš, že sis vybrala lepší bento box."
        "Po chvíli se ti začne chtít na záchod, a navíc jsi strašně zvědavá, jak vypadají záchody v šinkanzenu."
        j "Dovolíš? Potřebuji si odskočit."
        show a nagoja
        a "Tak já půjdu raději s tebou."
        hide a nagoja
        "Zvedne se, pustí tě před sebe a vyrazíte k nebližším záchodům."
        "Projdete uličkou mimo dohled ostatních."
        show a nagoja
        a "Je těžké s tebou být chvíli o samotě."
        hide a nagoja
        j "Proč by si si se mnou chtěl být o samotě?"
        "Vylítne z tebe bezmyšlenkovitě."
        "Hned po vyslovení věty toho začínáš litovat. Adrian má červené tváře a je dost nervózní."
        "Přemýšlíš, jak to napravit, a pak si řekneš, že objetí nic nemůže zkazit."
        "Obejmeš Adriana. nejdříve zaraženě stojí, ale nakonec obmotá ruce kolem tebe a lehce si tě přitáhne."
        "Ztěžka dýchá. Trošku se od něj odkloníš a podíváš se mu do obličeje. Má strašně smutné oči. Přestože se na tebe usmál, když ses na něj podívala."
        "Pustíš ho a on pustí tebe, dojdeš si tedy na toaletu a Adrian tam na tebe čeká."
        j "Můžeš."
        show a nagoja
        a "Já jsem tě šel jen doprovodit."
        hide a nagoja
        j "Díky."
        "Vrátíte se tedy zpátky na svá místa."
        "Když míjíte Danteho, zvedne oči od knížky a změří si vás pohledem."
        "Usadila ses, dojedla bento box a je čas se sbalit a připravit se k výstupu."
    elif j.love_points.get(d.name, 0) > 4:
        "Máš místo vedle Danteho, gentlemansky tě pustil k okýnku."
        "Adrian s Mimoněm sedí před vámi, ale oba usli – snad ještě, než dosedli."
        "Vybalili jste si oba své bento boxy a pustili se do jídla."
        "Na stoleček před sebe sis kromě bento boxu postavila i mobil."
        "Užíváš si jídla a sem tam se díváš z okýnka na měnící se krajinu, i když převažuje oplocený koridor."
        "Nevíš, jak se ti to podařilo, ale při nabírání rýže z boxu ti tác podjel a drcnul do tvého mobilu."
        "Který na hladkém povrchu stolečku, dostal dostatečnou kinetickou energii a ihned si to zamířil k zemi."
        "Avšak Dante, který se snad nepodíval ani tvým směrem, tvůj mobil chytil ve vzduchu těsně po tom, co opustil stoleček."
        j "Díky, nechtěla bych ho tu lovit pod sedačkami mezi cestujícími."
        "A natáhneš ruku směrem k mobilu, ale Dante ti s rukou uhne."
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
                d "Počkej, chci pořádné objetí, pojď do té části, kde jsou dveře a záchody."
                hide d nagoja
                j "Nezneužíváš trošku situace?"
                show d nagoja
                d "Tak já ho můžu klidně upustit."
                hide d nagoja
                j "No dobře, už jdu."
                "Vstane s tvým telefonem v ruce a pustí tě před sebe do uličky. Přesunete se do chodbičky k záchodům a dveřím."
                "Je zde výrazně více místa než v českých vlacích. A nikde nikdo."
                "Dante se zastaví na kraji. Kouká na tebe a mlčí."
                "Sevře se ti žaludek a cítíš jak se ti do tváří hrne krev. A jsi dost nervózní."
                "Chvíli naproti němu jen stojíš a skoro nedýcháš. Nejradši bys utekla někam hodně daleko, ale zároveň tě strašně zajímá, jak tohle bude pokračovat."
                "Danteho přítomnost ti vůbec není nepříjemná. Ten jeho osobitý styl a tajemno kolem něj z něho dělají adepta na tvého přítele."
                "Zvedne tvůj mobil nad hlavu, a protože je vyšší než ty, nezbývá ti, než se k němu přiblížit a pro mobil se natáhnout na špičkách."
                "Když už mobil skoro držíš, chytí tě druhou rukou kolem pasu a přitáhne si tě do objetí."
                "A jak jsi stála na špičkách, tak jsi samozřejmě ztratila rovnováhu a 'spadla' jsi mu rukama kolem krku."
                "Když povolí sevření, honem je sundáš, ale Dante tě nepustil úplně."
                "Udělá krok k tobě, takže je zase nebezpečně blízko. Instinktivně ustoupíš o krok, o dva."
                "Ale během tvého 'pádu' si tě Dante malinko pootočil."
                "Takže při svém třetím krůčku narážíš do stěny. A Dante tě samozřejmě celou dobu tvého couvání nepustil ze svého dosahu."
                "Když narazíš zády do zdi, pousměje se. Evidentně to byl jeho plán."
                "Rukama se taktéž dotkneš zdi za sebou. Začínáš přemítat, co dělat."
                "Kdybys začla křičet, tak zburcuješ celý vlak. O to asi nemáš zájem."
                "Když se pokusíš vyvléknout tak, že se snížíš pod jeho ruce, a pak se pokusíš ze strany utéct, pravděpodobně nebudeš dost rychlá."
                "A vlastně docela pochybuješ, že by ti něco ve vlaku udělal. A pokud si tě dostal do téhle pozice, aby tě políbil,"
                "tak ti to vlastně asi nevadí. Zavřeš tedy oči a necháš rty mírně pootevřené."
                "Cítíš a slyšíš, jak položil svou pravou ruku těsně nad tvé levé rameno kousek od tvého ucha."
                "Skoro nedýcháš. Slyšíš, jak se jeho dech k tobě přibližuje."
                "Ale místo polibku ti jen do pravého ucha zašeptá:"
                show d nagoja
                d "Měla by ses o své věci lépe starat."
                hide d nagoja
                "Vytřeštíš oči. Tohle jsi nečekala, ale to už ti Dante strká tvůj mobil do ruky a během okamžiku jsi v místnosti sama."
                "Snažíš se nějak vstřebat, co se stalo, když tu z druhé strany přichází nějaký Japonec."
                "Asi si myslí, že čekáš frontu na záchod."
                "A protože svítí, že záchod je volný, začne na tebe mluvit japonsky a gestem ti dává přednost směr záchod."
                j "ie, arigató,"
                "špitneš a vyrazíš směr tvé místo."
                "Japonec ještě něco mrmlá v japonštině, ale nejsi schopná ho vnímat."
                "Že by Dante věděl, že se ten Japonec blíží? Blbost. Nebo se mu nelíbíš? Nebo si s tebou jenom tak hraje?"
                "Mnohem radši bys dostala tu pusu. Jak se teď máš k Dantemu vrátit?"
                "Když se blížíš k místu, kde sedíte, Dante vyleze do uličky a pustí tě sednout."
                "Když se protahuješ kolem něho, aby sis mohla sednout, mrkne na tebe."
                "Evidentně svoje jídlo už dojedl a stihl si vytáhnout notebook. Teď na něm datluje."
                "Dojíš si svůj bento box a když se otočíš Danteho směrem, tak Dante klávesovou zkratkou přepne obrazovky,"
                "takže vidíš jen neutrální pozadí. A Dante přestane psát."
                j "Promiň, neměla jsem v úmyslu koukat ti pod ruce, jen mě zaujalo, jak si rychle psal."
                "Otočíš se a upřeně koukáš z okýnka ven."
                show d nagoja
                d "Já se nezlobím, ale jsou věci, které by si neměla vidět ve svém zájmu."
                hide d nagoja
                "Vlastně ani nevíš proč, ale jeho věta tě rozčílí."
                j "Už mě to unavuje. Nechceš si přestat hrát na důležitého, tajemného, a že všechno děláš kvůli mému dobru?"
                show d nagoja
                d "Já si na nic nehraju. A nevím, čím jsem tě tak rozčílil."
                hide d nagoja
                j "Možná by si v rámci mého dobra měl příště sedět s Adrianem a nemámit ze mě objetí, když vzápětí utečeš."
                "Dante se rozeměje."
                show d nagoja
                d "Jo tak tohle tě naštvalo. A to si chtěla, abychom se líbali před tím Japoncem?"
                hide d nagoja
                j "Výmluvy, o něm si nemohl vědět. Počkej, takže si mě chtěl tedy políbit?"
                show d nagoja
                d "Kdo ví. Myslím, že solidně podceňuješ moje schopnosti. A za chvíli vystupujeme, měli bychom vzbudit kluky a sbalit se."
                hide d nagoja
                "Vstane a šťouchne do Adriana, aby ho probudil. Sbalí si věci a notebook do batohu, společně popoženete Mimoně a jdete se připravit k výstupu."
                "Vystoupili jste hladce, i cestu z nástupiště jste našli na první dobrou."
                "Zjistili jste, že to na ubytování jsou ještě asi 3 km. A protože Sučan už je prý na místě a Adrian vypadá strhaně."
                "Rozhodnete se, že použijete hromadnou dopravu, podle všeho Kjóto má metro."
                "Adrian tedy dojde koupit 4 lístky a vyrazíte do metra."
                "Za necelou půlhodinku jste u ubytování, kde na vás čeká Sučan."
                "Jdete vyzvednout kufry do auta a ubytovat se."
                # TODO mimoň mekáč
            "Ne":
                j "Hele, za to mi to nestojí, hoď ho klidně na zem."
                show d nagoja
                d "No když myslíš,"
                hide d nagoja
                "řekl, mobil upustil a ten zaplul někam pod vaše sedačky."
                "Zkusíš se sehnout a mobil nahmatat, ale nedaří se ti to."
                "Takže zavřeš bento box, složíš stoleček, bento box položíš na sedačku a klekneš si mezi sedačky."
                show d nagoja
                d "Kdybych tušil, že mi budeš klečet u nohou, ani bych se ho nepokusil chytit."
                hide d nagoja
                "Potřebuješ se sklonit pod sedačky, ale Dante tam má nohy."
                j "Jsem ráda, že se bavíš. Uhneš? Potřebuju se dostat pod sedačky."
                show d nagoja
                d "A kouzelné slovíčko by nebylo?"
                hide d nagoja
                j "Abrakadabra? Neštvi mě, stejně je to tvoje chyba, že spadl tak blbě."
                show d nagoja
                d "Jo tak ona to nakonec je moje chyba, že ti spadl telefon."
                hide d nagoja
                "Chytneš se levou rukou za Danteho koleno a pokusíš se napresovat pravým ramenem mezi něj a sedačku, abys mohla pravou rukou šáhnout pod sedačku."
                show d nagoja
                d "Tady se to začíná přiostřovat, počkej, já ti teda uhnu. Ještě by si to mohli Japonci špatně vyložit."
                hide d nagoja
                "Vstane do uličky a ty se můžeš natáhnout pod sedačky pro mobil."
                "Mobil si vylovila, ale získáváš dva GP za nevhodné chování ve vlaku."
                $ j.increment_gaijin_points(2)
                show screen stats_overview
                "Mobil si raději uložíš do síťky na sedadle, sedneš si, sklopíš stoleček a položíš si na něj zpátky svůj bento box."
                "Dante si sedne zpět. Když dojíš, je pomalu čas se balit a připravovat na výstup."
                "Dante vstane a šťouchne do Adriana, aby ho probudil."
                "Vystoupili jste hladce, i cestu z nástupiště jste našli na první dobrou."
                "Zjistili jste, že to na ubytování jsou ještě asi 3 km. A protože Sučan už je prý na místě a Adrian vypadá strhaně,"
                "rozhodnete se, že použijete hromadnou dopravu. Podle všeho má Kjóto metro."
                "Adrian tedy dojde koupit 4 lístky a vyrazíte do metra."
                "Za necelou půlhodinku jste u ubytování, kde na vás čeká Sučan."
                "Jdete vyzvednout kufry do auta a ubytovat se."
    else:
        "Mimoň a Adrian jen co dosednou, tak usnou. Dante si vytáhl mobil s GPS, aby viděl, kolik ten vlak jede."
        "Otevřela sis svůj bento box a dala ses do jídla. U toho koukáš z okénka."
        "Po asi deseti minutách se vydáš na záchod, aby sis udělala obrázek, jak vypadají záchody v šinkanzenu."
        "Když se vrátíš na místo, rychle dojíš a je čas začít se balit. Za chvíli vystupujete."
        "Dante vstane a šťouchne do Adriana, aby ho probudil. Sbalí si věci a knížku do batohu, společně popoženete Mimoně a jdete se připravit k výstupu."
        "Vystoupili jste hladce, i cestu z nástupiště jste našli na první dobrou."
        "Zjistili jste, že to na ubytování jsou ještě asi 3 km. A protože Sučan už je prý na místě a Adrian vypadá strhaně,"
        "rozhodnete se, že použijete hromadnou dopravu. Podle všeho má Kjóto metro."
        "Adrian tedy dojde koupit 4 lístky a vyrazíte do metra."
        "Za necelou půlhodinku jste u ubytování, kde na vás čeká Sučan."
        "Jdete vyzvednout kufry do auta a ubytovat se."

label kjoto_guest_house:
    "Na recepci pracuje podle vzhledu cizinka, takže tentokrát si s angličtinou vystačíte."
    "Poté, co si z vašich pasů opsala všechny informace, dostáváte klíče od pokoje."
    "Jste až v sedmém patře. Podle všeho musíte výtahem, schodiště nikde nevidíte."
    "Ale tak s kufry lepší varianta, než kdyby to bylo naopak."
    "Když odemknete, otevře se před vámi docela velký prostor. Jsou zde 2 postele a tři futonové postele."
    "Adrian zamířil rovnou do koupelny."
    show d nagoja
    d "Navrhuji, aby si postele vzali [j.name] a Adrian a my si vezmeme ty futonové."
    hide d nagoja
    "Ale než to stihnete s Dantem prodiskutovat, tak se Mimoň už válí v jedné z normálních postelí."
    show d nagoja
    d "Aha... [j.name_5p], vadilo by ti spát na té matraci na zemi? Adrian vypadá, že mu není dobře."
    hide d nagoja
    menu:
        "Kde budeš spát?"
        "Ne, nevadí mi spát na té matraci na zemi.":
            "Položíš si tedy kufr ke krajnímu futonu."
            if j.love_points.get(d.name, 0) > 5:
                "Dante si dá věci na futon vedle tebe a Sučan k balkonu."
            else:
                "Sučan si položil věci na futon vedle tebe."
            "Po chvíli vychází úplně sinalý Adrian, který beze slova zamíří k volné posteli. Kde doslova odpadne."
            "Jsi ráda, že jsi mu přenechala postel, navíc futony vypadají také dost pohodlně."
            show d nagoja
            d "Navrhuju trochu vydechnout a jít se projít."
            hide d nagoja
            "Hlavou pohodí směrem k Adrianovi a pochopíte, že mu chce nechat klid."
            "Se Sučanem oba přikývnete."
            "Mimoň našel ovládání od televize a samozřejmě ji musel hned pustit. A protože si vybral postel, která je nejdál od televize, pustil si ji fakt nahlas."
            "Chvíli se ho snažíte přesvědčovat, ať to vypne anebo ztlumí, nebo ať jde s vámi, ale všechno marné."
            "Naneštěstí nebo možná naštěstí, Adrian i přes všechen ten hluk spí."
            "Vystřídali jste se v koupelně, ty sis dala i rychlou sprchu, protože po celém dni jsi byla strašně ulepená."
            "Sbalili jste si věci a do hodinky jste připraveni k odchodu."
            jump vecer_nagoja 
        "No, radši bych spala na normální posteli.":
            show d nagoja
            d "Jo jasně, on to Adrian na zemi zvládne. Je tvoje."
            hide d nagoja
            "Dáš si věci k posteli a rozhodneš se, že proběhneš sprchou, než budete řešit, co dál."
            "Po chvíli vychází úplně sinalý Adrian, který beze slova zamíří, k volnému futonu. Kde doslova odpadne."
            show d nagoja
            d "Navrhuju trochu vydechnout a jít se projít."
            hide d nagoja
            "Hlavou pohodí směrem k Adrianovi a pochopíte, že mu chce nechat klid."
            "Se Sučanem oba přikývnete. Ty si sbalíš věci na převlečení a zamíříš do koupelny."
            "Opravdu rychle se osprchuješ a převlíkneš. Když se vrátíš do pokoje, tak tam nehorázně řve televize."
            "S nějakou japonskou soutěží."
            j "Nechcete to vypnout? Adrian spí."
            "Jen co položíš otázku, zahlídneš naštvaný výraz u Danteho i Sučana. Když svůj pohled stočíš k Mimoňovi, tak pochopíš."
            "Ovládání má on."
            j "Aha. Tak já si sbalím věci a tak za čtvrthodinky můžeme vyrazit."
            "Jdeš si přebalit věci a kluci se mezitím vystřídají v koupelně."

label vecer_nagoja:
    "Klíče máte dvoje, takže jedny přenecháte Adrianovi s Mimoněm a vyrážíte na odpolední procházku po Kjótu."
    "Ty, Sučan a Dante. Zamíříte do zahrad Nidžó hradu. Cesta vám zabere něco okolo půl hodinky."
    "Jako vše v Japonsku zahrady ale zavírají brzo – v šest hodin."
    "Takže na prohlídku máte necelou hodinku."
    "Zahrady jsou krásné. Dokonce obsahují něco na styl vyhlídky."
    "Takže si je můžete prohlédnout i z vyvýšeného místa."
    "Ze zahrad vás vyžene rozhlas upozorňující na zavíračku."
    "Chvíli jste se ještě rozhlíželi v okolí zahrad, a pak jste se domluvili, že se přiblížíte k ubytování a dáte si někde večeři."
    "Asi 4 ulice od ubytování najdete podnik, který vás zaujme."
    "Napíšete Adrianovi a Mimoňovi, zda se nechtějí připojit."
    "Ozve se Mimoň, že přijde, a že Adrian spí."
    "Asi po deseti minutách čekání Mimoň dorazil,"
    "takže jste zalezli do podniku. Číšník si vás změřil pohledem a hlavně přepočítal. A nechal vás posadit v chodbičce, v takové čekárně na jídlo."
    "Za chvíli se vrátil a bere vás někam dolů do suterénu."
    "Usadí vás v rohu místnosti ke stolu pro 4."
    "A dá vám jídelní lístky, samozřejmě jsou jen v japonštině. Nevadí, překladač to jistí."
    "Navíc je to tonkatsu – smážo restaurace, takže zde mají obalované všemožné řízečky. A před vstupem jste si prohlídli plastové maketky."
    "Tohle je asi poprvé od toho, co jste přijeli do Japonska, co si musíte objednat bez Adrianovy japonštiny."
    "Ale nakonec to úspěšně zvládnete."
    "A po chvíli se vám nese pití, co jste si objednali, čaj, který je k jídlu zdarma, sezam a set omáček."
    "A po asi 10 minutách dostáváte objednané jídlo."
    "Poděkujete a pustíte se do jídla."
    "Tentokrát platíš ty, aby se dluhy mezi vámi trošku vyrovnaly."
    "S plnými žaludky vyrazíte na ubytko."
    "Po cestě se stavíte ještě v 7eleven, a po domluvě s Dantem koupíte kolu a nějaké pečivo pro Adriana."
    "Venku už je tma, takže se více nezdržujete a jdete na pokoj."
    "Vystřídáte se v koupelně, Adrian si vezme kolu, napije se a vypadá o něco lépe."
   
    return
