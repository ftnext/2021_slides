from pathlib import Path
from types import GeneratorType
from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock, patch

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


class CssNamingRuleTestCase(TestCase):
    def setUp(self):
        self.rule = sut.CssNamingRule()

    def test_inheritance(self):
        actual = self.rule

        self.assertIsInstance(actual, sut.BaseNamingRule)

    def test_source(self):
        actual = self.rule.source

        expected = Path("build/revealjs") / "_static" / "css"
        self.assertEqual(actual, expected)

    def test_destination(self):
        actual = self.rule.destination

        expected = Path("docs") / "_static" / "css"
        self.assertEqual(actual, expected)

    @patch(
        "deployslide.naming_rules.CssNamingRule.source",
        new_callable=PropertyMock,
    )
    def test_iter_target(self, source_property):
        path = MagicMock(spec=Path(""))
        source_property.return_value = path
        path.glob.return_value = iter(
            (
                Path("build/revealjs/_static/css/iter1.css"),
                Path("build/revealjs/_static/css/iter2.css"),
            )
        )

        generator = self.rule.iter_target()
        actual = list(generator)

        self.assertIsInstance(generator, GeneratorType)
        expected = [
            Path("build/revealjs/_static/css/iter1.css"),
            Path("build/revealjs/_static/css/iter2.css"),
        ]
        self.assertEqual(actual, expected)
        path.glob.assert_called_once_with("*.css")


class EntireRulesTestCase(TestCase):
    @patch("deployslide.naming_rules.CssNamingRule")
    @patch("deployslide.naming_rules.ImagesNamingRule")
    @patch("deployslide.naming_rules.HtmlNamingRule")
    def test_build(
        self, html_naming_rule, images_naming_rule, css_naming_rule
    ):
        slide_directory_name = "test_entire_rules"

        actual = sut.EntireRules.build(slide_directory_name)

        self.assertIsInstance(actual, sut.EntireRules)
        self.assertEqual(actual.for_html, html_naming_rule.return_value)
        self.assertEqual(actual.for_images, images_naming_rule.return_value)
        self.assertEqual(actual.for_css, css_naming_rule.return_value)
        html_naming_rule.assert_called_once_with("test_entire_rules")
        images_naming_rule.assert_called_once_with()
        css_naming_rule.assert_called_once_with()
