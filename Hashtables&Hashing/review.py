print(hash(48))
print(hash("Addi"))

import hashlib

data_to_encrypt = 'Password'

print(hashlib.sha224(data_to_encrypt.encode()))