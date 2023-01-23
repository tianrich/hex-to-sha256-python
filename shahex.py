import hashlib

while True:
    # Get hex string from user input
    hex_string = input("Enter the hex string: ")

    # Convert hex string to bytes
    hex_bytes = bytes.fromhex(hex_string)

    # Create SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update hash object with hex bytes
    hash_object.update(hex_bytes)

    # Get SHA-256 hash in hexadecimal format
    hash_hex = hash_object.hexdigest()

    # Print the hash to the terminal
    print(hash_hex)
