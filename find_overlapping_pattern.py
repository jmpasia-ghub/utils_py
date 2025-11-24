import re

s = input()
k = input()

def find_overlapping_pattern(S, k):
    """
    Goal: Find the overlapping occurences of pattern k from string S
    Input S: string
          k: string
    Output: list with two elements (a,b) where a is the starting index
    and b is the last index, inclusive.
    """
    
    pattern = rf'(?=({k}))'
    matches = list(re.finditer(pattern, S))
    
    if not matches:
        return [(-1,-1)]
    
    return [(m.start(1), m.end(1)-1) for m in matches]        
     
