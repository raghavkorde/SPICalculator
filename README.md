# SPI and CPI Calculation System

The Grade Calculation System is a Python program that allows users to calculate their Semester Performance Index (SPI) and update their Cumulative Performance Index (CPI) based on the grades they input for their subjects. The program utilizes a CSV database to store subject details and provides a tabulated marksheet as an output.

#### Video Demo:  <https://youtu.be/jo_2ETbOQ5U>

## Features

- Calculate SPI: The program calculates the Semester Performance Index (SPI) based on the user's grades and credit points.
- Update CPI: The program updates the Cumulative Performance Index (CPI) based on the calculated SPI and the user's current CPI.
- Display Marksheet: The program displays a tabulated marksheet showing the subjects, their Theory/Practical classification, credits, and grades.
- Add Subjects: Users can add subjects to the database for their specific branch if it doesn't exist.

## Prerequisites

- Python 3.x
- csv module
- tabulate module 
(install from `requirements.txt`)

```python
pip install -r requirements.txt
```

## Usage

1. Clone the repo open it in the terminal or command prompt.
2. Navigate to the directory where the `grades.py` file is located.
3. Run the following command to execute the program:
```
python grades.py
```
4. Follow the prompts to enter your branch and grades for each subject.
5. Once all grades are entered, the program will display the SPI, prompt for the current CPI, and display the updated CPI.
6. The marksheet with subject details will also be displayed.

## Adding Subjects

If the branch database doesn't exist or if the user's branch is not found, the program will prompt to add the branch courses. Follow these steps to add subjects:

1. Enter the branch name when prompted.
2. Specify the number of subjects (including practical) to be added.
3. Enter the subject name, subject code, and credit for each subject.
4. Once all subjects are added, the program will create a new branch database and update the branch list.

**Note:** The branch list is stored in `data/branch.csv`, and the subject databases are stored in `data/{branch_name}.csv`.

## Database Structure

### Branch Database (`data/branch.csv`)

The `branch.csv` file stores the list of branches available in the system. Each branch name is stored as a separate row in the CSV file.

### Subject Databases (`data/{branch_name}.csv`)

Each branch has its own subject database file in the format `{branch_name}.csv`. The database contains the following columns:

- Subject: The name of the subject.
- Code: The code or identifier for the subject.
- Credits: The number of credits assigned to the subject.

The first row of the CSV file contains the column headers.

## Explanation of Functions

### `process(name)`

The `process` function is responsible for processing the grades for a given branch. It reads the subject details from the branch's CSV database and prompts the user to enter their grades for each subject. It calculates the SPI (Semester Performance Index) and updates the CPI (Cumulative Performance Index) based on the entered grades. Finally, it displays the marksheet.

### `calculate_cpi(spi, current_cpi)`

The `calculate_cpi` function calculates the updated CPI by considering the current SPI and CPI. It uses the formula `(spi + 2 * current_cpi) / 3.0` to calculate the updated CPI and returns the rounded value.

### `get_marksheet(marksheet)`

The `get_marksheet` function displays the marksheet in a tabulated format using the `tabulate` module. It takes the marksheet as input, which is a 2D list containing the subject details, and prints the tabulated marksheet to the console.

### `add(name)`

The `add` function allows users to add subjects to the database for their branch. It prompts the user to enter the subject name, subject code, and credits for each subject. It creates a new CSV file for the branch's subject database and appends the subject details to the file. It also updates the branch list in the `data/branch.csv` file.

### `main()`

The `main` function is the entry point of the program. It prompts the user to enter their branch and checks if the branch exists in the branch list. If the branch is found, it calls the `process` function to calculate the grades. If the branch is not found, it prompts the user to add the branch courses and then calls the `process` function.

### Tabulate Module Syntax

The `tabulate` module is used to format and display the marksheet in a tabulated format. It takes a N-D list of data and the column headers as input and generates a formatted table.

The syntax to use `tabulate` is as follows:

```python
print(tabulate(data, headers, tablefmt="grid"))
```

- `data` is the N-D list containing the data to be displayed in the table.
- `headers` is a list of strings representing the column headers.
- `tablefmt` specifies the format of the table, and in this case, we are using the "grid" format.

The `tabulate` function formats the data into a table and returns it as a string. In the code, the formatted table (marksheet) is printed using the print statement.

