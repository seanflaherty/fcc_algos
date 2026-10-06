"""Luhn Algorithm"""
def verify_card_number(card_number: str) -> str:
    """Function to verify a credit card number using the Luhn algorithm."""
    # Remove hyphens, spaces, and non-digit characters
    digits = [int(char) for char in card_number if char.isdigit()]

    # Check if we have a non-empty list of digits
    if not digits:
        return "INVALID!"

    # Luhn Algorithm implementation
    # Double every second digit from right to left
    checksum = 0
    reverse_digits = digits[::-1]

    for index, digit in enumerate(reverse_digits):
        if index % 2 == 1:  # Every second digit (0-indexed from right)
            doubled = digit * 2
            # Subtract 9 if doubling results in a number > 9 (equivalent to adding digits)
            checksum += doubled if doubled < 10 else doubled - 9
        else:
            checksum += digit

    # If the sum is divisible by 10, the card is valid
    return "VALID!" if checksum % 10 == 0 else "INVALID!"
