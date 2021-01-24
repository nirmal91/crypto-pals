from s1.s1c1.hex_to_base64 import hex_decode
from s1.s1c2.fixed_xor import xor


def assign_score(str):
    score = 0
    for ch in str:
        if ch >= 65 and ch <= 65+25:
            score += 1

        if ch >= 97 and ch < 97 + 26:
            score += 1

    return score


def find_best_score_for_word(hex_encoded_string):
    hex_decoded_bytes = hex_decode(hex_encoded_string)

    index_scores = []
    for i in range(256):
        input_bytes = bytes([i]) * len(hex_decoded_bytes)
        xor_string = xor(hex_decoded_bytes, input_bytes)
        score = assign_score(xor_string)
        index_scores.append((i, score, xor_string))

    index_scores = sorted(index_scores, key=lambda x: x[1], reverse=True)
    return (index_scores[0][1], index_scores[0][2])


def get_single_char_xor(hex_encoded_string):
    hex_decoded_bytes = hex_decode(hex_encoded_string)

    index_scores = []
    for i in range(256):
        input_bytes = bytes([i]) * len(hex_decoded_bytes)
        xor_string = xor(hex_decoded_bytes, input_bytes)
        score = assign_score(xor_string)
        index_scores.append((i, score, xor_string))

    index_scores = sorted(index_scores, key=lambda x: x[1], reverse=True)
    print(index_scores)

    # the very first entry here is the important character which caused the flip. It's "X"
    return chr(index_scores[0][0]), index_scores[0][2]


if __name__ == '__main__':
    hex_encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print(get_single_char_xor(hex_encoded_string))
