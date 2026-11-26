# FixtureForge

A round-robin tournament management system in Python. FixtureForge generates every
fixture for a league, records match results, maintains a live points table, and saves
tournaments to CSV — all from a simple terminal menu.

Built for the Collaborative Problem-Solving Project in **Computational Thinking and
Programming (2026CSAE100)**, Bennett University.

## Features

- Round-robin scheduling — every team plays every other team once (n(n−1)/2 fixtures)
- Result entry in `g1-g2` format with instant table updates
- League table: Pld, W, D, L, Pts, GF, GA, GD — Win 3 / Draw 1 / Loss 0,
  sorted by points then goal difference
- Save and reopen tournaments as CSV files
- Full input validation — bad input re-prompts, never crashes

## How to run

Requires Python 3 only (no external packages).

```bash
python3 main.py
```

Flow: create/open a save → set up teams → generate fixtures → enter results →
view the table → save to CSV.

## Project structure

```
main.py        # entry point: state machine and page dispatch
tournament.py  # round-robin fixtures, standings, table formatting
utils.py       # input validation and menu prompts
writer.py      # CSV save/load (os + csv from the standard library)
format.py      # banner and display helpers
pages/         # screens: main menu, create/open save, list saves, tournament menu
saves/         # tournament CSV files (created automatically)
EXPERIENTIAL_LEARNINGS.md  # experiential-learning topics used in this project
```

## Team

| Member | GitHub | LinkedIn |
|---|---|---|
| Aditya (Leader) | [zerodeathsO6](https://github.com/zerodeathso6) | [Profile](https://www.linkedin.com/in/aditya-samaddar-6560902b2/) |
| Jayant | [architect0fgod](https://github.com/architect0fgod) | [Profile](https://www.linkedin.com/in/jayant-b5520a452) |
| Sanyam | [sanyamsharma33](https://github.com/sanyamsharma33) | [Profile](https://www.linkedin.com/in/sanyam-sharma-b0019b43b) |
| Aryan | [disnony](https://github.com/disnony) | [Profile](https://www.linkedin.com/in/aryan-aggarwal-6790b6451/) |

Section: S14 · Academic year 2026–27
