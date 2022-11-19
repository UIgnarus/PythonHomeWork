file = "text.txt"
result = "text2.txt"

with open(file, 'r', encoding="utf-8") as f:
    text = f.read()

text = text.split()
for i in range(len(text)):
    if "абв" in text[i]:
        if not text[i].isidentifier():
            text[i] = text[i][-1]
        else: 
            text[i] = ''
text = " ".join(text)
print(text)
with open(result, "w", encoding="utf-8") as f:
    f.write(text)