import knapsack


def calculate(usb_size, memes):
    """
    Function that solves the knapsack problem.
    Places the most expensive memes without repeating on the USB stick.

    :param usb_size: Capacity of usb stick in GiB
    :param memes: List of tuples. In each tuple there is the name, size in MiB and value.
    :return:Function return most expensive set of memes and name of each memes in tuple
    """
    capacity = usb_size * 1024
    memes = list(set(memes))
    meme_weight, meme_size, meme_name = [i[1] for i in memes], [i[2] for i in memes], [i[0] for i in memes]
    k = knapsack.knapsack(meme_weight, meme_size).solve(capacity)
    return k[0], tuple([meme_name[i] for i in k[1]])
