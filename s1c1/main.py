BASE64_ENCODING_MAP = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"
]


# TODO: Don't use in built python for this either
def convert_hex_to_base64(input):
    input_bytes = bytes.fromhex(input)
    return convert_bytes_to_base64(input_bytes)


def convert_bytes_to_base64(ch_bytes):
    # Bytes are integers that hold the ASCII value of characters
    # 1. Convert them to bits
    # 2. group them into groups of 6
    # 3. Convert the group of 6 bits into an integer with base 10
    # 4. use that as an index and Find the corresponding letter in the base64
    bit_string = ""
    for ch_byte in ch_bytes:
        bit_string += '{0:08b}'.format(ch_byte)

    groups = [bit_string[i:i+6] for i in range(0, len(bit_string), 6)]

    result = ""
    for group in groups:
        base64_index = int(group, 2)
        result += BASE64_ENCODING_MAP[base64_index]

    return result


if __name__ == '__main__':
    print(convert_hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
