import uuid

# Generate a random UUID
random_uuid = uuid.uuid4()

print("UUID object:", random_uuid)

# Convert UUID to string
uuid_string = str(random_uuid)
print("UUID string:", uuid_string)

# Get hexadecimal representation
uuid_hex = random_uuid.hex
print("UUID HEX:", uuid_hex)
