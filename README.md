## Harvard CS50’s Introduction to Programming with Python — Solutions & Final Project

### About
These are my solutions for Harvard CS50’s Introduction to Programming with Python (CS50P), including problem sets, unit tests for selected problems, and a final project. Most programs are small, self-contained CLI scripts.

- Final project: Rock, Paper, Scissors & Sheldon’s Game (Big Bang Theory variant)
- Some folders include tests runnable with pytest

### Repository layout
- `final/`: Final project (two games). Run: `python final/project.py`
- `bitcoin/`: Fetches BTC price and multiplies by an amount. Run: `python bitcoin/bitcoin.py 2`
- `figlet/`: ASCII-art text rendering with selectable fonts. Run: `python figlet/figlet.py -f slant`
- `emojize/`: Converts aliases like ":smile:" to emoji. Run: `python emojize/emojize.py`
- `shirt/`: Overlays a shirt image onto a photo using Pillow. Run: `python shirt/shirt.py input.jpg output.jpg`
- `shirtificate/`: Generates a CS50 “shirtificate” PDF. Run: `python shirtificate/shirtificate.py`
- `pizza/`: Pretty-prints a CSV as a table. Run: `python pizza/pizza.py menu.csv`
- `scourgify/`: Cleans a CSV of names into first/last columns. Run: `python scourgify/scourgify.py before.csv after.csv`
- `seasons/`: Prints minutes lived from a YYYY-MM-DD DOB in words. Run: `python seasons/seasons.py`
- `response/`: Simple email validator. Run: `python response/response.py`
- Many other folders (`adieu/`, `bank/`, `camel/`, `coke/`, `deep/`, `einstein/`, `extensions/`, `faces/`, `game/`, `grocery/`, `indoor/`, `interpreter/`, `jar/`, `lines/`, `meal/`, `nutrition/`, `outdated/`, `plates/`, `playback/`, `professor/`, `taqueria/`, `tip/`, `twttr/`, `um/`, `watch/`, `working/`) contain one small CLI script each. Enter the folder and run the Python file inside.

### Setup
- Ensure Python 3.10+ is installed
- (Recommended) Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```
- Install dependencies used across exercises
```bash
python -m pip install requests emoji pyfiglet Pillow fpdf2 inflect tabulate validator-collection pytest
```

### How to run
- From the repository root, run individual scripts by path, for example:
```bash
python bitcoin/bitcoin.py 2
python figlet/figlet.py -f slant
python shirt/shirt.py input.jpg output.jpg
```
- Many scripts read from standard input; prompts will guide you. Press Ctrl+D (or Ctrl+C) to exit where noted.

### Tests
Run all tests from the repository root:
```bash
pytest -q
```
Run a specific test file (examples):
```bash
pytest final/test_project.py -q
pytest test_fuel/test_fuel.py -q
pytest test_twttr/test_twttr.py -q
```

### Final project
- Folder: `final/`
- Run: `python final/project.py`
- Two modes:
  - 1: Classic Rock–Paper–Scissors (first to 3 points)
  - 2: Sheldon’s Game (Rock–Paper–Scissors–Lizard–Spock, first to 3 points)
- Exit anytime with Ctrl+D or Ctrl+C
- Tests: `pytest final/test_project.py -q`
- Demo video: [YouTube](https://youtu.be/zJonXFwMPYk)

### Dependencies reference
- `requests` (used by `bitcoin`)
- `emoji` (used by `emojize`)
- `pyfiglet` (used by `figlet`)
- `Pillow` (PIL; used by `shirt`)
- `fpdf2` (used by `shirtificate`)
- `inflect` (used by `seasons`, `adieu`)
- `tabulate` (used by `pizza`, `scourgify`)
- `validator-collection` (used by `response`)
- `pytest` (for tests)

### Acknowledgements
Thanks to Harvard University, Prof. David J. Malan, and the CS50 staff for an excellent course.