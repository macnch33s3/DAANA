DAANA

Data Analysis & Automatic Notification Application

🚀 Overview

DAANA is a Python-based framework for automated data analysis and reporting.
It is structured for interactive exploration via Jupyter notebooks and reproducible execution via uv (Python package and environment manager).

This repository includes:

Case study: Fallstudie_Rettungswesen

Exercises: Uebungen

Custom example: own_case

Demo notebook: test.ipynb

Project configuration: pyproject.toml and uv.lock

✅ Features

Structured modular folder layout for case studies, exercises, and personal projects

Reproducible environments powered by uv

Interactive Jupyter notebooks for analysis and experimentation

Simple to extend for new datasets or business cases

🧪 Getting Started
Prerequisites

Python ≥ 3.11 (as defined in .python-version)

uv
 installed globally

Install uv (if not already installed):

pip install uv

Installation & Setup
# Clone the repository
git clone https://github.com/macnch33s3/DAANA.git
cd DAANA

# Create and sync environment using uv
uv sync


uv sync will automatically:

Create a virtual environment in .venv

Install all dependencies from pyproject.toml and uv.lock

Running the Demo Notebook
# Activate environment
source .venv/bin/activate     # on Windows: .venv\Scripts\activate

# Launch Jupyter Notebook
uv run jupyter notebook


Open test.ipynb, execute the cells, and verify that all modules load correctly.

🗂 Repository Structure
DAANA/
├── Fallstudie_Rettungswesen/    # Case study: rescue services
├── Uebungen/                    # Exercises
├── own_case/                    # Custom case study
├── test.ipynb                   # Demo notebook
├── pyproject.toml               # Project configuration
├── uv.lock                      # Dependency lock file
├── .python-version              # Python version indicator
└── README.md                    # This file

🎯 Usage

Use the provided notebooks to analyse sample datasets.

Extend the own_case directory with your own data and logic.

Automate or schedule analysis by wrapping logic into scripts and running via uv run <script>.

Example:

uv run python scripts/analyse.py

🛠 Configuration & Customisation

Add or update dependencies:

uv add pandas numpy jupyter


Remove dependencies:

uv remove <package>


Update all dependencies:

uv lock --upgrade


Modify pyproject.toml to define metadata, dependencies, and scripts.

📚 Recommended Workflow

Clone repository

Run uv sync

Test environment via uv run jupyter notebook

Explore Fallstudie_Rettungswesen or Uebungen

Build your own case under own_case

Extend or automate via scripts or scheduled jobs

🤖 Future Enhancements

CLI for non-interactive execution

Integration with databases or APIs

Reporting dashboards (Streamlit / Dash)

Continuous integration workflows

📄 License & Contribution

Specify your license here (e.g., MIT or Apache 2.0).

Contributions are welcome — fork, branch, and open a pull request.
