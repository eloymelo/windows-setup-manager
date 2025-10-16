import os
import shutil
from pathlib import Path
from git import Repo

def deploy_script():
    """Deploy generated script to website repository"""
    
    # Get website path from environment variable
    website_path = os.getenv('WSM_WEBSITE_PATH')
    
    if not website_path:
        raise ValueError("WSM_WEBSITE_PATH environment variable not set")
    
    website_path = Path(website_path)
    
    # Verify website repo exists
    if not website_path.exists():
        raise FileNotFoundError(f"Website path does not exist: {website_path}")
    
    # Get source and destination paths
    current_dir = Path(__file__).parent
    source_file = current_dir.parent / 'output' / 'setup.ps1'
    
    if not source_file.exists():
        raise FileNotFoundError("setup.ps1 not found. Run 'generate' command first.")
    
    # Create destination directory if needed
    dest_dir = website_path / 'static' / 'scripts' / 'win'
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    dest_file = dest_dir / 'setup.ps1'
    
    # Copy script
    shutil.copy(source_file, dest_file)
    
    # Git operations
    repo = Repo(website_path)
    repo.index.add(['static/scripts/win/setup.ps1'])
    repo.index.commit('update: refresh Windows setup script')
    repo.remote('origin').push()
    
    return dest_file