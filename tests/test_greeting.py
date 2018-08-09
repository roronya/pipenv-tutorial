from hello_world.greeting import greet
import unittest

class TestGreet(unittest.TestCase):
  def test_greet(self):
    result = greet('roronya')
    print(result)
    self.assertEqual(result, "Hello, roronya")

if __name__ == '__main__':
  unittest.run()
   
