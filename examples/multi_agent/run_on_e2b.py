import os
import os
from e2b_code_interpreter import Sandbox
from dotenv import load_dotenv

def setup_environment():
    """Load environment variables and validate sandbox ID."""
    load_dotenv()

    # For now, we hardcode the sandbox id
    # TODO: infer the sandbox id from the current directory
    # It looks like e2b creates e2b.toml file in the current directory
    # and we can read the sandbox id from there
    sandbox_id = "trb0gi2erw7c3zwq4fvi"

    if not sandbox_id:
        raise ValueError("You must provide an e2b sandbox id when using the docker e2b executor")

    return sandbox_id

def run_sandbox_command(sandbox: Sandbox, cmd: str, env_vars: dict) -> dict:
    """Execute a command in the sandbox with given environment variables."""
    return sandbox.commands.run(
        cmd=cmd,
        envs=env_vars,
        on_stdout=lambda data: print(data),  # Stream stdout to console
        on_stderr=lambda data: print(data),  # Stream stderr to console
    )


def main():
    print("***EXPERIMENTAL FEATURE***")

    try:
        # Setup environment and get sandbox ID
        sandbox_id = setup_environment()
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