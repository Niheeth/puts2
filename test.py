from main import substraction
from main import addition
from main import division
import main
import unittest


class TestOnlineCalculator(unittest.TestCase):
    """Testing features of substraction in online calculator"""
    """Testing features of addition in online calculator"""
    
    """Testing features of division in online calculator"""

    def setUp(self):
        """Sets up the app for testing"""
        main.app.testing = True
        self.app = main.app.test_client()

    def test_substraction(self):
        """Tests page with /sub route, testing substraction feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/sub?A=34&B=30')
        self.assertEqual(b'4 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/sub?A=2/3&B=3/7')
        self.assertEqual(b'0.24 \n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/sub?A=5.4&B=3.4')
        self.assertEqual(b'2 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/sub?A=8&B=1.234')
        self.assertEqual(b'6.77 \n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/sub?A=-5.35&B=2')
        self.assertEqual(b'-7.35 \n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/sub?A=4/5&B=3')
        self.assertEqual(b'-2.20 \n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/sub?A=7&B=5/6')
        self.assertEqual(b'6.17 \n', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to integer
        response_data = self.app.get('/sub?A=-1/0&B=7/9')
        self.assertEqual(b"A's denominator should not be zero! \n", response_data.data)

        # when B = x/0 where x belongs to integer
        response_data = self.app.get('/sub?A=-4&B=1000/0')
        self.assertEqual(b"B's denominator should not be zero! \n", response_data.data)

        # when A is a non-number
        response_data = self.app.get('/sub?A=x&B=niheeth')
    def test_addition(self):
        """Tests page with /add route, testing addition feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/add?A=100&B=3')
        self.assertEqual(b'103 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/add?A=2/3&B=3/7')
        self.assertEqual(b'1.10 \n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/add?A=5.4&B=3.4')
        self.assertEqual(b'8.80 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/add?A=8&B=-1.234')
        self.assertEqual(b'6.77 \n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/add?A=-5.352&B=2')
        self.assertEqual(b'-3.35 \n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/add?A=4/5&B=3')
        self.assertEqual(b'3.80 \n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/add?A=7&B=5/6')
        self.assertEqual(b'7.83 \n', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to integer
        response_data = self.app.get('/add?A=-1/0&B=7/9')
        self.assertEqual(b"A's denominator should not be zero! \n", response_data.data)

        # when B = x/0 where x belongs to integer
        response_data = self.app.get('/add?A=-4&B=1000/0')
        self.assertEqual(b"B's denominator should not be zero! \n", response_data.data)

        # when A is a non-number
        response_data = self.app.get('/add?A=x&B=niheeth')
        self.assertEqual(b"A's value should be a number (includes fraction, float, integer). \n", response_data.data)
    def test_multiplication(self):
        """Tests page with /mul route, testing multiplication feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/mul?A=3&B=4')
        self.assertEqual(b'12 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/mul?A=2/3&B=3/7')
        self.assertEqual(b'0.29 \n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/mul?A=5.4&B=3.4')
        self.assertEqual(b'18.36 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/mul?A=8&B=1.234')
        self.assertEqual(b'9.87 \n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/mul?A=-5.35&B=2')
        self.assertEqual(b'-10.70 \n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/mul?A=4/5&B=3')
        self.assertEqual(b'2.40 \n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/mul?A=7&B=5/6')
        self.assertEqual(b'5.83 \n', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to integer
        response_data = self.app.get('/mul?A=-1/0&B=7/9')
        self.assertEqual(b"A's denominator should not be zero! \n", response_data.data)

        # when B = x/0 where x belongs to integer
        response_data = self.app.get('/mul?A=-4&B=1000/0')
        self.assertEqual(b"B's denominator should not be zero! \n", response_data.data)

        # when A is a non-number
        response_data = self.app.get('/mul?A=x&B=niheeth')
        self.assertEqual(b"A's value should be a number (includes fraction, float, integer). \n", response_data.data)

    def test_division(self):
        """Tests page with /div route, testing division feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/div?A=3&B=4')
        self.assertEqual(b'0.75 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/div?A=2/3&B=3/7')
        self.assertEqual(b'1.56 \n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/div?A=5.4&B=3.4')
        self.assertEqual(b'1.59 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/div?A=8&B=1.234')
        self.assertEqual(b'6.48 \n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/div?A=-5.35&B=2')
        self.assertEqual(b'-2.67 \n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/div?A=4/5&B=3')
        self.assertEqual(b'0.27 \n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/div?A=7&B=5/6')
        self.assertEqual(b'8.40 \n', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to integer
        response_data = self.app.get('/div?A=-1/0&B=7/9')
        self.assertEqual(b"A's denominator should not be zero! \n", response_data.data)

        # when B = x/0 where x belongs to integer
        response_data = self.app.get('/div?A=-4&B=1000/0')
        self.assertEqual(b"B's denominator should not be zero! \n", response_data.data)

        # when A is a non-number
        response_data = self.app.get('/div?A=x&B=niheeth')
        self.assertEqual(b"A's value should be a number (includes fraction, float, integer). \n", response_data.data)

if __name__ == '__main__':
    unittest.main()