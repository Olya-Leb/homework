import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Test for walk function in runner"""
        runner = Runner("Artur")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """Test for run function in runner"""
        runner = Runner("Maria")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        """Inequality test"""
        runner1, runner2 = Runner("Sergey"), Runner("Anastasia")
        for _ in range(10):
            runner1.walk(), runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()
