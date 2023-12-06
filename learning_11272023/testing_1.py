"""Testing in python lessons, Menoko OG, 11-2023"""
# test files never go into production, they are used during development, the end user will never see these type of
# files.
import unittest
import main1


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main1.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "skjhkf"
        result = main1.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def setUp(self):
        print("about to test a function")

    def test_do_stuff3(self):
        """Hi!!!!!!"""
        test_param = None
        result = main1.do_stuff(test_param)
        self.assertEqual(result, "_Please enter number_")

    def test_do_stuff4(self):
        test_param = ""
        result = main1.do_stuff(test_param)
        self.assertEqual(result, "_Please enter number_")

    def tearDown(self):
        print("Cleaning up")


if __name__ == "__main__":
    unittest.main()
