from gensim.utils import tokenize
import nltk 
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from gensim.similarities import SparseMatrixSimilarity

#nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

f_small = open("small.txt")

def preprocess(line):
    line = line.lower()
    tokens = tokenize(line)
    tokens = [token for token in tokens if token not in stopwords]
    return list(tokens)

sentences = []
notes = f_small.readlines()
for line in notes:
    sentences.append(preprocess(line))

dictionary = Dictionary(sentences)

corpus_bow = [dictionary.doc2bow(sent) for sent in sentences]

tfidf_model = TfidfModel(corpus_bow, normalize=True)

index = SparseMatrixSimilarity(tfidf_model[corpus_bow], num_docs= len(corpus_bow), num_terms= len(dictionary))

query ="leis de emigração e politicas estrangeiras"
query_tokenized = preprocess(query)

query_bow = dictionary.doc2bow(query_tokenized)
tfidf_query = tfidf_model[query_bow]

sims = index[tfidf_query]

sims_ordered = sorted(enumerate(sims), key= lambda item: item[1], reverse = True)

for index, sim in sims_ordered[:10]:
    print(sim)
    print(notes[index])

