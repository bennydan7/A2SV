def get_row_index(row):
    if row == 0:
        return [1]
    prev_row = get_row_index(row - 1)
    return [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]
