freq = 'esiarntolcdugpmkhbyfvwzxqj'
findCharacters = ['o','r','y','p']
characterPosition = [-2,-2,4,0]
notin = ['a','n','i','s','e','c','u','t','l','d','g','k']
# posNotin = []
with open("\\words.txt") as f:
    words = f.readlines()
    words = [w.strip() for w in words]
    words = [w.lower() for w in words]
    highscore = 100000
    for word in words:
        score = 0
        if len(word) != 5:
            continue
        if len(set(list(word))) != len(word):
            continue
        flag = 0
        i = -1
        for charecter in findCharacters:
            i += 1
            charPosition = word.find(charecter)
            if (charPosition == -1):
                flag = -1
                continue 
            if ((characterPosition[i] != charPosition) and (characterPosition[i] != -2)):
                flag = -1
                continue 
                
#         print (word ,char ,position ,characterPosition[i],i,flag)
        if flag  != -1 :
            for no in notin:
#               print (word ,char ,position ,characterPosition[i],i)
                if(word.find(no)!=-1):
                    flag=-1
                    continue
        if flag  != -1 :
            for c in word:
                if c in freq:
                    score += freq.index(c)
                else:
                    score = 100
            if score < highscore:
                highscore = score
                print (word, score)
    
    
