import unittest
import tests_12_3

run_and_tourST = unittest.TestSuite()
run_and_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
run_and_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_and_tourST)