import argparse

from deployslide.core import SlideDeployer
from deployslide.naming_rules import EntireRules


def main():
    """Entrypoint function."""
    parser = argparse.ArgumentParser()
    parser.add_argument("slide_directory_name")
    args = parser.parse_args()

    entire_rules = EntireRules.build(args.slide_directory_name)
    slide_deployer = SlideDeployer.create_from_entire_rules(entire_rules)
    slide_deployer.deploy()
