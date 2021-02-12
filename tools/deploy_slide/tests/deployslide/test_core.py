import tempfile
from pathlib import Path
from unittest import TestCase
from unittest.mock import MagicMock, call, patch

from deployslide import core as sut
from deployslide.naming_rules import (
    EntireRules,
    HtmlNamingRule,
    ImagesNamingRule,
)


class SlideDeployerTestCase(TestCase):
    def setUp(self):
        # Passing None causes TypeError in destination property.
        # It seems that all properties are evaluated.
        # ref: https://bugs.python.org/issue41768
        self.html_rule = MagicMock(spec=HtmlNamingRule(""))
        self.images_rule = MagicMock(spec=ImagesNamingRule())

        self.deployer = sut.SlideDeployer(self.html_rule, self.images_rule)

    def test_create_from_entire_rules(self):
        entire_rules = MagicMock(spec=EntireRules(None, None, None))

        actual = sut.SlideDeployer.create_from_entire_rules(entire_rules)

        expected = sut.SlideDeployer(
            entire_rules.for_html, entire_rules.for_images
        )
        self.assertEqual(actual, expected)

    @patch("deployslide.core.SlideDeployer._copy_images")
    @patch("deployslide.core.SlideDeployer._deploy_slide")
    @patch("deployslide.core.SlideDeployer._create_directories")
    def test_deploy(self, _create_directories, _deploy_slide, _copy_images):
        self.deployer.deploy()

        _create_directories.assert_called_once_with()
        _deploy_slide.assert_called_once_with()
        _copy_images.assert_called_once_with()

    def test__create_directories(self):
        self.deployer._create_directories()

        self.html_rule.source.mkdir.assert_called_once_with(
            parents=True, exist_ok=True
        )
        self.html_rule.destination.mkdir.assert_called_once_with(
            parents=True, exist_ok=True
        )
        self.images_rule.source.mkdir.assert_called_once_with(
            parents=True, exist_ok=True
        )
        self.images_rule.destination.mkdir.assert_called_once_with(
            parents=True, exist_ok=True
        )

    def test__deploy_slide(self):
        fixture_directory_path = Path(__file__).parent / "fixtures"
        self.html_rule.source.glob.return_value = iter(
            (fixture_directory_path / "deploy_slide" / "source.html",)
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            self.html_rule.destination = Path(temp_dir)

            self.deployer._deploy_slide()

            expected_html_path = (
                fixture_directory_path / "deploy_slide" / "expected.html"
            )
            expected = expected_html_path.read_text(encoding="utf-8")
            with open(f"{temp_dir}/source.html", encoding="utf-8") as f:
                actual = f.read()
            self.assertEqual(actual, expected)

        self.html_rule.source.glob.assert_called_once_with("*.html")

    @patch("deployslide.core.shutil")
    def test__copy_images(self, shutil):
        image1_path = Path("build/revealjs/_images/image01.png")
        image2_path = Path("build/revealjs/_images/image02.png")
        self.images_rule.source.glob.return_value = iter(
            (image1_path, image2_path)
        )
        images_destination_path = Path("docs/_images")
        self.images_rule.destination = images_destination_path

        self.deployer._copy_images()

        self.images_rule.source.glob.assert_called_once_with("*.png")
        shutil.copyfile.assert_has_calls(
            [
                call(image1_path, images_destination_path / "image01.png"),
                call(image2_path, images_destination_path / "image02.png"),
            ]
        )
