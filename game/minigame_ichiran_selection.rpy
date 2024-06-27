# picture from https://www.shiroang.com/blog/ichiran-main-store-pilgrimage-visit-to-a-ramen-chain-hq-in-fukuoka
# https://www.deviantart.com/lrissman/art/Red-Circle-2-867253268

init python:

    # from radio_buttons import RadioButtonGroup
    # from renpy.display.layout import compute_raw


    def get_spiciness_input(rb_group, show: bool):
        if not show:
            return
        xpos, ypos, _, _ = renpy.focus_coordinates()
        renpy.call_in_new_context('switch_context', xpos, ypos, rb_group)


    def show_spiciness_input(num: float, xpos, ypos, rb_group):
        rb_group.spiciness = str(int(num))
        print(f"Spiciness: {num}")
    #     renpy.call_in_new_context('spicy_context', num, xpos, ypos)


    def show_hbox(rb_group, h_spacing, max_choice, show_input: bool = False):
        len_options = len(rb_group.options)
        with ui.hbox(spacing=h_spacing):
            for count, (option_id, option_image) in enumerate(rb_group.options):
                # with ui.vbox(align=(.5, 0)):
                is_option_selected = rb_group.is_selected(option_id)
                tint_factor = 1 if is_option_selected else .5
                tinted_image = im.MatrixColor(
                    option_image, im.matrix.tint(tint_factor, tint_factor, tint_factor),
                )
                # alpha_image = im.MatrixColor(
                #     option_image, im.matrix.tint(tint_factor, tint_factor, tint_factor),
                # )
                idle_image = tinted_image if is_option_selected else "images/transparent_image.png"
                actions = [
                    Function(rb_group.set_option, option_id, max_choice),
                    rb_group.actions[option_id],
                ]
                selected_image = option_image
                if count == len_options - 1:
                    # TODO
                    selected_image = f"images/{rb_group.spiciness}.png" if is_option_selected else selected_image
                    actions.append(Function(get_spiciness_input, rb_group, show_input))

                button = ui.imagebutton(
                    at=radio_buttons,
                    # xysize=(330, 330),
                    idle=idle_image,
                    hover=tinted_image,
                    selected=selected_image,
                    action=actions,
                )

        # return compute_raw(button.style.left_margin, 496 * .2), compute_raw(button.style.top_margin, 484 * .2)


    def show_vbox(rb_groups, align_x, align_y, v_spacing, h_spacing, max_choice):
        count = 0
        with ui.vbox(spacing=v_spacing, align=(align_x, align_y)):
            for count, rb_group in enumerate(rb_groups):
                if rb_group is None:
                    break
                show_hbox(rb_group, 53 if count == 3 else h_spacing, max_choice)

        with ui.vbox(spacing=31, align=(align_x, .84)):
            for not_show_input, rb_group in enumerate(rb_groups[count + 1:]):
                show_hbox(rb_group, h_spacing, max_choice, show_input=not not_show_input)


    def show_ichiran_menu(rb_groups: list[RadioButtonGroup], max_choice: int = 1):
        show_vbox(rb_groups, .55, .36, -8, 4, max_choice)


    def try_float(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return -1


transform radio_buttons:
    zoom .2


screen ichiran_menu(rb_groups, max_choice=1):
    $ show_ichiran_menu(rb_groups, max_choice=1)

    textbutton "Pokračovat":
        xalign .95 yalign .95
        action Return()


label switch_context(xpos, ypos, rb_group):
    $ num = None
    while not isinstance(num, float):
        $ num = try_float(renpy.input("Vyber si pálivost od 3 do 10").strip().replace(",", "."))
        if not 3 <= num <= 10:
            $ num = None
            "Špatný vstup. Zadej číslo mezi 3 a 10."
    $ show_spiciness_input(num, xpos, ypos, rb_group)
    # TODO show it somehow. Change the image of the last button?
    return


# label spicy_context(num, xpos, ypos):
#     $ ui.text(str(num), xpos=xpos, ypos=ypos)
