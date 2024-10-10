import os

def print_directory_contents(path, ignore_items=None, prefix="", include_content=True):
    if ignore_items is None:
        ignore_items = set()
    
    items = os.listdir(path)
    items.sort()
    
    for index, item in enumerate(items):
        if item in ignore_items:
            continue
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            if index == len(items) - 1:
                print(f"{prefix}└── {item}/")
                print_directory_contents(full_path, ignore_items, prefix + "    ", include_content)
            else:
                print(f"{prefix}├── {item}/")
                print_directory_contents(full_path, ignore_items, prefix + "│   ", include_content)
        elif os.path.isfile(full_path):
            if index == len(items) - 1:
                print(f"{prefix}└── {item}")
            else:
                print(f"{prefix}├── {item}")
            
            if include_content:
                print(f"{prefix}    Content:")
                try:
                    with open(full_path, 'r') as file:
                        content = file.read()
                        print(f"{prefix}    {content}")  # Print full content
                except Exception as e:
                    print(f"{prefix}    Error reading file: {str(e)}")
                print(f"{prefix}    " + "-"*50)  # Separator

root_dir = "/Users/bilal/Documents/Work/Github/MyProjects/NoteCardApp/notecard-optimizer"
ignore_items = {"node_modules", ".git", ".vscode", "package-lock.json"}

# Redirect stdout to a file
import sys
original_stdout = sys.stdout
with open('folder_structure_with_full_content.txt', 'w') as f:
    sys.stdout = f
    print(f"{os.path.basename(root_dir)}/")
    print_directory_contents(root_dir, ignore_items)
    sys.stdout = original_stdout

print("Folder structure with full content has been written to folder_structure_with_full_content.txt")
