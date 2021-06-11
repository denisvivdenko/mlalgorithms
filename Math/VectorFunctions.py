import math
from Math.Vector import Vector


def add_vectors(vector1: Vector, vector2: Vector):
    vector1.check_dimensions_compatibility(vector2)

    new_values = []
    
    for dimension in range(vector1.dimensions_number):
        new_value = vector1.values[dimension] + vector2.values[dimension]
        new_values.append(new_value)

    return Vector(new_values)


def subtract_vectors(vector1: Vector, vector2: Vector):
    vector1.check_dimensions_compatibility(vector2)

    new_values = []

    for dimension in range(vector1.dimensions_number):
        new_value = vector1.values[dimension] - vector2.values[dimension]
        new_values.append(new_value)

    return Vector(new_values)


def sum_vectors(*vectors):
    vectors_number = len(vectors)

    if vectors_number < 2:
        raise Exception('number of vectors is less than 2')

    resulting_vector = vectors[0]
    for vector_index in range(1, vectors_number):
        resulting_vector = add_vectors(resulting_vector, vectors[vector_index])

    return resulting_vector


def multiply_vector_on_scalar(scalar, vector: Vector):
    new_values = []

    for dimension in range(vector.dimensions_number):
        new_values.append(vector.values[dimension] * scalar)

    return Vector(new_values)


def get_scalar_product(vector1: Vector, vector2: Vector):
    vector1.check_dimensions_compatibility(vector2)

    result = 0
    for dimension in range(vector1.dimensions_number):
        result += vector1.values[dimension] * vector2.values[dimension]

    return result


def get_sum_of_squares(vector: Vector):
    new_values = []

    for dimension in range(vector.dimensions_number):
        new_values.append(vector.values[dimension] ** 2)

    return sum(new_values)


def get_magnitude(vector: Vector):
    magnitude = math.sqrt(get_sum_of_squares(vector))
    return magnitude


def get_squared_distance(vector1: Vector, vector2: Vector):
    return get_sum_of_squares(subtract_vectors(vector1, vector2))


def get_distance(vector1: Vector, vector2: Vector):
    return get_magnitude(subtract_vectors(vector1, vector2))


