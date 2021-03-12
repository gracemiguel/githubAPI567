import unittest
import hw4a 
 

class git_test(unittest.TestCase):
    def test1(self):
        self.assertEquals(hw4.github_repos("ladksjnfi"), "User does not exist  An exception has occurred, use %tb to see the full traceback.")
    def test2(self):
        self.assertRaises(TypeError, hw4.github_repos(4))
    def test3(self):
        self.assertEquals(hw4.github_repos(""))

      



