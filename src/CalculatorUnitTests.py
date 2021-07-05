import unittest
from Calculator import Calculator
from CSVReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instance(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']), 0)

    def test_subtraction(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), float(row['Result']), 0)

    def test_multiplication(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), float(row['Result']), 0)


if __name__ == '__main__':
    unittest.main()
