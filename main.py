def Welcome():
  print("Hello!")
  while True:
    try:
      n=int(input("""
1. To go to the driver's menu
2. To go to the cities menu
3. To exit the system
Please enter : """))
      if n==1:
        print("function1")
      elif n==2:
        print("function2")
      elif n==3:
        quit()
    except ValueError:
      print("Invalid input! please try again. ")

Welcome()