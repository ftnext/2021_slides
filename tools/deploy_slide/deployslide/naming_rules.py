from dataclasses import dataclass


class HtmlNamingRule:
    pass


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
