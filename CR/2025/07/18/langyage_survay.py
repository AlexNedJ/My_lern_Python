from survey import Anonymous_Survey
questiuon = 'what language did your first learn to speak? '
my_survay = Anonymous_Survey(questiuon)
my_survay.show_question()
print("Enter 'q' at any time to quite.\n")

while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survay.stor_respones(response)

print("\nThank you to everyone who participates i the survey")
my_survay.show_Resutls()