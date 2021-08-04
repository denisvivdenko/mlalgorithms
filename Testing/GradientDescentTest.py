from GradientDescent.GradientDescent import GradientDescent


def get_x_square_derivative(values):
    return [2 * value for value in values]

gradient_descent = GradientDescent(get_function_gradient=get_x_square_derivative, function_input_size=1,
                                    learning_rate=0.01, tolerance_level=0.0001, max_epohs=1000)
print(gradient_descent.get_content())