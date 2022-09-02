import os, time, sys

#Deletando arquivos Day - 1 em pastas distintas

caminho= r"<caminho>"
  
path = caminho +  r"\tmp"
now = time.time()

for filename in os.listdir(path):
  if os.path.getmtime(os.path.join(path, filename)) < now - 1 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))
            
            
path = caminho +  r"\upload" 
now = time.time()

for filename in os.listdir(path):
  if os.path.getmtime(os.path.join(path, filename)) < now - 1 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))