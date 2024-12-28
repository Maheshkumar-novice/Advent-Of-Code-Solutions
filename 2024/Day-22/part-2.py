"""Too much time and memory. Will try to optimize later."""

import sys
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from functools import cache


@cache
def _next_secret(number: int) -> int:
    secret = (number ^ (number * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    return (secret ^ (secret * 2048)) % 16777216


with open("input.txt") as f:
    secrets = list(map(int, f.read().splitlines()))

if len(sys.argv) < 2:  # noqa: PLR2004
    result = 0
    d = defaultdict(dict)
    for secret in secrets:
        diffs, prev, main_secret = [], None, secret
        for _ in range(2000):
            if prev is None:
                prev = secret
            else:
                prev_last = int(str(prev)[-1])
                curr_last = int(str(secret)[-1])
                diffs.append(curr_last - prev_last)
                prev = secret

                if len(diffs) >= 4:  # noqa: PLR2004
                    key = tuple(diffs[-4:])
                    if key not in d[main_secret]:
                        d[main_secret][key] = curr_last

            secret = _next_secret(secret)  # noqa: PLW2901
        result += secret

    mega = set()
    for secret in secrets:
        mega |= d[secret].keys()

    m = -1
    for dl in mega:
        total = 0
        for secret in secrets:
            if dl in d[secret]:
                total += d[secret][dl]
        m = max(total, m)

    print(m)

else:

    def _do1(secrets: list) -> defaultdict:
        result = 0
        d = defaultdict(dict)
        for secret in secrets:
            diffs, prev, main_secret = [], None, secret
            for _ in range(2000):
                if prev is None:
                    prev = secret
                else:
                    prev_last = int(str(prev)[-1])
                    curr_last = int(str(secret)[-1])
                    diffs.append(curr_last - prev_last)
                    prev = secret

                    if len(diffs) >= 4:  # noqa: PLR2004
                        key = tuple(diffs[-4:])
                        if key not in d[main_secret]:
                            d[main_secret][key] = curr_last

                secret = _next_secret(secret)  # noqa: PLW2901
            result += secret
        return d

    with ProcessPoolExecutor(max_workers=2) as e:
        futures = [e.submit(_do1, secrets[i : i + 1000]) for i in range(0, len(secrets), 1000)]
        result = [k.result() for k in futures]
        new_d = {}
        for k in result:
            new_d |= k
    d = new_d

    mega = set()
    for secret in secrets:
        mega |= d[secret].keys()

    def _do(l: list, d: defaultdict) -> int:  # noqa: E741
        m = -1
        for dl in l:
            total = 0
            for secret in secrets:
                if dl in d[secret]:
                    total += d[secret][dl]
            m = max(total, m)
        return m

    with ProcessPoolExecutor(max_workers=5) as e:
        mega = list(mega)
        lenght = len(mega)
        futures = [e.submit(_do, mega[i : i + 10000], d) for i in range(0, lenght, 10000)]
        result = [k.result() for k in futures]
        print(max(result))
