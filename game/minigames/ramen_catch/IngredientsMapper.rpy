init python:
    class IngredientsMapper:

 
        @staticmethod
        def scale_value(value, target_max):
            return int((value / 4) * target_max)
        
        @staticmethod
        def map_ingredients(input_dict):
            mapped_ingredients = {}

            for ingredient, value in input_dict.items():
                if ingredient == "noodle":
                    mapped_ingredients["noodle"] = 10
                elif ingredient == "dashi":
                    mapped_ingredients["dashi"] = IngredientsMapper.scale_value(value, 5)
                elif ingredient == "chashu":
                    mapped_ingredients["chaschu"] = IngredientsMapper.scale_value(value, 8)
                elif ingredient == "garlic":
                    mapped_ingredients["garlic"] = IngredientsMapper.scale_value(value, 6)
                elif ingredient == "onion":
                    # Handle the special cases for onions based on the value
                    if value == 1:
                        mapped_ingredients["white_onion"] = 5
                        mapped_ingredients["green_onion"] = 0
                    elif value == 2:
                        mapped_ingredients["green_onion"] = 5
                        mapped_ingredients["white_onion"] = 0
                elif ingredient == "spiciness":
                    mapped_ingredients["chilli"] = int(value * 2)

            return mapped_ingredients