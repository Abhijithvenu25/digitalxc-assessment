# Acme Secret Santa Assignment System

This is a Python-based solution for the Acme Secret Santa Coding Challenge. It automates the process of assigning secret children to employees based on specific rules, including avoiding self-assignments and preventing repetitions from the previous year.

## Features
- **Object-Oriented Design:** Modular code separated into logical components (`models`, `io_handlers`, `assigner`, `exceptions`).
- **Mathematical Guarantee:** Uses a randomized single-cycle permutation algorithm to ensure everyone gives exactly one gift, receives exactly one gift, and no one is assigned to themselves.
- **Constraints Handling:** Seamlessly supports importing previous year's assignments to ensure no repetitions occur.
- **Robust Testing:** Thoroughly covered by unit tests.

## Requirements
- Python 3.7+
- No external dependencies required to run the core application (uses Python standard library).

## How to Run
The program is invoked via the command line and expects CSV files for input and output. Since the raw data is provided in `.xlsx` format, first run the conversion script to generate the necessary CSV files:

```bash
python convert.py
```

This will automatically create `employees_list.csv` and `secret_santa_game_result_2023.csv` from the Excel files.

### Generating Assignments
To generate the new Secret Santa assignments while strictly avoiding last year's pairings, run the following exact command using the generated CSVs:

```bash
python main.py employees_list.csv new_assignments.csv --previous secret_santa_game_result_2023.csv
```

## Running the Tests
The project includes a suite of unit tests. To run them, simply use the built-in `unittest` module:
```bash
python -m unittest discover -s tests/
```

## Input CSV Format
The input CSV file (e.g., `employees.csv`) must contain the following headers:
- `Employee_Name`
- `Employee_EmailID`

## Output CSV Format
The generated output CSV file (e.g., `assignments.csv`) will contain the following headers:
- `Employee_Name`
- `Employee_EmailID`
- `Secret_Child_Name`
- `Secret_Child_EmailID`
# digitalxc-assessment
