drivers = []
citys = ["beirut","zahle","akar","saida","jbeil"]                   #Global arrays
global id
id = 0

def Welcome():
  print("Hello!")
  while True:
    try:
      n=int(input("""
1. To go to the driver's menu
2. To go to the cities menu
3. To exit the system
Please enter : """))
      if n==1:                                                        #Welcome Function
        driversMenu()
      elif n==2:
        citiesMenu()
      elif n==3:
        quit()
    except ValueError:
      print("Invalid input! please try again. ")

def citiesMenu():
    print("\n**WELCOME TO CITIES MENU**")
    while True:
      try:
        n=int(input("""
1. To show cities
2. Print neighboring cities
3. Print drivers delivering to city
Please enter : """))
        if n==1:
          pass                                    #Drivers Menu
        elif n==2:
          pass
        elif n==3:
          pass
      except ValueError:
        print("Invalid input! please try again. ")                                       #Cities Menu

def driversMenu():
    print("\n**WELCOME TO DRIVERS MENU**")
    while True:
      try:
        n=int(input("""
1. To view all drivers
2. To add a driver
3. To go back to main menu
Please enter : """))
        if n==1:
          showDrivers()                                                #Drivers Menu
        elif n==2:
          addDRIVER()
        elif n==3:
          Welcome()
      except ValueError:
        print("Invalid input! please try again. ")

def showDrivers():
  if len(drivers)==0:                                       #show drivers functiom
    print("No drivers")
  else:
    for x in drivers:
      print(f"ID: {x.ID}, name: {x.name}, startcity: {x.startcity}")

def addDRIVER():
    name = input("Enter driver name: ").lower()
    startcity = input("Enter start city: ").lower()
    if startcity not in citys:
      print("Avalibe cities are: ")
      print("\n")
      for c in citys:
        print(c,end=" ")                                         #Add drivers function
    else:
      D = Drivers(name,startcity)
      D.addDriver()

class Drivers:
  def __init__(self,name,startcity):
    global id
    self.ID = id 
    self.name=name                                            #Drivers Class
    self.startcity=startcity
    id+=1 

  def addDriver(self):
    drivers.append(self)

Welcome()