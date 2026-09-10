import unittest
from vec import Vec

class TestVec(unittest.TestCase):
    def test_init_and_null(self):
        v = Vec((1,2,3))
        self.assertEqual(v.elements,(1,2,3))
        self.assertEqual(len(v),3)

    def test_zeros(self):
        z= Vec.zeros(3)
        self.assertEqual(len(z),3)

    def test_add(self):
        v1 = Vec((1,2))
        v2 = Vec((3,4))
        self.assertEqual((v1+v2).elements,(4,6))

    def test_radd(self):
        v1 = Vec((1,2))
        self.assertEqual((3+v1).elements,(4,5))

    def test_imul(self):
        v = Vec((2,4))
        v*=3
        self.assertEqual(v.elements,(6,12))

    def test_uniform(self):
        v = Vec.uniform(3)
        self.assertEqual(len(v),3)
        for value in v.elements:
            self.assertTrue(0 <= value <= 1)

    def test_dimention(self):
        with self.assertRaises(TypeError):
            _= Vec((1,2)+Vec(1,2,3))


if __name__ == "__main__":
    unittest.main()
        
