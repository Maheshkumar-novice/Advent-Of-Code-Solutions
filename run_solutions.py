#!/usr/bin/env python3
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table


@dataclass
class Result:
    day: int
    part: int
    output: str
    error: Optional[str]
    time: float
    status: bool


def run_solution(day_dir: Path, part: int, input_file: Path) -> Result:
    """Run a single solution and return the result"""
    start_time = time.time()
    script = day_dir / f"part-{part}.py"
    executable = sys.executable

    if not script.exists():
        script = day_dir / f"part-{part}.rb"
        executable = "ruby"

        if not script.exists():
            return Result(
                day=int(day_dir.name.split("-")[1]),
                part=part,
                output="",
                error="Script not found",
                time=0.0,
                status=False,
            )

    # Change to the day directory before running the solution
    original_dir = Path.cwd()
    try:
        os.chdir(day_dir)  # Change to day directory so relative paths work

        # Run the solution script with the input file as argument
        result = subprocess.run(
            [executable, script.name, input_file.name],
            capture_output=True,
            text=True,
            timeout=30,  # 10 second timeout
        )

        execution_time = time.time() - start_time

        return Result(
            day=int(day_dir.name.split("-")[1]),
            part=part,
            output=result.stdout.strip(),
            error=result.stderr if result.stderr else None,
            time=execution_time,
            status=result.returncode == 0,
        )

    except subprocess.TimeoutExpired:
        return Result(
            day=int(day_dir.name.split("-")[1]),
            part=part,
            output="",
            error="Timeout (>10s)",
            time=10.0,
            status=False,
        )
    except Exception as e:
        return Result(
            day=int(day_dir.name.split("-")[1]),
            part=part,
            output="",
            error=str(e),
            time=time.time() - start_time,
            status=False,
        )
    finally:
        os.chdir(original_dir)  # Always restore original directory


def format_time(seconds: float) -> str:
    """Format time in a human-readable way"""
    if seconds < 0.001:
        return f"{seconds*1000000:.0f}µs"
    elif seconds < 1:
        return f"{seconds*1000:.0f}ms"
    else:
        return f"{seconds:.2f}s"


def create_results_table(results: list[Result]) -> Table:
    """Create a rich table with the results"""
    table = Table(title="Advent of Code Solutions")

    table.add_column("Day", justify="right", style="cyan")
    table.add_column("Part", justify="right", style="magenta")
    table.add_column("Status", justify="center")
    table.add_column("Time", justify="right", style="green")
    table.add_column("Output", style="blue")
    table.add_column("Error", style="red")

    for result in sorted(results, key=lambda x: (x.day, x.part)):
        status = "✅" if result.status else "❌"
        table.add_row(
            f"Day {result.day:02d}",
            str(result.part),
            status,
            format_time(result.time),
            result.output if result.output else "",
            result.error if result.error else "",
        )

    return table


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <year>")
        sys.exit(1)

    year = sys.argv[1]
    year_dir = Path(year)

    if not year_dir.exists():
        print(f"Year directory {year} not found!")
        sys.exit(1)

    console = Console()

    # Get all day directories
    day_dirs = sorted(
        [d for d in year_dir.iterdir() if d.is_dir() and d.name.startswith("Day-")]
    )

    if not day_dirs:
        print(f"No day directories found in {year}!")
        sys.exit(1)

    results = []
    total_time = time.time()

    # Create a progress message
    console.print(
        Panel.fit(f"Running Advent of Code {year} solutions...", style="bold blue")
    )

    for day_dir in day_dirs:
        input_file = day_dir / "input.txt"
        if not input_file.exists():
            continue

        for part in [1, 2]:
            result = run_solution(day_dir, part, input_file)
            results.append(result)
        # Print results table
        console.clear()
        console.print(create_results_table(results))

    total_time = time.time() - total_time

    # Print summary
    successful = sum(1 for r in results if r.status)
    total = len(results)

    summary = Table.grid()
    summary.add_row(
        f"Total time: [green]{format_time(total_time)}[/]",
        f" Success rate: [{'green' if successful == total else 'red'}]{successful}/{total}[/]",
    )

    console.print(Panel(summary, title="Summary", style="bold"))


if __name__ == "__main__":
    main()
