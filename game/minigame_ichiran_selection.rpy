# picture from https://www.shiroang.com/blog/ichiran-main-store-pilgrimage-visit-to-a-ramen-chain-hq-in-fukuoka

# start minigame by "jump / call ichiran_selection_minigame_main" from script


transform radio_buttons:
    zoom .2


transform size_1_3:
    zoom 1.3


style text_red:
    color "#d71616"
    size 270
    line_leading 120
    # justify True


screen ichiran_menu(rb_groups, max_choice=1):
    $ show_ichiran_menu(rb_groups, max_choice=1)

    textbutton "Pokračovat":
        xalign .95 yalign .95
        action Return()


label switch_context(rb_group):
    $ num = None
    while not isinstance(num, float):
        $ num = try_float(renpy.input("Vyber si pálivost od 3 do 10").strip().replace(",", "."))
        if not 3 <= num <= 10:
            $ num = None
            "Špatný vstup. Zadej číslo mezi 3 a 10."
    $ rb_group.set_spiciness(int(num))
    jump ichiran_selection_minigame


label ichiran_selection_minigame_main:
    image black = "#000"
    scene black
    show ichiran_order_sheet at size_1_3, top
    # TODO rewrite the below to init python block if you need to access the selected values outside of renpy script
    $ circle = "images/select_circle.png"
    $ transparent = "images/transparent_image.png"
    $ image_matrix = [
        [circle, transparent, circle, transparent, circle],
        [circle] * 5,
        [circle] * 5,
        [*[circle] * 3],
        [circle, transparent, transparent, circle, transparent],
        None,
        [circle] * 5,
        [circle] * 5,
    ]
    $ tbtn = [RadioButtonGroupSpicy(image_list) if image_list else None for image_list in image_matrix]


label ichiran_selection_minigame:
    call screen ichiran_menu(tbtn)
    $ choices = ["dashi", "richness", "garlic", "onion", "chashu", None, "spiciness", "noodle"]
    if not all(len(tbtn_instance.get_selected_index()) for tbtn_instance in tbtn if tbtn_instance):
        "Vyber si prosím všechny ingredience."
        call screen ichiran_menu(tbtn)
    $ print({
        # map choice to selection index,
        choice: tbtn_instance.get_selected_index()[0]
        # but for spiciness return float value
        if choice != 'spiciness'
        else tbtn_instance.get_spiciness()
        for choice, tbtn_instance in zip(choices, tbtn) if tbtn_instance
    })
    return  # TODO jump if calling this label causes problems
