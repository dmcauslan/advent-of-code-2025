def read_input_file(day, one_or_two):
    path = f"inputs/day{day}.{one_or_two}.txt"
    with open(path) as f:
        return [r.strip() for r in f.readlines() if r]