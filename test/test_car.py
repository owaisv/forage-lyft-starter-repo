import unittest
from datetime import datetime
import sys
sys.path.append('/Users/owais/OneDrive/Documents/forage-lyft-starter-repo')
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(current_mileage, last_service_mileage, last_service_date)
        self.assertTrue(car.needsService())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope( current_mileage, last_service_mileage, last_service_date)
        self.assertFalse(car.needsService())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope( current_mileage, last_service_mileage, last_service_date)
        self.assertTrue(car.needsService())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Calliope( current_mileage, last_service_mileage, last_service_date)
        self.assertFalse(car.needsService())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(current_mileage, last_service_mileage, last_service_date)
        self.assertTrue(car.needsService())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(current_mileage, last_service_mileage, last_service_date)
        self.assertFalse(car.needsService())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Glissade(current_mileage, last_service_mileage, last_service_date)
        self.assertTrue(car.needsService())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Glissade(current_mileage, last_service_mileage, last_service_date)
        self.assertFalse(car.needsService())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = Palindrome(warning_light_is_on, last_service_date)
        self.assertTrue(car.needsService())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False

        car = Palindrome(warning_light_is_on, last_service_date)
        self.assertFalse(car.needsService())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = Palindrome(warning_light_is_on, last_service_date)
        self.assertTrue(car.needsService())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = Palindrome(warning_light_is_on, last_service_date)
        self.assertFalse(car.needsService())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(current_mileage, last_service_mileage, last_service_date)
        self.assertTrue(car.needsService())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(current_mileage, last_service_mileage, last_service_date)
        self.assertFalse(car.needsService())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Rorschach(current_mileage, last_service_mileage, last_service_date)
        self.assertTrue(car.needsService())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Rorschach(current_mileage, last_service_mileage, last_service_date)
        self.assertFalse(car.needsService())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(current_mileage, last_service_mileage, last_service_date)
        self.assertTrue(car.needsService())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(current_mileage, last_service_mileage, last_service_date)
        self.assertFalse(car.needsService())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Thovex(current_mileage, last_service_mileage, last_service_date)
        self.assertTrue(car.needsService())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Thovex(current_mileage, last_service_mileage, last_service_date)
        self.assertFalse(car.needsService())


if __name__ == '__main__':
    unittest.main()
