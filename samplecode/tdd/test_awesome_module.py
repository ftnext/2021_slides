from unittest import TestCase
from unittest.mock import patch


class MainTestCase(TestCase):
    @patch("awesome_module.a")
    def test_main(self, a):
        from awesome_module import main

        actual = main()

        self.assertEqual(actual, a.return_value)
        a.assert_called_once_with(42, "spam")
