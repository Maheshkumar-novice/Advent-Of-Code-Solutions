#!/usr/bin/env python3
import os
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
import argparse

@dataclass
class DayStatus:
    year: int
    day: int
    has_part1: bool
    has_part2: bool

def check_day_status(year: int, day_dir: Path) -> DayStatus:
    """Check the status of files in a day directory"""
    return DayStatus(
        year=year,
        day=int(day_dir.name.split('-')[1]),
        has_part1=(day_dir / "part-1.py").exists(),
        has_part2=(day_dir / "part-2.py").exists()
    )

def create_year_status_table(days: List[DayStatus]) -> str:
    """Create a markdown table showing completion status for a specific year"""
    header = [
        "| Day    | Part 1  | Part 2  |",
        "|--------|---------|---------|"
    ]
    
    rows = []
    for day in sorted(days, key=lambda x: x.day):
        rows.append(
            f"| Day {day.day:2d} | "
            f"{'✅' if day.has_part1 else '❌'}     | "
            f"{'✅' if day.has_part2 else '❌'}     |"
        )
    
    return "\n".join(header + rows)

def create_year_statistics(year: int, days: List[DayStatus]) -> str:
    """Create statistics about completion status for a specific year"""
    total_days = len(days)
    completed_part1 = sum(1 for day in days if day.has_part1)
    completed_part2 = sum(1 for day in days if day.has_part2)
    stars = completed_part1 + completed_part2
    max_stars = total_days * 2
    
    return f"""### Year {year} Statistics
- Total Days: {total_days}
- Stars Collected: {stars}/{max_stars}
- Part 1 Completion: {completed_part1}/{total_days} ({completed_part1/total_days*100:.1f}%)
- Part 2 Completion: {completed_part2}/{total_days} ({completed_part2/total_days*100:.1f}%)"""

def create_overall_statistics(all_days: List[DayStatus]) -> str:
    """Create overall statistics across all years"""
    total_days = len(all_days)
    completed_part1 = sum(1 for day in all_days if day.has_part1)
    completed_part2 = sum(1 for day in all_days if day.has_part2)
    total_stars = completed_part1 + completed_part2
    max_stars = total_days * 2
    
    years_completed = {day.year for day in all_days}
    max_possible_days = len(years_completed) * 25
    
    return f"""## Overall Progress
- Years Attempted: {len(years_completed)}
- Total Days Attempted: {total_days}/{max_possible_days}
- Total Stars Collected: {total_stars}/{max_stars}
- Overall Completion Rate: {(total_stars/(max_stars if max_stars > 0 else 1))*100:.1f}%"""

def create_main_header() -> str:
    """Create the main header section"""
    return """# 🎄 Advent of Code Solutions 🎄

This repository contains my solutions for [Advent of Code](https://adventofcode.com/) challenges across multiple years.

Each year's solutions are organized in their respective directories."""

def generate_consolidated_readme(root_dir: Path) -> str:
    """Generate the complete consolidated README content"""
    # Get all year directories (in YYYY format)
    year_dirs = [d for d in root_dir.iterdir() if d.is_dir() and d.name.isdigit() and len(d.name) == 4]
    
    if not year_dirs:
        return "# Advent of Code\nNo solutions yet!"
    
    # Collect all days across all years
    all_days = []
    year_days: Dict[int, List[DayStatus]] = {}
    
    for year_dir in year_dirs:
        year = int(year_dir.name)
        day_dirs = [d for d in year_dir.iterdir() if d.is_dir() and d.name.startswith("Day-")]
        
        if day_dirs:
            days = [check_day_status(year, day_dir) for day_dir in day_dirs]
            all_days.extend(days)
            year_days[year] = days
    
    # Create README sections
    sections = [create_main_header(), create_overall_statistics(all_days)]
    
    # Add year-specific sections
    sections.append("\n## Year-by-Year Progress")
    for year in sorted(year_days.keys(), reverse=True):
        sections.extend([
            f"\n### {year}",
            create_year_status_table(year_days[year]),
            create_year_statistics(year, year_days[year])
        ])
    
    return "\n\n".join(sections)

def main():
    parser = argparse.ArgumentParser(description='Generate consolidated README for Advent of Code solutions')
    parser.add_argument('--root', type=str, default='.', help='Root directory containing year directories')
    args = parser.parse_args()
    
    root_dir = Path(args.root)
    if not root_dir.exists():
        print(f"Root directory {args.root} not found!")
        return
        
    readme_content = generate_consolidated_readme(root_dir)
    readme_path = root_dir / "README.md"
    
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    print(f"Generated consolidated README at {readme_path}")

if __name__ == "__main__":
    main()