def ksa(key):
    key_length = len(key)
    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def prga(S, length):
    i = 0
    j = 0
    key = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key.append(S[(S[i] + S[j]) % 256])

    return key

def rc4_encrypt(data, key):
    S = ksa(key)
    key_stream = prga(S, len(data))
    encrypted = bytearray()
    for i in range(len(data)):
        encrypted.append(data[i] ^ key_stream[i])
    return encrypted

def rc4_decrypt(data, key):
    return rc4_encrypt(data, key)  # RC4 decryption is the same as encryption

# Example usage:
if __name__ == "__main__":
    plaintext = b"Hello, world!"
    key = b"my_secret_key"
    
    encrypted = rc4_encrypt(plaintext, key)
    decrypted = rc4_decrypt(encrypted, key)
    
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
