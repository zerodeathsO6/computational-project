# Experiential Learnings Applied — FixtureForge

This document lists only the experiential-learning (EL) topics that are actually used
in FixtureForge. Topics that are not used are intentionally omitted.

| EL | Topic | Where it is used in FixtureForge |
|----|-------|----------------------------------|
| E1 | Python setup, IDEs and first program | The CLI is started with `python3 main.py` from the terminal or IDE. |
| E2 | Operators and expressions | Points arithmetic (`+3`, `+1`), comparisons (`goals1 > goals2`) and f-strings. |
| E3 | Modules, imports and functions | The project is split into modules (`main`, `pages`, `utils`, `writer`, `tournament`) that import each other. |
| E4 | String slicing and string methods | `strip()`, `replace()`, `split('-')`, slicing in `format_table_row()`, and f-strings. |
| E5 | Loop control statements (`break`, `continue`, `pass`) | `while` menus, `break` to exit, `continue` for invalid/empty cases, and `pass` in `create_save()`. |
| E6 | Membership operators (`in`, `not in`) | Checks such as `if "-" in result`, menu-option membership, and `"teams" not in tournament_data`. |
| E7 | Integrated collection processing | Lists of teams/fixtures/standings and the `tournament_data` dictionary processed by functions. |
| E8 | Lambda functions and `sorted(key=...)` | `sorted(standings, key=lambda x: (x[5], x[8]), reverse=True)` in `calculate_standings()`. |
| E10 | Exception handling | `try/except` for `ValueError`, `OSError`, `EOFError` and `KeyboardInterrupt`; `raise ValueError`. |

## Notes

- The project report follows the prescribed report format and does not add an EL section.
- A summary of this mapping is also included in the presentation.
- Only the topics above are claimed; the project does not claim any other EL topic.
