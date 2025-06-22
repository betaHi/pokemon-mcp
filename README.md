## Install uv
1. MacOS/Linux
    ```
    curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Windows
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
## Set up
1. clone project
   ```
   git clone https://github.com/betaHi/pokemon-mcp.git

   cd pokemon
   ```
2. Activate uv
   ```
   uv venv

   .venv\Scripts\activate
   ```
3. Mcp config
   ```
   "mcpServers": {
      "get-pokemon": {
        "command": "uv",
          "args": [
            "--directory",
            "{absolute folder path about pokemon}",
            "run",
            "get-pokemon.py"
        ]
      }
    }
   ```