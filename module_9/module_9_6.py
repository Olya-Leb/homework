def all_variants(text):
    for x in range(len(text)):
        for y in range(x, len(text)):
            yield text[x: y+1]

a = all_variants("abc")
for i in a:
    print(i)