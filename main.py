drivers = []
citys = {"beirut":0,
         "zahle":1,
         "akar":2,
         "saida":3,
         "jbeil":4}                   #Global arrays
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
          for c in citys:
            print(c,end=" ")                                         #Drivers Menu
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

class Node:
  def __init__(self, info, next):
    self.info = info
    self.next = next

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0  #how many nodes are in my LL

  def addToHead(self, info):  #O(1)
    n = Node(info, None)
    if self.size == 0:  # LL is empty, I have no nodes inside
      self.head = n
      self.tail = n
      self.size = 1
    else:
      n.next = self.head
      self.head = n
      self.size += 1

  def addToTail(self, info):  #O(1)
    if self.size == 0:
      self.addToHead(info)
    else:
      n = Node(info, None)
      self.tail.next = n
      self.tail = n
      self.size += 1


  def deleteHead(self):  # O(1)
    if self.size == 0:  # empty
      return None
    elif self.size == 1:
      val = self.head.info
      self.head = None
      self.tail = None
      self.size = 0
      return val
    else:
      val = self.head.info
      self.head = self.head.next
      self.size -= 1
      return val


  def printLL(self):  #O(n), where n is the number of nodes in the list
    list_of_key = list(citys.keys())
    list_of_value = list(citys.values())

    i = self.head
    while i != None:
      position = list_of_value.index(i.info)
      print(list_of_key[position],"->", end="")
      i = i.next
    print()


  def deleteTail(self): #O(n), where n is the length of my LL
    if self.size<=1:
      return self.deleteHead()
    else:
      val=self.tail.info
      #loop to find the element before the last
      i=self.head
      while i.next.next!=None: #I did not reach the node before the last
        i=i.next
      #update the tail and its next
      self.tail=i
      self.tail.next=None
      self.size-=1
      return val

  # remove the node that contains info
  def removeNode(self,info):
    pass
    
  # search for info in LL 
  def search(self,info):
    if self.size==0:
      return False
    current=self.head
    while current!=None:
      if current.info==info:
        return True
      current=current.next
    return False

class AdjacencyList:
  def __init__(self,V):
    self.graph=[]
    for i in range(V):
      self.graph.append(LinkedList())

  def addEdge(self,i,j):
    #O(V)
    if self.graph[i].search(j):
      return None
    else:
      self.graph[i].addToHead(j)
  #O(V)
  def deleteEdge(self,i,j):
    self.graph[i].removeNode(j)

  def printGraph(self):
    list_of_key = list(citys.keys())
    list_of_value = list(citys.values())
  
    for i in range(len(self.graph)):
      position = list_of_value.index(i)
      print(list_of_key[position],end=": ")
      self.graph[i].printLL()

graph=AdjacencyList(5)

graph.addEdge(citys["jbeil"],citys["akar"])
graph.addEdge(citys["jbeil"],citys["beirut"])
graph.addEdge(citys["akar"],citys["jbeil"])
graph.addEdge(citys["beirut"],citys["jbeil"])
graph.addEdge(citys["saida"],citys["zahle"])
graph.addEdge(citys["zahle"],citys["saida"])
graph.printGraph()

#Welcome()