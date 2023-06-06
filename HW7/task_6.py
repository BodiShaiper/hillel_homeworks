def min_arrow_rotations(S):
    arrow_counts = {'^': 0, 'v': 0, '<': 0, '>': 0}

    max_count = 0
    for arrow in S:
        arrow_counts[arrow] += 1
        max_count = max(max_count, arrow_counts[arrow])

    total_arrows = len(S)
    rotations_needed = total_arrows - max_count

    return rotations_needed


print(min_arrow_rotations("^vv<v"))
print(min_arrow_rotations("v>>>vv"))
print(min_arrow_rotations("<<<"))
