a = input("текст на английском вводи: ")
b = ' '.join(w[0].upper() + w[1:].lower() for w in a.split())
print(b)
