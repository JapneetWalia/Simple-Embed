'''
##############
Dependencies
##############

!pip install git+https://github.com/UKPLab/sentence-transformers
!pip install embedding_as_service
!pip install laserembeddings
!python -m laserembeddings download-models
!pip install sent2vec

'''


import spacy
from sentence_transformers import SentenceTransformer 
from sentence_transformers import models


# Works for most of the HuggingFace models and some other models as well.

def getSentenceVector(doc, model_params: dict = {}, encoder = "bert", model_name = 'bert-base-cased' ):
  
  sp = spacy.load('en_core_web_sm')
  tokenized = sp(doc)
  sentences = []
  for token in tokenized.sents:
    sentences.append(token.text)

  if encoder in ['bert', 'xlnet', 'longformer', 'reformer', 'distilbert', 'roberta', 'bart', 'finbert']:
    # Use encoder for mapping tokens to embeddings
    word_embedding_model = models.Transformer(model_name, 
                tokenizer_args= model_params['tokenizer_args'] if 'tokenizer_args' in model_params else {})
    # Apply mean pooling to get one fixed sized sentence vector
    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                                   pooling_mode_mean_tokens=True,
                                   pooling_mode_cls_token=False,
                                   pooling_mode_max_tokens=False)
    model = SentenceTransformer(modules=[word_embedding_model, pooling_model])   
    sentence_embeddings = model.encode(sentences)
    

  elif encoder == 'use':
    #!pip install embedding-as-service
    from embedding_as_service.text.encode import Encoder
    en = Encoder(embedding='use', model='use_dan', max_seq_length=256)
    sentence_embeddings = en.encode(texts=sentences)


  elif encoder == 'infersent':
    import nltk
    nltk.download('punkt')
    from models import InferSent
    params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                    'pool_type': 'max', 'dpout_model': 0.0, 'version': 2}
    infersent = InferSent(params_model)
    W2V_PATH = 'drive/My Drive/wiki-news-300d-1M.vec'
    infersent.set_w2v_path(W2V_PATH)
    infersent.build_vocab(sentences, tokenize=True)
    sentence_embeddings = infersent.encode(sentences, tokenize=True)


  elif encoder == 'sent2vec':
    import sent2vec
    model = sent2vec.Sent2vecModel()
    model.load_model('drive/My Drive/torontobooks_unigram.bin') 
    sentence_embeddings = model.embed_sentences(sentences)
   

  elif encoder == 'laser':
    from laserembeddings import Laser
    laser = Laser()  ## Also used for multilingual sentence embeddings
    sentence_embeddings = laser.embed_sentences(sentences, lang='en') 
  
  
  else:
    raise ValueError('Invalid encoder {} or encoder Unavailable.'.format(encoder))  
  
  return list(zip(sentences, sentence_embeddings))