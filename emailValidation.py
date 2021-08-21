import re

email_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

def validateEamil(email):
    if re.search(email_pattern, email):
        return True
    else: 
        return False
