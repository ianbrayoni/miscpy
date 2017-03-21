"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

from itertools import groupby

# The file containing the restaurant data.
FILENAME = '/Users/brayoni/Sandbox/Python/miscpy/restaurant_recommender/restaurants_small.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)


    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Dumplings R Us', 'Queen St. Cafe']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = {'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Dumplings R Us', 'Queen St. Cafe']
    """
    list_of_interest = []

    for cuisine in cuisines_list:
        for restaurant in cuisine_to_names[cuisine]:
            if restaurant in names_matching_price:
                list_of_interest.append(restaurant)

    return list_of_interest

def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    
    >>>read_restaurants(FILENAME)
    ({'Deep Fried Everything': 52, 
     'Mexican Grill': 85,
     'Dumplings R Us': 71, 
     'Georgie Porgie': 87, 
     'Queen St. Cafe': 82},
    {'$$': ['Mexican Grill'], 
    '$$$$': [], 
    '$$$': ['Georgie Porgie'], 
    '$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']},
    {'Canadian': ['Georgie Porgie'], 
    'Mexican': ['Mexican Grill'], 
    'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'], 
    'Malaysian': ['Queen St. Cafe'], 
    'Thai': ['Queen St. Cafe'], 
    'Chinese': ['Dumplings R Us']})
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    with open(file, 'r') as f:
        # read file object as list
        # ['Georgie Porgie', '87%', '$$$', 'Canadian,Pub Food', '',
        #  'Queen St. Cafe', '82%', '$', 'Malaysian,Thai', '',
        # 'Dumplings R Us', '71%', '$', 'Chinese', '',
        # 'Mexican Grill', '85%', '$$', 'Mexican', '',
        # 'Deep Fried Everything', '52%', '$', 'Pub Food']
        restaurant_list_obj = f.read().splitlines()

    # create a list of lists for individual restaurant profiles
    # grouped on empty string element
    restaurant_profiles = \
        [list(group) for k,
                         group in groupby(restaurant_list_obj,
                                          lambda x: x == "") if not k]

    # [['Georgie Porgie', '87%', '$$$', 'Canadian,Pub Food'],
    #  ['Queen St. Cafe', '82%', '$', 'Malaysian,Thai'],
    #  ['Dumplings R Us', '71%', '$', 'Chinese'],
    #  ['Mexican Grill', '85%', '$$', 'Mexican'],
    #  ['Deep Fried Everything', '52%', '$', 'Pub Food']]

    for lst in restaurant_profiles:
        # update name_to_rating dict with name and rating
        # rating% converted from str '85%' to int i.e. 85
        name_to_rating.update({lst[0] : int(lst[1].strip('%'))})

        # populate price_to_names
        for key in price_to_names.keys():
            if lst[2] == key:
                price_to_names[key].append(lst[0])

        # populate cuisine_to_names
        # check if element values are comma separated and treat accordingly
        if ',' in lst[3]:
            tmp_lst = lst[3].split(',')

            for cuisine in tmp_lst:

                if cuisine in cuisine_to_names.keys():
                    cuisine_to_names[cuisine].append(lst[0])

                cuisine_to_names[cuisine] = [lst[0]]

        elif lst[3] in cuisine_to_names.keys():
            cuisine_to_names[lst[3]].append(lst[0])

        else:
            cuisine_to_names[lst[3]] = [lst[0]]

    return name_to_rating, price_to_names, cuisine_to_names


filter_by_cuisine(names_matching_price = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
                  cuisine_to_names = {'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']},
                  cuisines_list = ['Chinese', 'Thai'])


