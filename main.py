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
        citiesMenu()
      elif n==3:
        quit()
    except ValueError:
      print("Invalid input! please try again. ")

def citiesMenu():
  pass 

def driversMenu():
    print("\nWELCOME TO DRIVERS MENU")
    while True:
      try:
        n=int(input("""
1. To view all drivers
2. To add a driver
3. To go back to main menu
Please enter : """))
        if n==1:
          showDrivers()
        elif n==2:
          if addDRIVER()==True:
            pass 
          else:
            print("Avalibe cities are: ")
            print("\n")
            for c in citys:
              print(c,end=" ")
        elif n==3:
          Welcome()
      except ValueError:
        print("Invalid input! please try again. ")

def addDRIVER():
    name = input("Enter driver name: ").lower()
    startcity = input("Enter start city: ").lower()
    if startcity not in citys:
      return False
    else:
      D = Drivers(name,startcity)
      D.addDriver()
      return True

drivers = []
citys = ["beirut","zahle","akar","saida","jbeil"]
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



Welcome()