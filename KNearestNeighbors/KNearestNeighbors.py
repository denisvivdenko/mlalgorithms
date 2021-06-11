from Math.Vector import Vector
from Math import VectorFunctions


class KNearestNeighbors:

    def __init__(self, k):
        if k < 1:
            raise Exception()

        self.k_neighbors_number = k
        self.fitted_X = Vector([])
        self.fitted_y = Vector([])

    def fit(self, X, y):
        if len(X) != len(y):
            raise Exception('fitted data is not the same length')

        self.fitted_X = Vector([Vector(features) for features in X])    # TODO only two features are available
        self.fitted_y = Vector(y)

    def predict_list(self, X):
        results = list()
        for input in X:
            results.append(self.predict(input))

        return results

    def predict(self, X):
        self.is_fitted()
        input_vector = Vector(X)
        input_vector.check_dimensions_compatibility(self.fitted_X.values[0])

        distances = list()
        for fitted_vector in self.fitted_X.values:
            distance = VectorFunctions.get_distance(input_vector, fitted_vector)
            distances.append([distance, fitted_vector.values])

        distances.sort(key=lambda x: float(x[0]))
        return self.get_majority_vote(distances[:self.k_neighbors_number])

    def get_majority_vote(self, distances):
        nearest_points = list()
        for distance in distances:
            nearest_points.append(distance[1])

        indices = list()
        index = 0
        for fitted_data in self.fitted_X.values:
            if len(indices) == len(nearest_points):
                break

            if fitted_data.values in nearest_points:
                indices.append(index)

            index += 1

        answers = [self.fitted_y.values[index] for index in indices]
        return max(answers)

    def is_fitted(self):
        if self.fitted_X.is_vector_empty() | self.fitted_y.is_vector_empty():
            raise Exception('knn is not fitted yet')

        return True
