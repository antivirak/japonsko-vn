# picture from https://www.shiroang.com/blog/ichiran-main-store-pilgrimage-visit-to-a-ramen-chain-hq-in-fukuoka
# https://www.deviantart.com/lrissman/art/Red-Circle-2-867253268




transform radio_buttons:
    zoom .2


screen ichiran_menu(rb_groups, max_choice=1):
    $ show_ichiran_menu(rb_groups, max_choice=1)
    $ align_y = .55
    vbox:
        align (.5, align_y)
        spacing 80
        for count, rb_group in enumerate(rb_groups):
            # if rb_group is None:
            #     vbox:
            #         align (.5, align_y)
            #         spacing 0
            #     continue
            hbox:
                spacing 90
                for option_id, option_image in rb_group.options:
                    vbox:
                        align (.5, 0)  # or zero?
                        $ is_option_selected = rb_group.is_selected(option_id)
                        # TODO remove tint
                        $ tint_factor = 1 if is_option_selected else .5
                        $ tinted_image = im.MatrixColor(
                            option_image, im.matrix.tint(tint_factor, tint_factor, tint_factor),
                        )
                        imagebutton:
                            at radio_buttons
                            xysize (50, 50)
                            # idle "images/transparent_image.png"
                            idle tinted_image
                            hover option_image
                            selected option_image
                            action [
                                Function(rb_group.set_option, option_id, max_choice),
                                rb_group.actions[option_id],
                            ]
    textbutton "Pokračovat":
        xalign .95 yalign .95
        action Return()
