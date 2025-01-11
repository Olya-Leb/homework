import logging
import unittest
from rt_with_exceptions import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        """Test for walk function in runner"""
        try:
            runner = Runner("Artur", -1)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно', exc_info=True)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        """Test for run function in runner"""
        try:
            runner = Runner(["Maria"])
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно', exc_info=True)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        """Inequality test"""
        runner1, runner2 = Runner("Sergey"), Runner("Anastasia")
        for _ in range(10):
            runner1.walk(), runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(name)s | (%(filename)s).%(funcName)s(%(lineno)d) | %(message)s")
