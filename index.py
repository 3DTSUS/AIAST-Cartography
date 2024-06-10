import ast
from typing import Dict, List, Set, Tuple

class CodeIndex:
    def __init__(self, filenames: List[str]):
        self.filenames = filenames
        self.indexes = self._build_indexes()
        
    def _build_indexes(self) -> Dict[str, Dict]:
        indexes = {}
        for filename in self.filenames:
            with open(filename, 'r') as f:
                tree = ast.parse(f.read())
                
            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
            variables = [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
            
            file_index = {
                'functions': functions,
                'classes': classes,
                'variables': variables
            }
            indexes[filename] = file_index
            
        return indexes
        
    def get_functions(self, filename: str) -> List[str]:
        return self.indexes[filename]['functions']
    
    def get_classes(self, filename: str) -> List[str]:
        return self.indexes[filename]['classes']
    
    def get_variables(self, filename: str) -> List[str]:
        return self.indexes[filename]['variables']
        
    def get_element_files(self, element: str) -> Set[str]:
        files = set()
        for filename, index in self.indexes.items():
            if element in index['functions'] or element in index['classes'] or element in index['variables']:
                files.add(filename)
        return files
        
    def get_related_elements(self, element: str) -> Set[Tuple[str, str]]:
        related = set()
        for filename, index in self.indexes.items():
            if element in index['functions']:
                related.update([(filename, var) for var in index['variables']])
            elif element in index['classes']:
                related.update([(filename, func) for func in index['functions']])
                related.update([(filename, var) for var in index['variables']])
        return related
