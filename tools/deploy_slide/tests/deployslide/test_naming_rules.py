from unittest import TestCase
from unittest.mock import patch

from deployslide import naming_rules as sut


class EntireRulesTestCase(TestCase):
    @patch("deployslide.naming_rules.ImagesNamingRule")
    @patch("deployslide.naming_rules.HtmlNamingRule")
    def test_build(self, html_naming_rule, images_naming_rule):
        slide_directory_name = "test_entire_rules"

        actual = sut.EntireRules.build(slide_directory_name)

        self.assertIsInstance(actual, sut.EntireRules)
        self.assertEqual(actual.for_html, html_naming_rule.return_value)
        self.assertEqual(actual.for_images, images_naming_rule.return_value)
        html_naming_rule.assert_called_once_with("test_entire_rules")
        images_naming_rule.assert_called_once_with()
