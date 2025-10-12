import click
from .config import get_packages

@click.group()
def cli():
    "Windows package installation tool"
    pass

@cli.command()
def list():
    "List all packages"
    print("DEBUG: list command called")
    data = get_packages()
    packages = data['packages']

    by_category = {}

    for pkg in packages:
        category = pkg['category']
        name = pkg['name']
        if category in by_category:
            by_category[category].append(name)
        else:
            by_category[category] = [name]

    for category, package_list in by_category.items():
        print(f"\n{category}:")
        for package in package_list:
            print(f" - {package}")