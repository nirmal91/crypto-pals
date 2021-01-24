from s1.s1c3.single_byte_xor_cipher import find_best_score_for_word


if __name__ == '__main__':
    scores_and_sentences = []
    with open('4.txt', 'r') as f:
        for line in f.readlines():
            word = line.strip()
            score, sentence = find_best_score_for_word(word)
            print(score, sentence)
            scores_and_sentences.append((score, sentence))

    scores_and_sentences = sorted(scores_and_sentences, key=lambda x: x[0], reverse=True)

    # Ideally, the result should be at [0]. Improve the scoring function
    # The answer is "Now that the party is jumping"
    print(scores_and_sentences[1])
