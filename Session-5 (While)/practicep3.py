print("Một con vịt bình thường có mấy chân? 1. 2 chân, 2. 3 chân, 3. 1 chân, 4. 0 chân")
while True:
    answer = input("Enter your answer")
    if answer.isalpha():
        print("Invalid choice. Hãy nhập lại")
    else:
        int_answer = int(answer)
        if int_answer in range (1,5) and int_answer !=1:
            print("Wrong answer")
            break
        elif int_answer == 1:
            print("Right answer")
            break
        else: 
            print ("Invalid choice. Hãy nhập lại")

