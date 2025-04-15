def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt text using Caesar Cipher algorithm.
    
    Args:
        text (str): The text to encrypt/decrypt
        shift (int): The number of positions to shift
        mode (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The encrypted or decrypted text
    """
    result = ""
    
    # If decrypting, reverse the shift
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Determine the base ASCII value (A for uppercase, a for lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Calculate the new position
            new_pos = (ord(char) - base + shift) % 26
            # Convert back to character
            result += chr(base + new_pos)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def main():
    print("Caesar Cipher Program")
    print("--------------------")
    
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue
            
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value (1-25): "))
        
        if not 1 <= shift <= 25:
            print("Shift value must be between 1 and 25.")
            continue
            
        mode = 'encrypt' if choice == '1' else 'decrypt'
        result = caesar_cipher(text, shift, mode)
        
        print(f"\n{mode.capitalize()}ed text: {result}")

if __name__ == "__main__":
    main() 