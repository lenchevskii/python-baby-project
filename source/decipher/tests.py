import os
import unittest


class MyTest(unittest.TestCase):
    async def test(self):
        expected_output = "edward"
        output = await os.popen('python3 edward.py cipher.txt').read().strip()
        self.assertEqual(output, expected_output)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
