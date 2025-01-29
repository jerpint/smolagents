# 🤖 Running Multi-Agent Systems with e2b

This example demonstrates how to containerize and deploy your multi-agent `smolagent` to run 100% remotely on [E2B](https://e2b.dev/).

**Note**: This is an experimental feature, currently tested on MacOS.

## 🚀 Getting Started

### Prerequisites
- An [E2B](https://e2b.dev/) account with API key (set in `.env`)
- E2B CLI installed
- Docker installed and running locally

### 🏃‍♂️ Quick Start

1. **Prepare your agent logic**

See `multi_agent_system.py` for an example of a multi-agent system.
It is adapted from the [smolagents documentation](https://huggingface.co/docs/smolagents/en/examples/multiagents).

2. **Build the Container**
```bash
sh build_container.sh
```

The script uses the `e2b.Dockerfile` in this directory.
It will build and push the container to E2B's registry.
Feel free to customize it with any additional dependencies your agents need.
The initial build might take a few minutes.

You should see the sandbox ID in the output of the build script.
You will need this ID to run the system on e2b.
You can also get it from the `e2b.toml` file (automatically created in your directory after a build).

3. **Launch Your Agents on e2b**
```bash
python run_on_e2b.py --sandbox-id <your-sandbox-id>
```

### 📝 Making Changes
The `smolagent` logic lives in `multi_agent_system.py`. If you modify this file, you'll need to:
1. Rebuild the container
2. Run the system again

Want to learn more about the multi-agent system? Check out the [detailed documentation](https://huggingface.co/docs/smolagents/en/examples/multiagents).