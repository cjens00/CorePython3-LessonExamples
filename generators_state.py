# Generator 1: Take()
#
def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


#
def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


#
def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    # To evaluate the entire generator first, wrap with list()
    # for item in take(3, list(distinct(items))):
    for item in take(3, distinct(items)):
        print(item)


if __name__ == "__main__":
    run_pipeline()
