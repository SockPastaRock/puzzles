#!/usr/bin/python3

# {{{ Imports

import random
import collections

# }}}
# {{{ Constants

N_FACES = 6  # Number of faces on each die
N_DICE = 3  # Number of dice

# }}}
# {{{ Functions

# {{{ main


def main():

    sample_size = 100000
    s = 0

    for _ in range(sample_size):
        s += rollSame(N_DICE, N_FACES)

    print(s/sample_size)

# }}}
# {{{ rollSame


def rollSame(n_dice, n_faces):
    """Docstring for rollSame"""

    dice_pool = n_dice
    reserve_size = 0
    iterations = 0

    while dice_pool > 0:
        iterations += 1
        rolls = [int(random.uniform(0, n_faces)) + 1 for _ in range(dice_pool)]

        # calculate the frequency of each item
        data = collections.Counter(rolls)
        data_list = dict(data)

        # Find the highest frequency
        max_count = max(list(data.values()))
        mode = [num for num, freq in data_list.items() if freq == max_count][0]

        if max_count > reserve_size:
            reserve_value = mode
            reserve_size = max_count
            dice_pool = n_dice - max_count
        else:
            reserve_size += data[reserve_value]
            dice_pool -= data[reserve_value]

    return iterations

# }}}

# }}}


if __name__=="__main__":
    main()
