from gensim.models import Word2Vec
from gensim.similarities import WmdSimilarity
from gensim.utils import tokenize
import nltk 
#nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

model_w2v = Word2Vec.load("dre_w2v.model").wv
model_w2v.init_sims(replace=True) 

#model_w2v.fill_norms()
f_small = open("small.txt")

def preprocess(line):
    line = line.lower()
    tokens = tokenize(line)
    tokens = [token for token in tokens if token not in stopwords]
    return list(tokens)

sentences = []
notes = f_small.readlines()
for line in notes:
    tokens = preprocess(line)
    sentences.append(tokens)

doc_index = WmdSimilarity(sentences, model_w2v, num_best= 10)

query = "leis para emigração e politicas estrangeiras"

query_tokens = preprocess(query)

sims = doc_index[query_tokens]

for index, sim in sims:
    print('sim = %.4f' % sim)
    print(notes[index])