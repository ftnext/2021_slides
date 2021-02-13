import re
import shutil
from dataclasses import dataclass

from deployslide import naming_rules


@dataclass
class SlideDeployer:
    html_rule: naming_rules.HtmlNamingRule
    images_rule: naming_rules.ImagesNamingRule
    css_rule: naming_rules.CssNamingRule

    @classmethod
    def create_from_entire_rules(
        cls, entire_rules: "naming_rules.EntireRules"
    ):
        """Factory from `naming_rules.EntireRules` instance."""
        return cls(
            entire_rules.for_html,
            entire_rules.for_images,
            entire_rules.for_css,
        )

    @property
    def rules(self):
        return (self.html_rule, self.images_rule, self.css_rule)

    def deploy(self):
        self._create_directories()
        self._deploy_slide()
        self._copy_images()

    def _create_directories(self):
        mkdir_kwargs = dict(parents=True, exist_ok=True)
        for rule in self.rules:
            rule.source.mkdir(**mkdir_kwargs)
            rule.destination.mkdir(**mkdir_kwargs)

    def _deploy_slide(self):
        # TODO: HTMLの中身について知りすぎているので、converterを渡せるように変更する
        slide_paths = list(self.html_rule.source.glob("*.html"))
        assert len(slide_paths) == 1, "multiple html slides!"
        slide_path = slide_paths[0]

        with slide_path.open(encoding="utf-8") as fin:
            converted_lines = [
                re.sub("_static/revealjs4", "reveal.js", line) for line in fin
            ]

        destination_path = self.html_rule.destination / slide_path.name
        destination_path.write_text("".join(converted_lines), encoding="utf-8")

    def _copy_images(self):
        for image_path in self.images_rule.source.glob("*.png"):
            destination_path = self.images_rule.destination / image_path.name
            shutil.copyfile(image_path, destination_path)

    def _copy_css(self):
        raise NotImplementedError
