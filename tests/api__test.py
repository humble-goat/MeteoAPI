import unittest


class TestUrl(unittest.TestCase):

    def test_date(self):
        import datetime
        import requests
        from random import randrange
        date = datetime.date(randrange(2000, 2021, 1), randrange(1, 12, 1), randrange(1, 26, 1))

        req = requests.get(f'https://darksky.net/details/40.3327,21.7927/{date}')
        self.assertEqual(req.status_code, 200)

    def test_location(self):
        from random import uniform
        import requests

        req = requests.get(f'https://darksky.net/forecast/{uniform(-85.0, 85.0)},{uniform(-85.0, 85.0)}')
        self.assertEqual(req.status_code, 200)


if __name__ == '__main__':
    unittest.main()
