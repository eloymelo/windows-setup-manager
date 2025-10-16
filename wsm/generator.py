from pathlib import Path
from datetime import datetime
from jinja2 import Template
from .config import get_packages

def generate_script():
    """Generate PowerShell setup script from packages"""
    
    # Get packages data
    data = get_packages()
    packages = data['packages']
    
    # Get template path
    current_dir = Path(__file__).parent
    template_path = current_dir.parent / 'templates' / 'setup.ps1.j2'
    
    # Read template
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Create Jinja2 template
    template = Template(template_content)
    
    # Render template with data
    output = template.render(
        packages=packages,
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    
    # Write to output file
    output_dir = current_dir.parent / 'output'
    output_dir.mkdir(exist_ok=True)  # Create output folder if it doesn't exist
    
    output_file = output_dir / 'setup.ps1'
    with open(output_file, 'w') as f:
        f.write(output)
    
    return output_file