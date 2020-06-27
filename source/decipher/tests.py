import subprocess
import unittest


class MyTest(unittest.TestCase):
    def test_case1(self):
        expected_output = "edward"
        output = subprocess.run(['python3', 'edward.py', 'cipher1.txt'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(output, expected_output)

    def test_case2(self):
        expected_output = "edwardlenchevski"
        output = subprocess.run(['python3', 'edward.py', 'cipher2.txt'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(output, expected_output)

    def test_case3(self):
        expected_output = ""
        output = subprocess.run(['python3', 'edward.py', 'cipher3.csv'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(output, expected_output)

    def test_case4(self):
        expected_output = ""
        output = subprocess.run(['python3', 'edward.py', 'cipher4.txt'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
