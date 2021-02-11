from unittest import TestCase
from unittest.mock import MagicMock

from deployslide import core as sut
from deployslide.naming_rules import EntireRules


class SlideDeployerTestCase(TestCase):
    def test_create_from_entire_rules(self):
        entire_rules = MagicMock(spec=EntireRules(None, None))

        actual = sut.SlideDeployer.create_from_entire_rules(entire_rules)

        expected = sut.SlideDeployer(
            entire_rules.for_html, entire_rules.for_images
        )
        self.assertEqual(actual, expected)
