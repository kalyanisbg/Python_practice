import hashlib

data_to_encrypt = "password"



print(hashlib.sha256(data_to_encrypt.encode()))  # WORKS but doesnt show us the hashed value
print(hashlib.sha256(data_to_encrypt.encode()).hexdigest())  # get the hashed value using .hexdigest()

print(hashlib.sha224(data_to_encrypt.encode()))  # WORKS but doesnt show us the hashed value
print(hashlib.sha224(data_to_encrypt.encode()).hexdigest())  # get the hashed value using .hexdigest()
