
ques = { "Who wrote the play Romeo and Juliet? " :"C",
        "Who painted the Mona Lisa? " :"A",
        "Who wrote Harry Potter? " : "B",
        "Who was the first President of the United States?" : "B",
        "What planet is known as the Red Planet?" : "A"
}

answers = [["A. Ahmed Shawqi","B. Bukovski","C. William Shakespeare"],
        ["A. Leonardo Da Vinci","B. Pablo Picasso","C. Salvador Dali"],
        ["A. James Joyce","B. J.K. Rowling","C. Ernest Hemingway"],
        ["A. James Madison","B. George Washington","C. braham Lincoln","D. George Bush"],
        ["A. Mars","B. Jupiter","C. Venus","D. Neptune"]]

def quiz_game():
    sum = 0
    user=None
    score =[]
    rec = 0

    for key in ques:
        print()
        print(key)
        for i in answers[rec]:
            print(i)
        user= (input("PLEASE ENTER YOUR GUESSES : ")).upper()
        score.append(user)
        sum += check_answers(ques.get(key),user)
        rec+=1

    dis_score(sum , score)


def check_answers(answers,user):
        if answers == user:
            print("CORRECT!!")
            return 1
        else :
            print("WRONG!!")
            return 0



def dis_score(sum,score):
    print("THE CORRECT ANSWERS : ",end="")
    for i in ques:
        print(ques.get(i),end=" ")
    print()
    print("YOUR GUESSES : ",end="")
    for i in score:
        print(i,end=" ")
    print()
    res = int((sum/len(ques))*100)
    print("RESUALT : "+str(res)+"%")

def new_again():    #_________________________this game still end yet_________________________#
    pass

quiz_game()           