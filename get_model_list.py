

def get_model_list():

  l = {'bert': ['bert-base-uncased', 'bert-base-cased', 'bert-large-uncased', 'bert-large-cased'],
         'longformer': ['allenai/longformer-base-4096', 'allenai/longformer-large-4096'], 
         'xlnet': ['xlnet-base-cased', 'xlnet-large-cased'], 
         'finbert': ['anhdungitvn/finbert', 'ipuneetrathore/bert-base-cased-finetuned-finBERT']
         'reformer': ['google/reformer-enwik8'],
         'transformer-xl': ['transfo-xl-wt103'],
         'use': ['use-dan', 'use-transformer-lite', 'use-transformer-large'], 
         'infersent': [], 
         'laser': [],
         'sent2vec': []}

  print(l)      