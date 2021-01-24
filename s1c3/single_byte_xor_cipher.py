from s1c1.hex_to_base64 import hex_decode
from s1c2.fixed_xor import xor


def assign_score(str):
    score = 0
    for ch in str:
        if ch >= 65 and ch <= 65+25:
            score += 1

        if ch >= 97 and ch < 97 + 26:
            score += 1

    return score


if __name__ == '__main__':
    hex_encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    hex_decoded_bytes = hex_decode(hex_encoded_string)

    new_input_bytes = []
    for i in range(34):
        new_input_bytes.append(0)

    index_scores = []
    for i in range(256):
        input_bytes = bytes([i]) * len(hex_decoded_bytes)
        xor_string = xor(hex_decoded_bytes, input_bytes)
        score = assign_score(xor_string)
        index_scores.append((i, score, xor_string))

    index_scores = sorted(index_scores, key=lambda x: x[1], reverse=True)
    print(index_scores)

    # the very first entry here is the important character which caused the flip. It's "X"
    print(chr(index_scores[0][0]))
