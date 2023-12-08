import re

import os
script_path = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_path, 'sample_input.txt')
file_path = os.path.join(script_path, 'input')


def count_copies():
    file = open(file_path, 'r')
    # dict to count how many copies of each card we have
    copies = {}
    # keep track of which card number we are in
    card_num = 1

    # do a positive look-behind to match everything after the colon exept for the colon
    pattern  = r'(?<=: ).*'
    line = file.readline().strip()
    while line:
        # split_line  = re.split(pattern, line)
        card = re.findall(pattern, line)
        card = card[0].split('|')
        winning_nums_list = card[0].split()
        our_nums = card[1].split()
    
        matches = 0

        # check how many matches we have
        for i in winning_nums_list:
            if i in our_nums:
                matches += 1

        if not copies.get(str(card_num)):
            copies[str(card_num)] = 1
        else:
            copies[str(card_num)] += 1
        # the amount of copies the current card
        card_count = copies.get(str(card_num))
        add_copies(card_num, matches, copies, counter=card_count)

        line = file.readline().strip()
        card_num += 1    
            
    file.close()
    return copies

# we need to repeat this process for each copy of the current card
def add_copies(card_num, matches, copies, counter):
    while counter > 0:
        for i in range(card_num + 1, card_num+matches+1):
            if copies.get(str(i)):
                copies[str(i)] += 1
            else:
                copies[str(i)] = 1
        counter -= 1 

    





if __name__ == '__main__':
    copies_per_card = count_copies()
    total = sum(copies_per_card.values())
    print(total)
