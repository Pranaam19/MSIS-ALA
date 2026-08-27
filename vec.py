
import sys
import random
from typing import Self


"""
A custom vector class implementation for educational purposes.
"""

class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = ()
        else:
            elements = tuple(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

    def __add__(self, t: Self) -> Self:
        '''
        Adds two vectors of the same dimension.
        Raise TypeError if dimentions are not the same or if the other operand is not a Vec.
        '''
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        return Vec((round(x + y, 5) for x, y in zip(self.elements, t.elements)))


    def __rmul__(self, scalar: int | float) -> Self:
        '''
        Multiplies a vector by a scalar (from the left).
        Raise TypeError if the scalar is not a number.
        '''
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        #
        return Vec((round(x * scalar, 5) for x in self.elements))

    def __imul__(self, scalar: int | float) -> Self:
        """
        In-place multiplication of the vector by a scalar.
        Raises TypeError if the scalar is not a number.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        self.elements = tuple(round(val* scalar,5) for val in self.elements)
        # self.elements =new_element
        return self

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        '''
        Subtracts two vectors of the same dimension.
        Raise TypeError if dimentions are not the same or if the other operand is not a
        Vec.
        '''
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")
        return Vec((round(x - y , 5) for x, y in zip(self.elements, t.elements)))

    def __neg__(self) -> Self:
        '''
        Negates the vector, returning a new vector with all elements negated.
        '''
        return  Vec((-x) for x in self.elements)
        

    def __radd__(self, other: int | float) -> Self:
        '''
        Adds a scalar to each element of the vector.
        Raises TypeError if the other operand is not a number.
        returns NotImplemented if the other operand is not a number.
        '''
        if isinstance(other, (int, float)):
            return Vec(other + value for value in self.elements)
        return NotImplemented

    def __iadd__(self, other):
        '''
        In-place addition of another vector to this vector.
        Raises TypeError if the other operand is not a Vec or if the dimensions do not match.'''
        if not isinstance(other, Vec):
                raise TypeError(f"Expected Vec: {type(other)}")
        if len(self.elements) != len(other):
                raise TypeError(f"Type error - vectors must be of same dimensions")
        self.elements = tuple((round(x + y, 5) for x, y in zip(self.elements, other.elements)))
        # self.elements = new_element
        return self

    # return a vector of @n zeroes. precondition: @n > 0
    @staticmethod
    def zeros(n: int) -> Self:
        """
        Returns a vector of n zeroes.
        Precondition: n > 0
        """
        if(n<0):
            raise RuntimeError("n is less than 0")
        v = ((0,)*n)
        return Vec(v)

    # return a vector of @n. precondition: @n > 0
    @staticmethod
    def ones(n: int) -> Self:
        '''
        Returns a vector of n ones.
        Precondition: n > 0
        '''
        if(n<0):
            raise RuntimeError("n is less than 0")
        v = ((1,)*n)
        return Vec(v)

    # return a vector of @n uniformly distributed numbers in [0, 1]. precondition: @n > 0
    @staticmethod
    def uniform(n: int) -> Self:
        '''
        Returns a vector of n uniformly distributed random numbers in the range [0, 1].
        Precondition: n > 0
        '''
        if(n<0):
            raise RuntimeError("n is less than 0")
        random_numbers = (random.random() for _ in range(3))
        return random_numbers
        

        

    # Calculates the Euclidean norm (L2 norm) of the vector.
    # sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)
    def norm(self) -> float:
        raise RuntimeError("norm unimpleented")
    

"""
(1) Understand the basic design of the vector abstraction. Review the implementation.
(2) Document each function.
(3) Implement all unimplemented methods.
(4) Create appropriate tests for this implementation, increasing the confidence about its correctness.
(5) Test this implementation by importing the class in a sepatate python script.
(6) Measure the performance of each of these functions on vectors of varying lengths.
    Try 2k to 64k dimension vectors and time the results.
    How would you do the measurements?
(7) Measure the performance on your machine. Check it on colab.
(8) use numpy and compare the performance.
"""


if sys.version_info < (3, 8):
     sys.exit("Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":
    #z1 = Vec.zeros(10)
    v1 = Vec((0, 1, 1.03))
    v2 = Vec((1, 2, 3))
    print(v1)
    v3 = 2.2 * v1
    v3 *= 5
    v3 = 1 + v3
    v1 += v3
    print(v1)
    print(v3)
    v2 = v1 + v3
    print(v1 + v3)
    v1 *= 5
    print(v1)
    v4 =-v1
    print(v4)
    o1 = Vec.zeros(3)
    print(o1)
    print(v1+v2)
    #print(-(v1 + v3))