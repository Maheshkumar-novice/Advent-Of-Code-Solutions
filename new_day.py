#!/usr/bin/env python3
"""Make a day's folder and download its input.

    uv run new_day.py <day> <year>

Safe to run again: it only adds files that are missing, never overwrites
your code, and downloads the input only while input.txt is empty.
"""

import os
import sys
from pathlib import Path

import browser_cookie3
import requests

TEMPLATE = """
import sys

# uv run part-1.py sample.txt  -> the example
# uv run part-1.py             -> your input
path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(path) as f:
    input_data = f.read()
""".lstrip()


def get_aoc_cookie():
    """Find the adventofcode.com session cookie in a browser, or in AOC_SESSION_COOKIE."""
    browsers = [
        (browser_cookie3.chrome, "Chrome"),
        (browser_cookie3.firefox, "Firefox"),
        (browser_cookie3.edge, "Edge"),
        (browser_cookie3.safari, "Safari"),
    ]

    for browser_func, browser_name in browsers:
        try:
            cookies = browser_func(domain_name="adventofcode.com")
            for cookie in cookies:
                if cookie.name == "session":
                    print(f"Found cookie in {browser_name}")
                    return cookie.value
        except Exception:
            continue

    return os.getenv("AOC_SESSION_COOKIE")


def make_day_folder(day: int, year: int) -> Path:
    """Create the day's folder and any missing files. Existing files are left alone."""
    day_dir = Path(str(year)) / f"Day-{day:02d}"
    if day_dir.exists():
        print(f"{day_dir} already exists, adding only what's missing.")
    day_dir.mkdir(parents=True, exist_ok=True)

    for part in ("part-1", "part-2"):
        script = day_dir / f"{part}.py"
        if not script.exists():
            script.write_text(TEMPLATE.replace("part-1", part))

    (day_dir / "sample.txt").touch()
    (day_dir / "input.txt").touch()
    return day_dir


def download_input(day: int, year: int, day_dir: Path) -> bool:
    """Download the input into input.txt, unless it already has something in it."""
    input_file = day_dir / "input.txt"
    if input_file.stat().st_size > 0:
        print(f"{input_file} already has your input.")
        return True

    session_cookie = get_aoc_cookie()
    if not session_cookie:
        print("Could not find your session cookie in a browser or in AOC_SESSION_COOKIE.")
        return False

    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={"Cookie": f"session={session_cookie}", "Connection": "close"},
        timeout=30,
    )
    if response.status_code != 200:
        print(f"Couldn't download the input (status {response.status_code}). Run the same command again later.")
        return False

    input_file.write_text(response.text)
    print(f"Downloaded the input for {year} day {day}.")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <day> <year>")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
        year = int(sys.argv[2])
    except ValueError:
        print("Day and year must be whole numbers.")
        sys.exit(1)

    folder = make_day_folder(day, year)
    sys.exit(0 if download_input(day, year, folder) else 1)
