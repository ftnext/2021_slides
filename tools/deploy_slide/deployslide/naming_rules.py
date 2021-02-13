from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path


class BaseNamingRule(ABC):
    @property
    @abstractmethod
    def source(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def destination(self):
        raise NotImplementedError


@dataclass
class HtmlNamingRule(BaseNamingRule):
    slide_directory_name: str

    @property
    def source(self):
        return Path("build/revealjs") / self.slide_directory_name

    @property
    def destination(self):
        return Path("docs") / self.slide_directory_name


class ImagesNamingRule(BaseNamingRule):
    @property
    def source(self):
        return Path("build/revealjs") / "_images"

    @property
    def destination(self):
        return Path("docs") / "_images"


class CssNamingRule(BaseNamingRule):
    @property
    def source(self):
        return Path("build/revealjs") / "_static" / "css"

    @property
    def destination(self):
        return Path("docs") / "_static" / "css"

    def iter_target(self):
        yield from self.source.glob("*.css")


@dataclass
class EntireRules:
    for_html: HtmlNamingRule
    for_images: ImagesNamingRule
    for_css: CssNamingRule

    @classmethod
    def build(cls, slide_directory_name):
        html_rule = HtmlNamingRule(slide_directory_name)
        images_rule = ImagesNamingRule()
        css_rule = CssNamingRule()
        return cls(html_rule, images_rule, css_rule)
