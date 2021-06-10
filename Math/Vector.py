class Vector:

    def __init__(self, values):
        self.values = values
        self.dimensions_number = len(values)

    def check_dimensions_compatibility(self, vector):
        if self.dimensions_number != vector.dimensions_number:
            raise Exception('vectors dimensions are different')