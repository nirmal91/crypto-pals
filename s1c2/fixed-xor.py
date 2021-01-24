from s1c1.hex_to_base64 import hex_decode


def xor(str1, str2):
    return bytes(a ^ b for (a,b) in zip(str1, str2))


def manual_xor(str1, str2):
    assert len(str1) == len(str2)
    result_bytes = []
    for i in range(len(str1)):
        byte1 = str1[i]
        byte2 = str2[i]

        result_byte = byte1 ^ byte2
        result_bytes.append(result_byte)

    return bytes(result_bytes)


if __name__ == '__main__':
    str1 = "1c0111001f010100061a024b53535009181c"
    str2 = "686974207468652062756c6c277320657965"

    str1_decoded = hex_decode(str1)
    str2_decoded = hex_decode(str2)
    print(str1_decoded)
    print(str2_decoded)

    result = manual_xor(hex_decode(str1), hex_decode(str2))
    # encode it back to hex
    print(bytes.hex(result))
