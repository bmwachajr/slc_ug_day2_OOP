import unittest
from unittest import TestCase
from OOP import Animal
from OOP import Pet

class OOPTestCases(unittest.TestCase):    
  def setUp(self):
    self.Animal_1 = Animal("Henry", "Male")
    self.Animal_2 = Animal("Wolfee", "Male")
    
    self.bato = Pet("Bato", "Male", "Dog")
    
    self.pet1 = Pet()
    self.pet2 = Pet()
    
  def test_ouput_Animal1(self):
    result1 = self.Animal_1.getName()
    result2 = self.Animal_2.getName()
    self.assertEqual(self.Animal_1.getName(), "Henry", msg='Expected {}, got {}'.format("Henry", result1))
    self.assertEqual(self.Animal_1.getGender(), "Male", msg='Expected {}, got {}'.format("Male", result2))

  def test_ouput_Animal2(self):
    result1 = self.Animal_2.getName()
    result2 = self.Animal_2.getGender()
    self.assertEqual(self.Animal_2.getName(), "Wolfee", msg='Expected {}, got {}'.format("Wolfee", result1))
    self.assertEqual(self.Animal_2.getGender(), "Male", msg='Expected {}, got {}'.format("Male", result2))

  def test_ouput_bato(self):
    result1 = self.bato.getName()
    result2 = self.bato.getGender()
    result3 = self.bato.gettype()
    self.assertEqual(self.bato.getName(), "Bato", msg='Expected {}, got {}'.format("Bato", result1))
    self.assertEqual(self.bato.getGender(), "Male", msg='Expected {}, got {}'.format("Male", result2))
    self.assertEqual(self.bato.gettype(), "Dog", msg='Expected {}, got {}'.format("Dog", result3))
    
  def test_ouput_pet(self):
    self.pet1.setName("Rat")
    self.pet1.setGender("Female")
    self.pet1.settype("Silver back Rat")
    self.assertEqual(self.pet1.getName(), "Rat", msg='Expected {}, got {}'.format("Rat", self.pet1.getName()))
    self.assertEqual(self.pet1.getGender(), "Female", msg='Expected {}, got {}'.format("Female", self.pet1.getGender()))
    self.assertEqual(self.pet1.gettype(), "Silver back Rat", msg='Expected {}, got {}'.format("Silver back Rat", self.pet1.gettype()))
    
  
  def test_empty_pet(self):
    result1 = self.pet2.getName()
    result1 = self.pet2.getGender()
    result1 = self.pet2.gettype()
    self.assertEqual(self.pet2.getName(), "", msg='Expected {}, got {}'.format("", result1))
    self.assertEqual(self.pet2.getGender(), "", msg='Expected {}, got {}'.format("", result2))
    self.assertEqual(self.pet2.gettype(), "", msg='Expected {}, got {}'.format("", result3))
    

      
if __name__ == "__main__":
  unittest.main()