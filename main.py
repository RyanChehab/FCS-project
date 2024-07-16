# def Welcome():
#   print("Hello!")
#   while True:
#     try:
#       n=int(input("""
# 1. To go to the driver's menu
# 2. To go to the cities menu
# 3. To exit the system
# Please enter : """))
#       if n==1:
#         driversMenu()
#       elif n==2:
#         print("function2")
#       elif n==3:
#         quit()
#     except ValueError:
#       print("Invalid input! please try again. ")

# def driversMenu():
#     while True:
#       try:
#         n=int(input("""
# 1. To view all drivers
# 2. To add a driver
# 3. To go back to main menu
# Please enter : """))
#         if n==1:
#           print("show all drivers")
#         elif n==2:
#           print("add driver")
#         elif n==3:
#           Welcome()
#       except ValueError:
#         print("Invalid input! please try again. ")

class Drivers:
  def __init__(self,ID,name,startcity):
    self.ID=ID
    self.name=name
    self.startcity=startcity
    self.drivers=[]

  def addDriver(self,ID,name,startcity):
    newdriver= Drivers(ID,name,startcity)
    self.drivers.append(newdriver)
  
  def showDrivers(self):
    
    print("** List of Drivers:**")
    if not self.drivers:
      print("No drivers added")
    
    n=1
    for x in self.drivers:
      print(f"{n}. ID: {x.ID}, name: {x.name}, startcity: {x.startcity}")
      n+=1




