from typing import Callable
from tqdm import tqdm
from typing import List
from Math.Vector import Vector
import Math.VectorFunctions
import random


class GradientDescent:


    def __init__(self, get_function_gradient: Callable[[List[float]], List[float]], 
                function_input_size: int, learning_rate=.001, max_epohs=1000, tolerance_level=0.001) -> None:
        '''
        param get_function_gradient: callable that returns derivative
        param function_input_size: how much variables takes function
        param learning_rate: learning rate
        param max_epohs: amount of repeats
        param tolerance_level: step distance after which we assume that we found the minimum
        '''

        self._learning_rate = learning_rate
        self._max_epohs = max_epohs
        self._tolerance_level = tolerance_level

        starting_point = self.__generate_starting_point(function_input_size)
        try:
            self._found_minimum = self.__find_minimum(get_function_gradient, starting_point)
        except Exception:
            print('unable to find minimum of the function')
            self._found_minimum = []

    def get_content(self) -> List[float]:
        return self._found_minimum;

    def __find_minimum(self, get_function_gradient: Callable[[List[float]], List[float]], 
                        starting_point: List[float]) -> List[float]:
        epohs = 0

        current_point = starting_point
        for epoh in tqdm(range(self._max_epohs)):

            function_gradient = get_function_gradient(current_point)
            next_point = self.__make_step(current_state=current_point, function_gradient=function_gradient)
            step_distance = Math.VectorFunctions.get_distance(Vector(next_point), Vector(current_point))
            
            if step_distance < self._tolerance_level:
                return next_point
            
            current_point = next_point

        raise Exception('epohs > max_epohs. forced stop')

    def __make_step(self, current_state: List[float], function_gradient: List[float]) -> List[float]:
        return [current_argument_state - direction * self._learning_rate
                for current_argument_state, direction in zip(current_state, function_gradient)]

    def __generate_starting_point(self, function_input_size) -> List[float]:
        starting_point = [random.randint(-100, 100) for repeat in range(function_input_size)]
        return starting_point


