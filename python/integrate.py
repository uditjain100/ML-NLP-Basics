import ast
import subprocess
import sys

def install_libraries_from_file(file_path):
    # Read the Python file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Parse the Python file content into an Abstract Syntax Tree (AST)
    tree = ast.parse(file_content)

    # Extract all the module names from import statements
    modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                modules.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            modules.add(node.module)

    # Install the libraries using pip
    for module in modules:
        print(f"Installing {module}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# Example usage
file_path = 'your_python_file.py'  # Replace with your file path
install_libraries_from_file(file_path)