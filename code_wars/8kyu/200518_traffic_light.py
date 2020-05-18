import unittest
import enum


class TrafficLight(enum.Enum):
    GREEN_LIGHT = 'green'
    YELLOW_LIGHT = 'yellow'
    RED_LIGHT = 'red'


def update_light(current):
    return {
        TrafficLight.GREEN_LIGHT.value: TrafficLight.YELLOW_LIGHT.value,
        TrafficLight.YELLOW_LIGHT.value: TrafficLight.RED_LIGHT.value,
        TrafficLight.RED_LIGHT.value: TrafficLight.GREEN_LIGHT.value
    }[current]

    
class TestUpdateLight(unittest.TestCase):
    def test_should_return_yellow_when_given_current_is_green(self):
        self.assertEqual(update_light(TrafficLight.GREEN_LIGHT.value), TrafficLight.YELLOW_LIGHT.value)

    def test_should_return_red_when_given_current_is_yellow(self):
        self.assertEqual(update_light(TrafficLight.YELLOW_LIGHT.value), TrafficLight.RED_LIGHT.value)

    def test_should_return_green_when_given_current_is_red(self):
        self.assertEqual(update_light(TrafficLight.RED_LIGHT.value), TrafficLight.GREEN_LIGHT.value)
