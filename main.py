print("Affirmations")
userName = input("What is your Name?: ")
print("My name is ", userName)
print()
currentDayOfTheWeek = input("What is the current day of the week?: ")
print("Today is ", currentDayOfTheWeek)
if currentDayOfTheWeek == "Monday":
  print(userName, " Monday is a busy day to start working.")
elif currentDayOfTheWeek == "Tuesday":
  print(userName, " Tuesday is hot for this season.")
elif currentDayOfTheWeek == "Wednesday":
  print(userName, "It is the middle of the week.")
elif currentDayOfTheWeek == "Thursday":
  print("One more day to weekend")
elif currentDayOfTheWeek == "Friday":
  print(userName, "Finally Friday is here, can't wait for tomorrow.")
else:
 print(userName, " Weekend is here. Lets chill out.")
print()
favMovie = input("What is your favorite movie?: ")
print("My favorite Movie is ",favMovie)
print()
favLocation = input("What is your favorite location?: ")
if favLocation == "Paris" or favLocation == "paris":
  print("Beautiful location to visit.")
else: 
  print("Nice to visit")