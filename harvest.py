############
# Part 1   #
############

# In this exercise:
#       take a real world set of objects, data, and behaviors
#       create several classes that could encapsulate these objects in a Python program.
#       create one relationship between two classes.

#   The scenario:
#   At a nearby melon farm, a large melon harvest is imminent. 
#   The farm grows several types of melons. The farm expects to harvest many melons each day.

# We’ll have two objects:
# MelonType
# Melon

# melon type should be able to have multiple pairings
# melon type should be able to have report code updated

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, reporting_code, name, first_harvest, color, bestseller, seedless):
        """Initialize a melon."""
        
        self.pairings = []
        self.name = name
        self.reporting_code = reporting_code
        self.first_harvest = first_harvest
        self.color = color
        self.bestseller = bestseller
        self.seedless = seedless 

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.reporting_code = new_code
        print(f"Code updated to {new_code}")


def make_melon_types():
    """Returns a list of current melon types."""
# reporting_code, name, first_harvest, color, bestseller, seedless
    all_melon_types = []

    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    
    cas = MelonType('cas', 'Casaba', 2003, 'orange', True, True)
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)
    
    cren = MelonType("cren", "Crenshaw", 1996, "green", True, True)
    cren.add_pairing('prosciutto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'yellow watermelon', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

# takes list = [melon_types]
# return dict = {melon_type, code}
# going to need to iterate list to see if melon is in list, if so, get id
# store id resullts

    melons_by_id = {}
    for melon in melon_types:
        if melon.code not in melons_by_id:
            melons_by_id[melon.code] = melon
    
    return melons_by_id

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # def  __init__ and is_sellable methods
    # melon = 1
    # melon_type = 'yw'
    # shape_rating = 8
    # color_rating = 7
    # harvested = 'Field 2'
    # harvested_by = 'Sheila'

    # melon = 2
    # melon_type = 'yw'
    # shape_rating = 3
    # color_rating = 4
    # harvested = 'Field 2'
    # harvested_by = 'Sheila'

    # melon = 3
    # melon_type = 'yw'
    # shape_rating = 9
    # color_rating = 8
    # harvested = 'Field 3'
    # harvested_by = 'Sheila'
    
    # melon = 4
    # melon_type = 'cas'
    # shape_rating = 10
    # color_rating: 6
    # harvested = 'Field 35'
    # harvested_by = 'Sheila'

    # melon = 5
    # melon_type = 'cren'
    # shape_rating = 8
    # color_rating = 9
    # harvested = 'Field 35'
    # harvested_by = 'Michael'

    # melon = 6
    # melon_type = 'cren'
    # shape_rating = 8
    # color_rating = 2
    # harvested = 'Field 35'
    # harvested_by = 'Michael'

    # melon = 7
    # Mmelon_type = 'cren'
    # shape_rating = 2
    # color_rating = 3
    # harvested = 'Field 4'
    # harvested_by = 'Michael'

    # melon = 8
    # melon_type = 'musk'
    # shape_rating = 6
    # color_rating = 7
    # harvested = 'Field 4'
    # harvested_by ='Michael'

    # melon = 9
    # melon_type = 'yw'
    # shape_rating = 7
    # color_rating = 10
    # harvested = 'Field 3'
    # harvested_by = 'Sheila'

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    pass
    # Fill in the rest
    # return melon_type


# melons can be sold if shape and color rating > than 5 and not from Field 3
def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest


 