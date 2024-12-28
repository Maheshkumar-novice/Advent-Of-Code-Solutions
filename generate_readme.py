#!/usr/bin/env python3
import os
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
import argparse
from datetime import datetime
import sys
from rich.console import Console
from rich.progress import track
from rich import print as rprint

console = Console()

@dataclass
class DayStatus:
    year: int
    day: int
    has_part1: bool
    has_part2: bool

class AoCStats:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.current_year = datetime.now().year
        
    def validate_directory_structure(self) -> bool:
        """Validate the directory structure and provide helpful feedback"""
        if not self.root_dir.exists():
            console.print(f"[red]Error: Directory '{self.root_dir}' not found![/red]")
            return False
            
        year_dirs = [d for d in self.root_dir.iterdir() if d.is_dir() and d.name.isdigit() and len(d.name) == 4]
        if not year_dirs:
            console.print(f"[yellow]Warning: No year directories (YYYY format) found in '{self.root_dir}'[/yellow]")
            console.print("Expected structure:")
            console.print("  root/")
            console.print("    ├── 2024/")
            console.print("    │   ├── Day-1/")
            console.print("    │   └── Day-2/")
            console.print("    └── 2023/")
            console.print("        ├── Day-1/")
            console.print("        └── Day-2/")
            return False
        return True

    def check_day_status(self, year: int, day_dir: Path) -> DayStatus:
        """Check the status of files in a day directory"""
        return DayStatus(
            year=year,
            day=int(day_dir.name.split('-')[1]),
            has_part1=(day_dir / "part-1.py").exists() or (day_dir / "part-1.rb").exists(),
            has_part2=(day_dir / "part-2.py").exists() or (day_dir / "part-2.rb").exists(),
        )

    def create_year_status_table(self, days: List[DayStatus]) -> str:
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

    def create_year_statistics(self, year: int, days: List[DayStatus]) -> str:
        """Create statistics about completion status for a specific year"""
        total_days = len(days)
        if total_days == 0:
            return f"### Year {year} Statistics\n- No solutions yet!"
            
        completed_part1 = sum(1 for day in days if day.has_part1)
        completed_part2 = sum(1 for day in days if day.has_part2)
        stars = completed_part1 + completed_part2
        max_stars = total_days * 2
        
        # Calculate percentage of year completed
        days_in_year = 25  # Total days in AoC
        completion_percentage = (total_days / days_in_year) * 100
        
        stats = f"""### Year {year} Statistics
- Progress: {total_days}/{days_in_year} days ({completion_percentage:.1f}% of challenges attempted)
- Stars Collected: {stars}/{max_stars} ({(stars/max_stars*100):.1f}% of attempted challenges completed)
- Part 1 Completion: {completed_part1}/{total_days} ({completed_part1/total_days*100:.1f}%)
- Part 2 Completion: {completed_part2}/{total_days} ({completed_part2/total_days*100:.1f}%)"""

        if year == self.current_year:
            remaining_days = 25 - total_days
            if remaining_days > 0:
                stats += f"\n- Remaining Challenges: {remaining_days} days"
                
        return stats

    def create_overall_statistics(self, all_days: List[DayStatus]) -> str:
        """Create overall statistics across all years"""
        if not all_days:
            return "## Overall Progress\n- No solutions yet!"
            
        total_days = len(all_days)
        completed_part1 = sum(1 for day in all_days if day.has_part1)
        completed_part2 = sum(1 for day in all_days if day.has_part2)
        total_stars = completed_part1 + completed_part2
        max_stars = total_days * 2
        
        years_completed = {day.year for day in all_days}
        years_list = sorted(years_completed, reverse=True)
        years_str = ", ".join([str(y) for y in years_list])
        
        total_possible_days = len(years_completed) * 25
        total_possible_stars = total_possible_days * 2
        
        return f"""## Overall Progress
- Years Participated: {years_str}
- Days Completed: {total_days}/{total_possible_days} ({(total_days/total_possible_days*100):.1f}% of all possible days)
- Total Stars: {total_stars}/{total_possible_stars} ({(total_stars/total_possible_stars*100):.1f}% of all possible stars)
- Average Stars per Day: {(total_stars/total_days):.1f} (when attempted)"""

    def create_main_header(self) -> str:
        """Create the main header section with badges"""
        stars_repo_name = self.root_dir.resolve().name
        return """# 🎄 Advent of Code Solutions 🎄

This repository contains my solutions for [Advent of Code](https://adventofcode.com/) challenges across multiple years.

> [!TIP]
> Each year's solutions are organized in their respective directories. Solutions are automatically tracked and this README is updated after each push."""

    def generate_readme(self) -> str:
        """Generate the complete README content"""
        if not self.validate_directory_structure():
            return None
            
        # Get all year directories
        year_dirs = [d for d in self.root_dir.iterdir() 
                    if d.is_dir() and d.name.isdigit() and len(d.name) == 4]
        
        if not year_dirs:
            return "# Advent of Code\nNo solutions yet!"
        
        # Collect all days across all years
        all_days = []
        year_days: Dict[int, List[DayStatus]] = {}
        
        for year_dir in track(year_dirs, description="Processing years..."):
            year = int(year_dir.name)
            day_dirs = [d for d in year_dir.iterdir() 
                       if d.is_dir() and d.name.startswith("Day-")]
            
            if day_dirs:
                days = [self.check_day_status(year, day_dir) for day_dir in day_dirs]
                all_days.extend(days)
                year_days[year] = days
        
        # Create README sections
        sections = [
            self.create_main_header(),
            self.create_overall_statistics(all_days),
            "\n## Year-by-Year Progress"
        ]
        
        # Add year-specific sections
        for year in sorted(year_days.keys(), reverse=True):
            sections.extend([
                f"\n### {year}",
                self.create_year_status_table(year_days[year]),
                self.create_year_statistics(year, year_days[year])
            ])
        
        return "\n\n".join(sections)

def main():
    parser = argparse.ArgumentParser(
        description='Generate consolidated README for Advent of Code solutions',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example directory structure:
  repository_root/
    ├── 2024/
    │   ├── Day-1/
    │   │   ├── part-1.py
    │   │   └── part-2.py
    │   └── Day-2/
    ├── 2023/
    │   ├── Day-1/
    │   └── Day-2/
    └── README.md
        """
    )
    parser.add_argument('--root', type=str, default='.',
                      help='Root directory containing year directories (default: current directory)')
    args = parser.parse_args()
    
    try:
        stats = AoCStats(Path(args.root))
        readme_content = stats.generate_readme()
        
        if readme_content:
            readme_path = Path(args.root) / "README.md"
            with open(readme_path, 'w') as f:
                f.write(readme_content)
            console.print(f"[green]Successfully generated README at {readme_path}[/green]")
            
            # Preview the changes only in interactive terminal
            if sys.stdout.isatty() and not os.getenv('GITHUB_ACTIONS'):
                console.print("\n[yellow]Preview of the first 500 characters:[/yellow]")
                console.print(readme_content[:500] + "...\n")
    except Exception as e:
        console.print(f"[red]Error generating README: {str(e)}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()