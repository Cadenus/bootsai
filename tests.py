from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

run_cases_info = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../")
]

run_cases_content = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat")
]

run_cases_write = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed")
]

run_cases_run = [
    ("calculator", "main.py", None),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py", None),
    ("calculator", "../main.py", None),
    ("calculator", "nonexistent.py", None)
]

def test_info(input1, input2):
    print("---------------------------------")
    print(f"Inputs: [{input1}], [{input2}]")
    get_files_info(input1, input2)


def test_content(input1, input2):
    print("---------------------------------")
    print(f"Inputs: [{input1}], [{input2}]")
    result = get_file_content(input1, input2)
    print(result)


def test_write(input1, input2, input3):
    print("---------------------------------")
    print(f"Inputs: [{input1}], [{input2}] [{input3}]")
    result = write_file(input1, input2, input3)
    print(result)


def test_run(input1, input2, input3):
    print("---------------------------------")
    print(f"Inputs: [{input1}], [{input2}] [{input3}]")
    if input3 is None:
        result = run_python_file(input1, input2)  # Don't pass the third argument
    else:
        result = run_python_file(input1, input2, input3)
    print(result)

def main():
    print("Running tests")
    #for testcase in run_cases_info:
    #    test_info(*testcase)
    #for testcase in run_cases_write:
    #    test_write(*testcase)
    for testcase in run_cases_run:
        test_run(*testcase)

main()