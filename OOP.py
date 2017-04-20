class Animal(object):
  def __init__(self, *args):
    if len(args) >=2:
      self.name = args[0]
      self.gender = args[1]
    else:
      self.name = ""
      self.gender = ""
    
  def setName(self, name):
    self.name= name

  def setGender(self, gender):
    self.gender = gender
	   
  def getName(self):
    return self.name

  def getGender(self):
    return self.gender

class Pet(Animal):
    type = ''
    def __init__(self, *args):
      if len(args) >= 3:
        self.name = args[0]
        self.gender = args[1]
        type = args[2]
      else:
        self.name = ''
        self.gender = ''
        type = ''
    
    def settype(self, type):
        self.type = type
    
    #method to get type
    def gettype(self):
        return self.type
    