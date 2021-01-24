from s1.s1c1.hex_to_base64 import hex_decode
from s1.s1c2.fixed_xor import xor


def repeating_key_xor(input_bytes, key_bytes):
    # keep iterating through the input string and keep adding the corresponding character from key string to it
    stretched_bytes = bytearray()
    for i in range(len(input_bytes)):
        key_byte = key_bytes[i % len(key_bytes)]
        stretched_bytes.append(key_byte)
    print(input_bytes)
    print(stretched_bytes)
    return xor(input_bytes, stretched_bytes)


if __name__ == '__main__':
    input_string = b"Burning 'em, if you ain't quick and nimble" \
                   b" I go crazy when I hear a cymbal"
    key_string = b"ICE"
    resultant_bytes = repeating_key_xor(input_string, key_string)
    answer = resultant_bytes.hex()
    assert answer == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
