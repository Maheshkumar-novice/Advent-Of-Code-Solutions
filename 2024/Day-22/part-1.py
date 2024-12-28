from functools import cache


@cache
def _next_secret(number: int) -> int:
    secret = (number ^ (number * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    return (secret ^ (secret * 2048)) % 16777216


with open("input.txt") as f:
    secrets = list(map(int, f.read().splitlines()))

result = 0
for secret in secrets:
    for _ in range(2000):
        secret = _next_secret(secret)  # noqa: PLW2901
    result += secret
print(result)
