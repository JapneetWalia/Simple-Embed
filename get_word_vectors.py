import spacy
!python3 -m spacy download en_core_web_sm

def get_word_vector(sentence):
  nlp = spacy.load("en_core_web_sm")
  tokens = nlp(sentence)
  words = []; vectors = []
  for token in tokens:
    words.append(token.text)
    vectors.append(token.vector_norm)    #token.has_vector, token.is_oov
  return list(zip(words, vectors))
    



## Function call

res = get_word_vector('This is a sentence')
for token in res:
    print('{}: {}'.format(token[0], token[1]))