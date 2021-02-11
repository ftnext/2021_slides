import sys
from unittest import TestCase
from unittest.mock import patch

from deployslide import main


class MainTestCase(TestCase):
    @patch("deployslide.core.SlideDeployer.create_from_entire_rules")
    @patch("deployslide.naming_rules.EntireRules.build")
    def test_main(
        self, entire_rules_build, slide_deployer_create_from_entire_rules
    ):
        rules = entire_rules_build.return_value
        slide_deployer = slide_deployer_create_from_entire_rules.return_value

        sys.argv = ["deployslide", "test_main_slide"]

        main()

        entire_rules_build.assert_called_once_with("test_main_slide")
        slide_deployer_create_from_entire_rules.assert_called_once_with(rules)
        slide_deployer.deploy.assert_called_once_with()
