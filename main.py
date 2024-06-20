import json
import requests 

def main(): 
  num= input("Ingresa un numero: ")
  print(trivia_fetch(num))

def trivia_fetch(num): 
  response = requests.get("http://numbersapi.com/" + str(num) + "?json")
  valor = json.loads(response.content)
  return valor

if __name__=="__main__":
  main()