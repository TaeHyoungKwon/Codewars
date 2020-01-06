
# TODO: 다 폿품

def find_missing_element_half_side(sequence, mid_pos, diff):
    sequence = sequence[mid_pos:] if sequence[0] + diff * mid_pos == sequence[mid_pos] else sequence[:mid_pos]
    for idx, ele in enumerate(sequence):
        if ele + diff != sequence[idx + 1]:
            return ele + diff


def find_missing(sequence):
    mid_pos = 0 + (len(sequence) - 0) // 2
    diff = (sequence[-1] - sequence[0]) // len(sequence)
    find_missing_element_half_side(sequence, mid_pos, diff)