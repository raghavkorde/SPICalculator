import csv
import sys
from tabulate import tabulate

factor = {'AA': 1, 'AB': 0.9, 'BB': 0.8, 'BC': 0.7, 'CC': 0.6, 'DD': 0.5, 'FF': 0}

def process(name, subjects):
    marksheet = [["Subject", "T/P", "Credits", "Grade"]]
    total_grade_points = 0.0
    total_credits = 0
    for subject in subjects:
        subject_name, subject_code, credit = subject
        grade = input(f"Enter your grade for {subject_name} {subject_code}: ").strip().upper()
        marksheet.append([subject_name, subject_code, credit, grade])
        total_grade_points += float(factor.get(grade, 0)) * float(credit)
        total_credits += float(credit)

    spi = (total_grade_points * 10) / total_credits
    print(f"SPI: {round(spi, 2)}")
    return [spi, marksheet]


def calculate_cpi(spi, current_cpi):
    updated_cpi = (spi + 2 * current_cpi) / 3.0
    return round(updated_cpi, 2)


def get_marksheet(marksheet):
    return tabulate(marksheet[1:], marksheet[0], tablefmt="grid")


def add(name):
    n = int(input("Enter the number of subjects (including practical): "))
    subjects = []
    for _ in range(n):
        subject_name = input("Enter subject name: ")
        subject_code = input("Enter subject code: ")
        credit = input("Enter subject credit: ")
        subjects.append([subject_name, subject_code, credit])

    with open(f"data/{name}.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Code", "Credits"])
        writer.writerows(subjects)

    with open("data/branch.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name])



def main():
    branch = input("Enter your Branch: ").upper().strip()
    branches = []
    try:
        with open("data/branch.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                branches.extend(row)
            if branch in branches:
                subjects = []
                try:
                    with open(f"data/{branch}.csv", "r") as file:
                        reader = csv.reader(file)
                        next(reader)  # Skip the header row
                        subjects = list(reader)
                except FileNotFoundError:
                    sys.exit("Database for your branch not found")
                spi, marksheet = process(branch, subjects)
                current_cpi = float(input("Enter your current CPI: "))
                cpi = calculate_cpi(spi, current_cpi)
                print(f"Updated CPI: {cpi}")
                print(get_marksheet(marksheet))
                
            else:
                print("Branch not found")
                print("Add your branch courses to continue...")
                add(branch)
                subjects = []
                try:
                    with open(f"data/{branch}.csv", "r") as file:
                        reader = csv.reader(file)
                        next(reader)  # Skip the header row
                        subjects = list(reader)
                except FileNotFoundError:
                    sys.exit("Database for your branch not found")
                spi, marksheet = process(branch, subjects)
                current_cpi = float(input("Enter your current CPI: "))
                cpi = calculate_cpi(spi, current_cpi)
                print(f"Updated CPI: {cpi}")
                print(get_marksheet(marksheet))
    except FileNotFoundError:
        sys.exit("Database not found")


if __name__ == "__main__":
    main()
