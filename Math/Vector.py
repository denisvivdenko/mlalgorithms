class Vector:

    def __init__(self, values):
        self.values = values
        self.dimensions_number = len(values)

    def check_dimensions_compatibility(self, vector):
        if self.dimensions_number != vector.dimensions_number:
            raise Exception('vectors dimensions are different')

    def is_vector_empty(self):
        if self.dimensions_number < 1:
            return True

        return False

    def get_shape_recursive(self, values, shape):
        shape.append(len(values))

        if type(values[0]) == Vector:
            self.get_shape_recursive(values[0].values, shape)

        return shape

    def get_shape(self):
        return self.get_shape_recursive(self.values, list())