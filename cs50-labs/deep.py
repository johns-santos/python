

userAnswer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
correctAnswer = "Yes"

if userAnswer == "42" or userAnswer == "forty-two" or userAnswer == "forty two":
    print("Yes")
else:
    print("No")