a,b=map(str,input().split())
if len(a)>len(b):
    print(a,len(a),end=' ')
if len(a)<len(b):
    print(b,len(b),end=' ')
else:
    print('same')


# sentence = "He says \"It's a really simple sentence\"."
# print(sentence)