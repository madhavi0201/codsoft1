import string
import secrets
import sys

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Generates a random password of a given length and complexity.
    
    Parameters:
        length (int): The length of the password.
        use_upper (bool): Whether to include uppercase letters.
        use_lower (bool): Whether to include lowercase letters.
        use_digits (bool): Whether to include digits.
        use_special (bool): Whether to include special characters.
        
    Returns:
        str: The generated password.
        
    Raises:
        ValueError: If length is less than 1 or if no character types are selected.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")
        
    pools = []
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_special:
        # Use string.punctuation for a comprehensive set of special characters
        pools.append(string.punctuation)
        
    if not pools:
        raise ValueError("At least one character type must be selected.")
        
    password_chars = []
    
    # To guarantee that at least one character from each selected type is present,
    # we first pull one character from each selected pool (if length allows).
    if length >= len(pools):
        for pool in pools:
            password_chars.append(secrets.choice(pool))
        remaining_length = length - len(pools)
    else:
        remaining_length = length
        
    # Fill the remaining characters from the combined pool of all selected types
    combined_pool = "".join(pools)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(combined_pool))
        
    # Shuffle the characters cryptographically so the guaranteed characters
    # are not always at the beginning of the password.
    secrets.SystemRandom().shuffle(password_chars)
    
    return "".join(password_chars)

def get_yes_no(prompt, default=True):
    """Prompts the user for a yes/no input, returning a boolean."""
    default_str = " [Y/n]" if default else " [y/N]"
    while True:
        choice = input(prompt + default_str + ": ").strip().lower()
        if not choice:
            return default
        if choice in ('y', 'yes'):
            return True
        if choice in ('n', 'no'):
            return False
        print("Invalid input. Please enter 'y' or 'n'.")

def get_password_length():
    """Prompts the user to enter a valid password length."""
    while True:
        try:
            val = input("Enter the desired password length (minimum 4, recommended 12+): ").strip()
            length = int(val)
            if length < 1:
                print("Password length must be at least 1. Please try again.")
            else:
                if length < 8:
                    print("Note: Passwords shorter than 8 characters are generally not secure.")
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("========================================")
    print("      Strong Password Generator         ")
    print("========================================")
    
    while True:
        length = get_password_length()
        
        # Ask if they want to customize complexity or use defaults
        use_default = get_yes_no("Use default settings (include all character types)", default=True)
        
        if use_default:
            use_upper = use_lower = use_digits = use_special = True
        else:
            print("\nCustomize character types:")
            while True:
                use_upper = get_yes_no("  Include uppercase letters (A-Z)?", default=True)
                use_lower = get_yes_no("  Include lowercase letters (a-z)?", default=True)
                use_digits = get_yes_no("  Include numbers (0-9)?", default=True)
                use_special = get_yes_no("  Include special characters (e.g. !, @, #, $)?", default=True)
                
                if use_upper or use_lower or use_digits or use_special:
                    break
                print("\nError: You must select at least one character type. Please configure again.")
        
        # Generate and display the password
        try:
            password = generate_password(
                length, 
                use_upper=use_upper, 
                use_lower=use_lower, 
                use_digits=use_digits, 
                use_special=use_special
            )
            print("\n----------------------------------------")
            print(f"Generated Password: {password}")
            print("----------------------------------------")
        except ValueError as e:
            print(f"\nError generating password: {e}")
            
        print()
        if not get_yes_no("Do you want to generate another password?", default=False):
            print("\nThank you for using Strong Password Generator. Goodbye!")
            break
        print("\n" + "="*40)

if __name__ == "__main__":
    main()
