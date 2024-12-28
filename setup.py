#!/usr/bin/env python3
import os
import sys
from pathlib import Path

import browser_cookie3  # pip install browser-cookie3
import requests


def get_aoc_cookie():
    """Extract AOC session cookie from browsers"""
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
        except:
            continue

    return None


def create_aoc_directory(day: int, year: int, session_cookie: str):
    # Input validation
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <current-day-number> <year>")
        sys.exit(1)

    # Format day with leading zero
    day_str = f"{day:02d}"

    # Create year directory if it doesn't exist
    year_dir = Path(str(year))
    day_dir = year_dir / f"Day-{day_str}"

    # Check if day directory already exists
    if day_dir.exists():
        print(f"{day_dir} already exists.")
        sys.exit(1)

    # Create directories
    day_dir.mkdir(parents=True)

    # Create files
    (day_dir / "sample.txt").touch()
    (day_dir / "input.txt").touch()

    # Create Python files with initial content
    template = """
with open("sample.txt") as f:
    input_data = f.read()
""".strip()

    with open(day_dir / "part-1.py", "w") as f:
        f.write(template)

    with open(day_dir / "part-2.py", "w") as f:
        f.write(template)

    # Download input file
    headers = {"Cookie": f"session={session_cookie}", "Connection": "close"}

    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", headers=headers
    )

    if response.status_code == 200:
        with open(day_dir / "input.txt", "w") as f:
            f.write(response.text)
        print(f"Successfully created and downloaded input for Day {day}")
    else:
        print(f"Failed to download input file. Status code: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <current-day-number> <year>")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
        year = int(sys.argv[2])
    except ValueError:
        print("Day and year must be integers")
        sys.exit(1)

    # Try to get cookie from browser
    session_cookie = get_aoc_cookie()
    if not session_cookie:
        # Fallback to environment variable
        session_cookie = os.getenv("AOC_SESSION_COOKIE")
        if not session_cookie:
            print(
                "Could not find AOC session cookie in browsers or environment variable"
            )
            sys.exit(1)

    create_aoc_directory(day, year, session_cookie)
