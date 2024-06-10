def extract_code_section(source, section_type, section_name):
    """
    Extract a code section (function or class) into a standalone string.
    Args:
        source (str): The full source code
        section_type (str): 'function' or 'class'
        section_name (str): Name of the function or class to extract
    Returns:
        str: The extracted code section as a string
        int: Start index of the section in the source
        int: End index of the section in the source
    """
    import re
    
    # Function pattern
    func_pattern = r'def\s+%s\s*\(.*?\):(?:\n+(?:    .+\n*)*?\n*?)\n*?'
    # Class pattern
    class_pattern = r'class\s+%s\s*\(.*?\):(?:\n+(?:    .+\n*)*?\n*?)\n*?'
    
    if section_type == 'function':
        pattern = func_pattern % section_name
    elif section_type == 'class':
        pattern = class_pattern % section_name
    else:
        raise ValueError('Invalid section_type, must be "function" or "class"')
        
    match = re.search(pattern, source, re.DOTALL)
    if match:
        start, end = match.span()
        return match.group(), start, end
    else:
        raise ValueError(f'Could not find {section_type} {section_name} in source')
