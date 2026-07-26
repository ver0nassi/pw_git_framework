# Playwright Python Framework

A Playwright-based UI automation framework built with Python.

## Prerequisites

* Python 3.10 or newer
* Git
* Playwright-supported operating system (Linux, macOS, or Windows)

## Clone the Repository

```bash
git clone git@github.com:<your-github-username>/pw-git-framework.git

cd pw-git-framework
```

## Create a Virtual Environment

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## Install Dependencies

Install the project and its dependencies:

```bash
pip install -e .
```

## Install Playwright Browsers

```bash
playwright install
```

## Verify the Installation

Check the installed Playwright version:

```bash
playwright --version
```

Verify that the project dependencies are installed:

```bash
pip list
```

## Running Tests

Once tests are added to the project:

```bash
pytest
```

or

```bash
pytest tests/
```

## Updating Dependencies

After pulling the latest changes from Git:

```bash
git pull
pip install -e .
```

If Playwright has been updated:

```bash
playwright install
```

## Project Structure

```text
pw-git-framework/
├── browser/
├── components/
├── pages/
├── tests/
├── pyproject.toml
├── README.md
└── .gitignore
```

## License

Specify your project's license here (for example, MIT License).
