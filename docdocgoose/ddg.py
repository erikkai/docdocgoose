import click 
import os
import shutil
import importlib.resources as resources
import json
import time

# HELPER FUNCTIONS 

# Loads the configuration file and returns the json so it can be scanned
def load_config():
    config_path = ".docdocgoose/config.json"
    if not os.path.exists(config_path):
        return None

    with open(config_path, "r") as f:
        return json.load(f)

# Saves changes to configuration data 
def save_config(config_data):
    config_path = ".docdocgoose/config.json"

    with open(config_path, "w") as f:
        json.dump(config_data, f, indent=2)

# CLI COMMANDS AND IMPLEMENTATION
# --- Group 1: The Main Goose ---
@click.group()
def cli():
    """Official Goose Business."""
    pass

@cli.command()
def honk():
    click.echo("📢 HONK! Give me the bread.")

@cli.command()
def init():
    click.echo("Let's get started!")
    if not os.path.isdir(".git"):
        click.echo("HONK! 🪿 Please run this command from the root of your GitHub repository.")
        return
    
# Check for file structure and add it if it's not there, then install the link checker. 
    os.makedirs(".github/workflows", exist_ok=True)
    os.makedirs(".docdocgoose/logs", exist_ok=True)
    os.makedirs(".docdocgoose/exec", exist_ok=True)
    
    config = {
        "alert_mode": "single_issue"
    }

    with open(".docdocgoose/config.json", "w") as f: 
        json.dump(config, f, indent=2)

    click.echo("🪿 DocDocGoose directories are ready!")

    destination = ".github/workflows/docdocgoose_link_checker.yml"
    if os.path.exists(destination):
        click.echo("🪿 HONK! The file already exists. No changes were made, the install process stopped.") 
        return

    with resources.files("docdocgoose").joinpath("templates/link-checker.yml").open("rb") as src:
        with open(destination, "wb") as dst:
            shutil.copyfileobj(src, dst) 
            click.echo("Link checker successfully installed.")

@cli.command()
def scan():
    config = load_config()

    if config is None: 
        click.echo("HONK! 🪿 Run ddg init first.")
        return
    
    click.echo("🪿 Scanning for documentation health...")


    click.echo("Scan complete.")




