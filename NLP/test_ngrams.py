import re
from nltk.util import ngrams

if __name__ == "__main__":
    sentence = "I love deep learning as it can help me resolve some complicated problems in 2018."

    # tokenize the sentence into tokens
    pattern = re.compile(r"([-\s.,;!?])+")
    tokens = pattern.split(sentence)
    tokens = [x for x in tokens if x and x not in '- \t\n.,;!?']

    bigrams = list(ngrams(tokens, 2))
    print([" ".join(x) for x in bigrams])
