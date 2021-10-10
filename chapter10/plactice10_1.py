import random
import hashlib

random.seed(10)


def hash_with_salt(val, salt=None):
    if not salt:
        salt = str(random.randint(1, 100))
    m = hashlib.sha3_512()
    m.update(val.encode('UTF-8') + salt.encode('UTF-8'))
    return m.hexdigest(), salt


print(hash_with_salt('password'))
