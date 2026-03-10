import click 
import os
import shutil
import importlib.resources as resources
import json
import subprocess
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

# Retrieve the repo info for scan
def get_repo_info():
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        capture_output=True,
        text=True
    )

    url = result.stdout.strip()

    if "github.com" not in url:
        raise Exception("This does not appear to be a GitHub repository.")
    
    repo_part = url.split("github.com")[-1]

    repo_part = repo_part.replace(".git", "")

    owner, repo = repo_part.split("/")

    return owner, repo

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
    
    if os.path.isdir(".docdocgoose/"):
        if click.confirm("HONK! 🪿 Docdocgoose appears to already be initialized. Reinitialize and overwrite configuration? (IT OVERWRITES EVERYTHING!)"):
            click.echo('Continuing...')
        else: 
            click.echo('Aborted.')
            return

# Check for file structure and add it if it's not there, then install the link checker. 
    os.makedirs(".github/workflows", exist_ok=True)
    os.makedirs(".docdocgoose/logs", exist_ok=True)
    os.makedirs(".docdocgoose/exec", exist_ok=True)
    
    config = {
        "alert_mode": "single_issue",
        "docrot": {
        "priorities_days": {
            "P1": 7,
            "P2": 90,
            "P3": 180
        },
        "documents": {}
        }
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

    with open(".docdocgoose/config.json", 'r') as file:
        config = json.load(file)
        documents = config["docrot"]["documents"]
        if not documents:
            click.echo("No documents configured.")
        else: 
            owner, repo = get_repo_info()
            print(owner)
            print(repo)
            for item in documents:
                print(item)    

        
    click.echo("Scan complete.")




