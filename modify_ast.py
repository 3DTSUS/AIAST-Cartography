import ast

def modify_ast(source, transform_func):
    """
    Parse source into an AST, transform it, and return modified source
    Args:
        source (str): Code to transform
        transform_func (callable): Function to call on each top-level node
    Returns:
        str: Modified source code
    """
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
            transform_func(node)
            
    return ast.dump(tree)
