import os
import argparse
from e2b_code_interpreter import Sandbox
from dotenv import load_dotenv


def run_sandbox_command(sandbox: Sandbox, cmd: str, env_vars: dict) -> dict:
    """Execute a command in the sandbox with given environment variables."""
    return sandbox.commands.run(
        cmd=cmd,
        envs=env_vars,
        on_stdout=lambda data: print(data),  # Stream stdout to console
        on_stderr=lambda data: print(data),  # Stream stderr to console
    )

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Run commands in e2b sandbox')
    parser.add_argument('--sandbox-id',
                      required=True,
                      help='The e2b sandbox ID to use')
    return parser.parse_args()

def main():
    print("***EXPERIMENTAL FEATURE***")
    load_dotenv()
    try:
        # Parse command line arguments
        args = parse_args()

        sandbox_id = args.sandbox_id
        assert sandbox_id, "You must provide an e2b sandbox id when using the docker e2b executor"
        print(f"Using docker container on e2b with {sandbox_id=}")

        # Initialize sandbox
        sandbox = Sandbox(sandbox_id)

        # Prepare command and environment variables
        cmd = "python /app/multi_agent_system.py"
        env_vars = {"OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")}

        # Run command and get result
        result = run_sandbox_command(sandbox=sandbox, cmd=cmd, env_vars=env_vars)
        print(result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()