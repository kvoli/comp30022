import unittest, re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def invalid_email(x):
    a=0
    y=len(x)
    dot=x.find(".")
    at=x.find("@")
    for i in range (0,at):
        if((x[i]>='a' and x[i]<='z') or (x[i]>='A' and x[i]<='Z')):
            a=a+1
    return not (a>0 and at>0 and (dot-at)>0 and (dot+1)<y)

class Test(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_validate_email(self):
        self.assertFalse(invalid_email("k@github.com"))
        self.assertTrue(invalid_email("gg.com"))
        self.assertFalse(invalid_email("a@student.com"))

if __name__ == '__main__':
    unittest.main()
