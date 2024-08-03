init python:
    class ItemCounter:
        def __init__(self, item_types, target_amounts):
            self.counters = {item_type: 0 for item_type in item_types}
            self.target_amounts = target_amounts

        def increase_counter(self, item_type):
            if item_type in self.counters:
                self.counters[item_type] += 1   
                print(f"{item_type} {self.counters[item_type]}")

        def get_counter(self, item_type):
            return self.counters.get(item_type, 0)
        
        def get_target_amount(self, item_type):
            return self.target_amounts.get(item_type, 0)
        
        def reset_counters(self):
            for item_type in self.counters:
                self.counters[item_type] = 0
                
        def all_counters_reached_target_amount(self):
                return all(self.counters[item_type] >= self.get_target_amount(item_type) for item_type in self.counters)