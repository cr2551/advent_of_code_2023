file_path = 'input'
# file_path = 'sample_input.txt'

def get_points_list():
    """create an array of the points from each scratchcard/line"""
    points_arr = []
    with open(file_path, 'r') as file:
        line = file.readline().strip()
        while line:
            card = line.split(':')[1]
            winning_numbers = card.split('|')[0].split()
            # the actual numbers that we have
            our_numbers = card.split('|')[1].split()
            card_points = 0
            for num in our_numbers:
                if num in winning_numbers:
                    if card_points == 0:
                        card_points = 1
                    else:
                        card_points *= 2
            points_arr.append(card_points)
            line = file.readline().strip()
    return points_arr

total = sum(get_points_list())
print(total)
                
