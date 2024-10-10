# Folder Structure Printer

A Python script to print the folder structure of a directory, including the contents of files.

## Installation

To use this script, you need to have Python installed on your system. You can download the latest version of Python from the official Python website.

Additionally, you can make the script globally accessible by placing it in a directory that is included in your system's PATH. Follow the instructions below to do this:

### Making the Script Globally Accessible

1. **Add the Shebang Line**

   Open the script in your favorite text editor and add the following shebang line to the very top of the script to ensure it uses Python:

   ```python
   #!/usr/bin/env python3
   ```
Save the Script in a System Directory

Copy the script to a directory included in your system's PATH, such as /usr/local/bin/.

    ```
    sudo cp foldercontent.py /usr/local/bin/
    ```

Make the Script Executable

After copying, you need to make the script executable so that it can be run directly from the command line:

    ```
    sudo chmod +x /usr/local/bin/foldercontent.py
    ```

Verify PATH Configuration

Ensure that /usr/local/bin is part of your PATH by running:

    ```
    echo $PATH
    ```

If /usr/local/bin is not in your PATH, you may need to add it manually by editing your shell configuration file (e.g., ~/.zshrc or ~/.bash_profile).

    ```
    export PATH="$PATH:/usr/local/bin"
    ```

Then reload the configuration:

    ```
    source ~/.zshrc  # or source ~/.bash_profile
    ```

Now, you can use the script from any directory by simply typing foldercontent.py.

Usage
To use this script, save it to a file (e.g., foldercontent.py) and run it from the command line using the following syntax:

    ```
    foldercontent.py /path/to/root/directory --ignore item1 item2 --output output.txt --include-content
    ```

Replace /path/to/root/directory with the actual path to the directory you want to print, and item1 and item2 with the names of the items you want to ignore. The --output option specifies the output file or destination, and the --include-content option includes the contents of files in the output.

Options
root_dir: The root directory to print.
--ignore: A list of items to ignore.
--output: The output file or destination.
--include-content: A flag to include the contents of files in the output.