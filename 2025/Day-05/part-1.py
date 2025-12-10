with open("input.txt") as f:
    ranges, ingredients = f.read().split("\n\n")
    ranges = [tuple(map(int, range_.strip().split("-"))) for range_ in ranges.split()]
    ingredients = list(map(int, ingredients.strip().split()))
    result = 0
    for i in ingredients:
        for x, y in ranges:
            if x <= i <= y:
                result += 1
                break
    print(result)
