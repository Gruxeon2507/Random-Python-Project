import os
import subprocess
from asciitree import LeftAligned


def format_directory_results(results):
    tree = {}
    for result in results:
        path_parts = result.split('.')
        current_level = tree
        for part in path_parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
    return tree


def save_tree_to_file(tree, output_file):
    renderer = LeftAligned()
    rendered_tree = renderer(tree)
    print(rendered_tree)
    with open(output_file, 'w') as file:
        file.write(rendered_tree)


def run_dirsearch(url, output_file):
    # Run dirsearch command
    command = f"dirsearch -u {url}"
    result = subprocess.check_output(command, shell=True, text=True)
    directory_results = result.splitlines()

    # Format directory results as a tree
    tree = format_directory_results(directory_results)

    # Save tree to a text file
    save_tree_to_file(tree, output_file)

    print(f"Directory enumeration tree saved in {output_file}")


if __name__ == "__main__":
    url = input("Enter the URL: ")
    output_file = "directories.txt"
    run_dirsearch(url, output_file)
