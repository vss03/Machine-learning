import wikipedia
import re
import nltk
from nltk.util import ngrams
from collections import Counter
import matplotlib.pyplot as plt

topic1="Elephant"
wikipedia.set_lang('fr')
fr1 = wikipedia.page(topic1).content

def cleanup(text):
  text = text.lower()  # make it lowercase
  text = re.sub('[^a-z]+', '', text) # only keep characters
  return text

eng=cleanup(fr1)
# convert a tuple of characters to a string
def tuple2string(tup):
  st = ''
  for ii in tup:
    st = st + ii
  return st

# convert a tuple of tuples to a list of strings
def key2string(keys):
  return [tuple2string(i) for i in keys]

# plot the histogram
def plothistogram(ngram):
  keys = key2string(ngram.keys())
  values = list(ngram.values())

  # sort the keys in alphabetic order
  combined = zip(keys, values)
  zipped_sorted = sorted(combined, key=lambda x: x[0])
  keys, values = map(list, zip(*zipped_sorted))
  plt.bar(keys, values)

trigram_fr1 = Counter(ngrams(fr1,3))
plothistogram(trigram_fr1)
plt.title('French 1')
plt.show()
