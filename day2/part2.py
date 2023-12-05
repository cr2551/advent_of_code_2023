import os 
from cube_conondrum import Game


script_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_path, 'input.txt')

def calc_power():
    """ Get the sum of all the product of the minimum number of cubes for each game.
    """
    total = 0
    file = open(file_path, 'r')
    line = file.readline().strip()
    colors = ['red', 'green', 'blue']
    while line:
        colors_dict = dict.fromkeys(colors, 0)
        game = Game(line)
        # convert each list of game_dicts into a single dictionary
        # min_cubes is the dictionary containing the min number of cubes of each color
        # print(game.game_dicts)
        min_cubes = combine_dicts(game.game_dicts, colors_dict)
        # print(min_cubes)
        # counter for the product of the num of cubes in each game/line
        game_power = 1
        # calculate product of the min number of cubes
        for val in min_cubes.values():
            game_power *= val
        # add it to the total
        total += game_power
        # prepare for next line
        line = file.readline().strip()
    file.close()
    print(total)
    return total
        

# cubes()

test1 = [{'blue': 12, 'red': 15, 'green': 2}, {'red': 17, 'green': 8, 'blue': 5}, {'red': 8, 'blue': 17}, {'green': 9, 'blue': 1, 'red': 4}]
def combine_dicts(dict_list: list, base_dictionary: dict) -> dict:
    """Take in a list of dictionaries and combine them by key. The value for that key will be the largest number of all those
    values for the given key. 
    dict_list: a list of dictionaries
    base_dictionary: a dictionary in the form {'key1': [], 'key2': [], ...}. This dictionary will be returned with the list being replaced by the largest value in the list
    
    Example:
    input: [{'blue': 12, 'red': 15, 'green': 2}, {'red': 17, 'green': 8, 'blue': 5}, {'red': 8, 'blue': 17}, {'green': 9, 'blue': 1, 'red': 4}]
    output: {'blue': 17, 'red': 17, 'green': 9}
    """
    
 
    for dictionary in dict_list:
        for key in dictionary:

            if key in base_dictionary.keys():
                previous_cube_count = base_dictionary[key]
                current_cube_count = dictionary[key]
                if current_cube_count > previous_cube_count:
                    base_dictionary[key] = current_cube_count
    return base_dictionary


def main():
    calc_power()


if __name__ == '__main__':
    main()



