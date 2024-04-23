from gensim.models import Word2Vec
from gensim.utils import tokenize

def preprocess(line):
    line = line.lower()
    tokens = tokenize(line)
    return list(tokens)

file = open("small.txt")

sentences = []
for line in file:
    sentences.append(preprocess(line))

print("Model training started!")
model = Word2Vec(sentences, min_count=2, epochs=20, vector_size=300)

model.save("dre_w2v.model")