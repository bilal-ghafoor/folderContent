# Folder Structure Printer

A Python script to print the folder structure of a directory, including the contents of files.

## Installation

To use this script, you need to have Python installed on your system. You can download the latest version of Python from the official Python website.

## Usage

To use this script, save it to a file (e.g., `foldercontent.py`) and run it from the command line using the following syntax:
```bash                     (change this)             (items to ignore)
python foldercontent.py /path/to/root/directory --ignore item1 item2 --output output.txt --include-content
```

Replace /path/to/root/directory with the actual path to the directory you want to print, and item1 and item2 with the names of the items you want to ignore. The --output option specifies the output file or destination, and the --include-content option includes the contents of files in the output.

Options

root_dir: The root directory to print.
--ignore: A list of items to ignore.
--output: The output file or destination.
--include-content: A flag to include the contents of files in the output.