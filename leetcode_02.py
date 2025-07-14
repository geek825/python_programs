score = []

while True:
    score_number = input("Enter the number :")
    
    if score_number == 'c':
        if score:
            score.pop()
        else:
            print("Score is already empty")
    elif score_number == 'd':
        if score:
            last = int(score[-1])
            score.append(str(2 * last))
        else:
            print("No score to dobule")
    elif score_number == 't':
        if score:
            total = 0 
            for i in score:
                total += int(i)
            print(total)
        else:
            print("No total score")
    else:
        score.append(score_number)

    print(score)