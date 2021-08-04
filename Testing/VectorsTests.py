from Math.Vector import Vector
from Math.VectorFunctions import *

vector1 = Vector([1, 3])
vector2 = Vector([2, 5])
vector3 = Vector([7, 7])
vector4 = Vector([1, 1])
vector5 = Vector([
    Vector([
        Vector([1, 2, 3]),
        Vector([4, 3, 1])
    ]),
    Vector([
        Vector([4, 2, 1]),
        Vector([51, 1, 5])
    ])
])

print(add_vectors(vector1, vector2).values)
print(subtract_vectors(vector1, vector2).values)
print(sum_vectors(vector1, vector2, vector3).values)
print(multiply_vector_on_scalar(3, vector1).values)
print(get_scalar_product(vector1, vector2))     # 1*2 + 3*5 = 17
print(get_sum_of_squares(vector1))
print(get_magnitude(vector4))
print(get_squared_distance(vector1, vector2))
print(get_distance(vector1, vector2))
print(vector5.get_shape())  # [2, 2, 3]


