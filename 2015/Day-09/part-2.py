from itertools import pairwise, permutations

with open("input.txt") as f:
    distance_between_locations = {}
    distinct_locations = set()
    for line in f:
        src, dest_with_distance = line.strip().split(" to ")
        dest, distance = dest_with_distance.split(" = ")
        distance_between_locations[(src, dest)] = int(distance)
        distance_between_locations[(dest, src)] = int(distance)
        distinct_locations.add(src)
        distinct_locations.add(dest)

    print(distance_between_locations)
    print(distinct_locations)

    current_result = -1
    for perm in permutations(list(distinct_locations), len(distinct_locations)):
        covered_distance = 0
        print(" -> ".join(perm))
        for src, dest in pairwise(perm):
            print(" -> ", src, dest)
            covered_distance += distance_between_locations.get((src, dest))
        print(" -> ", covered_distance)
        current_result = max(current_result, covered_distance)

    print("Max distance: ", current_result)
