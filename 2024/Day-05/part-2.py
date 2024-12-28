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
        update, incorrect = update.split(","), False  # noqa: PLW2901
        for idx, page in enumerate(update[1:]):
            if update[idx] not in rules_dict[page]["before"]:
                incorrect = True
                break

        if incorrect:
            updating = True
            while updating:
                updating = False
                for idx, page in enumerate(update[1:]):
                    if update[idx] not in rules_dict[page]["before"]:
                        updating = True
                        update[idx], update[idx + 1] = update[idx + 1], update[idx]
            result += int(update[len(update) // 2])

    print(result)  # noqa: T201

"""
5900
         3841 function calls in 0.009 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.008    0.008    0.009    0.009 part-2.py:1(<module>)
     1371    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
     2352    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      107    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
"""
