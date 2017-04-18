import unittest
from unittest import TestCase
from OOP import Animal
from OOP import Pet

class OOPTestCases(unittest.TestCase):    
  def setUp(self):
    self.Animal_1 = Animal("Henry", "Male")
    self.Animal_2 = Animal("Wolfee", "Male")

    self.pet1 = Pet()
    self.pet1.name = "Rat"
    self.pet1.gender = "Female"
    self.pet1.type = "Silver back Rat"
    
    self.pet2 = Pet()
    
  def test_Object_Animal1(self):
    result1 = self.Animal_1.getName()
    result2 = self.Animal_2.getName()
    self.assertEqual(self.Animal_1.getName(), "Henry", msg='Expected {}, got {}'.format("Henry", result1))
    self.assertEqual(self.Animal_1.getGender(), "Male", msg='Expected {}, got {}'.format("Male", result2))

  def test_Object_Anima2(self):
    result1 = self.Animal_2.getName()
    result2 = self.Animal_2.getGender()
    self.assertEqual(self.Animal_2.getName(), "Wolfee", msg='Expected {}, got {}'.format("Wolfee", result1))
    self.assertEqual(self.Animal_2.getGender(), "Male", msg='Expected {}, got {}'.format("Male", result2))
    
  def test_Pet_pet(self):
    self.assertEqual(self.pet1.getName(), "Rat", msg='Expected {}, got {}'.format("Rat", self.pet1.getName()))
    self.assertEqual(self.pet1.getGender(), "Female", msg='Expected {}, got {}'.format("Female", self.pet1.getGender()))
    self.assertEqual(self.pet1.type, "Silver back Rat", msg='Expected {}, got {}'.format("Silver back Rat", self.pet1.type))
    
  
  def test_empty_pet(self):
    result1 = self.pet2.getName()
    result2 = self.pet2.getGender()
    result3 = self.pet2.type
    self.assertEqual(self.pet2.getName(), "", msg='Expected {}, got {}'.format("", result1))
    self.assertEqual(self.pet2.getGender(), "", msg='Expected {}, got {}'.format("", result2))
    self.assertEqual(self.pet2.gettype(), "", msg='Expected {}, got {}'.format("", result3))
    

      
if __name__ == "__main__":
  unittest.main()