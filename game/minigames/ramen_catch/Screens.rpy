# Call this label to start the ramen catch minigame.
label ramencatch_start:
    $ spawner = ItemSpawner(spawn_interval=2)
    $ bowl = Bowl(
        im.Scale("ramen_bowl_p1.png", 150, 150),
        x=config.screen_width / 2,
        y=config.screen_height - 200,
        width=150,
        height=150,
        collidable_width=120,
        collidable_height=25,
    )
    $ item_counter = ItemCounter(
        item_types=["noodle", "dashi", "chaschu", "garlic", "white_onion", "green_onion", "chilli"],
        target_amounts=ramencatch_target_amounts,
    )
    $ collision_detector = CollisionDetector(spawner=spawner, bowl=bowl, counter=item_counter)

    # Start the minigame screen
    call screen ramencatch

define item_counter_hbox_width = 180
screen item_counters_vbox(item_counter):

    default item_dimensions = {
        "noodle": (75, 75),
        "dashi": (75, 75),
        "chaschu": (75, 75),
        "garlic": (75, 75),
        "white_onion": (75, 75),
        "green_onion": (75, 75),
        "chilli": (45, 100),
    }

    vbox:
        xalign 1.0
        yalign 0.5

        for item_type, count in item_counter.counters.items():
            $ item_width, item_height = item_dimensions.get(item_type)
            hbox:
                xminimum item_counter_hbox_width
                xmaximum item_counter_hbox_width
                spacing 10
                add im.Scale(f"{item_type}.png", item_width, item_height)
                text "[count]/[item_counter.get_target_amount(item_type)]"

screen ramencatch():
    add bowl
    add collision_detector
    use item_counters_vbox(item_counter)
    timer spawner.spawn_interval repeat True action Function(spawner.spawn_item)

label ramencatch_lost:
    show text "Prohrál['a' if j.gender == 'f' else ''] jsi minihru!" at Position(xalign=0.5, yalign=0.2) with dissolve

    menu:
        "Restart":
            hide text with dissolve
            $ renpy.call_in_new_context("ramencatch_start")
        "Přeskočit minihru":
            hide text with dissolve
            jump ramencatch_won
