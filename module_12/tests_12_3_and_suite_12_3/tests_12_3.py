import unittest
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        """Test for walk function in runner"""
        runner1 = Runner("Artur")
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        """Test for run function in runner"""
        runner2 = Runner("Maria")
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        """Inequality test"""
        runner1, runner2 = Runner("Sergey"), Runner("Anastasia")
        for _ in range(10):
            runner1.walk(), runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls): # срабатывает 1 раз, перед каждым началом класса
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self): # срабатывает 1 раз, перед каждым началом фикстуры
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls): # срабатывает 1 раз, после каждого завершения класса
        for result in cls.all_results.values():
            print({place: str(runner) for place, runner in result.items()})

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_first_tournament(self): # фикстура № 1
        t1 = Tournament(90, self.runner1, self.runner3)
        result = t1.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_second_tournament(self): # фикстура № 2
        t2 = Tournament(90, self.runner2, self.runner3)
        result = t2.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third_tournament(self): # фикстура № 3
        t3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = t3.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_fourth_tournament(self): # фикстура № 4
        t4 = Tournament(2, self.runner2, self.runner1, self.runner3)
        result = t4.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

if __name__ == "__main__":
    unittest.main()