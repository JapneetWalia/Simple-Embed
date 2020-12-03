def get_meta_data(encoder, model = ''):

  if encoder == 'bert':
    if model == 'bert-base-uncased':
      meta_data = {'Number_of_layers': 12, 'Number_of_hidden_states': 768, 'Number_of_attention_heads': 12 , 'Number_of_parameters': '110M'}
    elif model == 'bert-base-cased':
      meta_data = {'Number_of_layers': 12, 'Number_of_hidden_states': 768, 'Number_of_attention_heads': 12 , 'Number_of_parameters': '109M'}  
    elif model == 'bert-large-uncased':
      meta_data = {'Number_of_layers': 24, 'Number_of_hidden_states': 1024, 'Number_of_attention_heads': 16 , 'Number_of_parameters': '336M'}
    elif model == 'bert-large-cased':
      meta_data = {'Number_of_layers': 24, 'Number_of_hidden_states': 1024, 'Number_of_attention_heads': 16 , 'Number_of_parameters': '335M'}  
    else:
      meta_data = 'Model Not Supported Yet.'



  if encoder == 'finbert':
    if model == 'ipuneetrathore/bert-base-cased-finetuned-finBERT':
      meta_data = {'Number_of_layers': 12, 'Number_of_hidden_states': 768, 'Number_of_attention_heads': 12 , 'Number_of_parameters': '110M'}
    elif model == 'anhdungitvn/finbert':
      meta_data = {'Number_of_layers': 12, 'Number_of_hidden_states': 768, 'Number_of_attention_heads': 12 , 'Number_of_parameters': '109M'}  
    else:  
      meta_data = 'Model Not Supported Yet.'



  elif encoder ==  'longformer':
    if model == 'allenai/longformer-base-4096':
      meta_data = {'Number_of_layers': 12, 'Number_of_hidden_states': 512, 'Number_of_attention_heads': 8 , 'Number_of_parameters': '41M'}
    elif model == 'allenai/longformer-large-4096':
      meta_data = {'Number_of_layers': 30, 'Number_of_hidden_states': 512, 'Number_of_attention_heads': 8 , 'Number_of_parameters': '102M'} 
    else:
      meta_data = 'Model Not Supported Yet.'  


  elif encoder ==  'xlnet':
    if model == 'xlnet-base-cased':
      meta_data = {'Number_of_layers': 12, 'Number_of_hidden_states': 768, 'Number_of_attention_heads': 12 , 'Number_of_parameters': '110M'}
    elif model == 'xlnet-large-cased':
      meta_data = {'Number_of_layers': 24, 'Number_of_hidden_states': 1024, 'Number_of_attention_heads': 16 , 'Number_of_parameters': '340M'}  
    else:
      meta_data = 'Model Not Supported Yet.'   



  elif encoder ==  'transformer-xl':
    if model == 'transfo-xl-wt103':
      meta_data = {'Number_of_layers': 18, 'Number_of_hidden_states': 1024, 'Number_of_attention_heads': 16, 'Number_of_parameters': '257M'} 
    else:
      meta_data = 'Model Not Supported Yet.' 



  elif encoder ==  'roberta':
    if model == 'xlnet-base-cased':
      meta_data = {'Number_of_layers': 12, 'Number_of_hidden_states': 768, 'Number_of_attention_heads': 12 , 'Number_of_parameters': '110M'}
    elif model == 'xlnet-large-cased':
      meta_data = {'Number_of_layers': 24, 'Number_of_hidden_states': 1024, 'Number_of_attention_heads': 16 , 'Number_of_parameters': '340M'}  
    else:
      meta_data = 'Model Not Supported Yet.'



  elif encoder == 'use':
    if model == 'use-dan':
      meta_data = 'No Data'
    elif model == 'use-transformer-lite':
      meta_data = 'No Data'
    elif model == 'use-transformer-large':
      meta_data =  'No Data'   
    else:
      meta_data = 'Model Not Supported Yet.'  
      

  elif encoder == 'infersent':
    meta_data = 'No Data'


  elif encoder == 'laser':
    meta_data = 'No Data'

    
  elif encoder == 'use-transformer-lite':
    meta_data = 'No Data'

  else:
    meta_data = 'Unknown Encoder.'
  return meta_data

    