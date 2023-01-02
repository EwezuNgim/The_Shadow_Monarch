alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
a=[]


def encrypt(text):
    text=text.split()
    text=''.join(text)
    #text=text.split('')
    print(text)
    print(text[0])
    for word in text:
      if(alphabet.index(word) + shift<=25):
        a.append(alphabet[alphabet.index(word) + shift])
      else:
          a.append(alphabet[alphabet.index(word) + shift - 26])
    print(text)
    print("The encoded text is," ''.join(a))
    
    
encrypt(text)
        
def decrypt(text):
    text=text.split()
    text=''.join(text)
    #text=text.split('')
    print(text)
    for word in text:
        a.append(alphabet[alphabet.index(word) - shift])
      
    print(text)
    print("The encoded text is", ''.join(a))
    
if direction=='decode':
   decrypt(text)
else:
    if direction=='encode':
        encrypt(text)
    else:
     print("Wrong key")
     
