
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


## Helper function that returns maximum input sequence length supported .
## To be completed and updated as we add support for other models as well. 
def getMaxLength(encoder):
  switcher = {
        'bert': 512,
        'longformer': 4096,
        'xlnet': None,
        'reformer': 64000,
        'finbert': None  # To be confirmed...
        'distilbert': 512 # To be confirmed...
        'roberta': 512
        'bart': 1024
        'use': 128,      # Source: https://github.com/tensorflow/hub/issues/572
        'transformer-xl': None
        'infersent': None,
        'sent2vec': None,
        'laser': None
        }

  return int(switcher.get(encoder, "Encoder not supported."))
  



### Similar to getSentenceVector() however we use a word tokenizer to calculate the document length for comparison
### with the results from getMeaxLength().  

def getDocumentEmbedding(doc, model_params: dict = {}, encoder = 'xlnet', model_name = 'xlnet-base-uncased'):
  #model = SentenceTransformer(model_name, model_params)
  #sentence_embedding = model.encode(doc)

  ## Word tokenizer
  from spacy.lang.en import English
  nlp = English()
  # Create a Tokenizer with the default settings for English including punctuation rules and exceptions
  tokenizer = nlp.Defaults.create_tokenizer(nlp)
  tokens = tokenizer("This is a sentence")
  if len(tokens) > getMaxLength(encoder):
    warnings.warn("The input sequence length exceeds the maximum limit.", Warning)



  if encoder in ['bert', 'xlnet', 'longformer', 'reformer', 'distilbert', 'roberta', 'bart', 'finbert']:
    # Use BERT for mapping tokens to embeddings
    word_embedding_model = models.Transformer(model_name)
    # Apply mean pooling to get one fixed sized sentence vector
    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                                   pooling_mode_mean_tokens=True,
                                   pooling_mode_cls_token=False,
                                   pooling_mode_max_tokens=False)
    model = SentenceTransformer(modules=[word_embedding_model, pooling_model])   
    sentence_embeddings = model.encode(doc)
    

  elif encoder == 'use':
    #!pip install embedding-as-service
    from embedding_as_service.text.encode import Encoder
    en = Encoder(embedding='use', model='use_dan', max_seq_length=256)
    sentence_embeddings = en.encode(texts=doc)


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
    sentence_embeddings = infersent.encode(doc, tokenize=True)


  elif encoder == 'sent2vec':
    import sent2vec
    model = sent2vec.Sent2vecModel()
    model.load_model('drive/My Drive/torontobooks_unigram.bin') 
    sentence_embeddings = model.embed_sentences(doc)



  elif encoder == 'laser':
    from laserembeddings import Laser
    laser = Laser()  ## Also used for multilingual sentence embeddings
    sentence_embeddings = laser.embed_sentences(sentences, lang='en') 


  return sentence_embeddings