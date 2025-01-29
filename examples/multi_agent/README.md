# Using e2b to run multi-agent systems

This example shows how to use e2b to run multi-agent systems.
It will build a docker container, upload it to e2b, and run it.

This is an experimental feature.
Tested on MacOS

## Requirements

- e2b account and API key set in .env file
- e2b CLI installed
- docker installed and running locally

## Running the example

All the logic of the multi-agent system is in `multi_agent_system.py`.
See https://huggingface.co/docs/smolagents/en/examples/multiagents for more details.

First, build the docker container

```bash
sh build_container.sh
```

This might take a while, especially the first time.

This will build the container from the e2b.Dockerfile in this directory.
You can modify the Dockerfile to add any other dependencies you might need.

Get the e2b sandbox id from the CLI output (or from the e2b.toml file in the current directory which will get created when you build the container).

Run the multi-agent system on e2b

```bash
python run_on_e2b.py
```

If you make any changes to `multi_agent_system.py`, you will need to rebuild the docker container and re-run the multi-agent system again.