import subprocess


def run_command(command):
    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            return f"ERROR:\n{result.stderr}"

        if not result.stdout.strip():
            return "NO_OUTPUT"

        return result.stdout

    except Exception as e:
        return f"EXCEPTION:\n{str(e)}"