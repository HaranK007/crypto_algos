import math

# Constants defined for MD5 algorithm
ROTATE_BY = [7, 12, 17, 22] * 4 + [5,  9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
CONSTANTS = [int(abs(math.sin(i + 1)) * 2 ** 32) & 0xFFFFFFFF for i in range(64)]

INIT_MDBUFFER = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

def pad_message(message):
    """
    Pad the message according to the MD5 algorithm.
    """
    original_length_bits = len(message)
    message.append(1 << 7)  # Appending a single '1' bit

    while len(message) % 512 != 448:  # Padding until length is congruent to 448 modulo 512
        message.append(0)

    # Appending the original message length (in bits) as a 64-bit integer
    message += original_length_bits.to_bytes(8, byteorder='big')
    return message

def left_rotate(x, amount):
    """
    Left rotate operation for 32-bit integers.
    """
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

def process_message(message):
    """
    Process the message according to the MD5 algorithm.
    """
    init_temp = INIT_MDBUFFER[:]
    for offset in range(0, len(message), 512):
        a, b, c, d = init_temp
        chunk = message[offset:offset + 512]
        for i in range(0, 512, 32):
            word = chunk[i:i+32]  # Get a 32-bit word from the chunk
            g = (i // 32)  # Calculate the word index (0 to 15)
            f = None  # Placeholder for the round function value
            if g < 16:
                f = (b & c) | ((~b) & d)
            elif g < 32:
                f = (d & b) | ((~d) & c)
            elif g < 48:
                f = b ^ c ^ d
            else:
                f = c ^ (b | (~d))
            f = (f + a + CONSTANTS[g] + word) & 0xFFFFFFFF
            a, b, c, d = d, (b + left_rotate(f, ROTATE_BY[g])) & 0xFFFFFFFF, b, c
        init_temp = [(x + y) & 0xFFFFFFFF for x, y in zip(init_temp, [a, b, c, d])]
    return init_temp


def md5(message):
    """
    Calculate the MD5 hash of the message.
    """
    message = pad_message(message)
    processed_message = process_message(message)
    message_hash = sum(buffer_content << (32 * i) for i, buffer_content in enumerate(processed_message))
    return '{:032x}'.format(message_hash)

if __name__ == '__main__':
    message = bytes.fromhex("48454c4c4f20576f726c64")  # Example input in bytes (hex representation)
    hash_result = md5(message)
    print("MD5 Hash: ", hash_result)
