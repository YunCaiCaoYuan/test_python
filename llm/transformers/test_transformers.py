### 1、
#from transformers import pipeline

#translator = pipeline("translation_en_to_fr")
#print(translator("How old are you?"))

#translator = pipeline("translation_en_to_zh", model='Helsinki-NLP/opus-mt-en-zh')
#translator("I'm learning deep learning.")


### 2、
from transformers import AutoModel , AutoTokenizer,MarianMTModel
from transformers import pipeline

text ="Memphis is a series of models which advance human-data models, offering good performance without relying on proprietary model outputs"
mname ='Helsinki-NLP/opus-mt-en-zh'
translator = pipeline(model=mname)
print(translator(text)[0].get("generated_text"))


