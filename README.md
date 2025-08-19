# agent_development_kit_anthropic 
Source (updated hard coded weather and time agent for Ney York only, to access the weather and time from any state in the US) --> https://google.github.io/adk-docs/get-started/quickstart/


cd agent_development_kit_anthropic
run in terminal: adk web
UI: http://localhost:8000
# Multi Tool Agent Project

This project demonstrates a simple agent that can answer questions about the time and weather in a city using the `google-adk` library.

## Prerequisites
- Python 3.11 or newer (for `zoneinfo` support)
- Internet connection (for package installation)

## Setup Instructions

1. **Clone the repository** (if you haven't already):
	```powershell
	git clone <your-repo-url>
	cd agent_development_kit_anthropic
	```

2. **Create and activate a virtual environment:**
	```powershell
	python -m venv .venv
	.venv\Scripts\Activate.ps1
	```

3. **Install required libraries:**
	```powershell
	pip install google-adk
	```
	The following libraries are used:
	- `google-adk` (for the Agent class)
	- `datetime` (standard library)
	- `zoneinfo` (standard library, Python 3.9+)

4. **Project Structure:**
	```
	agent_development_kit_anthropic/
	├── multi_tool_agent/
	│   ├── __init__.py
	│   ├── agent.py
	│   └── .env
	└── README.md
	```

For setup of the .env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_API_KEY


5. **Run the agent (example):**
   
	You can use the `root_agent` defined in `multi_tool_agent/agent.py` in your own scripts, or extend it as needed.

    Example usage (add to a script or interactive shell):
    ```python
    from multi_tool_agent.agent import root_agent
    result = root_agent.tools[0]("Los Angeles")  # Get weather for Los Angeles
    print(result)
    ```

    6. **Start the ADK web interface (if available):**
    ```powershell
    adk web
    ```

    ## Notes
    - The agent now supports queries for any city in the United States.
- Update the `get_weather` and `get_current_time` functions in `agent.py` to support more cities as needed.

## Troubleshooting
- If you encounter import errors for `google.adk.agents`, ensure `google-adk` is installed in your active virtual environment.
- For issues with `zoneinfo`, ensure you are using Python 3.9 or newer.

---

Feel free to modify and extend this project for your own use cases!


