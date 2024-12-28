"""My Initial Solution.

import hashlib.

with open("input.txt") as f:
    input_data = f.read().strip()
    for i in range(1, 10000000):
        if hashlib.md5((input_data + str(i)).encode()).hexdigest().startswith("000000"):  # noqa: S324
            print(i)
            break
"""

# Now the parallelized faster version.

import hashlib
from multiprocessing import Pool, cpu_count


def _find_hash(args: tuple) -> int | None:
    input_data, start, chunk_size = args
    # Pre-encode the input string to avoid repeated encoding
    base = input_data.encode()
    for i in range(start, start + chunk_size):
        # Use bytes concatenation instead of string concatenation
        current = base + str(i).encode()
        # Only compute the first 3 bytes (6 hex digits) instead of full hash
        if hashlib.md5(current).digest()[:3] == b"\x00\x00\x00":  # noqa: S324
            return i
    return None


def _mine_hash(input_data: str, chunk_size: int = 1000000) -> int | None:
    # Use all available CPU cores
    num_cores = cpu_count()

    with Pool(num_cores) as pool:
        # Create chunks of work for each process
        chunks = ((input_data, i, chunk_size) for i in range(0, 10000000, chunk_size))

        # Map the work across processes and get first valid result
        for result in pool.imap_unordered(_find_hash, chunks):
            if result is not None:
                pool.terminate()  # Stop all other processes
                return result

    return None


if __name__ == "__main__":
    # Read input only once
    with open("input.txt") as f:
        input_data = f.read().strip()

    result = _mine_hash(input_data)
    if result:
        print(result)
