# AIAST-Cartography
AI, Abstract Syntax Trees, and the Future of Code Refactoring

A potentially groundbreaking toolkit that empowers AI coding assistants to understand and modify complex codebases with the precision of a senior developer. By leveraging Abstract Syntax Trees (ASTs) and static analysis, AIAST-Cartography enables surgical code transformations without the instability of full-file regeneration.

## 🌟 Features

- **CodeIndex**: A robust indexing system that maps functions, classes, and variables across files, capturing their interrelationships.
- **AST Transformations**: Make precise, isolated code changes by manipulating ASTs rather than raw text.
- **Targeted Patching**: Splice transformed code sections back into original files, preserving context and structure.

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

```bash
pip install aicartography
```

Quick Start
```python
from aicartography import CodeIndex, modify_ast, patch_code_section

# Build a code map
index = CodeIndex(['file1.py', 'file2.py', 'file3.py'])

# Find where a function is used
print(index.get_element_files('my_func'))

# Get related variables for a class
print(index.get_related_elements('MyClass'))

# Transform a function
def optimize_pow(node):
    for child in ast.walk(node):
        if isinstance(child, ast.BinOp) and isinstance(child.op, ast.Pow) and isinstance(child.right, ast.Constant) and child.right.value == 2:
            child.parent.replace(child, ast.BinOp(child.left, ast.Mult(), child.left))

func_code, start, end = extract_code_section(source, 'function', 'sum_squares')
optimized_code = modify_ast(func_code, optimize_pow)

# Patch the optimized code back in
new_source = patch_code_section(source, optimized_code, start, end)
```

## Core Components
codeindex.py
modifyast.py
patch_code_section.py

## Advanced Usage
Optimizing a loop
```python
def optimize_loop(node):
    for child in ast.walk(node):
        if isinstance(child, ast.BinOp) and isinstance(child.op, ast.Pow) and isinstance(child.right, ast.Constant) and child.right.value == 2:
            new_node = ast.Multiply()
            new_node.left = child.left
            new_node.right = child.left
            child.parent.replace(child, new_node)

func_code, start, end = extract_code_section(source, 'function', 'sum_squares')
optimized_code = modify_ast(func_code, optimize_loop)
new_source = patch_code_section(source, optimized_code, start, end)
```

This example optimizes a function by replacing all x**2 operations with x*x, which is generally faster. The transformation is made precisely, without disturbing the rest of the code.
### 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

### Fork the Project
Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
Push to the Branch (`git push origin feature/AmazingFeature`)
Open a Pull Request

### 📜 License
Distributed under the MIT License. See LICENSE for more information.

###🌐 Contact
Tim Escolopio - linkedin.com/tescolopio - time@3dtechsolutions.us
Project Link: https://github.com/tescolopio/3dtsus/aiast-cartography

### 🙏 Acknowledgments

Hat tip to the Python ast module developers
Inspiration from all the devs wrestling with AI-generated code changes
