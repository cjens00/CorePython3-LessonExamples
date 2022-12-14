# with-blocks and context managers
# for the automatic opening and closing of resources.


def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]

