#The minion game

def minion_game(string):
    #define the vowels for reference
    vowels = 'AEIOU'
    kevin_score=0
    stuart_score=0
    length=len(string)
    
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length -i
        else:
            stuart_score+= length-i
    
    # Determine the winner or if it's a draw and print the result
    if(kevin_score>stuart_score):
        print("Kevin",kevin_score)
    elif(stuart_score>kevin_score):
        print("Stuart",stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)