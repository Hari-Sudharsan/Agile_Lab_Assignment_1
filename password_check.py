import re

def get_password_status(p):
    """
    Checks validity and returns (is_valid, reasons)
    """
    reasons = []
    
    # 1. Length check
    if not (6 <= len(p) <= 12):
        reasons.append("Must be 6-12 characters")
    
    # 2. Letter [a-z] check
    if not re.search("[a-z]", p):
        reasons.append("Missing lowercase letter [a-z]")
        
    # 3. Number [0-9] check
    if not re.search("[0-9]", p):
        reasons.append("Missing digit [0-9]")
        
    # 4. Letter [A-Z] check
    if not re.search("[A-Z]", p):
        reasons.append("Missing uppercase letter [A-Z]")
        
    # 5. Character [$#@] check
    if not re.search("[$#@]", p):
        reasons.append("Missing special character [$#@]")
    
    # 6. Whitespace check (implied by common validation standards)
    if re.search("\\s", p):
        reasons.append("Cannot contain spaces")

    is_valid = len(reasons) == 0
    return is_valid, reasons

# User interaction
user_input = input("Enter comma-separated passwords: ")
passwords = [p.strip() for p in user_input.split(',')]

print("\n--- Password Validation Report ---")
valid_list = []

for p in passwords:
    is_valid, errors = get_password_status(p)
    if is_valid:
        print(f" {p}: VALID")
        valid_list.append(p)
    else:
        print(f" {p}: INVALID ({', '.join(errors)})")

print("\nFinal Valid Sequence:", ",".join(valid_list))
