import unittest
import builtins
from unittest.mock import patch
import hw4a 
 

class git_test(unittest.TestCase):
    @patch('hw4a.get_user_id', return_value = "")
    def test1(self, input):
        self.assertEqual(hw4a.github_repos(), "No id given")

    @patch('hw4a.get_user_id', return_value = "askjfklsd")
    def test2(self, input):
        self.assertEquals(hw4a.github_repos(), "User does not exist")
    
    @patch('hw4a.get_user_id', return_value ="gracemiguel")
    def test3(self, input):
        self.assertEquals(hw4a.github_repos(), "Repo: coding-interview-university Number of commits: 30\nRepo: githubAPI567 Number of commits: 7\nRepo: gnation1 Number of commits: 1\nRepo: hello-world Number of commits: 3\nRepo: modSim Number of commits: 2 \nRepo: SSW567 Number of commits: 7\nRepo: StevensHiking Number of commits: 15\nRepo: Triangle Number of commits: 9")
 

if __name__ == '__main__':
    unittest.main()
      



