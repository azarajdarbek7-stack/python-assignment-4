import unittest
from analytics.analyser import CountryAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.sample = [{"country": "USA"}, {"country": "USA"}, {"country": "India"}]

    def test_total_students(self):
        analyser = CountryAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 3)

if __name__ == "__main__":
    unittest.main()