# 🤖 Running Multi-Agent Systems with e2b

This example demonstrates how to containerize and deploy your multi-smolagents to run in the cloud.

**Note**: This is an experimental feature, currently tested on MacOS.

## 🚀 Getting Started

### Prerequisites
- An e2b account with API key (set in `.env`)
- e2b CLI installed
- Docker installed and running

### 🏃‍♂️ Quick Start

1. **Build the Container**
```bash
sh build_container.sh
```

The script uses the `e2b.Dockerfile` in this directory.
Feel free to customize it with any additional dependencies your agents need.
The initial build might take a few minutes.

2. **Launch Your Agents on e2b**
```bash
python run_on_e2b.py
```
You'll need the e2b sandbox ID from either:
- The CLI output during build
- The `e2b.toml` file (automatically created in your directory)

### 📝 Making Changes
The smolagent logic lives in `multi_agent_system.py`. If you modify this file, you'll need to:
1. Rebuild the container
2. Run the system again

Want to learn more about the multi-agent system? Check out the [detailed documentation](https://huggingface.co/docs/smolagents/en/examples/multiagents).