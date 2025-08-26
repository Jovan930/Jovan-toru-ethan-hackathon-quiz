def display_score(score, total):
  print("Your Score is :", score)

  percentage = score / total * 100
  print("Your score: ", percentage, "%")

  if percentage >= 50:
    print("You smart, you passed the test.")
  else:
    print("You frikin failed the test.")
