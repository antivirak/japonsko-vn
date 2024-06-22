# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character(_("Mimoň"), color="#fe0303")
define s = Character(_("Sučan"), color="#0303fe")
define a = Character(_("Adrian"), color="#094611")
define d = Character(_("Dante"), color="#000000")

# The game starts here.

label start:


    scene bg letistenara
    with fade


    "Vítej ve hře cesta po Japonsku"
    "Tvým cílem hry je užít si dovolenou a procestovat velkou část Japonska, nezabít Mimoně, užít si i nějakou romanci a nasbírat co nejméně Gaijin pointů (GP)."
    "Jste parta, která se po internetu domluvil/a, že vyrazíte na 3 týdny na dovolenou do Japonska. Mezi sebou se moc neznáte. Kromě online nákupu letenek jsi se s některými účastníky nikdy neviděla. Jen ty a tvůj kámoš z dětství. A další 3 naprosto cizí lidé."
    # Tady mi udělejte výběr postavy

label vyberauta:

    scene bg vyzvednutiauta
    with fade
    "Absolvovali jste dlouhý a náročný let do Japonska a máte si vyzvednout auto, které vám bude dělat společnost další 3 týdny. "
    "A ejhle první problém, auto zařizoval Sučan - fanda do aut. Máte sporťák… "
    "Pro pět lidí s kufry, je to docela stísněný prostor."

label tokio1:

    scene bg mapatokio
    with fade

    # This ends the game.

    return
