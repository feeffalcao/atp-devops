import unittest

def soma(a, b): return a + b

class TestProjeto(unittest.TestCase):
    def test_1(self): self.assertEqual(soma(2, 2), 4)
    def test_2(self): self.assertEqual(soma(10, -5), 5)
    def test_3(self): self.assertTrue(True)
    def test_4(self): self.assertIn("PUC", "ATP PUC-PR")
    def test_5(self): self.assertNotEqual(10, 20)
