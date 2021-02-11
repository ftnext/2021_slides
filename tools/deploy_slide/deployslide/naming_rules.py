from dataclasses import dataclass
from pathlib import Path


@dataclass
class HtmlNamingRule:
    slide_directory_name: str

    @property
    def source(self):
        return Path("build/revealjs") / self.slide_directory_name


class ImagesNamingRule:
    pass


@dataclass
class EntireRules:
    for_html: HtmlNamingRule
    for_images: ImagesNamingRule

    @classmethod
    def build(cls, slide_directory_name):
        html_rule = HtmlNamingRule(slide_directory_name)
        images_rule = ImagesNamingRule()
        return cls(html_rule, images_rule)
