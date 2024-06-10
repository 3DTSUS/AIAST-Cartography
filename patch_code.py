import re

def patch_code_section(original_source, new_source, start, end):
    """
    Splice a new code section into the original source, preserving indents.
    Args:
        original_source (str): The full original source code
        new_source (str): The new source code for the section
        start (int): Start index of the section to replace
        end (int): End index of the section to replace
    Returns:
        str: The updated source code with the new section spliced in
    """
    new_lines = new_source.splitlines()
    
    # Determine indentation from the original code
    orig_indent = re.match(r'\n*(\s*)\S', original_source[end:]).group(1)
    
    # Reindent new lines to match original indentation
    new_lines = [orig_indent + line for line in new_lines]
    
    new_source = '\n'.join(new_lines)
    
    # Splice the new source into the original
    new_full_source = original_source[:start] + new_source + original_source[end:]
    
    return new_full_source
