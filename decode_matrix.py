#!/bin/python3

import re

def decode_matrix(matrix):
    """
    Input: List of strings (matrix rows) 
    Output: Return a decoded string where symbols between 
            alphanumeric characters are replaced by a space.
    """
    # transpose the matrix
    columns = list(zip(*matrix))
    
    # flatten the list of tuples
    columns = [x for sub in columns for x in sub]
    
    # convert to string
    text = "".join(columns)
    
    # replace symbols/spaces between alphanumerics with a single space
    text = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', text)
    
    # optional: strip leading/trailing non-alphanumerics
    text = re.sub(r'^\W+|\W+$', '', text)
    
    return text

print(result)
