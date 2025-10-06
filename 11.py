names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

def search(name):
    index=0
    while names[index]!=name:
        index=index+1
    return scores[index]
print(search('Bob'))