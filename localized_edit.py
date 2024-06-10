import ast

def modify_function(source, func_name, transform):
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            transform(node)
            break
    return ast.dump(tree)

def add_print(node):
    node.body.insert(0, ast.Expr(ast.Call(ast.Name('print', ast.Load()), 
                                          [ast.Constant('Entering function')], [])))
