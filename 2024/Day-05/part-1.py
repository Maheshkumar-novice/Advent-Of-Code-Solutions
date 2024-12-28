with open("input.txt") as f:  # noqa: PTH123, INP001, D100
    rules, updates = f.read().split("\n\n")

    rules_dict = {}
    for rule in rules.split("\n"):
        before, after = rule.split("|")

        if before not in rules_dict:
            rules_dict[before] = {"before": [], "after": []}
        if after not in rules_dict:
            rules_dict[after] = {"before": [], "after": []}

        rules_dict[before]["after"].append(after)
        rules_dict[after]["before"].append(before)

    result = 0
    for update in updates.split("\n"):
        update, flag = update.split(","), True  # noqa: PLW2901
        for idx, page in enumerate(update[1:]):
            if update[idx] not in rules_dict[page]["before"]:
                flag = False
                break
        if flag:
            result += int(update[len(update) // 2])

    print(result)  # noqa: T201

"""
4662
         3819 function calls in 0.002 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.001    0.001    0.002    0.002 part-1.py:1(<module>)
     1371    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
     2352    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
       85    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
"""
