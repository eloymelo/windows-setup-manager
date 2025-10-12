# Windows Setup Manager

Automate your Windows software installation with a single command.

## Why This Tool?

I was tired of manually installing packages one by one after every fresh Windows install. So I built this tool to automate the process — and decided to make it public to help others too.

## Features

- **One-command installation**: Run a single PowerShell command to set up your system
- **Interactive package selection**: Choose what to install from a list
- **Organized by category**: Browsers, Development Tools, Gaming, Security, and more
- **Powered by winget**: Uses Windows Package Manager for reliable installations
- **150+ packages**: My personal collection of essential Windows software

## Quick Start

Copy and paste this into PowerShell (run as Administrator):
```powershell
iwr -useb eloymelo.com/scripts/win/setup.ps1 | iex