from unittest import TestCase
from unittest.mock import MagicMock, patch

from deployslide import core as sut
from deployslide.naming_rules import (
    EntireRules,
    HtmlNamingRule,
    ImagesNamingRule,
)


class SlideDeployerTestCase(TestCase):
    def test_create_from_entire_rules(self):
        entire_rules = MagicMock(spec=EntireRules(None, None))

        actual = sut.SlideDeployer.create_from_entire_rules(entire_rules)

        expected = sut.SlideDeployer(
            entire_rules.for_html, entire_rules.for_images
        )
        self.assertEqual(actual, expected)

    @patch("deployslide.core.SlideDeployer._copy_images")
    @patch("deployslide.core.SlideDeployer._deploy_slide")
    @patch("deployslide.core.SlideDeployer._create_directories")
    def test_deploy(self, _create_directories, _deploy_slide, _copy_images):
        # Passing None causes TypeError in destination property.
        # It seems that all properties are evaluated.
        # ref: https://bugs.python.org/issue41768
        html_rule = MagicMock(spec=HtmlNamingRule(""))
        images_rule = MagicMock(spec=ImagesNamingRule())

        deployer = sut.SlideDeployer(html_rule, images_rule)
        deployer.deploy()

        _create_directories.assert_called_once_with()
        _deploy_slide.assert_called_once_with()
        _copy_images.assert_called_once_with()

    def test__create_directories(self):
        html_rule = MagicMock(spec=HtmlNamingRule(""))
        images_rule = MagicMock(spec=ImagesNamingRule())

        deployer = sut.SlideDeployer(html_rule, images_rule)
        deployer._create_directories()

        html_rule.source.mkdir.assert_called_once_with(
            parents=True, exist_ok=True
        )
        html_rule.destination.mkdir.assert_called_once_with(
            parents=True, exist_ok=True
        )
        images_rule.source.mkdir.assert_called_once_with(
            parents=True, exist_ok=True
        )
        images_rule.destination.mkdir.assert_called_once_with(
            parents=True, exist_ok=True
        )
