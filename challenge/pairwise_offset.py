from itertools import tee, zip_longest, chain
def pairwise_offset(sequence, offset=0, fillvalue="*"):
    # convert to list
    # list_sequence = []
    # if not isinstance(sequence, list):
    #     list_sequence = list(sequence)
    # else:
    #     list_sequence = sequence

    # top_seq = list_sequence + ([fillvalue] * offset)
    # bot_seq = ([fillvalue] * offset) + list_sequence

    # return zip(top_seq,bot_seq)

    # option 2
    clone1, clone2 = tee(sequence, 2)
    return zip_longest(clone1, chain(fillvalue * offset, clone2), fillvalue=fillvalue)