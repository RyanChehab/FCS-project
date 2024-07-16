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
        driversMenu()
      elif n==2:
        print("function2")
      elif n==3:
        quit()
    except ValueError:
      print("Invalid input! please try again. ")

def driversMenu():
    while True:
      try:
        n=int(input("""
1. To view all drivers
2. To add a driver
3. To go back to main menu
Please enter : """))
        if n==1:
          print("show all drivers")
        elif n==2:
          print("add driver")
        elif n==3:
          Welcome()
      except ValueError:
        print("Invalid input! please try again. ")


drivers = []
citys = []
global id
id = 0

class Drivers:
  def __init__(self,name,startcity):
    global id
    self.ID = id 
    self.name=name
    self.startcity=startcity
    id+=1 

  def addDriver(self):
    drivers.append(self)
  

def showDrivers():
  if len(drivers)==0:
    print("No drivers")
  else:
    for x in drivers:
      print(f"ID: {x.ID}, name: {x.name}, startcity: {x.startcity}")


if __name__ == 'main':
  Welcome()