words = ["apple", "banana", "grape", "blueberry", "orange"]  
ch = input().strip()  

count = 0  

for word in words:
    
    if len(word) >= 4 and (word[2] == ch or word[3] == ch):
        print(word)  
        count += 1   

print(count) 
