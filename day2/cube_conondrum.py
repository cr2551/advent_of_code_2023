import os

script_location = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_location, 'input.txt')


def possible_games(file_path):
    """get the Ids of the games that are possible"""
    # list to contain the ids of the games that are possible.
    games_possible_id= []
    #open file
    file = open(file_path, 'r')
    line = file.readline().strip()
    while line:
        game = Game(line)
        if game.game_is_possible():
            games_possible_id.append(game.id)
            # print(game.game_dicts)
        line = file.readline().strip()
    
    file.close()
    total = sum(games_possible_id)
    return total
        

def _string_to_dict(string: str):
    """given a string convert it into a dicitionary with the digits being the value
        and the other word being the key    
    """
    d = {}
    key = ''
    val =  ''
    for char in string:
        if char.isalpha():
            key += char
        elif char.isdigit():
            val += char
    if val == '':
        val = 0
    d[key] = int(val)
    return d
            
test1 = [' 9 green', ' 1 blue', ' 4 red']

def cube_count(draw: list) -> dict:
    """Takes in a list of strings containing a number and a word and returns a dictionary
        with the word as the key and num as the value.
        this function will call the `string_to_dict` function and then merge those dictionaries.

        output is in the form of: {'green': 9, 'blue': 1, 'red': 4}
    """
    complete = {}
    for s in draw:
        d = _string_to_dict(s)
        for k in d:
            complete[k] = d[k]
    return complete


def draw_is_possible(draw: dict) -> bool:
    """returns boolean depending on if a draw is possible given the initial amount of cubes
        This function will be called once for each dictionary by the function `game_is_possible`
    """
    cubes_in_bag = {'red': 12, 'green': 13, 'blue': 14}
    for key in draw:
        if draw[key] > cubes_in_bag[key]:
            return False
    return True
 

def _game_is_possible(dictionaries: list) -> bool:
    """Take in a list of dictionaries"""
    for d in dictionaries:
        if not draw_is_possible(d):
            return False
    return True


class Game:
    def __init__(self, line):
    #parse each line to get the id and how many cubes of what color
        id, game_string = line.split(':')
    # print(id)
        self.id = int(id.split(' ')[1])
    # a list containing the individual draws of cubes from the bag
        draws = game_string.split(';')
    # a list of dictionaries that will contain each draw in the from of: {'green': 9, 'blue': 1, 'red': 4}
        self.game_dicts = []

        for draw in draws:
            cubes = draw.split(',')
            # get each draw in dict format
            draw_dict = cube_count(cubes)
            # list of dictionaries
            self.game_dicts.append(draw_dict)
    def game_is_possible(self):
        return _game_is_possible(self.game_dicts)
    
    
            
if __name__ == '__main__':

    print(possible_games(file_path))