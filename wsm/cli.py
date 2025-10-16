import click
from .config import get_packages, save_packages
from .generator import generate_script
from .deployer import deploy_script

@click.group()
def cli():
    "Windows package installation tool"
    pass

@cli.command()
def list():
    "List all packages"
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

@cli.command()
@click.argument('package_id')
def add(package_id):
    "Add a new package to the collection"
    name = click.prompt("Package name")
    category = click.prompt("Category")
    description = click.prompt("Description (optional)", default="")
    
    data = get_packages()
    
    new_package = {
        'id': package_id,
        'name': name,
        'category': category,
        'description': description
    }

    data['packages'].append(new_package)
    
    save_packages(data)
    
    click.echo(f"Added {name} to the package list.")

@cli.command()
@click.argument('package_id')
def remove(package_id):
    'Remove a package from the collection'
    data = get_packages()
    packages = data['packages']

    package_to_remove = None
    for pkg in packages:
        if pkg['id'] == package_id:
            package_to_remove = pkg
            break

    if package_to_remove:
        packages.remove(package_to_remove)
        save_packages(data)
        click.echo(f"Removed {package_to_remove['name']} from the package list.")
    else:
        click.echo(f"Package {package_id} not found.", err=True)

@cli.command()
def generate():
    """Generate PowerShell setup script"""
    click.echo("Generating PowerShell script...")
    
    output_file = generate_script()
    
    click.echo(f"Script generated successfully!")
    click.echo(f"Location: {output_file}")

@cli.command()
def deploy():
    """Deploy generated script to website repository"""
    try:
        click.echo("Deploying script to website...")
        
        dest_file = deploy_script()
        
        click.echo(f"Script deployed successfully!")
        click.echo(f"Deployed to: {dest_file}")
        click.echo(f"Changes pushed to GitHub")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        click.echo("Set WSM_WEBSITE_PATH environment variable", err=True)
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
    except Exception as e:
        click.echo(f"Deployment failed: {e}", err=True)    