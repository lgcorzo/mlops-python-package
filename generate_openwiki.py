import subprocess
import json

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True, shell=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.stderr)
        return None

# Check the git log
def check_git_log():
    log = run_command("git log --name-only")
    print(log)

if __name__ == "__main__":
    check_git_log()
