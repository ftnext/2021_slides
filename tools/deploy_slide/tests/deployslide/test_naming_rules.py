from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from deployslide import naming_rules as sut


class HtmlNamingRuleTestCase(TestCase):
    def test_inheritance(self):
        actual = sut.HtmlNamingRule("hoge")

        self.assertIsInstance(actual, sut.BaseNamingRule)

    def test_source(self):
        slide_directory_name = "test_html_rule_src"

        rule = sut.HtmlNamingRule(slide_directory_name)
        actual = rule.source

        expected = Path("build/revealjs") / "test_html_rule_src"
        self.assertEqual(actual, expected)

    def test_destination(self):
        slide_directory_name = "test_html_rule_dest"

        rule = sut.HtmlNamingRule(slide_directory_name)
        actual = rule.destination

        expected = Path("docs") / "test_html_rule_dest"
        self.assertEqual(actual, expected)


class ImagesNamingRuleTestCase(TestCase):
    def test_inheritance(self):
        actual = sut.ImagesNamingRule()

        self.assertIsInstance(actual, sut.BaseNamingRule)

    def test_source(self):
        rule = sut.ImagesNamingRule()
        actual = rule.source

        expected = Path("build/revealjs") / "_images"
        self.assertEqual(actual, expected)

    def test_destination(self):
        rule = sut.ImagesNamingRule()
        actual = rule.destination

        expected = Path("docs") / "_images"
        self.assertEqual(actual, expected)


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
