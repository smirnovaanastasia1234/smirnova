!pip install transformers sentencepiece sacremoses
from transformers import pipeline
classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
x =  input("Введите текст ")
classifier(x)