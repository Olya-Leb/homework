import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # срабатывает 1 раз, перед каждым началом класса
        cls.all_results = {}

    def setUp(self): # срабатывает 1 раз, перед каждым началом фикстуры
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls): # срабатывает 1 раз, после каждого завершения класса
        for result in cls.all_results.values():
            print({place: str(runner) for place, runner in result.items()})

    def test_start1(self): # фикстура № 1
        t1 = Tournament(90, self.runner1, self.runner3)
        result = t1.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    def test_start2(self): # фикстура № 2
        t2 = Tournament(90, self.runner2, self.runner3)
        result = t2.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    def test_start3(self): # фикстура № 3
        t3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = t3.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    def test_start4(self): # фикстура № 4
        t4 = Tournament(2, self.runner2, self.runner1, self.runner3)
        result = t4.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

if __name__ == "__main__":
    unittest.main()