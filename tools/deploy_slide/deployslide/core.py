from dataclasses import dataclass

from deployslide import naming_rules


@dataclass
class SlideDeployer:
    html_rule: naming_rules.HtmlNamingRule
    images_rule: naming_rules.ImagesNamingRule

    @classmethod
    def create_from_entire_rules(
        cls, entire_rules: "naming_rules.EntireRules"
    ):
        """Factory from `naming_rules.EntireRules` instance."""
        return cls(entire_rules.for_html, entire_rules.for_images)
