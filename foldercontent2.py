import os
import argparse
import sys

# Define a function to print the directory contents
def print_directory_contents(path, ignore_items=None, prefix="", include_content=True):
    # If ignore_items is not provided, create an empty set
    if ignore_items is None:
        ignore_items = set()
    
    # Get a list of items in the directory
    items = os.listdir(path)
    # Sort the list of items
    items.sort()
    
    # Iterate over the items in the directory
    for index, item in enumerate(items):
        # If the item is in the ignore_items set, skip it
        if item in ignore_items:
            continue
        # Get the full path of the item
        full_path = os.path.join(path, item)
        # Check if the item is a directory
        if os.path.isdir(full_path):
            # If the item is the last item in the directory, print a └── symbol
            if index == len(items) - 1:
                print(f"{prefix}└── {item}/")
                # Recursively call the print_directory_contents function
                print_directory_contents(full_path, ignore_items, prefix + "    ", include_content)
            # If the item is not the last item in the directory, print a ├── symbol
            else:
                print(f"{prefix}├── {item}/")
                # Recursively call the print_directory_contents function
                print_directory_contents(full_path, ignore_items, prefix + "│   ", include_content)
        # Check if the item is a file
        elif os.path.isfile(full_path):
            # If the item is the last item in the directory, print a └── symbol
            if index == len(items) - 1:
                print(f"{prefix}└── {item}")
            # If the item is not the last item in the directory, print a ├── symbol
            else:
                print(f"{prefix}├── {item}")
            
            # If include_content is True, print the contents of the file
            if include_content:
                print(f"{prefix}    Content:")
                try:
                    # Open the file in read mode
                    with open(full_path, 'r') as file:
                        # Read the contents of the file
                        content = file.read()
                        # Print the contents of the file
                        print(f"{prefix}    {content}")  # Print full content
                except Exception as e:
                    # If an error occurs, print an error message
                    print(f"{prefix}    Error reading file: {str(e)}")
                # Print a separator line
                print(f"{prefix}    " + "-"*50)  # Separator

# Define a main function
def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Print folder structure with full content")
    # Add arguments to the parser
    parser.add_argument("root_dir", help="Root directory to print")
    parser.add_argument("--ignore", nargs="*", help="Items to ignore")
    parser.add_argument("--output", help="Output file or destination")
    parser.add_argument("--include-content", action="store_true", help="Include file contents")
    # Parse the arguments
    args = parser.parse_args()

    # Get the root directory from the arguments
    root_dir = args.root_dir
    # Get the ignore items from the arguments
    ignore_items = set(args.ignore) if args.ignore else set()
    # Get the output file or destination from the arguments
    output = args.output
    # Get the include_content flag from the arguments
    include_content = args.include_content

    # Redirect stdout to a file if specified
    if output:
        # Open the output file in write mode
        with open(output, 'w') as f:
            # Save the original stdout
            original_stdout = sys.stdout
            # Set stdout to the output file
            sys.stdout = f
            # Print the root directory
            print(f"{os.path.basename(root_dir)}/")
            # Call the print_directory_contents function
            print_directory_contents(root_dir, ignore_items, include_content=include_content)
            # Restore the original stdout
            sys.stdout = original_stdout
    else:
        # Print the root directory
        print(f"{os.path.basename(root_dir)}/")
        # Call the print_directory_contents function
        print_directory_contents(root_dir, ignore_items, include_content=include_content)

    # Print a message indicating that the folder structure has been written
    print("Folder structure with full content has been written to", output if output else "console")

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()
