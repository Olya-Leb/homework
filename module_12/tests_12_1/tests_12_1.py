from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Test for walk function in runner"""
        runner1 = Runner("Artur")
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        """Test for run function in runner"""
        runner2 = Runner("Maria")
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        """Inequality test"""
        runner1, runner2 = Runner("Sergey"), Runner("Anastasia")
        for _ in range(10):
            runner1.walk(), runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()
