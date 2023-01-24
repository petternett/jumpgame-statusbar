def map_to_coords(input_map):
    output_map = []

    for y, row in enumerate(input_map):
        for x, col in enumerate(row):
            if col:
                output_map.append((x, y))

    return output_map
