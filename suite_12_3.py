import unittest
import tests_12_3

ranner_TornamentTest = unittest.TestSuite()
ranner_TornamentTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
ranner_TornamentTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

go_tests = unittest.TextTestRunner(verbosity=2)
go_tests.run(ranner_TornamentTest)