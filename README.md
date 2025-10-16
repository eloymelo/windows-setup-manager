# Windows Setup Manager

Automate your Windows software installation with a single command.

## Why I Built This

I got tired of manually installing the same packages every time I did a fresh Windows install. It was tedious and time-consuming, so I created this tool to automate the entire process. I'm sharing it publicly in case it helps others dealing with the same frustration.

## What It Does

- **One-command installation** - Run a single PowerShell command to set up your system
- **Interactive selection** - Pick exactly what you want from a clean interface using Out-GridView
- **95+ curated packages** - Organized across 17 categories like Browsers, Development, Gaming, Security, and more
- **Clear descriptions** - Each package explains what it does so you know what you're installing
- **Powered by winget** - Uses Windows Package Manager for reliable, silent installations
- **Python CLI for management** - Easy-to-use commands for adding, removing, and deploying packages

## How to Use It

Open PowerShell as Administrator and run:
```powershell
iwr -useb eloymelo.com/scripts/win/setup.ps1 | iex
```

A selection window opens where you choose which packages to install. That's it.

If you need something I don't have here, check out [Chris Titus Tech's Windows Utility](https://christitus.com/windows-tool/). His tool inspired this project.

## For Developers

If you want to manage the package collection yourself, clone the repo and use the Python CLI:

### Setup
```bash
git clone https://github.com/eloymelo/windows-setup-manager
cd windows-setup-manager
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Available Commands
```bash
python3 run.py list              # View all packages
python3 run.py add PackageID     # Add a new package
python3 run.py remove PackageID  # Remove a package
python3 run.py generate          # Create PowerShell script
python3 run.py deploy            # Push to website
```

Note: The deploy command needs `WSM_WEBSITE_PATH` environment variable set.

## Built With

- Python, Click, YAML, Jinja2, GitPython
- PowerShell for the installation script
- winget as the package manager

## Current Status

**v1.0** is live with 95 packages and interactive selection.

## What's Coming in v2.0

These are features I'm planning to add:

- **Custom dark-theme interface** - Replace Out-GridView with something better looking
- **Package search in CLI** - Find packages by name or category quickly
- **Installation tracking** - See what you installed and when
- **Update notifications** - Get notified when new packages are added
- **Backup and restore** - Save your selections and restore them later

## Contributing

If you want to contribute, feel free to open an issue or submit a pull request. Package suggestions are welcome too.

## Get in Touch

Questions? Email me at [contact@eloymelo.com](mailto:contact@eloymelo.com)

## License

MIT License

---

Built by [Eloy Melo](https://eloymelo.com) • [GitHub](https://github.com/eloymelo)