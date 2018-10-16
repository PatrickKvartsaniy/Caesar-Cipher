alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(n):
  with open('msg.txt', 'r') as f:
    ciphertext = f.read()
  result = ''

  for l in ciphertext:
      try:
          i = (alphabet.index(l) - n) % 26
          result += alphabet[i]
      except ValueError:
          result += l
  print(f"Key:{n}-Message:{result}")

for key in range(1,27):
  decrypt(key)