# Full Project Conversation History



# Log: Day_1a_From_Prompt_to_Action.txt

{
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.13",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [],
      "isInternetEnabled": false,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "##### Copyright 2025 Google LLC."
      ],
      "metadata": {
        "id": "ajakRLWDQ0R3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:55:23.980165Z",
          "iopub.execute_input": "2025-11-10T21:55:23.980567Z",
          "iopub.status.idle": "2025-11-10T21:55:23.987199Z",
          "shell.execute_reply.started": "2025-11-10T21:55:23.980534Z",
          "shell.execute_reply": "2025-11-10T21:55:23.98583Z"
        },
        "id": "nkiM4LY3Q0R4"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 🚀 Your First AI Agent: From Prompt to Action\n",
        "\n",
        "**Welcome to the Kaggle 5-day Agents course!**\n",
        "\n",
        "This notebook is your first step into building AI agents. An agent can do more than just respond to a prompt — it can **take actions** to find information or get things done.\n",
        "\n",
        "In this notebook, you'll:\n",
        "\n",
        "- ✅ Install [Agent Development Kit (ADK)](https://google.github.io/adk-docs/)\n",
        "- ✅ Configure your API key to use the Gemini model\n",
        "- ✅ Build your first simple agent\n",
        "- ✅ Run your agent and watch it use a tool (like Google Search) to answer a question\n",
        "\n",
        "## ‼️ Please Read\n",
        "\n",
        "> ❌ **ℹ️ Note: No submission required!**\n",
        "> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n",
        "\n",
        "> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n",
        "\n",
        "**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**"
      ],
      "metadata": {
        "id": "CGRBwnS4Q0R5"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 📖 Get started with Kaggle Notebooks\n",
        "\n",
        "If this is your first time using Kaggle Notebooks, welcome! You can learn more about using Kaggle Notebooks [in the documentation](https://www.kaggle.com/docs/notebooks).\n",
        "\n",
        "Here's how to get started:\n",
        "\n",
        "**1. Verify Your Account (Required)**\n",
        "\n",
        "To use the Kaggle Notebooks in this course, you'll need to verify your account with a phone number.\n",
        "\n",
        "You can do this in your [Kaggle settings](https://www.kaggle.com/settings).\n",
        "\n",
        "**2. Make Your Own Copy**\n",
        "\n",
        "To run any code in this notebook, you first need your own editable copy.\n",
        "\n",
        "Click the `Copy and Edit` button in the top-right corner.\n",
        "\n",
        "![Copy and Edit button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_1.png)\n",
        "\n",
        "This creates a private copy of the notebook just for you.\n",
        "\n",
        "**3. Run Code Cells**\n",
        "\n",
        "Once you have your copy, you can run code.\n",
        "\n",
        "Click the ▶️ Run button next to any code cell to execute it.\n",
        "\n",
        "![Run cell button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_2.png)\n",
        "\n",
        "Run the cells in order from top to bottom.\n",
        "\n",
        "**4. If You Get Stuck**\n",
        "\n",
        "To restart: Select `Factory reset` from the `Run` menu.\n",
        "\n",
        "For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server."
      ],
      "metadata": {
        "id": "gAveaj8eQ0R6"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ⚙️ Section 1: Setup\n",
        "\n",
        "### 1.1: Install dependencies\n",
        "\n",
        "The Kaggle Notebooks environment includes a pre-installed version of the [google-adk](https://google.github.io/adk-docs/) library for Python and its required dependencies, so you don't need to install additional packages in this notebook.\n",
        "\n",
        "To install and use ADK in your own Python development environment outside of this course, you can do so by running:\n",
        "\n",
        "```\n",
        "pip install google-adk\n",
        "```"
      ],
      "metadata": {
        "id": "mBv_vGr3Q0R6"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.2: Configure your Gemini API Key\n",
        "\n",
        "This notebook uses the [Gemini API](https://ai.google.dev/gemini-api/docs), which requires authentication.\n",
        "\n",
        "**1. Get your API key**\n",
        "\n",
        "If you don't have one already, create an [API key in Google AI Studio](https://aistudio.google.com/app/api-keys).\n",
        "\n",
        "**2. Add the key to Kaggle Secrets**\n",
        "\n",
        "Next, you will need to add your API key to your Kaggle Notebook as a Kaggle User Secret.\n",
        "\n",
        "1. In the top menu bar of the notebook editor, select `Add-ons` then `Secrets`.\n",
        "2. Create a new secret with the label `GOOGLE_API_KEY`.\n",
        "3. Paste your API key into the \"Value\" field and click \"Save\".\n",
        "4. Ensure that the checkbox next to `GOOGLE_API_KEY` is selected so that the secret is attached to the notebook.\n",
        "\n",
        "**3. Authenticate in the notebook**\n",
        "\n",
        "Run the cell below to complete authentication."
      ],
      "metadata": {
        "id": "Vl5FeGLTQ0R6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from kaggle_secrets import UserSecretsClient\n",
        "\n",
        "try:\n",
        "    GOOGLE_API_KEY = UserSecretsClient().get_secret(\"GOOGLE_API_KEY\")\n",
        "    os.environ[\"GOOGLE_API_KEY\"] = GOOGLE_API_KEY\n",
        "    print(\"✅ Gemini API key setup complete.\")\n",
        "except Exception as e:\n",
        "    print(\n",
        "        f\"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}\"\n",
        "    )"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:55:23.988991Z",
          "iopub.execute_input": "2025-11-10T21:55:23.989268Z",
          "iopub.status.idle": "2025-11-10T21:55:24.077824Z",
          "shell.execute_reply.started": "2025-11-10T21:55:23.989247Z",
          "shell.execute_reply": "2025-11-10T21:55:24.076897Z"
        },
        "id": "PD8fNMHOQ0R7"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.3: Import ADK components\n",
        "\n",
        "Now, import the specific components you'll need from the Agent Development Kit and the Generative AI library. This keeps your code organized and ensures we have access to the necessary building blocks."
      ],
      "metadata": {
        "id": "ZpPWKFfhQ0R7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.adk.agents import Agent\n",
        "from google.adk.models.google_llm import Gemini\n",
        "from google.adk.runners import InMemoryRunner\n",
        "from google.adk.tools import google_search\n",
        "from google.genai import types\n",
        "\n",
        "print(\"✅ ADK components imported successfully.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:55:24.079126Z",
          "iopub.execute_input": "2025-11-10T21:55:24.079512Z",
          "iopub.status.idle": "2025-11-10T21:56:14.794837Z",
          "shell.execute_reply.started": "2025-11-10T21:55:24.079485Z",
          "shell.execute_reply": "2025-11-10T21:56:14.79388Z"
        },
        "id": "caaWLuANQ0R7"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.4: Helper functions\n",
        "\n",
        "We'll define some helper functions. If you are running this outside the Kaggle environment, you don't need to do this."
      ],
      "metadata": {
        "id": "vGOdeFeIQ0R7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define helper functions that will be reused throughout the notebook\n",
        "\n",
        "from IPython.core.display import display, HTML\n",
        "from jupyter_server.serverapp import list_running_servers\n",
        "\n",
        "\n",
        "# Gets the proxied URL in the Kaggle Notebooks environment\n",
        "def get_adk_proxy_url():\n",
        "    PROXY_HOST = \"https://kkb-production.jupyter-proxy.kaggle.net\"\n",
        "    ADK_PORT = \"8000\"\n",
        "\n",
        "    servers = list(list_running_servers())\n",
        "    if not servers:\n",
        "        raise Exception(\"No running Jupyter servers found.\")\n",
        "\n",
        "    baseURL = servers[0][\"base_url\"]\n",
        "\n",
        "    try:\n",
        "        path_parts = baseURL.split(\"/\")\n",
        "        kernel = path_parts[2]\n",
        "        token = path_parts[3]\n",
        "    except IndexError:\n",
        "        raise Exception(f\"Could not parse kernel/token from base URL: {baseURL}\")\n",
        "\n",
        "    url_prefix = f\"/k/{kernel}/{token}/proxy/proxy/{ADK_PORT}\"\n",
        "    url = f\"{PROXY_HOST}{url_prefix}\"\n",
        "\n",
        "    styled_html = f\"\"\"\n",
        "    <div style=\"padding: 15px; border: 2px solid #f0ad4e; border-radius: 8px; background-color: #fef9f0; margin: 20px 0;\">\n",
        "        <div style=\"font-family: sans-serif; margin-bottom: 12px; color: #333; font-size: 1.1em;\">\n",
        "            <strong>⚠️ IMPORTANT: Action Required</strong>\n",
        "        </div>\n",
        "        <div style=\"font-family: sans-serif; margin-bottom: 15px; color: #333; line-height: 1.5;\">\n",
        "            The ADK web UI is <strong>not running yet</strong>. You must start it in the next cell.\n",
        "            <ol style=\"margin-top: 10px; padding-left: 20px;\">\n",
        "                <li style=\"margin-bottom: 5px;\"><strong>Run the next cell</strong> (the one with <code>!adk web ...</code>) to start the ADK web UI.</li>\n",
        "                <li style=\"margin-bottom: 5px;\">Wait for that cell to show it is \"Running\" (it will not \"complete\").</li>\n",
        "                <li>Once it's running, <strong>return to this button</strong> and click it to open the UI.</li>\n",
        "            </ol>\n",
        "            <em style=\"font-size: 0.9em; color: #555;\">(If you click the button before running the next cell, you will get a 500 error.)</em>\n",
        "        </div>\n",
        "        <a href='{url}' target='_blank' style=\"\n",
        "            display: inline-block; background-color: #1a73e8; color: white; padding: 10px 20px;\n",
        "            text-decoration: none; border-radius: 25px; font-family: sans-serif; font-weight: 500;\n",
        "            box-shadow: 0 2px 5px rgba(0,0,0,0.2); transition: all 0.2s ease;\">\n",
        "            Open ADK Web UI (after running cell below) ↗\n",
        "        </a>\n",
        "    </div>\n",
        "    \"\"\"\n",
        "\n",
        "    display(HTML(styled_html))\n",
        "\n",
        "    return url_prefix\n",
        "\n",
        "\n",
        "print(\"✅ Helper functions defined.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:56:14.795801Z",
          "iopub.execute_input": "2025-11-10T21:56:14.797111Z",
          "iopub.status.idle": "2025-11-10T21:56:14.990522Z",
          "shell.execute_reply.started": "2025-11-10T21:56:14.797081Z",
          "shell.execute_reply": "2025-11-10T21:56:14.98963Z"
        },
        "id": "3E70xHSdQ0R8"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.5: Configure Retry Options\n",
        "\n",
        "When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff."
      ],
      "metadata": {
        "id": "qZfsLW3-Q0R8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "retry_config=types.HttpRetryOptions(\n",
        "    attempts=5,  # Maximum retry attempts\n",
        "    exp_base=7,  # Delay multiplier\n",
        "    initial_delay=1, # Initial delay before first retry (in seconds)\n",
        "    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:56:14.993067Z",
          "iopub.execute_input": "2025-11-10T21:56:14.993578Z",
          "iopub.status.idle": "2025-11-10T21:56:14.998872Z",
          "shell.execute_reply.started": "2025-11-10T21:56:14.993556Z",
          "shell.execute_reply": "2025-11-10T21:56:14.997778Z"
        },
        "id": "QyRKq0BuQ0R8"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 🤖 Section 2: Your first AI Agent with ADK\n",
        "\n",
        "### 🤔 2.1 What is an AI Agent?\n",
        "\n",
        "You've probably used an LLM like Gemini before, where you give it a prompt and it gives you a text response.\n",
        "\n",
        "`Prompt -> LLM -> Text`\n",
        "\n",
        "An AI Agent takes this one step further. An agent can think, take actions, and observe the results of those actions to give you a better answer.\n",
        "\n",
        "`Prompt -> Agent -> Thought -> Action -> Observation -> Final Answer`\n",
        "\n",
        "In this notebook, we'll build an agent that can take the action of searching Google. Let's see the difference!"
      ],
      "metadata": {
        "id": "sJIkS8fHQ0R9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.2 Define your agent\n",
        "\n",
        "Now, let's build our agent. We'll configure an `Agent` by setting its key properties, which tell it what to do and how to operate.\n",
        "\n",
        "To learn more, check out the documentation related to [agents in ADK](https://google.github.io/adk-docs/agents/).\n",
        "\n",
        "These are the main properties we'll set:\n",
        "\n",
        "- **name** and **description**: A simple name and description to identify our agent.\n",
        "- **model**: The specific LLM that will power the agent's reasoning. We'll use \"gemini-2.5-flash-lite\".\n",
        "- **instruction**: The agent's guiding prompt. This tells the agent what its goal is and how to behave.\n",
        "- **tools**: A list of [tools](https://google.github.io/adk-docs/tools/) that the agent can use. To start, we'll give it the `google_search` tool, which lets it find up-to-date information online."
      ],
      "metadata": {
        "id": "Mt-a1p-vQ0R9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "root_agent = Agent(\n",
        "    name=\"helpful_assistant\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    description=\"A simple agent that can answer general questions.\",\n",
        "    instruction=\"You are a helpful assistant. Use Google Search for current info or if unsure.\",\n",
        "    tools=[google_search],\n",
        ")\n",
        "\n",
        "print(\"✅ Root Agent defined.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:56:14.99996Z",
          "iopub.execute_input": "2025-11-10T21:56:15.000328Z",
          "iopub.status.idle": "2025-11-10T21:56:15.021628Z",
          "shell.execute_reply.started": "2025-11-10T21:56:15.000298Z",
          "shell.execute_reply": "2025-11-10T21:56:15.020593Z"
        },
        "id": "0jpnzREVQ0R9"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.3 Run your agent\n",
        "\n",
        "Now it's time to bring your agent to life and send it a query. To do this, you need a [`Runner`](https://google.github.io/adk-docs/runtime/), which is the central component within ADK that acts as the orchestrator. It manages the conversation, sends our messages to the agent, and handles its responses.\n",
        "\n",
        "**a. Create an `InMemoryRunner` and tell it to use our `root_agent`:**"
      ],
      "metadata": {
        "id": "jfo5OvFhQ0R9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "runner = InMemoryRunner(agent=root_agent)\n",
        "\n",
        "print(\"✅ Runner created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:56:15.022527Z",
          "iopub.execute_input": "2025-11-10T21:56:15.022854Z",
          "iopub.status.idle": "2025-11-10T21:56:15.043825Z",
          "shell.execute_reply.started": "2025-11-10T21:56:15.02282Z",
          "shell.execute_reply": "2025-11-10T21:56:15.042786Z"
        },
        "id": "aPB3Vhr7Q0R-"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "👉 Note that we are using the Python Runner directly in this notebook. You can also run agents using ADK command-line tools such as `adk run`, `adk web`, or `adk api_server`. To learn more, check out the documentation related to [runtime in ADK](https://google.github.io/adk-docs/runtime/)."
      ],
      "metadata": {
        "id": "gOJGMSWoQ0R-"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**b. Now you can call the `.run_debug()` method to send our prompt and get an answer.**\n",
        "\n",
        "👉 This method abstracts the process of session creation and maintenance and is used in prototyping. We'll explore \"what sessions are and how to create them\" on Day 3."
      ],
      "metadata": {
        "id": "EhOBLyKTQ0R-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "response = await runner.run_debug(\n",
        "    \"What is Agent Development Kit from Google? What languages is the SDK available in?\"\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:56:15.044913Z",
          "iopub.execute_input": "2025-11-10T21:56:15.045194Z",
          "iopub.status.idle": "2025-11-10T21:56:17.143806Z",
          "shell.execute_reply.started": "2025-11-10T21:56:15.045171Z",
          "shell.execute_reply": "2025-11-10T21:56:17.142898Z"
        },
        "id": "iywPQevtQ0R-"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "You can see a summary of ADK and its available languages in the response.\n",
        "\n",
        "### 2.4 How does it work?\n",
        "\n",
        "The agent performed a Google Search to get the latest information about ADK, and it knew to use this tool because:\n",
        "\n",
        "1. The agent inspects and is aware of which tools it has available to use.\n",
        "2. The agent's instructions specify the use of the search tool to get current information or if it is unsure of an answer.\n",
        "\n",
        "The best way to see the full, detailed trace of the agent's thoughts and actions is in the **ADK web UI**, which we'll set up later in this notebook.\n",
        "\n",
        "And we'll cover more detailed workflows for logging and observability later in the course."
      ],
      "metadata": {
        "id": "7mOgE0XkQ0R-"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 🚀 2.5 Your Turn!\n",
        "\n",
        "This is your chance to see the agent in action. Ask it a question that requires current information.\n",
        "\n",
        "Try one of these, or make up your own:\n",
        "\n",
        "- What's the weather in London?\n",
        "- Who won the last soccer world cup?\n",
        "- What new movies are showing in theaters now?"
      ],
      "metadata": {
        "id": "YnKqJm6RQ0R_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "response = await runner.run_debug(\"What's the weather in London?\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:56:17.144662Z",
          "iopub.execute_input": "2025-11-10T21:56:17.144924Z",
          "iopub.status.idle": "2025-11-10T21:56:18.769676Z",
          "shell.execute_reply.started": "2025-11-10T21:56:17.144903Z",
          "shell.execute_reply": "2025-11-10T21:56:18.768676Z"
        },
        "id": "JL9GUiUmQ0R_"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 💻 Section 3: Try the ADK Web Interface\n",
        "\n",
        "### Overview\n",
        "\n",
        "ADK includes a built-in web interface for interactively chatting with, testing, and debugging your agents.\n",
        "\n",
        "<img width=\"1200\" src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day1/adk-web-ui.gif\" alt=\"ADK Web UI\" />\n",
        "\n",
        "To use the ADK web UI, you'll need to create an agent with Python files using the `adk create` command.\n",
        "\n",
        "Run the command below to generate a `sample-agent` folder that contains all the necessary files, including `agent.py` for your code, an `.env` file with your API key pre-configured, and an `__init__.py` file:"
      ],
      "metadata": {
        "id": "Z1fYvIUMQ0R_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!adk create sample-agent --model gemini-2.5-flash-lite --api_key $GOOGLE_API_KEY"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:56:18.770633Z",
          "iopub.execute_input": "2025-11-10T21:56:18.770935Z",
          "iopub.status.idle": "2025-11-10T21:56:42.57439Z",
          "shell.execute_reply.started": "2025-11-10T21:56:18.770907Z",
          "shell.execute_reply": "2025-11-10T21:56:42.573281Z"
        },
        "id": "s4WkBXu-Q0R_"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Get your custom URL to access the ADK web UI in the Kaggle Notebooks environment:"
      ],
      "metadata": {
        "id": "SPvU9GwMQ0SA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "url_prefix = get_adk_proxy_url()"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:56:42.575588Z",
          "iopub.execute_input": "2025-11-10T21:56:42.575874Z",
          "iopub.status.idle": "2025-11-10T21:56:42.585559Z",
          "shell.execute_reply.started": "2025-11-10T21:56:42.575843Z",
          "shell.execute_reply": "2025-11-10T21:56:42.584682Z"
        },
        "id": "0RRu0DTrQ0SA"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Now we can run ADK web:"
      ],
      "metadata": {
        "id": "rKa2kk9iQ0SA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!adk web --url_prefix {url_prefix}"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:56:42.586407Z",
          "iopub.execute_input": "2025-11-10T21:56:42.586948Z",
          "iopub.status.idle": "2025-11-10T21:57:15.119203Z",
          "shell.execute_reply.started": "2025-11-10T21:56:42.586925Z",
          "shell.execute_reply": "2025-11-10T21:57:15.118052Z"
        },
        "id": "58VPLRmyQ0SA"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Now you can access the ADK dev UI using the link above.\n",
        "\n",
        "Once you open the link, you'll see the ADK web interface where you can ask your ADK agent questions.\n",
        "\n",
        "Note: This sample agent does not have any tools enabled (like Google Search). It is a basic agent designed specifically to let you explore the UI features.\n",
        "\n",
        "‼️ **IMPORTANT: DO NOT SHARE THE PROXY LINK** with anyone - treat it as sensitive data as it contains your authentication token in the URL."
      ],
      "metadata": {
        "id": "AGkXijkJQ0SA"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## ✅ Congratulations!\n",
        "\n",
        "You've built and run your first agent with ADK! You've just seen the core concept of agent development in action.\n",
        "\n",
        "The big takeaway is that your agent didn't just *respond*—it **reasoned** that it needed more information and then **acted** by using a tool. This ability to take action is the foundation of all agent-based AI.\n",
        "\n",
        "**ℹ️ Note: No submission required!**\n",
        "\n",
        "This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "### 📚 Learn More\n",
        "\n",
        "Refer to the following documentation to learn more:\n",
        "\n",
        "- [ADK Documentation](https://google.github.io/adk-docs/)\n",
        "- [ADK Quickstart for Python](https://google.github.io/adk-docs/get-started/python/)\n",
        "- [ADK Agents Overview](https://google.github.io/adk-docs/agents/)\n",
        "- [ADK Tools Overview](https://google.github.io/adk-docs/tools/)\n",
        "\n",
        "### 🎯 Next Steps\n",
        "\n",
        "Ready for the next challenge? Continue to the next notebook to learn how to **architect multi-agent systems.**"
      ],
      "metadata": {
        "id": "Uw4uTWkhQ0SB"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "| Authors |\n",
        "| --- |\n",
        "| [Kristopher Overholt](http://linkedin.com/in/koverholt) |"
      ],
      "metadata": {
        "id": "iYW2hOudQ0SB"
      }
    }
  ]
}

---



# Log: Day_1b_Agent_Architectures_013cb7.txt

{
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.13",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [],
      "isInternetEnabled": true,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "##### Copyright 2025 Google LLC."
      ],
      "metadata": {
        "id": "e_dS59jARjUJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:57:40.307674Z",
          "iopub.execute_input": "2025-11-10T21:57:40.307986Z",
          "iopub.status.idle": "2025-11-10T21:57:40.313551Z",
          "shell.execute_reply.started": "2025-11-10T21:57:40.307935Z",
          "shell.execute_reply": "2025-11-10T21:57:40.312426Z"
        },
        "id": "K33JjGQ2RjUK"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 🚀 Multi-Agent Systems & Workflow Patterns\n",
        "\n",
        "**Welcome to the Kaggle 5-day Agents course!**\n",
        "\n",
        "In the previous notebook, you built a **single agent** that could take action. Now, you'll learn how to scale up by building **agent teams**.\n",
        "\n",
        "Just like a team of people, you can create specialized agents that collaborate to solve complex problems. This is called a **multi-agent system**, and it's one of the most powerful concepts in AI agent development.\n",
        "\n",
        "In this notebook, you'll:\n",
        "\n",
        "- ✅ Learn when to use multi-agent systems in [Agent Development Kit (ADK)](https://google.github.io/adk-docs/)\n",
        "- ✅ Build your first system using an LLM as a \"manager\"\n",
        "- ✅ Learn three core workflow patterns (Sequential, Parallel, and Loop) to coordinate your agent teams\n",
        "\n",
        "## ‼️ Please Read\n",
        "\n",
        "> ❌ **ℹ️ Note: No submission required!**\n",
        "> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n",
        "\n",
        "> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n",
        "\n",
        "**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**"
      ],
      "metadata": {
        "id": "EsM7M5tLRjUL"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 📖 Get started with Kaggle Notebooks\n",
        "\n",
        "If this is your first time using Kaggle Notebooks, welcome! You can learn more about using Kaggle Notebooks [in the documentation](https://www.kaggle.com/docs/notebooks).\n",
        "\n",
        "Here's how to get started:\n",
        "\n",
        "**1. Verify Your Account (Required)**\n",
        "\n",
        "To use the Kaggle Notebooks in this course, you'll need to verify your account with a phone number.\n",
        "\n",
        "You can do this in your [Kaggle settings](https://www.kaggle.com/settings).\n",
        "\n",
        "**2. Make Your Own Copy**\n",
        "\n",
        "To run any code in this notebook, you first need your own editable copy.\n",
        "\n",
        "Click the `Copy and Edit` button in the top-right corner.\n",
        "\n",
        "![Copy and Edit button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_1.png)\n",
        "\n",
        "This creates a private copy of the notebook just for you.\n",
        "\n",
        "**3. Run Code Cells**\n",
        "\n",
        "Once you have your copy, you can run code.\n",
        "\n",
        "Click the ▶️ Run button next to any code cell to execute it.\n",
        "\n",
        "![Run cell button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_2.png)\n",
        "\n",
        "Run the cells in order from top to bottom.\n",
        "\n",
        "**4. If You Get Stuck**\n",
        "\n",
        "To restart: Select `Factory reset` from the `Run` menu.\n",
        "\n",
        "For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server."
      ],
      "metadata": {
        "id": "HTs0UIsPRjUM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ⚙️ Section 1: Setup\n",
        "\n",
        "### 1.1: Install dependencies\n",
        "\n",
        "The Kaggle Notebooks environment includes a pre-installed version of the [google-adk](https://google.github.io/adk-docs/) library for Python and its required dependencies, so you don't need to install additional packages in this notebook.\n",
        "\n",
        "To install and use ADK in your own Python development environment outside of this course, you can do so by running:\n",
        "\n",
        "```\n",
        "pip install google-adk\n",
        "```"
      ],
      "metadata": {
        "id": "cCkOU-qjRjUM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.2: Configure your Gemini API Key\n",
        "\n",
        "This notebook uses the [Gemini API](https://ai.google.dev/gemini-api/docs), which requires authentication.\n",
        "\n",
        "**1. Get your API key**\n",
        "\n",
        "If you don't have one already, create an [API key in Google AI Studio](https://aistudio.google.com/app/api-keys).\n",
        "\n",
        "**2. Add the key to Kaggle Secrets**\n",
        "\n",
        "Next, you will need to add your API key to your Kaggle Notebook as a Kaggle User Secret.\n",
        "\n",
        "1. In the top menu bar of the notebook editor, select `Add-ons` then `Secrets`.\n",
        "2. Create a new secret with the label `GOOGLE_API_KEY`.\n",
        "3. Paste your API key into the \"Value\" field and click \"Save\".\n",
        "4. Ensure that the checkbox next to `GOOGLE_API_KEY` is selected so that the secret is attached to the notebook.\n",
        "\n",
        "**3. Authenticate in the notebook**\n",
        "\n",
        "Run the cell below to complete authentication."
      ],
      "metadata": {
        "id": "4OP_Rf7aRjUN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from kaggle_secrets import UserSecretsClient\n",
        "\n",
        "try:\n",
        "    GOOGLE_API_KEY = UserSecretsClient().get_secret(\"GOOGLE_API_KEY\")\n",
        "    os.environ[\"GOOGLE_API_KEY\"] = GOOGLE_API_KEY\n",
        "    print(\"✅ Gemini API key setup complete.\")\n",
        "except Exception as e:\n",
        "    print(\n",
        "        f\"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}\"\n",
        "    )"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:57:40.315649Z",
          "iopub.execute_input": "2025-11-10T21:57:40.316158Z",
          "iopub.status.idle": "2025-11-10T21:57:40.50102Z",
          "shell.execute_reply.started": "2025-11-10T21:57:40.316122Z",
          "shell.execute_reply": "2025-11-10T21:57:40.500007Z"
        },
        "id": "xjLVdJseRjUO"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.3: Import ADK components\n",
        "\n",
        "Now, import the specific components you'll need from the Agent Development Kit and the Generative AI library. This keeps your code organized and ensures we have access to the necessary building blocks."
      ],
      "metadata": {
        "id": "dqU3-MoDRjUO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent\n",
        "from google.adk.models.google_llm import Gemini\n",
        "from google.adk.runners import InMemoryRunner\n",
        "from google.adk.tools import AgentTool, FunctionTool, google_search\n",
        "from google.genai import types\n",
        "\n",
        "print(\"✅ ADK components imported successfully.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:57:40.501951Z",
          "iopub.execute_input": "2025-11-10T21:57:40.502216Z",
          "iopub.status.idle": "2025-11-10T21:58:30.635444Z",
          "shell.execute_reply.started": "2025-11-10T21:57:40.502195Z",
          "shell.execute_reply": "2025-11-10T21:58:30.634513Z"
        },
        "id": "IyTfcj79RjUP"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.4: Configure Retry Options\n",
        "\n",
        "When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff."
      ],
      "metadata": {
        "id": "k3hadMjDRjUQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "retry_config=types.HttpRetryOptions(\n",
        "    attempts=5,  # Maximum retry attempts\n",
        "    exp_base=7,  # Delay multiplier\n",
        "    initial_delay=1,\n",
        "    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:30.636332Z",
          "iopub.execute_input": "2025-11-10T21:58:30.637706Z",
          "iopub.status.idle": "2025-11-10T21:58:30.642973Z",
          "shell.execute_reply.started": "2025-11-10T21:58:30.637676Z",
          "shell.execute_reply": "2025-11-10T21:58:30.642024Z"
        },
        "id": "0qC7OzmeRjUQ"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🤔 Section 2: Why Multi-Agent Systems? + Your First Multi-Agent"
      ],
      "metadata": {
        "id": "tcGhXjzVRjUQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**The Problem: The \"Do-It-All\" Agent**\n",
        "\n",
        "Single agents can do a lot. But what happens when the task gets complex? A single \"monolithic\" agent that tries to do research, writing, editing, and fact-checking all at once becomes a problem. Its instruction prompt gets long and confusing. It's hard to debug (which part failed?), difficult to maintain, and often produces unreliable results.\n",
        "\n",
        "**The Solution: A Team of Specialists**\n",
        "\n",
        "Instead of one \"do-it-all\" agent, we can build a **multi-agent system**. This is a team of simple, specialized agents that collaborate, just like a real-world team. Each agent has one clear job (e.g., one agent *only* does research, another *only* writes). This makes them easier to build, easier to test, and much more powerful and reliable when working together.\n",
        "\n",
        "To learn more, check out the documentation related to [LLM agents in ADK](https://google.github.io/adk-docs/agents/llm-agents/).\n",
        "\n",
        "**Architecture: Single Agent vs Multi-Agent Team**\n",
        "\n",
        "<!--\n",
        "```mermaid\n",
        "graph TD\n",
        "    subgraph Single[\"❌ Monolithic Agent\"]\n",
        "        A[\"One Agent Does Everything\"]\n",
        "    end\n",
        "\n",
        "    subgraph Multi[\"✅ Multi-Agent Team\"]\n",
        "        B[\"Root Coordinator\"] -- > C[\"Research Specialist\"]\n",
        "        B -- > E[\"Summary Specialist\"]\n",
        "\n",
        "        C -- >|findings| F[\"Shared State\"]\n",
        "        E -- >|summary| F\n",
        "    end\n",
        "\n",
        "    style A fill:#ffcccc\n",
        "    style B fill:#ccffcc\n",
        "    style F fill:#ffffcc\n",
        "```\n",
        "-->"
      ],
      "metadata": {
        "id": "3Rpfnzm_RjUR"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img width=\"800\" src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day1/multi-agent-team.png\" alt=\"Multi-agent Team\" />"
      ],
      "metadata": {
        "id": "j19Dq9geRjUR"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.1 Example: Research & Summarization System\n",
        "\n",
        "Let's build a system with two specialized agents:\n",
        "\n",
        "1. **Research Agent** - Searches for information using Google Search\n",
        "2. **Summarizer Agent** - Creates concise summaries from research findings"
      ],
      "metadata": {
        "id": "Hq8TF3l7RjUR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Research Agent: Its job is to use the google_search tool and present findings.\n",
        "research_agent = Agent(\n",
        "    name=\"ResearchAgent\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    instruction=\"\"\"You are a specialized research agent. Your only job is to use the\n",
        "    google_search tool to find 2-3 pieces of relevant information on the given topic and present the findings with citations.\"\"\",\n",
        "    tools=[google_search],\n",
        "    output_key=\"research_findings\",  # The result of this agent will be stored in the session state with this key.\n",
        ")\n",
        "\n",
        "print(\"✅ research_agent created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:30.645941Z",
          "iopub.execute_input": "2025-11-10T21:58:30.646262Z",
          "iopub.status.idle": "2025-11-10T21:58:30.749639Z",
          "shell.execute_reply.started": "2025-11-10T21:58:30.646239Z",
          "shell.execute_reply": "2025-11-10T21:58:30.748555Z"
        },
        "id": "5FaDTeGkRjUR"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Summarizer Agent: Its job is to summarize the text it receives.\n",
        "summarizer_agent = Agent(\n",
        "    name=\"SummarizerAgent\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    # The instruction is modified to request a bulleted list for a clear output format.\n",
        "    instruction=\"\"\"Read the provided research findings: {research_findings}\n",
        "Create a concise summary as a bulleted list with 3-5 key points.\"\"\",\n",
        "    output_key=\"final_summary\",\n",
        ")\n",
        "\n",
        "print(\"✅ summarizer_agent created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:30.750807Z",
          "iopub.execute_input": "2025-11-10T21:58:30.751873Z",
          "iopub.status.idle": "2025-11-10T21:58:30.772838Z",
          "shell.execute_reply.started": "2025-11-10T21:58:30.751745Z",
          "shell.execute_reply": "2025-11-10T21:58:30.771675Z"
        },
        "id": "84L0d7rYRjUR"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Refer to the ADK documentation for more information on [guiding agents with clear and specific instructions](https://google.github.io/adk-docs/agents/llm-agents/).\n",
        "\n",
        "Then we bring the agents together under a root agent, or coordinator:"
      ],
      "metadata": {
        "id": "4eJwiZETRjUR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Root Coordinator: Orchestrates the workflow by calling the sub-agents as tools.\n",
        "root_agent = Agent(\n",
        "    name=\"ResearchCoordinator\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    # This instruction tells the root agent HOW to use its tools (which are the other agents).\n",
        "    instruction=\"\"\"You are a research coordinator. Your goal is to answer the user's query by orchestrating a workflow.\n",
        "1. First, you MUST call the `ResearchAgent` tool to find relevant information on the topic provided by the user.\n",
        "2. Next, after receiving the research findings, you MUST call the `SummarizerAgent` tool to create a concise summary.\n",
        "3. Finally, present the final summary clearly to the user as your response.\"\"\",\n",
        "    # We wrap the sub-agents in `AgentTool` to make them callable tools for the root agent.\n",
        "    tools=[AgentTool(research_agent), AgentTool(summarizer_agent)],\n",
        ")\n",
        "\n",
        "print(\"✅ root_agent created.\")"
      ],
      "metadata": {
        "id": "PKthuzRkBtHD",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:30.773871Z",
          "iopub.execute_input": "2025-11-10T21:58:30.77424Z",
          "iopub.status.idle": "2025-11-10T21:58:30.794459Z",
          "shell.execute_reply.started": "2025-11-10T21:58:30.774216Z",
          "shell.execute_reply": "2025-11-10T21:58:30.793451Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Here we're using `AgentTool` to wrap the sub-agents to make them callable tools for the root agent. We'll explore `AgentTool` in-detail on Day 2.\n",
        "\n",
        "Let's run the agent and ask it about a topic:"
      ],
      "metadata": {
        "id": "wmYMM0DbRjUR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "runner = InMemoryRunner(agent=root_agent)\n",
        "response = await runner.run_debug(\n",
        "    \"What are the latest advancements in quantum computing and what do they mean for AI?\"\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:30.795468Z",
          "iopub.execute_input": "2025-11-10T21:58:30.795789Z",
          "iopub.status.idle": "2025-11-10T21:58:38.505398Z",
          "shell.execute_reply.started": "2025-11-10T21:58:30.795758Z",
          "shell.execute_reply": "2025-11-10T21:58:38.504458Z"
        },
        "id": "e-0NZEgeRjUS"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "You've just built your first multi-agent system! You used a single \"coordinator\" agent to manage the workflow, which is a powerful and flexible pattern.\n",
        "\n",
        "‼️ However, **relying on an LLM's instructions to control the order can sometimes be unpredictable.** Next, we'll explore a different pattern that gives you guaranteed, step-by-step execution."
      ],
      "metadata": {
        "id": "xMCIHhQHRjUT"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 🚥 Section 3: Sequential Workflows - The Assembly Line\n",
        "\n",
        "**The Problem: Unpredictable Order**\n",
        "\n",
        "The previous multi-agent system worked, but it relied on a **detailed instruction prompt** to force the LLM to run steps in order. This can be unreliable. A complex LLM might decide to skip a step, run them in the wrong order, or get \"stuck,\" making the process unpredictable.\n",
        "\n",
        "**The Solution: A Fixed Pipeline**\n",
        "\n",
        "When you need tasks to happen in a **guaranteed, specific order**, you can use a `SequentialAgent`. This agent acts like an assembly line, running each sub-agent in the exact order you list them. The output of one agent automatically becomes the input for the next, creating a predictable and reliable workflow.\n",
        "\n",
        "**Use Sequential when:** Order matters, you need a linear pipeline, or each step builds on the previous one.\n",
        "\n",
        "To learn more, check out the documentation related to [sequential agents in ADK](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/).\n",
        "\n",
        "**Architecture: Blog Post Creation Pipeline**\n",
        "\n",
        "<!--\n",
        "```mermaid\n",
        "graph LR\n",
        "    A[\"User Input: Blog about AI\"] -- > B[\"Outline Agent\"]\n",
        "    B -- >|blog_outline| C[\"Writer Agent\"]\n",
        "    C -- >|blog_draft| D[\"Editor Agent\"]\n",
        "    D -- >|final_blog| E[\"Output\"]\n",
        "\n",
        "    style B fill:#ffcccc\n",
        "    style C fill:#ccffcc\n",
        "    style D fill:#ccccff\n",
        "```\n",
        "-->"
      ],
      "metadata": {
        "id": "h6Bcds7EBtHE"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img width=\"1000\" src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day1/sequential-agent.png\" alt=\"Sequential Agent\" />"
      ],
      "metadata": {
        "id": "O6G7GeCURjUT"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.1 Example: Blog Post Creation with Sequential Agents\n",
        "\n",
        "Let's build a system with three specialized agents:\n",
        "\n",
        "1. **Outline Agent** - Creates a blog outline for a given topic\n",
        "2. **Writer Agent** - Writes a blog post\n",
        "3. **Editor Agent** - Edits a blog post draft for clarity and structure"
      ],
      "metadata": {
        "id": "s88O-LHmRjUT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Outline Agent: Creates the initial blog post outline.\n",
        "outline_agent = Agent(\n",
        "    name=\"OutlineAgent\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    instruction=\"\"\"Create a blog outline for the given topic with:\n",
        "    1. A catchy headline\n",
        "    2. An introduction hook\n",
        "    3. 3-5 main sections with 2-3 bullet points for each\n",
        "    4. A concluding thought\"\"\",\n",
        "    output_key=\"blog_outline\",  # The result of this agent will be stored in the session state with this key.\n",
        ")\n",
        "\n",
        "print(\"✅ outline_agent created.\")"
      ],
      "metadata": {
        "id": "TLflGqQVBtHE",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:38.506382Z",
          "iopub.execute_input": "2025-11-10T21:58:38.506622Z",
          "iopub.status.idle": "2025-11-10T21:58:38.51214Z",
          "shell.execute_reply.started": "2025-11-10T21:58:38.506603Z",
          "shell.execute_reply": "2025-11-10T21:58:38.511168Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Writer Agent: Writes the full blog post based on the outline from the previous agent.\n",
        "writer_agent = Agent(\n",
        "    name=\"WriterAgent\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    # The `{blog_outline}` placeholder automatically injects the state value from the previous agent's output.\n",
        "    instruction=\"\"\"Following this outline strictly: {blog_outline}\n",
        "    Write a brief, 200 to 300-word blog post with an engaging and informative tone.\"\"\",\n",
        "    output_key=\"blog_draft\",  # The result of this agent will be stored with this key.\n",
        ")\n",
        "\n",
        "print(\"✅ writer_agent created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:38.513236Z",
          "iopub.execute_input": "2025-11-10T21:58:38.513506Z",
          "iopub.status.idle": "2025-11-10T21:58:38.539204Z",
          "shell.execute_reply.started": "2025-11-10T21:58:38.513485Z",
          "shell.execute_reply": "2025-11-10T21:58:38.537426Z"
        },
        "id": "EZc8jgBDRjUT"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Editor Agent: Edits and polishes the draft from the writer agent.\n",
        "editor_agent = Agent(\n",
        "    name=\"EditorAgent\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    # This agent receives the `{blog_draft}` from the writer agent's output.\n",
        "    instruction=\"\"\"Edit this draft: {blog_draft}\n",
        "    Your task is to polish the text by fixing any grammatical errors, improving the flow and sentence structure, and enhancing overall clarity.\"\"\",\n",
        "    output_key=\"final_blog\",  # This is the final output of the entire pipeline.\n",
        ")\n",
        "\n",
        "print(\"✅ editor_agent created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:38.540563Z",
          "iopub.execute_input": "2025-11-10T21:58:38.541495Z",
          "iopub.status.idle": "2025-11-10T21:58:38.561769Z",
          "shell.execute_reply.started": "2025-11-10T21:58:38.541458Z",
          "shell.execute_reply": "2025-11-10T21:58:38.560759Z"
        },
        "id": "ZET7mpHHRjUU"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Then we bring the agents together under a sequential agent, which runs the agents in the order that they are listed:"
      ],
      "metadata": {
        "id": "BpjUwVGgRjUU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "root_agent = SequentialAgent(\n",
        "    name=\"BlogPipeline\",\n",
        "    sub_agents=[outline_agent, writer_agent, editor_agent],\n",
        ")\n",
        "\n",
        "print(\"✅ Sequential Agent created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:38.562668Z",
          "iopub.execute_input": "2025-11-10T21:58:38.562933Z",
          "iopub.status.idle": "2025-11-10T21:58:38.579932Z",
          "shell.execute_reply.started": "2025-11-10T21:58:38.562912Z",
          "shell.execute_reply": "2025-11-10T21:58:38.578888Z"
        },
        "id": "DRQmJmdKRjUU"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let's run the agent and give it a topic to write a blog post about:"
      ],
      "metadata": {
        "id": "pjW1aGyoRjUU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "runner = InMemoryRunner(agent=root_agent)\n",
        "response = await runner.run_debug(\n",
        "    \"Write a blog post about the benefits of multi-agent systems for software developers\"\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:38.581021Z",
          "iopub.execute_input": "2025-11-10T21:58:38.581417Z",
          "iopub.status.idle": "2025-11-10T21:58:45.39889Z",
          "shell.execute_reply.started": "2025-11-10T21:58:38.581391Z",
          "shell.execute_reply": "2025-11-10T21:58:45.397863Z"
        },
        "id": "IsPnut4fRjUU"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "👏 Great job! You've now created a reliable \"assembly line\" using a sequential agent, where each step runs in a predictable order.\n",
        "\n",
        "**This is perfect for tasks that build on each other, but it's slow if the tasks are independent.** Next, we'll look at how to run multiple agents at the same time to speed up your workflow."
      ],
      "metadata": {
        "id": "H1SnzIwdRjUU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🛣️ Section 4: Parallel Workflows - Independent Researchers\n",
        "\n",
        "**The Problem: The Bottleneck**\n",
        "\n",
        "The previous sequential agent is great, but it's an assembly line. Each step must wait for the previous one to finish. What if you have several tasks that are **not dependent** on each other? For example, researching three *different* topics. Running them in sequence would be slow and inefficient, creating a bottleneck where each task waits unnecessarily.\n",
        "\n",
        "**The Solution: Concurrent Execution**\n",
        "\n",
        "When you have independent tasks, you can run them all at the same time using a `ParallelAgent`. This agent executes all of its sub-agents concurrently, dramatically speeding up the workflow. Once all parallel tasks are complete, you can then pass their combined results to a final 'aggregator' step.\n",
        "\n",
        "**Use Parallel when:** Tasks are independent, speed matters, and you can execute concurrently.\n",
        "\n",
        "To learn more, check out the documentation related to [parallel agents in ADK](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/).\n",
        "\n",
        "**Architecture: Multi-Topic Research**\n",
        "\n",
        "<!--\n",
        "```mermaid\n",
        "graph TD\n",
        "    A[\"User Request: Research 3 topics\"] -- > B[\"Parallel Execution\"]\n",
        "    B -- > C[\"Tech Researcher\"]\n",
        "    B -- > D[\"Health Researcher\"]\n",
        "    B -- > E[\"Finance Researcher\"]\n",
        "\n",
        "    C -- > F[\"Aggregator\"]\n",
        "    D -- > F\n",
        "    E -- > F\n",
        "    F -- > G[\"Combined Report\"]\n",
        "\n",
        "    style B fill:#ffffcc\n",
        "    style F fill:#ffccff\n",
        "```\n",
        "-->"
      ],
      "metadata": {
        "id": "U37FxKxDBtHE"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img width=\"600\" src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day1/parallel-agent.png\" alt=\"Parallel Agent\" />"
      ],
      "metadata": {
        "id": "WL9lqjBeRjUV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.1 Example: Parallel Multi-Topic Research\n",
        "\n",
        "Let's build a system with four agents:\n",
        "\n",
        "1. **Tech Researcher** - Researches AI/ML news and trends\n",
        "2. **Health Researcher** - Researches recent medical news and trends\n",
        "3. **Finance Researcher** - Researches finance and fintech news and trends\n",
        "4. **Aggregator Agent** - Combines all research findings into a single summary"
      ],
      "metadata": {
        "id": "qcE6Ct6HRjUV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Tech Researcher: Focuses on AI and ML trends.\n",
        "tech_researcher = Agent(\n",
        "    name=\"TechResearcher\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    instruction=\"\"\"Research the latest AI/ML trends. Include 3 key developments,\n",
        "the main companies involved, and the potential impact. Keep the report very concise (100 words).\"\"\",\n",
        "    tools=[google_search],\n",
        "    output_key=\"tech_research\",  # The result of this agent will be stored in the session state with this key.\n",
        ")\n",
        "\n",
        "print(\"✅ tech_researcher created.\")"
      ],
      "metadata": {
        "id": "GBhNDWZ9BtHE",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:45.400276Z",
          "iopub.execute_input": "2025-11-10T21:58:45.401389Z",
          "iopub.status.idle": "2025-11-10T21:58:45.40774Z",
          "shell.execute_reply.started": "2025-11-10T21:58:45.401361Z",
          "shell.execute_reply": "2025-11-10T21:58:45.40655Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Health Researcher: Focuses on medical breakthroughs.\n",
        "health_researcher = Agent(\n",
        "    name=\"HealthResearcher\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    instruction=\"\"\"Research recent medical breakthroughs. Include 3 significant advances,\n",
        "their practical applications, and estimated timelines. Keep the report concise (100 words).\"\"\",\n",
        "    tools=[google_search],\n",
        "    output_key=\"health_research\",  # The result will be stored with this key.\n",
        ")\n",
        "\n",
        "print(\"✅ health_researcher created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:45.408647Z",
          "iopub.execute_input": "2025-11-10T21:58:45.408918Z",
          "iopub.status.idle": "2025-11-10T21:58:45.444563Z",
          "shell.execute_reply.started": "2025-11-10T21:58:45.408898Z",
          "shell.execute_reply": "2025-11-10T21:58:45.443455Z"
        },
        "id": "-70Dr6vhRjUV"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Finance Researcher: Focuses on fintech trends.\n",
        "finance_researcher = Agent(\n",
        "    name=\"FinanceResearcher\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    instruction=\"\"\"Research current fintech trends. Include 3 key trends,\n",
        "their market implications, and the future outlook. Keep the report concise (100 words).\"\"\",\n",
        "    tools=[google_search],\n",
        "    output_key=\"finance_research\",  # The result will be stored with this key.\n",
        ")\n",
        "\n",
        "print(\"✅ finance_researcher created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:45.445614Z",
          "iopub.execute_input": "2025-11-10T21:58:45.44587Z",
          "iopub.status.idle": "2025-11-10T21:58:45.46478Z",
          "shell.execute_reply.started": "2025-11-10T21:58:45.445848Z",
          "shell.execute_reply": "2025-11-10T21:58:45.463563Z"
        },
        "id": "lhXJBv3xRjUW"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# The AggregatorAgent runs *after* the parallel step to synthesize the results.\n",
        "aggregator_agent = Agent(\n",
        "    name=\"AggregatorAgent\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    # It uses placeholders to inject the outputs from the parallel agents, which are now in the session state.\n",
        "    instruction=\"\"\"Combine these three research findings into a single executive summary:\n",
        "\n",
        "    **Technology Trends:**\n",
        "    {tech_research}\n",
        "\n",
        "    **Health Breakthroughs:**\n",
        "    {health_research}\n",
        "\n",
        "    **Finance Innovations:**\n",
        "    {finance_research}\n",
        "\n",
        "    Your summary should highlight common themes, surprising connections, and the most important key takeaways from all three reports. The final summary should be around 200 words.\"\"\",\n",
        "    output_key=\"executive_summary\",  # This will be the final output of the entire system.\n",
        ")\n",
        "\n",
        "print(\"✅ aggregator_agent created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:45.466296Z",
          "iopub.execute_input": "2025-11-10T21:58:45.466598Z",
          "iopub.status.idle": "2025-11-10T21:58:45.483708Z",
          "shell.execute_reply.started": "2025-11-10T21:58:45.466577Z",
          "shell.execute_reply": "2025-11-10T21:58:45.482729Z"
        },
        "id": "arwBoAnORjUW"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "👉 **Then we bring the agents together under a parallel agent, which is itself nested inside of a sequential agent.**\n",
        "\n",
        "This design ensures that the research agents run first in parallel, then once all of their research is complete, the aggregator agent brings together all of the research findings into a single report:"
      ],
      "metadata": {
        "id": "TSs56EupRjUX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# The ParallelAgent runs all its sub-agents simultaneously.\n",
        "parallel_research_team = ParallelAgent(\n",
        "    name=\"ParallelResearchTeam\",\n",
        "    sub_agents=[tech_researcher, health_researcher, finance_researcher],\n",
        ")\n",
        "\n",
        "# This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.\n",
        "root_agent = SequentialAgent(\n",
        "    name=\"ResearchSystem\",\n",
        "    sub_agents=[parallel_research_team, aggregator_agent],\n",
        ")\n",
        "\n",
        "print(\"✅ Parallel and Sequential Agents created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:45.484694Z",
          "iopub.execute_input": "2025-11-10T21:58:45.485001Z",
          "iopub.status.idle": "2025-11-10T21:58:45.506434Z",
          "shell.execute_reply.started": "2025-11-10T21:58:45.484948Z",
          "shell.execute_reply": "2025-11-10T21:58:45.505523Z"
        },
        "id": "Ce36W0vtRjUX"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let's run the agent and give it a prompt to research the given topics:"
      ],
      "metadata": {
        "id": "ibU683xSRjUX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "runner = InMemoryRunner(agent=root_agent)\n",
        "response = await runner.run_debug(\n",
        "    \"Run the daily executive briefing on Tech, Health, and Finance\"\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:45.507612Z",
          "iopub.execute_input": "2025-11-10T21:58:45.507892Z",
          "iopub.status.idle": "2025-11-10T21:58:51.219566Z",
          "shell.execute_reply.started": "2025-11-10T21:58:45.507872Z",
          "shell.execute_reply": "2025-11-10T21:58:51.218755Z"
        },
        "id": "klSBEmcmRjUX"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "🎉 Great! You've seen how parallel agents can dramatically speed up workflows by running independent tasks concurrently.\n",
        "\n",
        "So far, all our workflows run from start to finish and then stop. **But what if you need to review and improve an output multiple times?** Next, we'll build a workflow that can loop and refine its own work."
      ],
      "metadata": {
        "id": "zKt7diXeRjUX"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## ➰ Section 5: Loop Workflows - The Refinement Cycle\n",
        "\n",
        "**The Problem: One-Shot Quality**\n",
        "\n",
        "All the workflows we've seen so far run from start to finish. The `SequentialAgent` and `ParallelAgent` produce their final output and then stop. This 'one-shot' approach isn't good for tasks that require refinement and quality control. What if the first draft of our story is bad? We have no way to review it and ask for a rewrite.\n",
        "\n",
        "**The Solution: Iterative Refinement**\n",
        "\n",
        "When a task needs to be improved through cycles of feedback and revision, you can use a `LoopAgent`. A `LoopAgent` runs a set of sub-agents repeatedly *until a specific condition is met or a maximum number of iterations is reached.* This creates a refinement cycle, allowing the agent system to improve its own work over and over.\n",
        "\n",
        "**Use Loop when:** Iterative improvement is needed, quality refinement matters, or you need repeated cycles.\n",
        "\n",
        "To learn more, check out the documentation related to [loop agents in ADK](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/).\n",
        "\n",
        "**Architecture: Story Writing & Critique Loop**\n",
        "\n",
        "<!--\n",
        "```mermaid\n",
        "graph TD\n",
        "    A[\"Initial Prompt\"] -- > B[\"Writer Agent\"]\n",
        "    B -- >|story| C[\"Critic Agent\"]\n",
        "    C -- >|critique| D{\"Iteration < Max<br>AND<br>Not Approved?\"}\n",
        "    D -- >|Yes| B\n",
        "    D -- >|No| E[\"Final Story\"]\n",
        "\n",
        "    style B fill:#ccffcc\n",
        "    style C fill:#ffcccc\n",
        "    style D fill:#ffffcc\n",
        "```\n",
        "-->"
      ],
      "metadata": {
        "id": "fP4I3mvtBtHF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img width=\"250\" src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day1/loop-agent.png\" alt=\"Loop Agent\" />"
      ],
      "metadata": {
        "id": "Q3G2EFIwRjUX"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.1 Example: Iterative Story Refinement\n",
        "\n",
        "Let's build a system with two agents:\n",
        "\n",
        "1. **Writer Agent** - Writes a draft of a short story\n",
        "2. **Critic Agent** - Reviews and critiques the short story to suggest improvements"
      ],
      "metadata": {
        "id": "awvL-ybdRjUX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# This agent runs ONCE at the beginning to create the first draft.\n",
        "initial_writer_agent = Agent(\n",
        "    name=\"InitialWriterAgent\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    instruction=\"\"\"Based on the user's prompt, write the first draft of a short story (around 100-150 words).\n",
        "    Output only the story text, with no introduction or explanation.\"\"\",\n",
        "    output_key=\"current_story\",  # Stores the first draft in the state.\n",
        ")\n",
        "\n",
        "print(\"✅ initial_writer_agent created.\")"
      ],
      "metadata": {
        "id": "a2b8WlJoBtHF",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:51.220426Z",
          "iopub.execute_input": "2025-11-10T21:58:51.220833Z",
          "iopub.status.idle": "2025-11-10T21:58:51.226716Z",
          "shell.execute_reply.started": "2025-11-10T21:58:51.220808Z",
          "shell.execute_reply": "2025-11-10T21:58:51.22581Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# This agent's only job is to provide feedback or the approval signal. It has no tools.\n",
        "critic_agent = Agent(\n",
        "    name=\"CriticAgent\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    instruction=\"\"\"You are a constructive story critic. Review the story provided below.\n",
        "    Story: {current_story}\n",
        "\n",
        "    Evaluate the story's plot, characters, and pacing.\n",
        "    - If the story is well-written and complete, you MUST respond with the exact phrase: \"APPROVED\"\n",
        "    - Otherwise, provide 2-3 specific, actionable suggestions for improvement.\"\"\",\n",
        "    output_key=\"critique\",  # Stores the feedback in the state.\n",
        ")\n",
        "\n",
        "print(\"✅ critic_agent created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:51.227688Z",
          "iopub.execute_input": "2025-11-10T21:58:51.227948Z",
          "iopub.status.idle": "2025-11-10T21:58:51.249912Z",
          "shell.execute_reply.started": "2025-11-10T21:58:51.227921Z",
          "shell.execute_reply": "2025-11-10T21:58:51.248891Z"
        },
        "id": "GAn6kCysRjUY"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Now, we need a way for the loop to actually stop based on the critic's feedback. The `LoopAgent` itself doesn't automatically know that \"APPROVED\" means \"stop.\"\n",
        "\n",
        "We need an agent to give it an explicit signal to terminate the loop.\n",
        "\n",
        "We do this in two parts:\n",
        "\n",
        "1. A simple Python function that the `LoopAgent` understands as an \"exit\" signal.\n",
        "2. An agent that can call that function when the right condition is met.\n",
        "\n",
        "First, you'll define the `exit_loop` function:"
      ],
      "metadata": {
        "id": "wXaiHc8zRjUY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# This is the function that the RefinerAgent will call to exit the loop.\n",
        "def exit_loop():\n",
        "    \"\"\"Call this function ONLY when the critique is 'APPROVED', indicating the story is finished and no more changes are needed.\"\"\"\n",
        "    return {\"status\": \"approved\", \"message\": \"Story approved. Exiting refinement loop.\"}\n",
        "\n",
        "\n",
        "print(\"✅ exit_loop function created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:51.250925Z",
          "iopub.execute_input": "2025-11-10T21:58:51.251205Z",
          "iopub.status.idle": "2025-11-10T21:58:51.268798Z",
          "shell.execute_reply.started": "2025-11-10T21:58:51.251185Z",
          "shell.execute_reply": "2025-11-10T21:58:51.267641Z"
        },
        "id": "ht2hHJUoRjUY"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "To let an agent call this Python function, we wrap it in a `FunctionTool`. Then, we create a `RefinerAgent` that has this tool.\n",
        "\n",
        "👉 **Notice its instructions:** this agent is the \"brain\" of the loop. It reads the `{critique}` from the `CriticAgent` and decides whether to (1) call the `exit_loop` tool or (2) rewrite the story."
      ],
      "metadata": {
        "id": "qc4o75klRjUY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# This agent refines the story based on critique OR calls the exit_loop function.\n",
        "refiner_agent = Agent(\n",
        "    name=\"RefinerAgent\",\n",
        "    model=Gemini(\n",
        "        model=\"gemini-2.5-flash-lite\",\n",
        "        retry_options=retry_config\n",
        "    ),\n",
        "    instruction=\"\"\"You are a story refiner. You have a story draft and critique.\n",
        "\n",
        "    Story Draft: {current_story}\n",
        "    Critique: {critique}\n",
        "\n",
        "    Your task is to analyze the critique.\n",
        "    - IF the critique is EXACTLY \"APPROVED\", you MUST call the `exit_loop` function and nothing else.\n",
        "    - OTHERWISE, rewrite the story draft to fully incorporate the feedback from the critique.\"\"\",\n",
        "    output_key=\"current_story\",  # It overwrites the story with the new, refined version.\n",
        "    tools=[\n",
        "        FunctionTool(exit_loop)\n",
        "    ],  # The tool is now correctly initialized with the function reference.\n",
        ")\n",
        "\n",
        "print(\"✅ refiner_agent created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:51.269552Z",
          "iopub.execute_input": "2025-11-10T21:58:51.269815Z",
          "iopub.status.idle": "2025-11-10T21:58:51.288906Z",
          "shell.execute_reply.started": "2025-11-10T21:58:51.269794Z",
          "shell.execute_reply": "2025-11-10T21:58:51.288012Z"
        },
        "id": "niKi4GANRjUY"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Then we bring the agents together under a loop agent, which is itself nested inside of a sequential agent.\n",
        "\n",
        "This design ensures that the system first produces an initial story draft, then the refinement loop runs up to the specified number of `max_iterations`:"
      ],
      "metadata": {
        "id": "gG91dZIZRjUY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# The LoopAgent contains the agents that will run repeatedly: Critic -> Refiner.\n",
        "story_refinement_loop = LoopAgent(\n",
        "    name=\"StoryRefinementLoop\",\n",
        "    sub_agents=[critic_agent, refiner_agent],\n",
        "    max_iterations=2,  # Prevents infinite loops\n",
        ")\n",
        "\n",
        "# The root agent is a SequentialAgent that defines the overall workflow: Initial Write -> Refinement Loop.\n",
        "root_agent = SequentialAgent(\n",
        "    name=\"StoryPipeline\",\n",
        "    sub_agents=[initial_writer_agent, story_refinement_loop],\n",
        ")\n",
        "\n",
        "print(\"✅ Loop and Sequential Agents created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:51.289928Z",
          "iopub.execute_input": "2025-11-10T21:58:51.290631Z",
          "iopub.status.idle": "2025-11-10T21:58:51.311222Z",
          "shell.execute_reply.started": "2025-11-10T21:58:51.290599Z",
          "shell.execute_reply": "2025-11-10T21:58:51.310292Z"
        },
        "id": "o-wnRkPzRjUZ"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let's run the agent and give it a topic to write a short story about:"
      ],
      "metadata": {
        "id": "c4u2uU6TRjUZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "runner = InMemoryRunner(agent=root_agent)\n",
        "response = await runner.run_debug(\n",
        "    \"Write a short story about a lighthouse keeper who discovers a mysterious, glowing map\"\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T21:58:51.312101Z",
          "iopub.execute_input": "2025-11-10T21:58:51.312344Z",
          "iopub.status.idle": "2025-11-10T21:59:07.438561Z",
          "shell.execute_reply.started": "2025-11-10T21:58:51.312325Z",
          "shell.execute_reply": "2025-11-10T21:59:07.437011Z"
        },
        "id": "r4YIXVcLRjUZ"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "You've now implemented a loop agent, creating a sophisticated system that can iteratively review and improve its own output. This is a key pattern for ensuring high-quality results.\n",
        "\n",
        "You now have a complete toolkit of workflow patterns. Let's put it all together and review how to choose the right one for your use case."
      ],
      "metadata": {
        "id": "-P0S9jFgRjUZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## Section 6: Summary - Choosing the Right Pattern\n",
        "\n",
        "### Decision Tree: Which Workflow Pattern?\n",
        "\n",
        "<!--\n",
        "```mermaid\n",
        "graph TD\n",
        "    A{\"What kind of workflow do you need?\"} -- > B[\"Fixed Pipeline<br>(A → B → C)\"];\n",
        "    A -- > C[\"Concurrent Tasks<br>(Run A, B, C all at once)\"];\n",
        "    A -- > D[\"Iterative Refinement<br>(A ⇆ B)\"];\n",
        "    A -- > E[\"Dynamic Decisions<br>(Let the LLM decide what to do)\"];\n",
        "\n",
        "    B -- > B_S[\"Use <b>SequentialAgent</b>\"];\n",
        "    C -- > C_S[\"Use <b>ParallelAgent</b>\"];\n",
        "    D -- > D_S[\"Use <b>LoopAgent</b>\"];\n",
        "    E -- > E_S[\"Use <b>LLM Orchestrator</b><br>(Agent with other agents as tools)\"];\n",
        "\n",
        "    style B_S fill:#f9f,stroke:#333,stroke-width:2px\n",
        "    style C_S fill:#ccf,stroke:#333,stroke-width:2px\n",
        "    style D_S fill:#cff,stroke:#333,stroke-width:2px\n",
        "    style E_S fill:#cfc,stroke:#333,stroke-width:2px\n",
        "```\n",
        "-->"
      ],
      "metadata": {
        "id": "-CKnXSHWBtHF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img width=\"1000\" src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day1/agent-decision-tree.png\" alt=\"Agent Decision Tree\" />"
      ],
      "metadata": {
        "id": "ZSQK3_oNRjUZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Quick Reference Table\n",
        "\n",
        "| Pattern | When to Use | Example | Key Feature |\n",
        "|---------|-------------|---------|-------------|\n",
        "| **LLM-based (sub_agents)** | Dynamic orchestration needed | Research + Summarize | LLM decides what to call |\n",
        "| **Sequential** | Order matters, linear pipeline | Outline → Write → Edit | Deterministic order |\n",
        "| **Parallel** | Independent tasks, speed matters | Multi-topic research | Concurrent execution |\n",
        "| **Loop** | Iterative improvement needed | Writer + Critic refinement | Repeated cycles |"
      ],
      "metadata": {
        "jp-MarkdownHeadingCollapsed": true,
        "id": "zKFKCW8pRjUa"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## ✅ Congratulations! You're Now an Agent Orchestrator\n",
        "\n",
        "In this notebook, you made the leap from a single agent to a **multi-agent system**.\n",
        "\n",
        "You saw **why** a team of specialists is easier to build and debug than one \"do-it-all\" agent. Most importantly, you learned how to be the **director** of that team.\n",
        "\n",
        "You used `SequentialAgent`, `ParallelAgent`, and `LoopAgent` to create deterministic workflows, and you even used an LLM as a 'manager' to make dynamic decisions. You also mastered the \"plumbing\" by using `output_key` to pass state between agents and make them collaborative.\n",
        "\n",
        "**ℹ️ Note: No submission required!**\n",
        "\n",
        "This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "### 📚 Learn More\n",
        "\n",
        "Refer to the following documentation to learn more:\n",
        "\n",
        "- [Agents in ADK](https://google.github.io/adk-docs/agents/)\n",
        "- [Sequential Agents in ADK](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/)\n",
        "- [Parallel Agents in ADK](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/)\n",
        "- [Loop Agents in ADK](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/)\n",
        "- [Custom Agents in ADK](https://google.github.io/adk-docs/agents/custom-agents/)\n",
        "\n",
        "### 🎯 Next Steps\n",
        "\n",
        "Ready for the next challenge? Stay tuned for Day 2 notebooks where we'll learn how to create **Custom Functions, use MCP Tools** and manage **Long-Running operations!**"
      ],
      "metadata": {
        "id": "wW-gU7giRjUa"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "| Authors |\n",
        "| --- |\n",
        "| [Kristopher Overholt](https://www.linkedin.com/in/koverholt) |"
      ],
      "metadata": {
        "id": "DSjOBOjoRjUa"
      }
    }
  ]
}

---



# Log: Day_2a_Agent_Tools.txt

{
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.13",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [],
      "isInternetEnabled": false,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "##### Copyright 2025 Google LLC."
      ],
      "metadata": {
        "id": "puc3l4iNeBNT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ],
      "metadata": {
        "id": "L3P7ZeNeeBNV",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:02:52.476943Z",
          "iopub.execute_input": "2025-11-10T22:02:52.477176Z",
          "iopub.status.idle": "2025-11-10T22:02:52.482514Z",
          "shell.execute_reply.started": "2025-11-10T22:02:52.477155Z",
          "shell.execute_reply": "2025-11-10T22:02:52.481531Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 🚀 Agent Tools\n",
        "\n",
        "**Welcome to Day-2 of the Kaggle 5-day Agents course!**\n",
        "\n",
        "In Day-1, you learned how to create agents with built-in tools like Google Search. You also learned how to orchestrate multi-agent systems. Now let's unlock the full power of agent tools by building custom logic, delegating to specialist agents, and handling real-world complexities."
      ],
      "metadata": {
        "id": "tiWhZUNveBNW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🤔 Why do Agents need Tools?\n",
        "\n",
        "**The Problem**\n",
        "\n",
        "Without tools, the agent's knowledge is frozen in time — it can't access today's news or your company's inventory. It has no connection to the outside world, so the agent can't take actions for you.\n",
        "\n",
        "**The Solution:** Tools are what transform your isolated LLM into a capable agent that can actually help you get things done.\n",
        "\n",
        "In this notebook, you'll:\n",
        "\n",
        "- ✅ Turn your Python functions into Agent tools\n",
        "- ✅ Build an Agent and use it **as a tool** in another agent\n",
        "- ✅ **Build your first multi-tool agent**\n",
        "- ✅ Explore the different tool types in ADK"
      ],
      "metadata": {
        "id": "g-rxFWtXeBNW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ‼️ Please Read\n",
        "\n",
        "> ❌ **ℹ️ Note: No submission required!**\n",
        "> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n",
        "\n",
        "> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n",
        "\n",
        "**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**"
      ],
      "metadata": {
        "id": "bdCxRM5nrAAf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 📖 Get started with Kaggle Notebooks\n",
        "\n",
        "If this is your first time using Kaggle Notebooks, welcome! You can learn more about using Kaggle Notebooks [in the documentation](https://www.kaggle.com/docs/notebooks).\n",
        "\n",
        "Here's how to get started:\n",
        "\n",
        "**1. Verify Your Account (Required)**\n",
        "\n",
        "To use the Kaggle Notebooks in this course, you'll need to verify your account with a phone number.\n",
        "\n",
        "You can do this in your [Kaggle settings](https://www.kaggle.com/settings).\n",
        "\n",
        "**2. Make Your Own Copy**\n",
        "\n",
        "To run any code in this notebook, you first need your own editable copy.\n",
        "\n",
        "Click the `Copy and Edit` button in the top-right corner.\n",
        "\n",
        "![Copy and Edit button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_1.png)\n",
        "\n",
        "This creates a private copy of the notebook just for you.\n",
        "\n",
        "**3. Run Code Cells**\n",
        "\n",
        "Once you have your copy, you can run code.\n",
        "\n",
        "Click the ▶️ Run button next to any code cell to execute it.\n",
        "\n",
        "![Run cell button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_2.png)\n",
        "\n",
        "Run the cells in order from top to bottom.\n",
        "\n",
        "**4. If You Get Stuck**\n",
        "\n",
        "To restart: Select `Factory reset` from the `Run` menu.\n",
        "\n",
        "For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server."
      ],
      "metadata": {
        "id": "p72CjeQ_eBNW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ⚙️ Section 1: Setup\n",
        "\n",
        "Before we go into today's concepts, follow the steps below to set up the environment."
      ],
      "metadata": {
        "id": "HXdzUD2qeBNX"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.1: Install dependencies\n",
        "\n",
        "The Kaggle Notebooks environment includes a pre-installed version of the [google-adk](https://google.github.io/adk-docs/) library for Python and its required dependencies.\n",
        "\n",
        "To install and use ADK in your own Python development environment outside of this course, you can do so by running:\n",
        "\n",
        "```\n",
        "pip install google-adk\n",
        "```"
      ],
      "metadata": {
        "id": "vui0_EzoeBNX"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.2: Configure your Gemini API Key\n",
        "\n",
        "This notebook uses the [Gemini API](https://ai.google.dev/gemini-api/), which requires an API key.\n",
        "\n",
        "**1. Get your API key**\n",
        "\n",
        "If you don't have one already, create an [API key in Google AI Studio](https://aistudio.google.com/app/api-keys).\n",
        "\n",
        "**2. Add the key to Kaggle Secrets**\n",
        "\n",
        "Next, you will need to add your API key to your Kaggle Notebook as a Kaggle User Secret.\n",
        "\n",
        "1. In the top menu bar of the notebook editor, select `Add-ons` then `Secrets`.\n",
        "2. Create a new secret with the label `GOOGLE_API_KEY`.\n",
        "3. Paste your API key into the \"Value\" field and click \"Save\".\n",
        "4. Ensure that the checkbox next to `GOOGLE_API_KEY` is selected so that the secret is attached to the notebook.\n",
        "\n",
        "**3. Authenticate in the notebook**\n",
        "\n",
        "Run the cell below to access the `GOOGLE_API_KEY` you just saved and set it as an environment variable for the notebook to use:"
      ],
      "metadata": {
        "id": "9n9_oE6keBNX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from kaggle_secrets import UserSecretsClient\n",
        "\n",
        "try:\n",
        "    GOOGLE_API_KEY = UserSecretsClient().get_secret(\"GOOGLE_API_KEY\")\n",
        "    os.environ[\"GOOGLE_API_KEY\"] = GOOGLE_API_KEY\n",
        "    print(\"✅ Setup and authentication complete.\")\n",
        "except Exception as e:\n",
        "    print(\n",
        "        f\"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}\"\n",
        "    )"
      ],
      "metadata": {
        "id": "WovV4AKMeBNX",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:02:52.485096Z",
          "iopub.execute_input": "2025-11-10T22:02:52.485424Z",
          "iopub.status.idle": "2025-11-10T22:02:52.580833Z",
          "shell.execute_reply.started": "2025-11-10T22:02:52.485397Z",
          "shell.execute_reply": "2025-11-10T22:02:52.579878Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.3: Import ADK components\n",
        "\n",
        "Now, import the specific components you'll need from the Agent Development Kit and the Generative AI library. This keeps your code organized and ensures we have access to the necessary building blocks."
      ],
      "metadata": {
        "id": "uUFXR8XLeBNY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.genai import types\n",
        "\n",
        "from google.adk.agents import LlmAgent\n",
        "from google.adk.models.google_llm import Gemini\n",
        "from google.adk.runners import InMemoryRunner\n",
        "from google.adk.sessions import InMemorySessionService\n",
        "from google.adk.tools import google_search, AgentTool, ToolContext\n",
        "from google.adk.code_executors import BuiltInCodeExecutor\n",
        "\n",
        "print(\"✅ ADK components imported successfully.\")"
      ],
      "metadata": {
        "id": "wgM4YoF2eBNY",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:02:52.581847Z",
          "iopub.execute_input": "2025-11-10T22:02:52.582116Z",
          "iopub.status.idle": "2025-11-10T22:03:47.3717Z",
          "shell.execute_reply.started": "2025-11-10T22:02:52.582094Z",
          "shell.execute_reply": "2025-11-10T22:03:47.37027Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.4: Helper functions\n",
        "\n",
        "Helper function that prints the generated Python code and results from the code execution tool:"
      ],
      "metadata": {
        "id": "MHom6wGyrAAj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def show_python_code_and_result(response):\n",
        "    for i in range(len(response)):\n",
        "        # Check if the response contains a valid function call result from the code executor\n",
        "        if (\n",
        "            (response[i].content.parts)\n",
        "            and (response[i].content.parts[0])\n",
        "            and (response[i].content.parts[0].function_response)\n",
        "            and (response[i].content.parts[0].function_response.response)\n",
        "        ):\n",
        "            response_code = response[i].content.parts[0].function_response.response\n",
        "            if \"result\" in response_code and response_code[\"result\"] != \"```\":\n",
        "                if \"tool_code\" in response_code[\"result\"]:\n",
        "                    print(\n",
        "                        \"Generated Python Code >> \",\n",
        "                        response_code[\"result\"].replace(\"tool_code\", \"\"),\n",
        "                    )\n",
        "                else:\n",
        "                    print(\"Generated Python Response >> \", response_code[\"result\"])\n",
        "\n",
        "\n",
        "print(\"✅ Helper functions defined.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:47.372791Z",
          "iopub.execute_input": "2025-11-10T22:03:47.37469Z",
          "iopub.status.idle": "2025-11-10T22:03:47.382384Z",
          "shell.execute_reply.started": "2025-11-10T22:03:47.374657Z",
          "shell.execute_reply": "2025-11-10T22:03:47.381329Z"
        },
        "id": "-VurRkd_rAAj"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.5: Configure Retry Options\n",
        "\n",
        "When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff."
      ],
      "metadata": {
        "id": "9ElgmM3QrAAj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "retry_config = types.HttpRetryOptions(\n",
        "    attempts=5,  # Maximum retry attempts\n",
        "    exp_base=7,  # Delay multiplier\n",
        "    initial_delay=1,\n",
        "    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:47.38345Z",
          "iopub.execute_input": "2025-11-10T22:03:47.384056Z",
          "iopub.status.idle": "2025-11-10T22:03:47.417534Z",
          "shell.execute_reply.started": "2025-11-10T22:03:47.384022Z",
          "shell.execute_reply": "2025-11-10T22:03:47.416496Z"
        },
        "id": "1AP-LvZ5rAAj"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🤖 Section 2: What are Custom Tools?\n",
        "\n",
        "**Custom Tools** are tools you build yourself using your own code and business logic. Unlike built-in tools that come ready-made with ADK, custom tools give you complete control over functionality.\n",
        "\n",
        "**When to use Custom Tools?**\n",
        "\n",
        "Built-in tools like Google Search are powerful, but **every business has unique requirements** that generic tools can't handle. Custom tools let you implement your specific business logic, connect to your systems, and solve domain-specific problems. ADK provides multiple custom tool types to handle these scenarios."
      ],
      "metadata": {
        "id": "uDejCev7nz7-"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.1: Building Custom Function Tools\n",
        "\n",
        "#### Example: Currency Converter Agent\n",
        "\n",
        "This agent can convert currency from one denomination to another and calculates the fees to do the conversion. The agent has two custom tools and follows the workflow:\n",
        "\n",
        "1. **Fee Lookup Tool** - Finds transaction fees for the conversion (mock)\n",
        "2. **Exchange Rate Tool** - Gets currency conversion rates (mock)\n",
        "3. **Calculation Step** - Calculates the total conversion cost including the fees\n",
        "\n",
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day2/currency-agent.png\" width=\"600\" alt=\"Currency Converter Agent\">"
      ],
      "metadata": {
        "id": "3dxm-HcReBNY"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 🤔 2.2: How to define a Tool?\n",
        "\n",
        "**Any Python function can become an agent tool** by following these simple guidelines:\n",
        "\n",
        "1. Create a Python function\n",
        "2. Follow the best practices listed below\n",
        "3. Add your function to the agent's `tools=[]` list and ADK handles the rest automatically.\n",
        "\n",
        "\n",
        "#### 🏆 ADK Best Practices in Action\n",
        "\n",
        "Notice how our tools follow ADK best practices:\n",
        "\n",
        "**1. Dictionary Returns**: Tools return `{\"status\": \"success\", \"data\": ...}` or `{\"status\": \"error\", \"error_message\": ...}`  \n",
        "**2. Clear Docstrings**: LLMs use docstrings to understand when and how to use tools  \n",
        "**3. Type Hints**: Enable ADK to generate proper schemas (`str`, `dict`, etc.)  \n",
        "**4. Error Handling**: Structured error responses help LLMs handle failures gracefully  \n",
        "\n",
        "These patterns make your tools reliable and easy for LLMs to use correctly.\n",
        "\n",
        "👉 Let's see this in action with our first tool:"
      ],
      "metadata": {
        "id": "KEyRX5lJeBNY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Pay attention to the docstring, type hints, and return value.\n",
        "def get_fee_for_payment_method(method: str) -> dict:\n",
        "    \"\"\"Looks up the transaction fee percentage for a given payment method.\n",
        "\n",
        "    This tool simulates looking up a company's internal fee structure based on\n",
        "    the name of the payment method provided by the user.\n",
        "\n",
        "    Args:\n",
        "        method: The name of the payment method. It should be descriptive,\n",
        "                e.g., \"platinum credit card\" or \"bank transfer\".\n",
        "\n",
        "    Returns:\n",
        "        Dictionary with status and fee information.\n",
        "        Success: {\"status\": \"success\", \"fee_percentage\": 0.02}\n",
        "        Error: {\"status\": \"error\", \"error_message\": \"Payment method not found\"}\n",
        "    \"\"\"\n",
        "    # This simulates looking up a company's internal fee structure.\n",
        "    fee_database = {\n",
        "        \"platinum credit card\": 0.02,  # 2%\n",
        "        \"gold debit card\": 0.035,  # 3.5%\n",
        "        \"bank transfer\": 0.01,  # 1%\n",
        "    }\n",
        "\n",
        "    fee = fee_database.get(method.lower())\n",
        "    if fee is not None:\n",
        "        return {\"status\": \"success\", \"fee_percentage\": fee}\n",
        "    else:\n",
        "        return {\n",
        "            \"status\": \"error\",\n",
        "            \"error_message\": f\"Payment method '{method}' not found\",\n",
        "        }\n",
        "\n",
        "\n",
        "print(\"✅ Fee lookup function created\")\n",
        "print(f\"💳 Test: {get_fee_for_payment_method('platinum credit card')}\")"
      ],
      "metadata": {
        "id": "3CHwFeZ9eBNY",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:47.41856Z",
          "iopub.execute_input": "2025-11-10T22:03:47.418967Z",
          "iopub.status.idle": "2025-11-10T22:03:47.441765Z",
          "shell.execute_reply.started": "2025-11-10T22:03:47.418934Z",
          "shell.execute_reply": "2025-11-10T22:03:47.440605Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let's follow the same best practices to define our second tool `get_exchange_rate`."
      ],
      "metadata": {
        "id": "0gH4iUt0eBNY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def get_exchange_rate(base_currency: str, target_currency: str) -> dict:\n",
        "    \"\"\"Looks up and returns the exchange rate between two currencies.\n",
        "\n",
        "    Args:\n",
        "        base_currency: The ISO 4217 currency code of the currency you\n",
        "                       are converting from (e.g., \"USD\").\n",
        "        target_currency: The ISO 4217 currency code of the currency you\n",
        "                         are converting to (e.g., \"EUR\").\n",
        "\n",
        "    Returns:\n",
        "        Dictionary with status and rate information.\n",
        "        Success: {\"status\": \"success\", \"rate\": 0.93}\n",
        "        Error: {\"status\": \"error\", \"error_message\": \"Unsupported currency pair\"}\n",
        "    \"\"\"\n",
        "\n",
        "    # Static data simulating a live exchange rate API\n",
        "    # In production, this would call something like: requests.get(\"api.exchangerates.com\")\n",
        "    rate_database = {\n",
        "        \"usd\": {\n",
        "            \"eur\": 0.93,  # Euro\n",
        "            \"jpy\": 157.50,  # Japanese Yen\n",
        "            \"inr\": 83.58,  # Indian Rupee\n",
        "        }\n",
        "    }\n",
        "\n",
        "    # Input validation and processing\n",
        "    base = base_currency.lower()\n",
        "    target = target_currency.lower()\n",
        "\n",
        "    # Return structured result with status\n",
        "    rate = rate_database.get(base, {}).get(target)\n",
        "    if rate is not None:\n",
        "        return {\"status\": \"success\", \"rate\": rate}\n",
        "    else:\n",
        "        return {\n",
        "            \"status\": \"error\",\n",
        "            \"error_message\": f\"Unsupported currency pair: {base_currency}/{target_currency}\",\n",
        "        }\n",
        "\n",
        "\n",
        "print(\"✅ Exchange rate function created\")\n",
        "print(f\"💱 Test: {get_exchange_rate('USD', 'EUR')}\")"
      ],
      "metadata": {
        "id": "wxG9jnoheBNY",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:47.444354Z",
          "iopub.execute_input": "2025-11-10T22:03:47.444647Z",
          "iopub.status.idle": "2025-11-10T22:03:47.470554Z",
          "shell.execute_reply.started": "2025-11-10T22:03:47.444623Z",
          "shell.execute_reply": "2025-11-10T22:03:47.469493Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        " Now let's create our currency agent. Pay attention to how the agent's instructions reference the tools:\n",
        "\n",
        "**Key Points:**\n",
        "- The `tools=[]` list tells the agent which functions it can use\n",
        "- Instructions reference tools by their exact function names (e.g.,\n",
        "`get_fee_for_payment_method()`)\n",
        "- The agent uses these names to decide when and how to call each tool"
      ],
      "metadata": {
        "id": "Njzcw0mweBNZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Currency agent with custom function tools\n",
        "currency_agent = LlmAgent(\n",
        "    name=\"currency_agent\",\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    instruction=\"\"\"You are a smart currency conversion assistant.\n",
        "\n",
        "    For currency conversion requests:\n",
        "    1. Use `get_fee_for_payment_method()` to find transaction fees\n",
        "    2. Use `get_exchange_rate()` to get currency conversion rates\n",
        "    3. Check the \"status\" field in each tool's response for errors\n",
        "    4. Calculate the final amount after fees based on the output from `get_fee_for_payment_method` and `get_exchange_rate` methods and provide a clear breakdown.\n",
        "    5. First, state the final converted amount.\n",
        "        Then, explain how you got that result by showing the intermediate amounts. Your explanation must include: the fee percentage and its\n",
        "        value in the original currency, the amount remaining after the fee, and the exchange rate used for the final conversion.\n",
        "\n",
        "    If any tool returns status \"error\", explain the issue to the user clearly.\n",
        "    \"\"\",\n",
        "    tools=[get_fee_for_payment_method, get_exchange_rate],\n",
        ")\n",
        "\n",
        "print(\"✅ Currency agent created with custom function tools\")\n",
        "print(\"🔧 Available tools:\")\n",
        "print(\"  • get_fee_for_payment_method - Looks up company fee structure\")\n",
        "print(\"  • get_exchange_rate - Gets current exchange rates\")"
      ],
      "metadata": {
        "id": "g1T26bReeBNZ",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:47.47164Z",
          "iopub.execute_input": "2025-11-10T22:03:47.472028Z",
          "iopub.status.idle": "2025-11-10T22:03:47.500597Z",
          "shell.execute_reply.started": "2025-11-10T22:03:47.471994Z",
          "shell.execute_reply": "2025-11-10T22:03:47.49941Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Test the currency agent\n",
        "currency_runner = InMemoryRunner(agent=currency_agent)\n",
        "_ = await currency_runner.run_debug(\n",
        "    \"I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?\"\n",
        ")"
      ],
      "metadata": {
        "id": "pUmOpHKceBNZ",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:47.501742Z",
          "iopub.execute_input": "2025-11-10T22:03:47.502142Z",
          "iopub.status.idle": "2025-11-10T22:03:50.613626Z",
          "shell.execute_reply.started": "2025-11-10T22:03:47.502086Z",
          "shell.execute_reply": "2025-11-10T22:03:50.61262Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Excellent!** Our agent now uses custom business logic with structured responses.\n",
        "\n",
        "## 💻 Section 3: Improving Agent Reliability with Code\n",
        "\n",
        "The agent's instruction says *\"calculate the final amount after fees\"* but LLMs aren't always reliable at math. They might make calculation errors or use inconsistent formulas.\n",
        "\n",
        "##### 💡 **Solution:** Let's ask our agent to generate a Python code to do the math, and run it to give us the final result! Code execution is much more reliable than having the LLM try to do math in its head!"
      ],
      "metadata": {
        "id": "knpMAIfdeBNZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day2/enhanced-currency-agent.png\" width=\"800\" alt=\"Enhanced Currency Converter Agent\">"
      ],
      "metadata": {
        "id": "2UD7GgqzeBNZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.1 Built-in Code Executor\n",
        "\n",
        "ADK has a built-in Code Executor capable of running code in a sandbox. **Note:** This uses Gemini's Code Execution capability.\n",
        "\n",
        "Let's create a `calculation_agent` which takes in a Python code and uses the `BuiltInCodeExecutor` to run it."
      ],
      "metadata": {
        "id": "82irqcTTeBNZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "calculation_agent = LlmAgent(\n",
        "    name=\"CalculationAgent\",\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    instruction=\"\"\"You are a specialized calculator that ONLY responds with Python code. You are forbidden from providing any text, explanations, or conversational responses.\n",
        "\n",
        "     Your task is to take a request for a calculation and translate it into a single block of Python code that calculates the answer.\n",
        "\n",
        "     **RULES:**\n",
        "    1.  Your output MUST be ONLY a Python code block.\n",
        "    2.  Do NOT write any text before or after the code block.\n",
        "    3.  The Python code MUST calculate the result.\n",
        "    4.  The Python code MUST print the final result to stdout.\n",
        "    5.  You are PROHIBITED from performing the calculation yourself. Your only job is to generate the code that will perform the calculation.\n",
        "\n",
        "    Failure to follow these rules will result in an error.\n",
        "       \"\"\",\n",
        "    code_executor=BuiltInCodeExecutor(),  # Use the built-in Code Executor Tool. This gives the agent code execution capabilities\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:50.614476Z",
          "iopub.execute_input": "2025-11-10T22:03:50.614726Z",
          "iopub.status.idle": "2025-11-10T22:03:50.621179Z",
          "shell.execute_reply.started": "2025-11-10T22:03:50.614707Z",
          "shell.execute_reply": "2025-11-10T22:03:50.619909Z"
        },
        "id": "8vrFXe6lrAAm"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.2: Update the Agent's instruction and toolset\n",
        "\n",
        "We'll do two key actions:\n",
        "\n",
        "1. **Update the `currency_agent`'s instructions to generate Python code**\n",
        "- Original: \"*Calculate the final amount after fees*\" (vague math instructions)\n",
        "- Enhanced: \"*Generate a Python code to calculate the final amount .. and use the `calculation_agent` to run the code and compute final amount*\"\n",
        "\n",
        "2. **Add the `calculation_agent` to the toolset**\n",
        "\n",
        "    ADK lets you use any agent as a tool using `AgentTool`.\n",
        "\n",
        "- Add `AgentTool(agent=calculation_agent)` to the tools list\n",
        "- The specialist agent appears as a callable tool to the root agent\n",
        "\n",
        "Let's see this in action:"
      ],
      "metadata": {
        "id": "ec3RvyoveBNZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "enhanced_currency_agent = LlmAgent(\n",
        "    name=\"enhanced_currency_agent\",\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    # Updated instruction\n",
        "    instruction=\"\"\"You are a smart currency conversion assistant. You must strictly follow these steps and use the available tools.\n",
        "\n",
        "  For any currency conversion request:\n",
        "\n",
        "   1. Get Transaction Fee: Use the get_fee_for_payment_method() tool to determine the transaction fee.\n",
        "   2. Get Exchange Rate: Use the get_exchange_rate() tool to get the currency conversion rate.\n",
        "   3. Error Check: After each tool call, you must check the \"status\" field in the response. If the status is \"error\", you must stop and clearly explain the issue to the user.\n",
        "   4. Calculate Final Amount (CRITICAL): You are strictly prohibited from performing any arithmetic calculations yourself. You must use the calculation_agent tool to generate Python code that calculates the final converted amount. This\n",
        "      code will use the fee information from step 1 and the exchange rate from step 2.\n",
        "   5. Provide Detailed Breakdown: In your summary, you must:\n",
        "       * State the final converted amount.\n",
        "       * Explain how the result was calculated, including:\n",
        "           * The fee percentage and the fee amount in the original currency.\n",
        "           * The amount remaining after deducting the fee.\n",
        "           * The exchange rate applied.\n",
        "    \"\"\",\n",
        "    tools=[\n",
        "        get_fee_for_payment_method,\n",
        "        get_exchange_rate,\n",
        "        AgentTool(agent=calculation_agent),  # Using another agent as a tool!\n",
        "    ],\n",
        ")\n",
        "\n",
        "print(\"✅ Enhanced currency agent created\")\n",
        "print(\"🎯 New capability: Delegates calculations to specialist agent\")\n",
        "print(\"🔧 Tool types used:\")\n",
        "print(\"  • Function Tools (fees, rates)\")\n",
        "print(\"  • Agent Tool (calculation specialist)\")"
      ],
      "metadata": {
        "id": "MwpLqjEmeBNZ",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:50.622591Z",
          "iopub.execute_input": "2025-11-10T22:03:50.622899Z",
          "iopub.status.idle": "2025-11-10T22:03:50.672163Z",
          "shell.execute_reply.started": "2025-11-10T22:03:50.622872Z",
          "shell.execute_reply": "2025-11-10T22:03:50.670906Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Define a runner\n",
        "enhanced_runner = InMemoryRunner(agent=enhanced_currency_agent)"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:50.673409Z",
          "iopub.execute_input": "2025-11-10T22:03:50.673652Z",
          "iopub.status.idle": "2025-11-10T22:03:50.705501Z",
          "shell.execute_reply.started": "2025-11-10T22:03:50.673621Z",
          "shell.execute_reply": "2025-11-10T22:03:50.704473Z"
        },
        "id": "NmkxmhAcrAAm"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Test the enhanced agent\n",
        "response = await enhanced_runner.run_debug(\n",
        "    \"Convert 1,250 USD to INR using a Bank Transfer. Show me the precise calculation.\"\n",
        ")"
      ],
      "metadata": {
        "id": "a3obf58AeBNZ",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:50.70669Z",
          "iopub.execute_input": "2025-11-10T22:03:50.707056Z",
          "iopub.status.idle": "2025-11-10T22:03:55.237573Z",
          "shell.execute_reply.started": "2025-11-10T22:03:50.707026Z",
          "shell.execute_reply": "2025-11-10T22:03:55.236477Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Excellent!** Notice what happened:\n",
        "\n",
        "- When the Currency agent calls the `CalculationAgent`, it passes in the generated Python code\n",
        "- The `CalculationAgent` in turn used the `BuiltInCodeExecutor` to run the code and gave us precise calculations instead of LLM guesswork!\n",
        "\n",
        "Now you can inspect the parts of the response that either generated Python code or that contain the Python code results, using the helper function that was defined near the beginning of this notebook:"
      ],
      "metadata": {
        "id": "lUj4Pi7reBNZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "show_python_code_and_result(response)"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:55.238886Z",
          "iopub.execute_input": "2025-11-10T22:03:55.239171Z",
          "iopub.status.idle": "2025-11-10T22:03:55.243913Z",
          "shell.execute_reply.started": "2025-11-10T22:03:55.239138Z",
          "shell.execute_reply": "2025-11-10T22:03:55.243001Z"
        },
        "id": "qKENQ2adrAAn"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 🤔 3.3: Agent Tools vs Sub-Agents: What's the Difference?\n",
        "\n",
        "This is a common question! Both involve using multiple agents, but they work very differently:\n",
        "\n",
        "**Agent Tools (what we're using):**\n",
        "- Agent A calls Agent B as a tool\n",
        "- Agent B's response goes **back to Agent A**\n",
        "- Agent A stays in control and continues the conversation\n",
        "- **Use case**: Delegation for specific tasks (like calculations)\n",
        "\n",
        "**Sub-Agents (different pattern):**\n",
        "- Agent A transfers control **completely to Agent B**\n",
        "- Agent B takes over and handles all future user input\n",
        "- Agent A is out of the loop\n",
        "- **Use case**: Handoff to specialists (like customer support tiers)\n",
        "\n",
        "**In our currency example:** We want the currency agent to get calculation results and continue working with them, so we use **Agent Tools**, not sub-agents."
      ],
      "metadata": {
        "id": "NuIzDxfGeBNZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🧰 Section 4: Complete Guide to ADK Tool Types\n",
        "\n",
        "Now that you've seen tools in action, let's understand the complete ADK toolkit:\n",
        "\n",
        "It's broadly divided into two categories: **Custom tools** and **Built-in tools**"
      ],
      "metadata": {
        "id": "x06SZdbLeBNd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **1. Custom Tools**"
      ],
      "metadata": {
        "id": "XwyjCs6WeBNd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day2/custom-tools.png\" width=\"800\" alt=\"Custom Tools\">"
      ],
      "metadata": {
        "id": "7VXdPTNKeBNd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**What**: Tools you build yourself for specific needs\n",
        "\n",
        "**Advantage**: Complete control over functionality — you build exactly what your agent needs\n",
        "\n",
        "#### **Function Tools** ✅ (You've used these!)\n",
        "- **What**: Python functions converted to agent tools\n",
        "- **Examples**: `get_fee_for_payment_method`, `get_exchange_rate`\n",
        "- **Advantage**: Turn any Python function into an agent tool instantly\n",
        "\n",
        "#### **Long Running Function Tools**\n",
        "- **What**: Functions for operations that take significant time\n",
        "- **Examples**: Human-in-the-loop approvals, file processing\n",
        "- **Advantage**: Agents can start tasks and continue with other work while waiting\n",
        "\n",
        "#### **Agent Tools** ✅ (You've used these!)\n",
        "- **What**: Other agents used as tools\n",
        "- **Examples**: `AgentTool(agent=calculation_agent)`\n",
        "- **Advantage**: Build specialist agents and reuse them across different systems\n",
        "\n",
        "#### **MCP Tools**\n",
        "- **What**: Tools from Model Context Protocol servers\n",
        "- **Examples**: Filesystem access, Google Maps, databases\n",
        "- **Advantage**: Connect to any MCP-compatible service without custom integration\n",
        "\n",
        "#### **OpenAPI Tools**\n",
        "- **What**: Tools automatically generated from API specifications\n",
        "- **Examples**: REST API endpoints become callable tools\n",
        "- **Advantage**: No manual coding — just provide an API spec and get working tools"
      ],
      "metadata": {
        "id": "HSfE3z6PeBNd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **2. Built-in Tools**"
      ],
      "metadata": {
        "id": "PjyNlyXEeBNd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day2/built-in-tools.png\" width=\"1200\" alt=\"Built-in Tools\">"
      ],
      "metadata": {
        "id": "kumnP6uKeBNd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**What**: Pre-built tools provided by ADK\n",
        "\n",
        "**Advantage**: No development time — use immediately with zero setup\n",
        "\n",
        "#### **Gemini Tools** ✅ (You've used these!)\n",
        "- **What**: Tools that leverage Gemini's capabilities\n",
        "- **Examples**: `google_search`, `BuiltInCodeExecutor`\n",
        "- **Advantage**: Reliable, tested tools that work out of the box\n",
        "\n",
        "#### **Google Cloud Tools** [needs Google Cloud access]\n",
        "- **What**: Tools for Google Cloud services and enterprise integration\n",
        "- **Examples**: `BigQueryToolset`, `SpannerToolset`, `APIHubToolset`\n",
        "- **Advantage**: Enterprise-grade database and API access with built-in security\n",
        "\n",
        "#### **Third-party Tools**\n",
        "- **What**: Wrappers for existing tool ecosystems\n",
        "- **Examples**: Hugging Face, Firecrawl, GitHub Tools\n",
        "- **Advantage**: Reuse existing tool investments — no need to rebuild what already exists"
      ],
      "metadata": {
        "id": "bgwc5LlzeBNd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ✅ Congratulations!\n",
        "\n",
        "You've successfully learned how to build agents that go beyond simple responses to take\n",
        "intelligent actions with custom tools. In this notebook, you learned:\n",
        "\n",
        "1. 🔧 **Function Tools** - Converted Python functions into agent tools\n",
        "2. 🤖 **Agent Tools** - Created specialist agents and used them as tools\n",
        "3. 🧰 **Complete Toolkit** - Explored all ADK tool types and when to use them\n",
        "\n",
        "**ℹ️ Note: No submission required!**\n",
        "\n",
        "This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "### 📚 Learn More\n",
        "\n",
        "Refer to the following documentation to learn more:\n",
        "\n",
        "- [ADK Documentation](https://google.github.io/adk-docs/)\n",
        "- [ADK Tools Documentation](https://google.github.io/adk-docs/tools/)\n",
        "- [ADK Custom Tools Guide](https://google.github.io/adk-docs/tools-custom/)\n",
        "- [ADK Function Tools](https://google.github.io/adk-docs/tools/function-tools/)\n",
        "- [ADK Plugins Overview](https://google.github.io/adk-docs/plugins/)\n",
        "\n",
        "### 🎯 Next Steps\n",
        "\n",
        "You've built the foundation of agent tool mastery.\n",
        "\n",
        "Ready for the next challenge? Continue to the next notebook to learn about **tool patterns**!"
      ],
      "metadata": {
        "id": "bMi40HWceBNd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<div align=\"center\">\n",
        "  <table>\n",
        "    <tr>\n",
        "      <th style=\"text-align:center\">Authors</th>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <td style=\"text-align:center\"><a href=\"https://www.linkedin.com/in/laxmi-harikumar/\">Laxmi Harikumar</a></td>\n",
        "    </tr>\n",
        "  </table>\n",
        "</div>"
      ],
      "metadata": {
        "id": "st95YA0ieBNd"
      }
    }
  ]
}

---



# Log: Day_2b_Agent_Tools_Best_Practices.txt

{
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.13",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [],
      "isInternetEnabled": true,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "##### Copyright 2025 Google LLC."
      ],
      "metadata": {
        "id": "pCc2m_VLpwG6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ],
      "metadata": {
        "id": "lrOWWTiepwG8",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-11T00:34:23.961776Z",
          "iopub.execute_input": "2025-11-11T00:34:23.96204Z",
          "iopub.status.idle": "2025-11-11T00:34:23.967154Z",
          "shell.execute_reply.started": "2025-11-11T00:34:23.962017Z",
          "shell.execute_reply": "2025-11-11T00:34:23.966273Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 🚀 Agent Tool Patterns and Best Practices\n",
        "\n",
        "**Welcome to Day-2 of the Kaggle 5-day Agents course!**\n",
        "\n",
        "In the previous notebook, you learned how to add custom Python functions as tools to your agent. In this notebook, we'll take the next step: **consuming external MCP services** and handling **long-running operations**.\n",
        "\n",
        "In this notebook, you'll learn how to:\n",
        "\n",
        "- ✅ **Connect to external MCP servers**\n",
        "- ✅ **Implement long-running operations** that can pause agent execution for external input\n",
        "- ✅ **Build resumable workflows** that maintain state across conversation breaks\n",
        "- ✅ Understand when and how to use these patterns"
      ],
      "metadata": {
        "id": "jP-yDdNYpwG8"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ‼️ Please Read\n",
        "\n",
        "> ❌ **ℹ️ Note: No submission required!**\n",
        "> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n",
        "\n",
        "> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n",
        "\n",
        "**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**"
      ],
      "metadata": {
        "id": "oA2oGhrBrnQZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 📖 Get started with Kaggle Notebooks\n",
        "\n",
        "If this is your first time using Kaggle Notebooks, welcome! You can learn more about using Kaggle Notebooks [in the documentation](https://www.kaggle.com/docs/notebooks).\n",
        "\n",
        "Here's how to get started:\n",
        "\n",
        "**1. Verify Your Account (Required)**\n",
        "\n",
        "To use the Kaggle Notebooks in this course, you'll need to verify your account with a phone number.\n",
        "\n",
        "You can do this in your [Kaggle settings](https://www.kaggle.com/settings).\n",
        "\n",
        "**2. Make Your Own Copy**\n",
        "\n",
        "To run any code in this notebook, you first need your own editable copy.\n",
        "\n",
        "Click the `Copy and Edit` button in the top-right corner.\n",
        "\n",
        "![Copy and Edit button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_1.png)\n",
        "\n",
        "This creates a private copy of the notebook just for you.\n",
        "\n",
        "**3. Run Code Cells**\n",
        "\n",
        "Once you have your copy, you can run code.\n",
        "\n",
        "Click the ▶️ Run button next to any code cell to execute it.\n",
        "\n",
        "![Run cell button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_2.png)\n",
        "\n",
        "Run the cells in order from top to bottom.\n",
        "\n",
        "**4. If You Get Stuck**\n",
        "\n",
        "To restart: Select `Factory reset` from the `Run` menu.\n",
        "\n",
        "For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server."
      ],
      "metadata": {
        "id": "CmgQuX0FpwG9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## ⚙️ Section 1: Setup\n",
        "\n",
        "### 1.1: Install dependencies\n",
        "\n",
        "The Kaggle Notebooks environment includes a pre-installed version of the [google-adk](https://google.github.io/adk-docs/) library for Python and its required dependencies.\n",
        "\n",
        "To install and use ADK in your own Python development environment outside of this course, you can do so by running:\n",
        "\n",
        "```\n",
        "pip install google-adk\n",
        "```"
      ],
      "metadata": {
        "id": "1eIDMHeSpwG9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.2: Configure your Gemini API Key\n",
        "\n",
        "This notebook uses the [Gemini API](https://ai.google.dev/gemini-api/), which requires an API key.\n",
        "\n",
        "**1. Get your API key**\n",
        "\n",
        "If you don't have one already, create an [API key in Google AI Studio](https://aistudio.google.com/app/api-keys).\n",
        "\n",
        "**2. Add the key to Kaggle Secrets**\n",
        "\n",
        "Next, you will need to add your API key to your Kaggle Notebook as a Kaggle User Secret.\n",
        "\n",
        "1. In the top menu bar of the notebook editor, select `Add-ons` then `Secrets`.\n",
        "2. Create a new secret with the label `GOOGLE_API_KEY`.\n",
        "3. Paste your API key into the \"Value\" field and click \"Save\".\n",
        "4. Ensure that the checkbox next to `GOOGLE_API_KEY` is selected so that the secret is attached to the notebook.\n",
        "\n",
        "**3. Authenticate in the notebook**\n",
        "\n",
        "Run the cell below to access the `GOOGLE_API_KEY` you just saved and set it as an environment variable for the notebook to use:"
      ],
      "metadata": {
        "id": "mkYnp2HrpwG9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from kaggle_secrets import UserSecretsClient\n",
        "\n",
        "try:\n",
        "    GOOGLE_API_KEY = UserSecretsClient().get_secret(\"GOOGLE_API_KEY\")\n",
        "    os.environ[\"GOOGLE_API_KEY\"] = GOOGLE_API_KEY\n",
        "    print(\"✅ Setup and authentication complete.\")\n",
        "except Exception as e:\n",
        "    print(\n",
        "        f\"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}\"\n",
        "    )"
      ],
      "metadata": {
        "id": "X4ge5O5LpwG9",
        "outputId": "e979fed9-ec85-4d7d-da4b-4b92464e880f",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-11T00:35:19.085552Z",
          "iopub.execute_input": "2025-11-11T00:35:19.085991Z",
          "iopub.status.idle": "2025-11-11T00:35:19.153728Z",
          "shell.execute_reply.started": "2025-11-11T00:35:19.085964Z",
          "shell.execute_reply": "2025-11-11T00:35:19.152866Z"
        }
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Setup and authentication complete.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.3: Import ADK components\n",
        "\n",
        "Now, import the specific components you'll need from the Agent Development Kit. This keeps your code organized and ensures we have access to the necessary building blocks."
      ],
      "metadata": {
        "id": "KfKu1N7LpwG-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import uuid\n",
        "from google.genai import types\n",
        "\n",
        "from google.adk.agents import LlmAgent\n",
        "from google.adk.models.google_llm import Gemini\n",
        "from google.adk.runners import Runner\n",
        "from google.adk.sessions import InMemorySessionService\n",
        "\n",
        "from google.adk.tools.mcp_tool.mcp_toolset import McpToolset\n",
        "from google.adk.tools.tool_context import ToolContext\n",
        "from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams\n",
        "from mcp import StdioServerParameters\n",
        "\n",
        "from google.adk.apps.app import App, ResumabilityConfig\n",
        "from google.adk.tools.function_tool import FunctionTool\n",
        "\n",
        "print(\"✅ ADK components imported successfully.\")"
      ],
      "metadata": {
        "id": "QyMjY5_ApwG-",
        "outputId": "e4bd7298-2e43-486c-ed1b-5d76a46a7225",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-11T00:40:10.518015Z",
          "iopub.execute_input": "2025-11-11T00:40:10.518958Z",
          "iopub.status.idle": "2025-11-11T00:41:00.535879Z",
          "shell.execute_reply.started": "2025-11-11T00:40:10.518922Z",
          "shell.execute_reply": "2025-11-11T00:41:00.534923Z"
        }
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ ADK components imported successfully.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.4: Configure Retry Options\n",
        "\n",
        "When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff."
      ],
      "metadata": {
        "id": "pVlUyDefrnQc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "retry_config = types.HttpRetryOptions(\n",
        "    attempts=5,  # Maximum retry attempts\n",
        "    exp_base=7,  # Delay multiplier\n",
        "    initial_delay=1,\n",
        "    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:46.701027Z",
          "iopub.execute_input": "2025-11-10T22:03:46.702445Z",
          "iopub.status.idle": "2025-11-10T22:03:46.707574Z",
          "shell.execute_reply.started": "2025-11-10T22:03:46.702416Z",
          "shell.execute_reply": "2025-11-10T22:03:46.706674Z"
        },
        "id": "G1L8-RQOrnQc"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🧰 Section 2: Model Context Protocol\n",
        "\n",
        "So far, you have learned how to create custom functions for your agents. But connecting to external systems (GitHub, databases, Slack) requires writing and maintaining API clients.\n",
        "\n",
        "**Model Context Protocol (MCP)** is an open standard that lets agents use community-built integrations. Instead of writing your own integrations and API clients, just connect to an existing MCP server.\n",
        "\n",
        "MCP enables agents to:\n",
        "\n",
        "✅ **Access live, external data** from databases, APIs, and services without custom integration code  \n",
        "✅ **Leverage community-built tools** with standardized interfaces  \n",
        "✅ **Scale capabilities** by connecting to multiple specialized servers"
      ],
      "metadata": {
        "id": "97RRe_Q8pwG_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.1: How MCP Works\n",
        "\n",
        "MCP connects your agent (the **client**) to external **MCP servers** that provide tools:\n",
        "\n",
        "- **MCP Server**: Provides specific tools (like image generation, database access)\n",
        "- **MCP Client**: Your agent that uses those tools\n",
        "- **All servers work the same way** - standardized interface\n",
        "\n",
        "**Architecture:**\n",
        "```\n",
        "┌──────────────────┐\n",
        "│   Your Agent     │\n",
        "│   (MCP Client)   │\n",
        "└────────┬─────────┘\n",
        "         │\n",
        "         │ Standard MCP Protocol\n",
        "         │\n",
        "    ┌────┴────┬────────┬────────┐\n",
        "    │         │        │        │\n",
        "    ▼         ▼        ▼        ▼\n",
        "┌────────┐ ┌─────┐ ┌──────┐ ┌─────┐\n",
        "│ GitHub │ │Slack│ │ Maps │ │ ... │\n",
        "│ Server │ │ MCP │ │ MCP  │ │     │\n",
        "└────────┘ └─────┘ └──────┘ └─────┘\n",
        "```"
      ],
      "metadata": {
        "id": "zVvwyGpupwG_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.2: Using MCP with Your Agent\n",
        "\n",
        "The workflow is simple:\n",
        "\n",
        "1. Choose an MCP Server and tool\n",
        "2. Create the MCP Toolset (configure connection)\n",
        "3. Add it to your agent\n",
        "4. Run and test the agent"
      ],
      "metadata": {
        "id": "_-yvhZHhrnQd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Step 1: Choose MCP Server**\n",
        "\n",
        "For this demo, we'll use the **[Everything MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/everything)** - an npm package (`@modelcontextprotocol/server-everything`) designed for testing MCP integrations.\n",
        "\n",
        "It provides a `getTinyImage` tool that returns a simple test image (16x16 pixels, Base64-encoded). **Find more servers:** [modelcontextprotocol.io/examples](https://modelcontextprotocol.io/examples)\n",
        "\n",
        "**‼️ NOTE: This is a demo server to learn MCP.** In production, you'll use servers for Google Maps, Slack, Discord, etc."
      ],
      "metadata": {
        "id": "53QhJFhQpwG_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Step 2: Create the MCP Toolset**\n",
        "\n",
        "The `McpToolset` is used to integrate an ADK Agent with an MCP Server.\n",
        "\n",
        "**What the code does:**\n",
        "- Uses `npx` (Node package runner) to run the MCP server\n",
        "- Connects to `@modelcontextprotocol/server-everything`\n",
        "- Filters to only use the `getTinyImage` tool (the server has others, but we only need this one)"
      ],
      "metadata": {
        "id": "Re7QewzCrnQe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# MCP integration with Everything Server\n",
        "mcp_image_server = McpToolset(\n",
        "    connection_params=StdioConnectionParams(\n",
        "        server_params=StdioServerParameters(\n",
        "            command=\"npx\",  # Run MCP server via npx\n",
        "            args=[\n",
        "                \"-y\",  # Argument for npx to auto-confirm install\n",
        "                \"@modelcontextprotocol/server-everything\",\n",
        "            ],\n",
        "            tool_filter=[\"getTinyImage\"],\n",
        "        ),\n",
        "        timeout=30,\n",
        "    )\n",
        ")\n",
        "\n",
        "print(\"✅ MCP Tool created\")"
      ],
      "metadata": {
        "id": "esU6sWB6pwG_",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:46.708736Z",
          "iopub.execute_input": "2025-11-10T22:03:46.709078Z",
          "iopub.status.idle": "2025-11-10T22:03:46.792206Z",
          "shell.execute_reply.started": "2025-11-10T22:03:46.709046Z",
          "shell.execute_reply": "2025-11-10T22:03:46.791087Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### **Behind the scenes:**\n",
        "1. **Server Launch**: ADK runs `npx -y @modelcontextprotocol/server-everything`\n",
        "2. **Handshake**: Establishes stdio communication channel\n",
        "3. **Tool Discovery**: Server tells ADK: \"I provide getTinyImage\" functionality\n",
        "4. **Integration**: Tools appear in agent's tool list automatically\n",
        "5. **Execution**: When agent calls `getTinyImage()`, ADK forwards to MCP server\n",
        "6. **Response**: Server result is returned to agent seamlessly\n",
        "\n",
        "**Why This Matters**: You get instant access to tools without writing integration code!"
      ],
      "metadata": {
        "id": "vmrFoVP-pwG_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Step 3: Add MCP tool to agent**\n",
        "\n",
        "Let's add the `mcp_server` to the agent's tool array and update the agent's instructions to handle requests to generate tiny images."
      ],
      "metadata": {
        "id": "xyE_Ku-jpwG_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Create image agent with MCP integration\n",
        "image_agent = LlmAgent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"image_agent\",\n",
        "    instruction=\"Use the MCP Tool to generate images for user queries\",\n",
        "    tools=[mcp_image_server],\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:46.795147Z",
          "iopub.execute_input": "2025-11-10T22:03:46.795436Z",
          "iopub.status.idle": "2025-11-10T22:03:46.821551Z",
          "shell.execute_reply.started": "2025-11-10T22:03:46.795412Z",
          "shell.execute_reply": "2025-11-10T22:03:46.820718Z"
        },
        "id": "wnfOtVxYrnQe"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create the runner:"
      ],
      "metadata": {
        "id": "fih9wpzyrnQf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.adk.runners import InMemoryRunner\n",
        "\n",
        "runner = InMemoryRunner(agent=image_agent)"
      ],
      "metadata": {
        "id": "YIgCK2ArpwG_",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:46.822512Z",
          "iopub.execute_input": "2025-11-10T22:03:46.822824Z",
          "iopub.status.idle": "2025-11-10T22:03:46.843042Z",
          "shell.execute_reply.started": "2025-11-10T22:03:46.822802Z",
          "shell.execute_reply": "2025-11-10T22:03:46.842108Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Step 4: Test the agent**\n",
        "\n",
        "Ask the agent to generate an image. Watch it use the MCP tool:"
      ],
      "metadata": {
        "id": "Ub3Eq2kQpwG_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "response = await runner.run_debug(\"Provide a sample tiny image\", verbose=True)"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:46.843947Z",
          "iopub.execute_input": "2025-11-10T22:03:46.844202Z",
          "iopub.status.idle": "2025-11-10T22:03:56.75131Z",
          "shell.execute_reply.started": "2025-11-10T22:03:46.84418Z",
          "shell.execute_reply": "2025-11-10T22:03:56.750297Z"
        },
        "id": "fk8fTPUKrnQf"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Display the image:**\n",
        "\n",
        "The server returns base64-encoded image data. Let's decode and display it:"
      ],
      "metadata": {
        "id": "wJ9DXI3FrnQf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from IPython.display import display, Image as IPImage\n",
        "import base64\n",
        "\n",
        "for event in response:\n",
        "    if event.content and event.content.parts:\n",
        "        for part in event.content.parts:\n",
        "            if hasattr(part, \"function_response\") and part.function_response:\n",
        "                for item in part.function_response.response.get(\"content\", []):\n",
        "                    if item.get(\"type\") == \"image\":\n",
        "                        display(IPImage(data=base64.b64decode(item[\"data\"])))"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:56.752352Z",
          "iopub.execute_input": "2025-11-10T22:03:56.752723Z",
          "iopub.status.idle": "2025-11-10T22:03:56.761727Z",
          "shell.execute_reply.started": "2025-11-10T22:03:56.752693Z",
          "shell.execute_reply": "2025-11-10T22:03:56.760771Z"
        },
        "id": "6HLzJ-idrnQg"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.3: Extending to Other MCP Servers\n",
        "\n",
        "The same pattern works for any MCP server - only the `connection_params` change. Here are some examples:\n",
        "\n",
        "#### **👉 Kaggle MCP Server** - For dataset and notebook operations\n",
        "\n",
        "Kaggle provides an MCP server that lets your agents interact with Kaggle datasets, notebooks, and competitions.\n",
        "\n",
        "**Connection example:**\n",
        "```python\n",
        "McpToolset(\n",
        "    connection_params=StdioConnectionParams(\n",
        "        server_params=StdioServerParameters(\n",
        "            command='npx',\n",
        "            args=[\n",
        "                '-y',\n",
        "                'mcp-remote',\n",
        "                'https://www.kaggle.com/mcp'\n",
        "            ],\n",
        "        ),\n",
        "        timeout=30,\n",
        "    )\n",
        ")\n",
        "```\n",
        "\n",
        "**What it provides:**\n",
        "- 📊 Search and download Kaggle datasets\n",
        "- 📓 Access notebook metadata\n",
        "- 🏆 Query competition information etc.,\n",
        "\n",
        "**Learn more:** [Kaggle MCP Documentation](https://www.kaggle.com/docs/mcp)"
      ],
      "metadata": {
        "id": "h40LoJkxrnQg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### **👉 GitHub MCP Server** - For PR/Issue analysis\n",
        "\n",
        "```python\n",
        "McpToolset(\n",
        "    connection_params=StreamableHTTPServerParams(\n",
        "        url=\"https://api.githubcopilot.com/mcp/\",\n",
        "        headers={\n",
        "            \"Authorization\": f\"Bearer {GITHUB_TOKEN}\",\n",
        "            \"X-MCP-Toolsets\": \"all\",\n",
        "            \"X-MCP-Readonly\": \"true\"\n",
        "        },\n",
        "    ),\n",
        ")\n",
        "```\n",
        "\n",
        "**More resources:** [ADK Third-party Tools Documentation](https://google.github.io/adk-docs/tools/third-party/)"
      ],
      "metadata": {
        "id": "aIyLW_0irnQg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🔄 Section 3: Long-Running Operations (Human-in-the-Loop)\n",
        "\n",
        "So far, all tools execute and return immediately:\n",
        "\n",
        "\n",
        "> ```User asks → Agent calls tool → Tool returns result → Agent responds```\n",
        "\n",
        "\n",
        "**But what if your tools are long-running or you need human approval before completing an action?**\n",
        "\n",
        "Example: A shipping agent should ask for approval before placing a large order.\n",
        "\n",
        "\n",
        "> ```User asks → Agent calls tool → Tool PAUSES and asks human → Human approves → Tool completes → Agent responds```\n",
        "\n",
        "\n",
        "This is called a **Long-Running Operation (LRO)** - the tool needs to pause, wait for external input (human approval), then resume."
      ],
      "metadata": {
        "id": "VLHI2k7zpwG_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**When to use Long-Running Operations:**\n",
        "\n",
        "- 💰 **Financial transactions** requiring approval (transfers, purchases)\n",
        "- 🗑️ **Bulk operations** (delete 1000 records - confirm first!)\n",
        "- 📋 **Compliance checkpoints** (regulatory approval needed)\n",
        "- 💸 **High-cost actions** (spin up 50 servers - are you sure?)\n",
        "- ⚠️ **Irreversible operations** (permanently delete account)"
      ],
      "metadata": {
        "id": "5TpZJ7bVrnQg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.1: What We're Building Today\n",
        "\n",
        "Let's build a **shipping coordinator agent with one tool** that:\n",
        "- Auto-approves small orders (≤5 containers)\n",
        "- **Pauses and asks for approval** on large orders (>5 containers)\n",
        "- Completes or cancels based on the approval decision\n",
        "\n",
        "This demonstrates the core long-running operation pattern: **pause → wait for human input → resume**."
      ],
      "metadata": {
        "id": "qT8Tz1pcrnQg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.2: The Shipping Tool with Approval Logic\n",
        "\n",
        "Here's the complete function.\n",
        "\n",
        "#### The `ToolContext` Parameter\n",
        "\n",
        "Notice the function signature includes `tool_context: ToolContext`. ADK automatically provides this object when your tool runs. It gives you two key capabilities:\n",
        "\n",
        "1. **Request approval:** Call `tool_context.request_confirmation()`\n",
        "2. **Check approval status:** Read `tool_context.tool_confirmation`"
      ],
      "metadata": {
        "id": "Uxo9hhXxrnQh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "LARGE_ORDER_THRESHOLD = 5\n",
        "\n",
        "\n",
        "def place_shipping_order(\n",
        "    num_containers: int, destination: str, tool_context: ToolContext\n",
        ") -> dict:\n",
        "    \"\"\"Places a shipping order. Requires approval if ordering more than 5 containers (LARGE_ORDER_THRESHOLD).\n",
        "\n",
        "    Args:\n",
        "        num_containers: Number of containers to ship\n",
        "        destination: Shipping destination\n",
        "\n",
        "    Returns:\n",
        "        Dictionary with order status\n",
        "    \"\"\"\n",
        "\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # SCENARIO 1: Small orders (≤5 containers) auto-approve\n",
        "    if num_containers <= LARGE_ORDER_THRESHOLD:\n",
        "        return {\n",
        "            \"status\": \"approved\",\n",
        "            \"order_id\": f\"ORD-{num_containers}-AUTO\",\n",
        "            \"num_containers\": num_containers,\n",
        "            \"destination\": destination,\n",
        "            \"message\": f\"Order auto-approved: {num_containers} containers to {destination}\",\n",
        "        }\n",
        "\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # SCENARIO 2: This is the first time this tool is called. Large orders need human approval - PAUSE here.\n",
        "    if not tool_context.tool_confirmation:\n",
        "        tool_context.request_confirmation(\n",
        "            hint=f\"⚠️ Large order: {num_containers} containers to {destination}. Do you want to approve?\",\n",
        "            payload={\"num_containers\": num_containers, \"destination\": destination},\n",
        "        )\n",
        "        return {  # This is sent to the Agent\n",
        "            \"status\": \"pending\",\n",
        "            \"message\": f\"Order for {num_containers} containers requires approval\",\n",
        "        }\n",
        "\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # SCENARIO 3: The tool is called AGAIN and is now resuming. Handle approval response - RESUME here.\n",
        "    if tool_context.tool_confirmation.confirmed:\n",
        "        return {\n",
        "            \"status\": \"approved\",\n",
        "            \"order_id\": f\"ORD-{num_containers}-HUMAN\",\n",
        "            \"num_containers\": num_containers,\n",
        "            \"destination\": destination,\n",
        "            \"message\": f\"Order approved: {num_containers} containers to {destination}\",\n",
        "        }\n",
        "    else:\n",
        "        return {\n",
        "            \"status\": \"rejected\",\n",
        "            \"message\": f\"Order rejected: {num_containers} containers to {destination}\",\n",
        "        }\n",
        "\n",
        "\n",
        "print(\"✅ Long-running functions created!\")"
      ],
      "metadata": {
        "id": "EvHFmXXcpwG_",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:56.76275Z",
          "iopub.execute_input": "2025-11-10T22:03:56.763001Z",
          "iopub.status.idle": "2025-11-10T22:03:56.812345Z",
          "shell.execute_reply.started": "2025-11-10T22:03:56.762982Z",
          "shell.execute_reply": "2025-11-10T22:03:56.811409Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.3: Understanding the Code\n",
        "\n",
        "Now that you've seen the complete function, let's break down how it works.\n",
        "\n",
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day2/lro-tool.png\" width=\"1000\" alt=\"Long-running operation tool\">"
      ],
      "metadata": {
        "id": "VF1clyq3rnQh"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### How the Three Scenarios Work\n",
        "\n",
        "The tool handles three scenarios by checking `tool_context.tool_confirmation`:\n",
        "\n",
        "**Scenario 1: Small order (≤5 containers)**: Returns immediately with auto-approved status.\n",
        "- `tool_context.tool_confirmation` is never checked\n",
        "\n",
        "**Scenario 2: Large order - FIRST CALL**\n",
        "- Tool detects it's a first call: `if not tool_context.tool_confirmation:`\n",
        "- Calls `request_confirmation()` to request human approval\n",
        "- Returns `{'status': 'pending', ...}` immediately\n",
        "- **ADK automatically creates `adk_request_confirmation` event**\n",
        "- Agent execution pauses - waiting for human decision\n",
        "\n",
        "**Scenario 3: Large order - RESUMED CALL**\n",
        "- Tool detects it's resuming: `if not tool_context.tool_confirmation:` is now False\n",
        "- Checks human decision: `tool_context.tool_confirmation.confirmed`\n",
        "- If True → Returns approved status\n",
        "- If False → Returns rejected status\n",
        "\n",
        "**Key insight:** Between the two calls, your workflow code (in Section 4) must detect the `adk_request_confirmation` event and resume with the approval decision."
      ],
      "metadata": {
        "id": "C4vlcfiUrnQi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.4: Create the Agent, App and Runner"
      ],
      "metadata": {
        "id": "3zdMpOuhrnQi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Step 1: Create the agent**\n",
        "\n",
        "Add the tool to the Agent. The tool decides internally when to request approval based on the order size."
      ],
      "metadata": {
        "id": "3ajP_1BYrnQi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Create shipping agent with pausable tool\n",
        "shipping_agent = LlmAgent(\n",
        "    name=\"shipping_agent\",\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    instruction=\"\"\"You are a shipping coordinator assistant.\n",
        "\n",
        "  When users request to ship containers:\n",
        "   1. Use the place_shipping_order tool with the number of containers and destination\n",
        "   2. If the order status is 'pending', inform the user that approval is required\n",
        "   3. After receiving the final result, provide a clear summary including:\n",
        "      - Order status (approved/rejected)\n",
        "      - Order ID (if available)\n",
        "      - Number of containers and destination\n",
        "   4. Keep responses concise but informative\n",
        "  \"\"\",\n",
        "    tools=[FunctionTool(func=place_shipping_order)],\n",
        ")\n",
        "\n",
        "print(\"✅ Shipping Agent created!\")"
      ],
      "metadata": {
        "id": "3du-oETLpwHA",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:56.813445Z",
          "iopub.execute_input": "2025-11-10T22:03:56.813849Z",
          "iopub.status.idle": "2025-11-10T22:03:56.845071Z",
          "shell.execute_reply.started": "2025-11-10T22:03:56.81382Z",
          "shell.execute_reply": "2025-11-10T22:03:56.843776Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Step 2: Wrap in resumable App**\n",
        "\n",
        "**The problem:** A regular `LlmAgent` is stateless - each call is independent with no memory of previous interactions. If a tool requests approval, the agent can't remember what it was doing.\n",
        "\n",
        "**The solution:** Wrap your agent in an **`App`** with **resumability enabled**. The App adds a persistence layer that saves and restores state.\n",
        "\n",
        "**What gets saved when a tool pauses:**\n",
        "- All conversation messages so far\n",
        "- Which tool was called (`place_shipping_order`)\n",
        "- Tool parameters (10 containers, Rotterdam)\n",
        "- Where exactly it paused (waiting for approval)\n",
        "\n",
        "When you resume, the App loads this saved state so the agent continues exactly where it left off - as if no time passed."
      ],
      "metadata": {
        "id": "JkUa2VsMrnQi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Wrap the agent in a resumable app - THIS IS THE KEY FOR LONG-RUNNING OPERATIONS!\n",
        "shipping_app = App(\n",
        "    name=\"shipping_coordinator\",\n",
        "    root_agent=shipping_agent,\n",
        "    resumability_config=ResumabilityConfig(is_resumable=True),\n",
        ")\n",
        "\n",
        "print(\"✅ Resumable app created!\")"
      ],
      "metadata": {
        "id": "ftb5tMOepwHA",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:56.846549Z",
          "iopub.execute_input": "2025-11-10T22:03:56.846912Z",
          "iopub.status.idle": "2025-11-10T22:03:56.874242Z",
          "shell.execute_reply.started": "2025-11-10T22:03:56.846884Z",
          "shell.execute_reply": "2025-11-10T22:03:56.872978Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Step 3: Create Session and Runner with the App**\n",
        "\n",
        "Pass `app=shipping_app` instead of `agent=...` so the runner knows about resumability."
      ],
      "metadata": {
        "id": "ut-5dntSpwHA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "session_service = InMemorySessionService()\n",
        "\n",
        "# Create runner with the resumable app\n",
        "shipping_runner = Runner(\n",
        "    app=shipping_app,  # Pass the app instead of the agent\n",
        "    session_service=session_service,\n",
        ")\n",
        "\n",
        "print(\"✅ Runner created!\")"
      ],
      "metadata": {
        "id": "B_vdPMf9pwHA",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:56.875366Z",
          "iopub.execute_input": "2025-11-10T22:03:56.875727Z",
          "iopub.status.idle": "2025-11-10T22:03:56.90108Z",
          "shell.execute_reply.started": "2025-11-10T22:03:56.875691Z",
          "shell.execute_reply": "2025-11-10T22:03:56.900232Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**✅ Recap: Your pausable shipping agent is now complete!**\n",
        "\n",
        "You've created:\n",
        "1. ✅ A tool that can pause for approval (`place_shipping_order`)\n",
        "2. ✅ An agent that uses this tool (`shipping_agent`)\n",
        "3. ✅ A resumable app that saves state (`shipping_app`)\n",
        "4. ✅ A runner that can handle pause/resume (`shipping_runner`)\n",
        "\n",
        "**Next step:** Build the workflow code and test that our Agent detects pauses and handles approvals.\n",
        "\n",
        "---"
      ],
      "metadata": {
        "id": "S-A3zIAVpwHB"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🏗️ Section 4: Building the Workflow\n",
        "\n",
        "‼️ **Important:** The workflow code uses ADK concepts like Sessions, Runners, and Events. **We'll cover what you need to know for long-running operations** in this notebook. For deeper understanding, we will cover these topics in Day 3, or you can check out the [ADK docs](https://google.github.io/adk-docs/runtime/) and this [video](https://www.youtube.com/watch?v=44C8u0CDtSo&list=PLOU2XLYxmsIIAPgM8FmtEcFTXLLzmh4DK&index=2&t=1s)."
      ],
      "metadata": {
        "id": "FbW0Doq8rnQj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.1: ⚠️ The Critical Part - Handling Events in Your Workflow\n",
        "\n",
        "The agent won't automatically handle pause/resume. **Every long-running operation workflow requires you to:**\n",
        "\n",
        "1. **Detect the pause:** Check if events contain `adk_request_confirmation`\n",
        "2. **Get human decision:** In production, show UI and wait for user click. Here, we simulate it.\n",
        "3. **Resume the agent:** Send the decision back with the saved `invocation_id`"
      ],
      "metadata": {
        "id": "SK8joNWarnQj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.2 Understand Key Technical Concepts\n",
        "\n",
        "👉 **`events`** - ADK creates events as the agent executes. Tool calls, model responses, function results - all become events\n",
        "\n",
        "👉 **`adk_request_confirmation` event** - This event is special - it signals \"pause here!\"\n",
        "- Automatically created by ADK when your tool calls `request_confirmation()`\n",
        "- Contains the `invocation_id`\n",
        "- Your workflow must detect this event to know the agent paused\n",
        "\n",
        "👉 **`invocation_id`** - Every call to `run_async()` gets a unique `invocation_id` (like \"abc123\")\n",
        "- When a tool pauses, you save this ID\n",
        "- When resuming, pass the same ID so ADK knows which execution to continue\n",
        "- Without it, ADK would start a NEW execution instead of resuming the paused one"
      ],
      "metadata": {
        "id": "vVslX9l_rnQj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.3: Helper Functions to Process Events\n",
        "\n",
        "These handle the event iteration logic for you."
      ],
      "metadata": {
        "id": "Pf_Ve7kUrnQj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**`check_for_approval()`** - Detects if the agent paused\n",
        "- Loops through all events and looks for the special `adk_request_confirmation` event\n",
        "- Returns `approval_id` (identifies this specific request) and `invocation_id` (identifies which execution to resume)\n",
        "- Returns `None` if no pause detected"
      ],
      "metadata": {
        "id": "DYj-IGVtrnQj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def check_for_approval(events):\n",
        "    \"\"\"Check if events contain an approval request.\n",
        "\n",
        "    Returns:\n",
        "        dict with approval details or None\n",
        "    \"\"\"\n",
        "    for event in events:\n",
        "        if event.content and event.content.parts:\n",
        "            for part in event.content.parts:\n",
        "                if (\n",
        "                    part.function_call\n",
        "                    and part.function_call.name == \"adk_request_confirmation\"\n",
        "                ):\n",
        "                    return {\n",
        "                        \"approval_id\": part.function_call.id,\n",
        "                        \"invocation_id\": event.invocation_id,\n",
        "                    }\n",
        "    return None"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:56.901938Z",
          "iopub.execute_input": "2025-11-10T22:03:56.902159Z",
          "iopub.status.idle": "2025-11-10T22:03:56.923861Z",
          "shell.execute_reply.started": "2025-11-10T22:03:56.902141Z",
          "shell.execute_reply": "2025-11-10T22:03:56.922754Z"
        },
        "id": "g4GNogo7rnQj"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**`print_agent_response()`** - Displays agent text\n",
        "- Simple helper to extract and print text from events"
      ],
      "metadata": {
        "id": "2VPMxcmArnQk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def print_agent_response(events):\n",
        "    \"\"\"Print agent's text responses from events.\"\"\"\n",
        "    for event in events:\n",
        "        if event.content and event.content.parts:\n",
        "            for part in event.content.parts:\n",
        "                if part.text:\n",
        "                    print(f\"Agent > {part.text}\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:56.925093Z",
          "iopub.execute_input": "2025-11-10T22:03:56.925396Z",
          "iopub.status.idle": "2025-11-10T22:03:56.94545Z",
          "shell.execute_reply.started": "2025-11-10T22:03:56.925373Z",
          "shell.execute_reply": "2025-11-10T22:03:56.944419Z"
        },
        "id": "ahIRQTbcrnQk"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**`create_approval_response()`** - Formats the human decision\n",
        "- Takes the approval info and boolean decision (True/False) from the human\n",
        "- Creates a `FunctionResponse` that ADK understands\n",
        "- Wraps it in a `Content` object to send back to the agent"
      ],
      "metadata": {
        "id": "PQydF_VHrnQk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def create_approval_response(approval_info, approved):\n",
        "    \"\"\"Create approval response message.\"\"\"\n",
        "    confirmation_response = types.FunctionResponse(\n",
        "        id=approval_info[\"approval_id\"],\n",
        "        name=\"adk_request_confirmation\",\n",
        "        response={\"confirmed\": approved},\n",
        "    )\n",
        "    return types.Content(\n",
        "        role=\"user\", parts=[types.Part(function_response=confirmation_response)]\n",
        "    )\n",
        "\n",
        "\n",
        "print(\"✅ Helper functions defined\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:56.946559Z",
          "iopub.execute_input": "2025-11-10T22:03:56.946895Z",
          "iopub.status.idle": "2025-11-10T22:03:56.973145Z",
          "shell.execute_reply.started": "2025-11-10T22:03:56.946872Z",
          "shell.execute_reply": "2025-11-10T22:03:56.971955Z"
        },
        "id": "wT4hAVP1rnQk"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.4: The Workflow Function - Let's tie it all together!\n",
        "\n",
        "The `run_shipping_workflow()` function orchestrates the entire approval flow.\n",
        "\n",
        "Look for the code explanation in the cell below."
      ],
      "metadata": {
        "id": "NarQ0NOhrnQk"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day2/lro-workflow.png\" width=\"1000\" alt=\"Long-running operation workflow\">"
      ],
      "metadata": {
        "id": "FS9Z7LS5rnQk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "async def run_shipping_workflow(query: str, auto_approve: bool = True):\n",
        "    \"\"\"Runs a shipping workflow with approval handling.\n",
        "\n",
        "    Args:\n",
        "        query: User's shipping request\n",
        "        auto_approve: Whether to auto-approve large orders (simulates human decision)\n",
        "    \"\"\"\n",
        "\n",
        "    print(f\"\\n{'='*60}\")\n",
        "    print(f\"User > {query}\\n\")\n",
        "\n",
        "    # Generate unique session ID\n",
        "    session_id = f\"order_{uuid.uuid4().hex[:8]}\"\n",
        "\n",
        "    # Create session\n",
        "    await session_service.create_session(\n",
        "        app_name=\"shipping_coordinator\", user_id=\"test_user\", session_id=session_id\n",
        "    )\n",
        "\n",
        "    query_content = types.Content(role=\"user\", parts=[types.Part(text=query)])\n",
        "    events = []\n",
        "\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # STEP 1: Send initial request to the Agent. If num_containers > 5, the Agent returns the special `adk_request_confirmation` event\n",
        "    async for event in shipping_runner.run_async(\n",
        "        user_id=\"test_user\", session_id=session_id, new_message=query_content\n",
        "    ):\n",
        "        events.append(event)\n",
        "\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # STEP 2: Loop through all the events generated and check if `adk_request_confirmation` is present.\n",
        "    approval_info = check_for_approval(events)\n",
        "\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # STEP 3: If the event is present, it's a large order - HANDLE APPROVAL WORKFLOW\n",
        "    if approval_info:\n",
        "        print(f\"⏸️  Pausing for approval...\")\n",
        "        print(f\"🤔 Human Decision: {'APPROVE ✅' if auto_approve else 'REJECT ❌'}\\n\")\n",
        "\n",
        "        # PATH A: Resume the agent by calling run_async() again with the approval decision\n",
        "        async for event in shipping_runner.run_async(\n",
        "            user_id=\"test_user\",\n",
        "            session_id=session_id,\n",
        "            new_message=create_approval_response(\n",
        "                approval_info, auto_approve\n",
        "            ),  # Send human decision here\n",
        "            invocation_id=approval_info[\n",
        "                \"invocation_id\"\n",
        "            ],  # Critical: same invocation_id tells ADK to RESUME\n",
        "        ):\n",
        "            if event.content and event.content.parts:\n",
        "                for part in event.content.parts:\n",
        "                    if part.text:\n",
        "                        print(f\"Agent > {part.text}\")\n",
        "\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    # -----------------------------------------------------------------------------------------------\n",
        "    else:\n",
        "        # PATH B: If the `adk_request_confirmation` is not present - no approval needed - order completed immediately.\n",
        "        print_agent_response(events)\n",
        "\n",
        "    print(f\"{'='*60}\\n\")\n",
        "\n",
        "\n",
        "print(\"✅ Workflow function ready\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:56.974041Z",
          "iopub.execute_input": "2025-11-10T22:03:56.974313Z",
          "iopub.status.idle": "2025-11-10T22:03:56.999889Z",
          "shell.execute_reply.started": "2025-11-10T22:03:56.97429Z",
          "shell.execute_reply": "2025-11-10T22:03:56.998882Z"
        },
        "id": "cbQkhztNrnQk"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### **Code breakdown**\n",
        "\n",
        "**Step 1: Send initial request to the Agent**\n",
        "- Call `run_async()` to start agent execution\n",
        "- Collect all events in a list for inspection\n",
        "\n",
        "**Step 2: Detect Pause**\n",
        "- Call `check_for_approval(events)` to look for the special event: `adk_request_confirmation`\n",
        "- Returns approval info (with `invocation_id`) if the special event is present; `None` if completed\n",
        "\n",
        "**Step 3: Resume execution**\n",
        "\n",
        "PATH A:\n",
        "- If the approval info is present, at this point the Agent *pauses* for human input.\n",
        "- Once the Human input is available, call the agent again using `run_async()` and pass in the Human input.\n",
        "- **Critical:** Same `invocation_id` (tells ADK to RESUME, not restart)\n",
        "- Display agent's final response after resuming\n",
        "\n",
        "PATH B:\n",
        "- If the approval info is not present, then approval is not needed and the agent completes execution."
      ],
      "metadata": {
        "id": "2-oPID08rnQk"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 🎬 4.5: Demo: Testing the Workflow\n",
        "\n",
        "Now, let's run our demos. Notice how much cleaner and easier to read they are. All the complex logic for pausing and resuming is now hidden away in our `run_workflow` helper function, allowing us to focus on the tasks we want the agent to perform.\n",
        "\n",
        "**Note:** You may see warnings like `Warning: there are non-text parts in the response: ['function_call']` - this is normal and can be ignored. It just means the agent is calling tools in addition to generating text."
      ],
      "metadata": {
        "id": "Uas-x3LxpwHE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Demo 1: It's a small order. Agent receives auto-approved status from tool\n",
        "await run_shipping_workflow(\"Ship 3 containers to Singapore\")\n",
        "\n",
        "# Demo 2: Workflow simulates human decision: APPROVE ✅\n",
        "await run_shipping_workflow(\"Ship 10 containers to Rotterdam\", auto_approve=True)\n",
        "\n",
        "# Demo 3: Workflow simulates human decision: REJECT ❌\n",
        "await run_shipping_workflow(\"Ship 8 containers to Los Angeles\", auto_approve=False)"
      ],
      "metadata": {
        "id": "uVaApsoupwHE",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-10T22:03:57.000996Z",
          "iopub.execute_input": "2025-11-10T22:03:57.001226Z",
          "iopub.status.idle": "2025-11-10T22:04:00.454765Z",
          "shell.execute_reply.started": "2025-11-10T22:03:57.001201Z",
          "shell.execute_reply": "2025-11-10T22:04:00.45364Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.6: (Optional) Complete execution flow\n",
        "\n",
        "Here's an example trace of the whole workflow.\n",
        "\n",
        "**TL;DR:** Tool pauses at TIME 6, workflow detects it at TIME 8, resumes at TIME 10 with same `invocation_id=\"abc123\"`.\n",
        "\n",
        "**Detailed timeline:**\n",
        "\n",
        "Here's what happens step-by-step when you run `run_shipping_workflow(\"Ship 10 containers to Rotterdam\", auto_approve=True)`:\n",
        "\n",
        "```\n",
        "TIME 1: User sends \"Ship 10 containers to Rotterdam\"\n",
        "        ↓\n",
        "TIME 2: Workflow calls shipping_runner.run_async(...)\n",
        "        ADK assigns a unique invocation_id = \"abc123\"\n",
        "        ↓\n",
        "TIME 3: Agent receives user message, decides to use place_shipping_order tool\n",
        "        ↓\n",
        "TIME 4: ADK calls place_shipping_order(10, \"Rotterdam\", tool_context)\n",
        "        ↓\n",
        "TIME 5: Tool checks: num_containers (10) > 5\n",
        "        Tool calls tool_context.request_confirmation(...)\n",
        "        ↓\n",
        "TIME 6: Tool returns {'status': 'pending', ...}\n",
        "        ↓\n",
        "TIME 7: ADK creates adk_request_confirmation event with invocation_id=\"abc123\"\n",
        "        ↓\n",
        "TIME 8: Workflow detects the event via check_for_approval()\n",
        "        Saves approval_id and invocation_id=\"abc123\"\n",
        "        ↓\n",
        "TIME 9: Workflow gets human decision → True (approve)\n",
        "        ↓\n",
        "TIME 10: Workflow calls shipping_runner.run_async(..., invocation_id=\"abc123\")\n",
        "         Passes approval decision as FunctionResponse\n",
        "         ↓\n",
        "TIME 11: ADK sees invocation_id=\"abc123\" - knows to RESUME (instead of starting new)\n",
        "         Loads saved state from TIME 7\n",
        "         ↓\n",
        "TIME 12: ADK calls place_shipping_order again with same parameters\n",
        "         But now tool_context.tool_confirmation.confirmed = True\n",
        "         ↓\n",
        "TIME 13: Tool returns {'status': 'approved', 'order_id': 'ORD-10-HUMAN', ...}\n",
        "         ↓\n",
        "TIME 14: Agent receives result and responds to user\n",
        "```\n",
        "\n",
        "**Key point:** The `invocation_id` is how ADK knows to resume the paused execution instead of starting a new one."
      ],
      "metadata": {
        "id": "8tAbcXvqrnQl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 📊 Section 5: Summary - Key Patterns for Advanced Tools\n",
        "\n",
        "In this notebook, you implemented two powerful, production-ready patterns for extending your agent's capabilities beyond simple functions.\n",
        "\n",
        "| Pattern | When to Use It | Key ADK Components |\n",
        "| :--- | :--- | :--- |\n",
        "| **MCP Integration** | You need to connect to **external, standardized services** (like time, databases, or file systems) without writing custom integration code. | `McpToolset` |\n",
        "| **Long-Running Operations** | You need to **pause a workflow** to wait for an external event, most commonly for **human-in-the-loop** approvals or long background tasks or for compliance/security checkpoints. | `ToolContext`, `request_confirmation`, `App`, `ResumabilityConfig` |\n",
        "\n",
        "### 🚀 Production Ready Concepts\n",
        "\n",
        "You now understand how to build agents that:\n",
        "- 🌐 **Scale**: Leverage community tools instead of building everything\n",
        "- ⏳ **Handle Time**: Manage operations that span minutes, hours, or days  \n",
        "- 🔒 **Ensure Compliance**: Add human oversight to critical operations\n",
        "- 🔄 **Maintain State**: Resume conversations exactly where they paused\n",
        "\n",
        "**Start Simple**: Begin with custom tools → Add MCP services → Add long-running as needed"
      ],
      "metadata": {
        "id": "8_DNvktYpwHE"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🎯 Exercise: Build an Image Generation Agent with Cost Approval\n",
        "\n",
        "**The scenario:**\n",
        "\n",
        "Build an agent that generates images using the MCP server, but requires approval for \"bulk\" image generation:\n",
        "- Single image request (1 image): Auto-approve, generate immediately\n",
        "- Bulk request (>1 image): Pause and ask for approval before generating multiple images\n",
        "- Explore different publicly available Image Generation MCP Servers"
      ],
      "metadata": {
        "id": "6pcTQW3GrnQl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 🎉 Congratulations! You've Learned Agent Patterns and Best Practices\n",
        "\n",
        "You've successfully learned how to build agents that handle complex, real-world workflows integrating external systems and spanning time.\n",
        "\n",
        "**ℹ️ Note: No submission required!**\n",
        "\n",
        "This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "### 📚 Learn More\n",
        "\n",
        "- [ADK Documentation](https://google.github.io/adk-docs/)\n",
        "- [MCP Tools Documentation](https://google.github.io/adk-docs/tools/mcp-tools/)\n",
        "- [Long-Running Operations Guide](https://google.github.io/adk-docs/tools/function-tools/)\n",
        "- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)\n",
        "- [The `App` and `Runner`](https://google.github.io/adk-docs/runtime/)\n",
        "\n",
        "### 🎯 Next Steps\n",
        "\n",
        "You've built the foundation for production-ready agent systems. Ready for the next challenge?\n",
        "\n",
        "Continue to **Day 3** to learn about **State and Memory Management**!"
      ],
      "metadata": {
        "id": "657bqQLCpwHE"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "<div align=\"center\">\n",
        "  <table>\n",
        "    <tr>\n",
        "      <th style=\"text-align:center\">Authors</th>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <td style=\"text-align:center\"><a href=\"https://www.linkedin.com/in/laxmi-harikumar/\">Laxmi Harikumar</a></td>\n",
        "    </tr>\n",
        "  </table>\n",
        "</div>"
      ],
      "metadata": {
        "id": "-u8V91VsrnQl"
      }
    }
  ]
}

---



# Log: Day_3a_Agent_Sessions.txt

{
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.13",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [],
      "isInternetEnabled": true,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "##### Copyright 2025 Google LLC."
      ],
      "metadata": {
        "id": "s4UdcDu7x6FS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:20:39.426463Z",
          "iopub.execute_input": "2025-11-13T13:20:39.426843Z",
          "iopub.status.idle": "2025-11-13T13:20:39.433646Z",
          "shell.execute_reply.started": "2025-11-13T13:20:39.426817Z",
          "shell.execute_reply": "2025-11-13T13:20:39.432271Z"
        },
        "id": "pl4UkW40x6FT"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 🚀 Memory Management - Part 1 - Sessions\n",
        "\n",
        "**Welcome to Day 3 of the Kaggle 5-day Agents course!**\n",
        "\n",
        "In this notebook, you'll learn:\n",
        "\n",
        "- ✅ What sessions are and how to use them in your agent\n",
        "- ✅ How to build *stateful* agents with sessions and events\n",
        "- ✅ How to persist sessions in a database\n",
        "- ✅ Context management practices such as context compaction\n",
        "- ✅ Best practices for sharing session State"
      ],
      "metadata": {
        "id": "gCqXkvp-x6FU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ‼️ Please Read\n",
        "\n",
        "\n",
        "> ❌ **ℹ️ Note: No submission required!**\n",
        "> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n",
        "\n",
        "> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n",
        "\n",
        "**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**"
      ],
      "metadata": {
        "id": "on9qUcTwx6FU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 📖 Get started with Kaggle Notebooks\n",
        "\n",
        "If this is your first time using Kaggle Notebooks, welcome! You can learn more about using Kaggle Notebooks [in the documentation](https://www.kaggle.com/docs/notebooks).\n",
        "\n",
        "Here's how to get started:\n",
        "\n",
        "**1. Verify Your Account (Required)**\n",
        "\n",
        "To use the Kaggle Notebooks in this course, you'll need to verify your account with a phone number.\n",
        "\n",
        "You can do this in your [Kaggle settings](https://www.kaggle.com/settings).\n",
        "\n",
        "**2. Make Your Own Copy**\n",
        "\n",
        "To run any code in this notebook, you first need your own editable copy.\n",
        "\n",
        "Click the `Copy and Edit` button in the top-right corner.\n",
        "\n",
        "![Copy and Edit button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_1.png)\n",
        "\n",
        "This creates a private copy of the notebook just for you.\n",
        "\n",
        "**3. Run Code Cells**\n",
        "\n",
        "Once you have your copy, you can run code.\n",
        "\n",
        "Click the ▶️ Run button next to any code cell to execute it.\n",
        "\n",
        "![Run cell button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_2.png)\n",
        "\n",
        "Run the cells in order from top to bottom.\n",
        "\n",
        "**4. If You Get Stuck**\n",
        "\n",
        "To restart: Select `Factory reset` from the `Run` menu.\n",
        "\n",
        "For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server."
      ],
      "metadata": {
        "jp-MarkdownHeadingCollapsed": true,
        "id": "5ylOowYXx6FV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## ⚙️ Section 1: Setup\n",
        "\n",
        "### 1.1: Install dependencies\n",
        "\n",
        "The Kaggle Notebooks environment includes a pre-installed version of the [google-adk](https://google.github.io/adk-docs/) library for Python and its required dependencies, so you don't need to install additional packages in this notebook.\n",
        "\n",
        "To install and use ADK in your own Python development environment outside of this course, you can do so by running:\n",
        "\n",
        "```\n",
        "pip install google-adk\n",
        "```"
      ],
      "metadata": {
        "id": "zNdXMMbbx6FV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.2: Configure your Gemini API Key\n",
        "\n",
        "This notebook uses the [Gemini API](https://ai.google.dev/gemini-api/docs), which requires authentication.\n",
        "\n",
        "**1. Get your API key**\n",
        "\n",
        "If you don't have one already, create an [API key in Google AI Studio](https://aistudio.google.com/app/api-keys).\n",
        "\n",
        "**2. Add the key to Kaggle Secrets**\n",
        "\n",
        "Next, you will need to add your API key to your Kaggle Notebook as a Kaggle User Secret.\n",
        "\n",
        "1. In the top menu bar of the notebook editor, select `Add-ons` then `Secrets`.\n",
        "2. Create a new secret with the label `GOOGLE_API_KEY`.\n",
        "3. Paste your API key into the \"Value\" field and click \"Save\".\n",
        "4. Ensure that the checkbox next to `GOOGLE_API_KEY` is selected so that the secret is attached to the notebook.\n",
        "\n",
        "**3. Authenticate in the notebook**\n",
        "\n",
        "Run the cell below to complete authentication."
      ],
      "metadata": {
        "id": "oTUVKxtVx6FW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from kaggle_secrets import UserSecretsClient\n",
        "\n",
        "try:\n",
        "    GOOGLE_API_KEY = UserSecretsClient().get_secret(\"GOOGLE_API_KEY\")\n",
        "    os.environ[\"GOOGLE_API_KEY\"] = GOOGLE_API_KEY\n",
        "    print(\"✅ Gemini API key setup complete.\")\n",
        "except Exception as e:\n",
        "    print(\n",
        "        f\"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}\"\n",
        "    )"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:20:45.267061Z",
          "iopub.execute_input": "2025-11-13T13:20:45.267399Z",
          "iopub.status.idle": "2025-11-13T13:20:45.421694Z",
          "shell.execute_reply.started": "2025-11-13T13:20:45.267373Z",
          "shell.execute_reply": "2025-11-13T13:20:45.420552Z"
        },
        "id": "lQL7Jw4gx6FX",
        "outputId": "42fd68f0-3288-494d-d9f6-f929f586441e"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Gemini API key setup complete.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.3: Import ADK components\n",
        "\n",
        "Now, import the specific components you'll need from the Agent Development Kit and the Generative AI library. This keeps your code organized and ensures we have access to the necessary building blocks."
      ],
      "metadata": {
        "id": "WwJSa203x6FY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from typing import Any, Dict\n",
        "\n",
        "from google.adk.agents import Agent, LlmAgent\n",
        "from google.adk.apps.app import App, EventsCompactionConfig\n",
        "from google.adk.models.google_llm import Gemini\n",
        "from google.adk.sessions import DatabaseSessionService\n",
        "from google.adk.sessions import InMemorySessionService\n",
        "from google.adk.runners import Runner\n",
        "from google.adk.tools.tool_context import ToolContext\n",
        "from google.genai import types\n",
        "\n",
        "print(\"✅ ADK components imported successfully.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:20:48.117182Z",
          "iopub.execute_input": "2025-11-13T13:20:48.117501Z",
          "iopub.status.idle": "2025-11-13T13:21:15.127145Z",
          "shell.execute_reply.started": "2025-11-13T13:20:48.117476Z",
          "shell.execute_reply": "2025-11-13T13:21:15.126083Z"
        },
        "id": "L-OW5JkQx6FZ",
        "outputId": "2ec5175a-99d1-4353-d1ef-47ae7cb5b0cb"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ ADK components imported successfully.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.4: Helper functions\n",
        "\n",
        "Helper function that manages a complete conversation session, handling session\n",
        "creation/retrieval, query processing, and response streaming. It supports\n",
        "both single queries and multiple queries in sequence.\n",
        "\n",
        "Example:\n",
        "\n",
        "```\n",
        ">>> await run_session(runner, \"What is the capital of France?\", \"geography-session\")\n",
        ">>> await run_session(runner, [\"Hello!\", \"What's my name?\"], \"user-intro-session\")\n",
        "```"
      ],
      "metadata": {
        "id": "pbCCLAPix6FZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define helper functions that will be reused throughout the notebook\n",
        "async def run_session(\n",
        "    runner_instance: Runner,\n",
        "    user_queries: list[str] | str = None,\n",
        "    session_name: str = \"default\",\n",
        "):\n",
        "    print(f\"\\n ### Session: {session_name}\")\n",
        "\n",
        "    # Get app name from the Runner\n",
        "    app_name = runner_instance.app_name\n",
        "\n",
        "    # Attempt to create a new session or retrieve an existing one\n",
        "    try:\n",
        "        session = await session_service.create_session(\n",
        "            app_name=app_name, user_id=USER_ID, session_id=session_name\n",
        "        )\n",
        "    except:\n",
        "        session = await session_service.get_session(\n",
        "            app_name=app_name, user_id=USER_ID, session_id=session_name\n",
        "        )\n",
        "\n",
        "    # Process queries if provided\n",
        "    if user_queries:\n",
        "        # Convert single query to list for uniform processing\n",
        "        if type(user_queries) == str:\n",
        "            user_queries = [user_queries]\n",
        "\n",
        "        # Process each query in the list sequentially\n",
        "        for query in user_queries:\n",
        "            print(f\"\\nUser > {query}\")\n",
        "\n",
        "            # Convert the query string to the ADK Content format\n",
        "            query = types.Content(role=\"user\", parts=[types.Part(text=query)])\n",
        "\n",
        "            # Stream the agent's response asynchronously\n",
        "            async for event in runner_instance.run_async(\n",
        "                user_id=USER_ID, session_id=session.id, new_message=query\n",
        "            ):\n",
        "                # Check if the event contains valid content\n",
        "                if event.content and event.content.parts:\n",
        "                    # Filter out empty or \"None\" responses before printing\n",
        "                    if (\n",
        "                        event.content.parts[0].text != \"None\"\n",
        "                        and event.content.parts[0].text\n",
        "                    ):\n",
        "                        print(f\"{MODEL_NAME} > \", event.content.parts[0].text)\n",
        "    else:\n",
        "        print(\"No queries!\")\n",
        "\n",
        "\n",
        "print(\"✅ Helper functions defined.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:21:22.795822Z",
          "iopub.execute_input": "2025-11-13T13:21:22.796188Z",
          "iopub.status.idle": "2025-11-13T13:21:22.805604Z",
          "shell.execute_reply.started": "2025-11-13T13:21:22.79616Z",
          "shell.execute_reply": "2025-11-13T13:21:22.804536Z"
        },
        "id": "fXl6DGLPx6Fa",
        "outputId": "844c9d63-d26a-4b40-d52c-92609608beec"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Helper functions defined.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.5: Configure Retry Options\n",
        "\n",
        "When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff."
      ],
      "metadata": {
        "id": "pg8MVvB0x6Fa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "retry_config = types.HttpRetryOptions(\n",
        "    attempts=5,  # Maximum retry attempts\n",
        "    exp_base=7,  # Delay multiplier\n",
        "    initial_delay=1,\n",
        "    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:21:27.521778Z",
          "iopub.execute_input": "2025-11-13T13:21:27.52215Z",
          "iopub.status.idle": "2025-11-13T13:21:27.528152Z",
          "shell.execute_reply.started": "2025-11-13T13:21:27.522124Z",
          "shell.execute_reply": "2025-11-13T13:21:27.526968Z"
        },
        "id": "td1cMd2Sx6Fb"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🤹 Section 2: Session Management\n",
        "\n",
        "### 2.1 The Problem\n",
        "\n",
        "At their core, Large Language Models are **inherently stateless**. Their awareness is confined to the information you provide in a single API call. This means an agent without proper context management will react to the current prompt without considering any previous history.\n",
        "\n",
        "**❓ Why does this matter?** Imagine trying to have a meaningful conversation with someone who forgets everything you've said after each sentence. That's the challenge we face with raw LLMs!\n",
        "\n",
        "In ADK, we use `Sessions` for **short term memory management** and `Memory` for **long term memory.** In the next notebook, you'll focus on `Memory`."
      ],
      "metadata": {
        "id": "88HmHbCox6Fb"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.2 What is a Session?\n",
        "\n",
        "#### **📦 Session**\n",
        "\n",
        "A session is a container for conversations. It encapsulates the conversation history in a chronological manner and also records all tool interactions and responses for a **single, continuous conversation**. A session is tied to a user and agent; it is not shared with other users. Similarly, a session history for an Agent is not shared with other Agents.\n",
        "\n",
        "In ADK, a **Session** is comprised of two key components `Events` and `State`:\n",
        "\n",
        "**📝 Session.Events**:\n",
        "\n",
        "> While a session is a container for conversations, `Events` are the building blocks of a conversation.\n",
        ">\n",
        "> Example of Events:\n",
        "> - *User Input*: A message from the user (text, audio, image, etc.)\n",
        "> - *Agent Response*: The agent's reply to the user\n",
        "> - *Tool Call*: The agent's decision to use an external tool or API\n",
        "> - *Tool Output*: The data returned from a tool call, which the agent uses to continue its reasoning\n",
        "    \n",
        "\n",
        "**{} Session.State**:\n",
        "\n",
        "> `session.state` is the Agent's scratchpad, where it stores and updates dynamic details needed during the conversation. Think of it as a global `{key, value}` pair storage which is available to all subagents and tools."
      ],
      "metadata": {
        "id": "-F2mKIBgx6Fb"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day3/session-state-and-events.png\" width=\"320\" alt=\"Session state and events\">\n",
        "\n",
        "<!-- ```mermaid\n",
        "graph TD\n",
        "    subgraph A[\"Agentic Application\"];\n",
        "        subgraph U[\"User\"]\n",
        "            subgraph S1[\"Session\"]\n",
        "                D1[\"Session.Events\"]\n",
        "                D2[\"Session.State\"]\n",
        "            end\n",
        "        end\n",
        "    end\n",
        "``` -->"
      ],
      "metadata": {
        "id": "UVxzIFnex6Fb"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.3 How to manage sessions?\n",
        "\n",
        "An agentic application can have multiple users and each user may have multiple sessions with the application.\n",
        "To manage these sessions and events, ADK offers a **Session Manager** and **Runner**.\n",
        "\n",
        "1. **`SessionService`**: The storage layer\n",
        "   - Manages creation, storage, and retrieval of session data\n",
        "   - Different implementations for different needs (memory, database, cloud)\n",
        "\n",
        "2. **`Runner`**: The orchestration layer\n",
        "   - Manages the flow of information between user and agent\n",
        "   - Automatically maintains conversation history\n",
        "   - Handles the Context Engineering behind the scenes\n",
        "\n",
        "Think of it like this:\n",
        "\n",
        "- **Session** = A notebook 📓\n",
        "- **Events** = Individual entries in a single page 📝\n",
        "- **SessionService** = The filing cabinet storing notebooks 🗄️\n",
        "- **Runner** = The assistant managing the conversation 🤖"
      ],
      "metadata": {
        "id": "GewZzl3Dx6Fb"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.4 Implementing Our First Stateful Agent\n",
        "\n",
        "Let's build our first stateful agent, that can remember and have constructive conversations.\n",
        "\n",
        "ADK offers different types of sessions suitable for different needs. As a start, we'll start with a simple Session Management option (`InMemorySessionService`):"
      ],
      "metadata": {
        "id": "hpveXajIx6Fc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "APP_NAME = \"default\"  # Application\n",
        "USER_ID = \"default\"  # User\n",
        "SESSION = \"default\"  # Session\n",
        "\n",
        "MODEL_NAME = \"gemini-2.5-flash-lite\"\n",
        "\n",
        "\n",
        "# Step 1: Create the LLM Agent\n",
        "root_agent = Agent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"text_chat_bot\",\n",
        "    description=\"A text chatbot\",  # Description of the agent's purpose\n",
        ")\n",
        "\n",
        "# Step 2: Set up Session Management\n",
        "# InMemorySessionService stores conversations in RAM (temporary)\n",
        "session_service = InMemorySessionService()\n",
        "\n",
        "# Step 3: Create the Runner\n",
        "runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)\n",
        "\n",
        "print(\"✅ Stateful agent initialized!\")\n",
        "print(f\"   - Application: {APP_NAME}\")\n",
        "print(f\"   - User: {USER_ID}\")\n",
        "print(f\"   - Using: {session_service.__class__.__name__}\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:21:35.999814Z",
          "iopub.execute_input": "2025-11-13T13:21:36.00072Z",
          "iopub.status.idle": "2025-11-13T13:21:36.008591Z",
          "shell.execute_reply.started": "2025-11-13T13:21:36.000683Z",
          "shell.execute_reply": "2025-11-13T13:21:36.007176Z"
        },
        "id": "q9p2Ozeox6Fc",
        "outputId": "cbae703f-5328-471e-bb34-acc1358726f5"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Stateful agent initialized!\n   - Application: default\n   - User: default\n   - Using: InMemorySessionService\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.5 Testing Our Stateful Agent\n",
        "\n",
        "Now let's see the magic of sessions in action!"
      ],
      "metadata": {
        "id": "ThUPyJIFx6Fc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Run a conversation with two queries in the same session\n",
        "# Notice: Both queries are part of the SAME session, so context is maintained\n",
        "await run_session(\n",
        "    runner,\n",
        "    [\n",
        "        \"Hi, I am Sam! What is the capital of United States?\",\n",
        "        \"Hello! What is my name?\",  # This time, the agent should remember!\n",
        "    ],\n",
        "    \"stateful-agentic-session\",\n",
        ")"
      ],
      "metadata": {
        "lines_to_next_cell": 2,
        "trusted": true,
        "id": "8lOKrSK1x6Fc"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "🎉 **Success!** The agent remembered your name because both queries were part of the same session. The Runner automatically maintained the conversation history.\n",
        "\n",
        "But there's a catch: `InMemorySessionService` is temporary. **Once the application stops, all conversation history is lost.**\n"
      ],
      "metadata": {
        "id": "yLcwFeBKx6Fc"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 🛑 (Optional) 2.6 Testing Agent's forgetfulness\n",
        "\n",
        "> To verify that the agent forgets the conversation, **restart the kernel**. Then, **run ALL the previous cells in this notebook EXCEPT the `run_session` in 2.5.**\n",
        ">\n",
        "> Now run the cell below. You'll see that the agent doesn't remember anything from the previous conversation."
      ],
      "metadata": {
        "id": "iS3VH_Uzx6Fd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Run this cell after restarting the kernel. All this history will be gone...\n",
        "await run_session(\n",
        "    runner,\n",
        "    [\"What did I ask you about earlier?\", \"And remind me, what's my name?\"],\n",
        "    \"stateful-agentic-session\",\n",
        ")  # Note, we are using same session name"
      ],
      "metadata": {
        "lines_to_next_cell": 2,
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:21:47.611825Z",
          "iopub.execute_input": "2025-11-13T13:21:47.612171Z",
          "iopub.status.idle": "2025-11-13T13:21:49.14902Z",
          "shell.execute_reply.started": "2025-11-13T13:21:47.612146Z",
          "shell.execute_reply": "2025-11-13T13:21:49.148024Z"
        },
        "id": "zylccSqux6Fd",
        "outputId": "941ffa2a-eefb-44df-8f0a-19703750b716"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n ### Session: stateful-agentic-session\n\nUser > What did I ask you about earlier?\ngemini-2.5-flash-lite >  I do not have access to your previous conversation history. Therefore, I cannot recall what you asked me about earlier.\n\nUser > And remind me, what's my name?\ngemini-2.5-flash-lite >  I do not have access to your personal information, including your name. Therefore, I cannot remind you of it.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### The Problem\n",
        "\n",
        "Session information is not persistent (i.e., meaningful conversations are lost). While this is advantageous in testing environments, **in the real world, a user should be able to refer from past and resume conversations.** To achieve this, we must persist information."
      ],
      "metadata": {
        "id": "B2aPfprix6Fd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 📈 Section 3: Persistent Sessions with `DatabaseSessionService`\n",
        "\n",
        "While `InMemorySessionService` is great for prototyping, real-world applications need conversations to survive restarts, crashes, and deployments. Let's level up to persistent storage!\n",
        "\n",
        "### 3.1 Choosing the Right SessionService\n",
        "\n",
        "ADK provides different SessionService implementations for different needs:\n",
        "\n",
        "| Service | Use Case | Persistence | Best For |\n",
        "|---------|----------|-------------|----------|\n",
        "| **InMemorySessionService** | Development & Testing | ❌ Lost on restart | Quick prototypes |\n",
        "| **DatabaseSessionService** | Self-managed apps | ✅ Survives restarts | Small to medium apps |\n",
        "| **Agent Engine Sessions** | Production on GCP | ✅ Fully managed | Enterprise scale |\n"
      ],
      "metadata": {
        "id": "NIXHUPy9x6Fd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.2 Implementing Persistent Sessions\n",
        "\n",
        "Let's upgrade to `DatabaseSessionService` using SQLite. This gives us persistence without needing a separate database server for this demo.\n",
        "\n",
        "Let's create a `chatbot_agent` capable of having a conversation with the user."
      ],
      "metadata": {
        "id": "s8y_HEyHx6Fd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Step 1: Create the same agent (notice we use LlmAgent this time)\n",
        "chatbot_agent = LlmAgent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"text_chat_bot\",\n",
        "    description=\"A text chatbot with persistent memory\",\n",
        ")\n",
        "\n",
        "# Step 2: Switch to DatabaseSessionService\n",
        "# SQLite database will be created automatically\n",
        "db_url = \"sqlite:///my_agent_data.db\"  # Local SQLite file\n",
        "session_service = DatabaseSessionService(db_url=db_url)\n",
        "\n",
        "# Step 3: Create a new runner with persistent storage\n",
        "runner = Runner(agent=chatbot_agent, app_name=APP_NAME, session_service=session_service)\n",
        "\n",
        "print(\"✅ Upgraded to persistent sessions!\")\n",
        "print(f\"   - Database: my_agent_data.db\")\n",
        "print(f\"   - Sessions will survive restarts!\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:29:09.970181Z",
          "iopub.execute_input": "2025-11-13T13:29:09.97059Z",
          "iopub.status.idle": "2025-11-13T13:29:10.103163Z",
          "shell.execute_reply.started": "2025-11-13T13:29:09.970562Z",
          "shell.execute_reply": "2025-11-13T13:29:10.102118Z"
        },
        "id": "8Nr-3UKxx6Fe",
        "outputId": "d2752649-e263-4256-f18c-f578db1da185"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Upgraded to persistent sessions!\n   - Database: my_agent_data.db\n   - Sessions will survive restarts!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.3 Test Run 1: Verifying Persistence\n",
        "\n",
        "In this first test run, we'll start a new conversation with the session ID `test-db-session-01`. We will first introduce our name as 'Sam' and then ask a question. In the second turn, we will ask the agent for our name.\n",
        "\n",
        "Since we are using `DatabaseSessionService`, the agent should remember the name.\n",
        "\n",
        "After the conversation, we'll inspect the `my_agent_data.db` SQLite database directly to see how the conversation `events` (the user queries and model responses) are stored.\n"
      ],
      "metadata": {
        "id": "x1mKbU69x6Fe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "await run_session(\n",
        "    runner,\n",
        "    [\"Hi, I am Sam! What is the capital of the United States?\", \"Hello! What is my name?\"],\n",
        "    \"test-db-session-01\",\n",
        ")"
      ],
      "metadata": {
        "lines_to_next_cell": 2,
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:29:42.667403Z",
          "iopub.execute_input": "2025-11-13T13:29:42.667725Z",
          "iopub.status.idle": "2025-11-13T13:29:44.041341Z",
          "shell.execute_reply.started": "2025-11-13T13:29:42.667703Z",
          "shell.execute_reply": "2025-11-13T13:29:44.04009Z"
        },
        "id": "ijd56CKqx6Fe",
        "outputId": "edeed12f-8e02-4f1b-cdc6-a0476d152851"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n ### Session: test-db-session-01\n\nUser > Hi, I am Sam! What is the capital of the United States?\ngemini-2.5-flash-lite >  Hi Sam! The capital of the United States is Washington, D.C.\n\nUser > Hello! What is my name?\ngemini-2.5-flash-lite >  You told me your name is Sam.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 🛑 (Optional) 3.4 Test Run 2: Resuming a Conversation\n",
        "\n",
        "> ‼️ Now, let's repeat the test again, but this time, **let's stop this Kaggle Notebook's kernel and restart it again.**\n",
        ">\n",
        "> 1. Run all the previous cells in the notebook, **EXCEPT** the previous Section 3.3 (`run_session` cell).\n",
        ">\n",
        "> 2. Now, run the below cell with the **same session ID** (`test-db-session-01`).\n",
        "\n",
        "We will ask a new question and then ask for our name again. **Because the session is loaded from the database, the agent should still remember** that our name is 'Sam' from the first test run. This demonstrates the power of persistent sessions.\n"
      ],
      "metadata": {
        "id": "8fA_4oolx6Ff"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "await run_session(\n",
        "    runner,\n",
        "    [\"What is the capital of India?\", \"Hello! What is my name?\"],\n",
        "    \"test-db-session-01\",\n",
        ")"
      ],
      "metadata": {
        "lines_to_next_cell": 2,
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:30:31.221603Z",
          "iopub.execute_input": "2025-11-13T13:30:31.221934Z",
          "iopub.status.idle": "2025-11-13T13:30:32.356572Z",
          "shell.execute_reply.started": "2025-11-13T13:30:31.22191Z",
          "shell.execute_reply": "2025-11-13T13:30:32.3552Z"
        },
        "id": "BKNszZW9x6Ff",
        "outputId": "6c49d659-3ee2-4c53-921b-8371b8151c01"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n ### Session: test-db-session-01\n\nUser > What is the capital of India?\ngemini-2.5-flash-lite >  The capital of India is New Delhi.\n\nUser > Hello! What is my name?\ngemini-2.5-flash-lite >  Your name is Sam.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.5 Let's verify that the session data is isolated\n",
        "\n",
        "As mentioned earlier, a session is private conversation between an Agent and a User (i.e., two sessions do not share information). Let's run our `run_session` with a different session name `test-db-session-02` to confirm this.\n"
      ],
      "metadata": {
        "id": "QBHHRVjFx6Ff"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "await run_session(\n",
        "    runner, [\"Hello! What is my name?\"], \"test-db-session-02\"\n",
        ")  # Note, we are using new session name"
      ],
      "metadata": {
        "lines_to_next_cell": 2,
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:30:39.635954Z",
          "iopub.execute_input": "2025-11-13T13:30:39.636306Z",
          "iopub.status.idle": "2025-11-13T13:30:40.100773Z",
          "shell.execute_reply.started": "2025-11-13T13:30:39.636285Z",
          "shell.execute_reply": "2025-11-13T13:30:40.099708Z"
        },
        "id": "E_C74BP6x6Ff",
        "outputId": "10d4194d-38a6-444a-da25-22077e5b9aec"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n ### Session: test-db-session-02\n\nUser > Hello! What is my name?\ngemini-2.5-flash-lite >  I do not have access to your personal information, so I do not know your name. \n\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.6 How are the events stored in the Database?\n",
        "\n",
        "Since we are using a sqlite DB to store information, let's have a quick peek to see how information is stored."
      ],
      "metadata": {
        "id": "Zmgyx3Wmx6Ff"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import sqlite3\n",
        "\n",
        "def check_data_in_db():\n",
        "    with sqlite3.connect(\"my_agent_data.db\") as connection:\n",
        "        cursor = connection.cursor()\n",
        "        result = cursor.execute(\n",
        "            \"select app_name, session_id, author, content from events\"\n",
        "        )\n",
        "        print([_[0] for _ in result.description])\n",
        "        for each in result.fetchall():\n",
        "            print(each)\n",
        "\n",
        "\n",
        "check_data_in_db()"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:30:48.21613Z",
          "iopub.execute_input": "2025-11-13T13:30:48.216463Z",
          "iopub.status.idle": "2025-11-13T13:30:48.223838Z",
          "shell.execute_reply.started": "2025-11-13T13:30:48.216439Z",
          "shell.execute_reply": "2025-11-13T13:30:48.222821Z"
        },
        "id": "TnI0PLwPx6Ff",
        "outputId": "9b11942d-1e6f-4fa0-aabc-d3f9f1b0179f"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "['app_name', 'session_id', 'author', 'content']\n('default', 'test-db-session-01', 'user', '{\"parts\": [{\"text\": \"Hi, I am Sam! What is the capital of the United States?\"}], \"role\": \"user\"}')\n('default', 'test-db-session-01', 'text_chat_bot', '{\"parts\": [{\"text\": \"Hi Sam! The capital of the United States is Washington, D.C.\"}], \"role\": \"model\"}')\n('default', 'test-db-session-01', 'user', '{\"parts\": [{\"text\": \"Hello! What is my name?\"}], \"role\": \"user\"}')\n('default', 'test-db-session-01', 'text_chat_bot', '{\"parts\": [{\"text\": \"You told me your name is Sam.\"}], \"role\": \"model\"}')\n('default', 'test-db-session-01', 'user', '{\"parts\": [{\"text\": \"What is the capital of India?\"}], \"role\": \"user\"}')\n('default', 'test-db-session-01', 'text_chat_bot', '{\"parts\": [{\"text\": \"The capital of India is New Delhi.\"}], \"role\": \"model\"}')\n('default', 'test-db-session-01', 'user', '{\"parts\": [{\"text\": \"Hello! What is my name?\"}], \"role\": \"user\"}')\n('default', 'test-db-session-01', 'text_chat_bot', '{\"parts\": [{\"text\": \"Your name is Sam.\"}], \"role\": \"model\"}')\n('default', 'test-db-session-02', 'user', '{\"parts\": [{\"text\": \"Hello! What is my name?\"}], \"role\": \"user\"}')\n('default', 'test-db-session-02', 'text_chat_bot', '{\"parts\": [{\"text\": \"I do not have access to your personal information, so I do not know your name. \\\\n\"}], \"role\": \"model\"}')\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## ⏳ Section 4: Context Compaction\n",
        "\n",
        "As you can see, all the events are stored in full in the session Database, and this quickly adds up. For a long, complex task, this list of events can become very large, leading to slower performance and higher costs.\n",
        "\n",
        "But what if we could automatically summarize the past? Let's use ADK's **Context Compaction** feature to see **how to automatically reduce the context that's stored in the Session.**"
      ],
      "metadata": {
        "id": "onbjg-kbx6Ff"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day3/context-compaction.png\" width=\"1400\" alt=\"Context compaction\">"
      ],
      "metadata": {
        "id": "qvk21bOYx6Fg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.1 Create an App for the agent\n",
        "\n",
        "To enable this feature, let's use the same `chatbot_agent` we created in Section 3.2.\n",
        "\n",
        "The first step is to create an object called `App`. We'll give it a name and pass in our chatbot_agent.\n",
        "\n",
        "We'll also create a new config to do the Context Compaction. This **`EventsCompactionConfig`** defines two key variables:\n",
        "\n",
        "- **compaction_interval**: Asks the Runner to compact the history after every `n` conversations\n",
        "- **overlap_size**: Defines the number of previous conversations to retain for overlap\n",
        "\n",
        "We'll then provide this app to the Runner.\n"
      ],
      "metadata": {
        "id": "OPE1GlCkx6Fg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Re-define our app with Events Compaction enabled\n",
        "research_app_compacting = App(\n",
        "    name=\"research_app_compacting\",\n",
        "    root_agent=chatbot_agent,\n",
        "    # This is the new part!\n",
        "    events_compaction_config=EventsCompactionConfig(\n",
        "        compaction_interval=3,  # Trigger compaction every 3 invocations\n",
        "        overlap_size=1,  # Keep 1 previous turn for context\n",
        "    ),\n",
        ")\n",
        "\n",
        "db_url = \"sqlite:///my_agent_data.db\"  # Local SQLite file\n",
        "session_service = DatabaseSessionService(db_url=db_url)\n",
        "\n",
        "# Create a new runner for our upgraded app\n",
        "research_runner_compacting = Runner(\n",
        "    app=research_app_compacting, session_service=session_service\n",
        ")\n",
        "\n",
        "\n",
        "print(\"✅ Research App upgraded with Events Compaction!\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:51:46.065495Z",
          "iopub.execute_input": "2025-11-13T13:51:46.065811Z",
          "iopub.status.idle": "2025-11-13T13:51:46.07695Z",
          "shell.execute_reply.started": "2025-11-13T13:51:46.065789Z",
          "shell.execute_reply": "2025-11-13T13:51:46.075798Z"
        },
        "id": "lXlKNnkYx6Fg",
        "outputId": "e10f8d4c-3b24-4d31-ade5-0ef8c6a71ed1"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Research App upgraded with Events Compaction!\n",
          "output_type": "stream"
        },
        {
          "name": "stderr",
          "text": "/tmp/ipykernel_136/3773147741.py:6: UserWarning: [EXPERIMENTAL] EventsCompactionConfig: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.\n  events_compaction_config=EventsCompactionConfig(\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.2 Running the Demo\n",
        "\n",
        "Now, let's have a conversation that is long enough to trigger the compaction. When you run the cell below, the output will look like a normal conversation. However, because we configured our `App`, a compaction process will run silently in the background after the 3rd invocation.\n",
        "\n",
        "In the next step, we'll prove that it happened."
      ],
      "metadata": {
        "id": "RfhgH7g0x6Fg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Turn 1\n",
        "await run_session(\n",
        "    research_runner_compacting,\n",
        "    \"What is the latest news about AI in healthcare?\",\n",
        "    \"compaction_demo\",\n",
        ")\n",
        "\n",
        "# Turn 2\n",
        "await run_session(\n",
        "    research_runner_compacting,\n",
        "    \"Are there any new developments in drug discovery?\",\n",
        "    \"compaction_demo\",\n",
        ")\n",
        "\n",
        "# Turn 3 - Compaction should trigger after this turn!\n",
        "await run_session(\n",
        "    research_runner_compacting,\n",
        "    \"Tell me more about the second development you found.\",\n",
        "    \"compaction_demo\",\n",
        ")\n",
        "\n",
        "# Turn 4\n",
        "await run_session(\n",
        "    research_runner_compacting,\n",
        "    \"Who are the main companies involved in that?\",\n",
        "    \"compaction_demo\",\n",
        ")"
      ],
      "metadata": {
        "scrolled": true,
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:52:06.292469Z",
          "iopub.execute_input": "2025-11-13T13:52:06.29279Z",
          "iopub.status.idle": "2025-11-13T13:52:24.916914Z",
          "shell.execute_reply.started": "2025-11-13T13:52:06.292768Z",
          "shell.execute_reply": "2025-11-13T13:52:24.915711Z"
        },
        "id": "U6FfabnHx6Fh",
        "outputId": "a5ebcc4f-71d3-4b1b-cc09-80cf037f9487"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n ### Session: compaction_demo\n\nUser > What is the latest news about AI in healthcare?\ngemini-2.5-flash-lite >  Here's a summary of some of the latest news and trends in AI in healthcare:\n\n**Key Areas of Progress and Investment:**\n\n*   **Drug Discovery and Development:** AI continues to be a major force in accelerating drug discovery. Companies are using AI to identify potential drug targets, predict the efficacy and safety of compounds, and optimize clinical trial design. Recent news often highlights partnerships between pharmaceutical giants and AI-focused biotech firms.\n*   **Diagnostic Imaging and Analysis:** AI algorithms are becoming increasingly sophisticated at analyzing medical images like X-rays, CT scans, and MRIs. They are showing promise in detecting subtle anomalies that might be missed by the human eye, aiding in the early diagnosis of conditions like cancer, diabetic retinopathy, and cardiovascular diseases.\n*   **Personalized Medicine and Treatment:** AI is enabling more tailored treatment plans by analyzing a patient's genetic data, medical history, lifestyle, and even real-time sensor data. This allows for more precise dosing, selection of the most effective therapies, and prediction of treatment responses.\n*   **Virtual Assistants and Chatbots:** AI-powered chatbots and virtual assistants are being used for patient engagement, appointment scheduling, symptom checking, and providing health information. They can improve accessibility and reduce the burden on healthcare providers.\n*   **Administrative Efficiency and Workflow Optimization:** AI is being deployed to streamline administrative tasks in hospitals and clinics, such as medical coding, claims processing, and resource allocation. This can lead to cost savings and allow healthcare professionals to focus more on patient care.\n*   **Predictive Analytics for Patient Outcomes:** AI models are being developed to predict patient readmissions, identify individuals at high risk of developing certain diseases, and forecast disease outbreaks. This allows for proactive interventions and better resource management.\n*   **Robotics in Surgery:** While not purely AI, AI is increasingly integrated into surgical robots to enhance precision, provide real-time guidance to surgeons, and automate certain repetitive tasks.\n\n**Recent Developments and Trends:**\n\n*   **Generative AI's Impact:** The rise of generative AI (like large language models) is creating new possibilities. These models can be used for tasks like summarizing medical literature, generating clinical notes, and even assisting in writing patient educational materials. However, concerns about accuracy and bias are also being actively discussed.\n*   **Regulatory Scrutiny and Ethical Considerations:** As AI in healthcare becomes more prevalent, regulatory bodies like the FDA are increasing their focus on ensuring the safety, efficacy, and fairness of these technologies. Ethical considerations around data privacy, algorithmic bias, and accountability are also major talking points.\n*   **Interoperability Challenges:** A significant hurdle remains in ensuring that AI systems can seamlessly integrate with existing electronic health record (EHR) systems and other healthcare IT infrastructure.\n*   **Focus on Explainability (XAI):** There's a growing demand for AI models in healthcare to be \"explainable,\" meaning their decision-making processes are transparent and understandable to clinicians. This is crucial for building trust and ensuring responsible deployment.\n*   **AI for Mental Health:** AI is being explored for applications in mental health, including early detection of depression and anxiety through voice or text analysis, and providing therapeutic support via chatbots.\n\n**Where to Find More Information:**\n\nTo get the absolute \"latest\" news, I recommend checking:\n\n*   **Reputable Healthcare Technology News Sites:** FierceHealthcare, STAT News (especially their AI coverage), MedCity News, Healthcare IT News.\n*   **Major Tech News Outlets:** Sections focusing on health, science, and AI from publications like Reuters, Associated Press, TechCrunch, The Verge, and Bloomberg.\n*   **Academic Journals and Conferences:** Publications in journals like Nature Medicine, The Lancet Digital Health, JAMA, and proceedings from AI in healthcare conferences.\n*   **Company Press Releases:** Many AI companies in healthcare issue press releases about their latest advancements and partnerships.\n\nThe field is moving incredibly fast, so what's \"latest\" today might be superseded in a few weeks!\n\n ### Session: compaction_demo\n\nUser > Are there any new developments in drug discovery?\ngemini-2.5-flash-lite >  Yes, there are **numerous exciting new developments in AI-driven drug discovery**. This is one of the most active and promising areas where AI is making a tangible impact. Here are some of the key trends and recent advancements:\n\n**1. Accelerating Target Identification and Validation:**\n\n*   **AI for Genomics and Proteomics:** AI is being used to analyze vast datasets of genomic, proteomic, and transcriptomic data to identify novel disease targets that were previously difficult to uncover. This includes pinpointing specific genes or proteins that play a critical role in disease pathways.\n*   **Network Biology Approaches:** AI models can map complex biological networks, understanding how different molecules interact. This helps researchers identify key nodes within these networks that, if targeted, could have a significant therapeutic effect.\n\n**2. Novel Molecule Design and Generation:**\n\n*   **Generative AI for De Novo Design:** This is a significant area of growth. Generative AI models (like GANs and Variational Autoencoders) can design entirely new molecules from scratch with desired properties, such as binding affinity to a specific target, good pharmacokinetic profiles, and reduced toxicity. This moves beyond simply screening existing libraries.\n*   **Reinforcement Learning for Optimization:** Reinforcement learning algorithms can be used to iteratively refine the design of potential drug candidates, optimizing them for multiple criteria simultaneously.\n\n**3. Enhancing Preclinical Testing and Prediction:**\n\n*   **Predicting Drug Properties:** AI is becoming more adept at predicting various properties of potential drug candidates *in silico* (computationally), including:\n    *   **Binding Affinity:** How strongly a molecule will bind to its intended target.\n    *   **ADMET Properties:** Absorption, Distribution, Metabolism, Excretion, and Toxicity – crucial for determining if a drug is safe and effective in the body.\n    *   **Solubility and Stability:** Important for formulation and shelf-life.\n*   **Virtual Screening at Scale:** AI can rapidly screen millions or even billions of virtual compounds against a target, significantly reducing the number of molecules that need to be synthesized and tested experimentally.\n\n**4. Improving Clinical Trial Design and Analysis:**\n\n*   **Predicting Clinical Trial Success:** AI models are being developed to analyze historical clinical trial data to predict the likelihood of success for new drug candidates.\n*   **Patient Stratification:** AI can identify patient subgroups that are most likely to respond to a particular treatment, leading to more efficient and successful clinical trials.\n*   **Biomarker Discovery:** AI helps identify biomarkers that can predict treatment response or disease progression, aiding in patient selection and monitoring.\n\n**5. \"Drug Repurposing\" with AI:**\n\n*   AI is proving very effective at identifying existing drugs that might be effective against new diseases. By analyzing vast datasets of drug-target interactions, gene expression profiles, and disease pathways, AI can find unexpected therapeutic connections.\n\n**Recent Examples and Trends:**\n\n*   **AI-powered companies making breakthroughs:** Companies like **Exscientia**, **Atomwise**, **Insilico Medicine**, **BenevolentAI**, and **Recursion Pharmaceuticals** are frequently in the news for their AI-driven approaches and the progress they are making in bringing drug candidates to clinical trials.\n*   **Partnerships:** Major pharmaceutical companies are actively partnering with or acquiring AI-driven drug discovery startups to leverage their technology.\n*   **Focus on specific disease areas:** While AI is broadly applicable, there's particular focus on AI for cancer, neurodegenerative diseases (like Alzheimer's), and infectious diseases.\n*   **Democratization of Discovery:** AI tools are starting to become more accessible, potentially enabling smaller labs and research institutions to participate more actively in drug discovery.\n\n**Challenges Remain:**\n\nDespite the rapid progress, challenges still exist:\n\n*   **Data Quality and Availability:** High-quality, curated datasets are essential for training robust AI models.\n*   **Experimental Validation:** AI predictions still need rigorous experimental validation, which can be time-consuming and expensive.\n*   **Interpretability and Trust:** Understanding *why* an AI model makes a certain prediction is crucial for building trust among scientists and regulators.\n*   **Regulatory Pathways:** Establishing clear regulatory pathways for AI-discovered drugs is an ongoing process.\n\nIn summary, AI is fundamentally transforming drug discovery by making it faster, more efficient, and more predictive. The focus is shifting from serendipitous discovery to intelligent, data-driven design.\n\n ### Session: compaction_demo\n\nUser > Tell me more about the second development you found.\ngemini-2.5-flash-lite >  You're referring to the second development I mentioned: **Novel Molecule Design and Generation**, particularly the use of **Generative AI for De Novo Design**.\n\nThis area is incredibly exciting because it represents a shift from merely searching for existing drugs that might work, to *creating entirely new drug candidates tailored to specific needs*.\n\nHere's a deeper dive into what this means and why it's a significant development:\n\n**What is \"De Novo\" Design?**\n\n\"De novo\" is a Latin phrase meaning \"from the beginning\" or \"anew.\" In drug discovery, de novo design refers to the process of creating novel chemical structures that have never existed before, rather than modifying existing known compounds.\n\n**How Generative AI Enables De Novo Design:**\n\nGenerative AI models are a type of artificial intelligence that can learn the underlying patterns and rules of a dataset and then generate new data that resembles the original. In the context of molecules, these models can:\n\n1.  **Learn Molecular Grammar:** They are trained on vast libraries of known molecules, learning the fundamental rules of chemistry – how atoms bond, what stable structures look like, and what chemical motifs are associated with certain properties.\n2.  **Generate Novel Structures:** Based on this learned \"grammar,\" the AI can then propose completely new molecular structures. This isn't just random generation; the models are guided by specific objectives.\n\n**Key Generative AI Techniques Used:**\n\n*   **Generative Adversarial Networks (GANs):** GANs consist of two neural networks: a \"generator\" that creates new molecules, and a \"discriminator\" that tries to distinguish between real molecules from the training data and the fake molecules created by the generator. This adversarial process pushes the generator to create increasingly realistic and valid molecules.\n*   **Variational Autoencoders (VAEs):** VAEs learn a compressed representation (latent space) of molecular structures. By sampling points from this latent space and decoding them, VAEs can generate new, diverse molecular structures.\n*   **Reinforcement Learning (RL) in conjunction with Generative Models:** This is a powerful combination. A generative model might propose a molecule, and then an RL agent can \"score\" that molecule based on desired properties (e.g., binding affinity, low toxicity). The RL agent then learns to guide the generative model to produce molecules that score higher on these objectives.\n\n**What Makes it a \"Development\"? What's New?**\n\n*   **Unprecedented Speed and Scale:** Manually designing and synthesizing novel molecules is a painstaking, slow, and often intuition-driven process. Generative AI can explore chemical space orders of magnitude faster.\n*   **Design for Specific Properties:** Unlike traditional methods that might stumble upon a useful molecule, generative AI can be explicitly tasked to design molecules with desired characteristics from the outset. For example:\n    *   \"Design a molecule that binds tightly to protein X.\"\n    *   \"Design a molecule that is predicted to have low toxicity and good oral bioavailability.\"\n    *   \"Design a molecule that can cross the blood-brain barrier.\"\n*   **Exploring Vast Chemical Space:** The number of theoretically possible small molecules is astronomical. Generative AI allows researchers to explore this vast \"chemical space\" much more effectively, potentially finding molecules that human chemists might never have conceived of.\n*   **Overcoming Limitations of Existing Libraries:** Many drug discovery efforts rely on screening existing libraries of compounds. Generative AI allows for the creation of entirely *new* chemical matter, opening up new avenues of therapeutic potential that might not be represented in current compound collections.\n\n**Impact:**\n\nThis development is crucial because it moves beyond simply finding needles in haystacks. It's about *designing the perfect needle* for a specific lock. By creating molecules with optimized properties from the start, AI can:\n\n*   Reduce the number of candidate molecules that fail in later stages of development.\n*   Accelerate the time from target identification to lead candidate.\n*   Potentially discover entirely new classes of drugs for previously undruggable targets.\n\nIt's a testament to the power of AI to not just analyze but also to *create*, fundamentally changing how we approach the complex art and science of designing medicines.\n\n ### Session: compaction_demo\n\nUser > Who are the main companies involved in that?\ngemini-2.5-flash-lite >  The landscape of companies involved in AI-driven de novo molecule design is dynamic and growing rapidly. It includes a mix of dedicated AI drug discovery startups, established pharmaceutical companies adopting these technologies, and academic research institutions pushing the boundaries.\n\nHere are some of the key players, categorized by their primary focus:\n\n**Dedicated AI Drug Discovery Startups (Often pioneers in de novo design):**\n\n*   **Exscientia:** One of the pioneers, Exscientia uses AI for both target identification and de novo drug design. They have multiple AI-designed molecules in clinical trials, including for oncology and immunology.\n*   **Insilico Medicine:** Known for its end-to-end AI platform, Insilico Medicine has made significant strides in generative chemistry for de novo design and has brought AI-discovered drugs to clinical trials. They focus on aging and age-related diseases, as well as other therapeutic areas.\n*   **Atomwise:** Atomwise uses deep learning, including generative models, for structure-based drug design. They focus on identifying and designing novel small molecules for a wide range of diseases.\n*   **Recursion Pharmaceuticals:** While they have a broader AI platform involving imaging and biology, Recursion also leverages AI for identifying and designing potential drug candidates.\n*   **BenevolentAI:** This company uses AI to mine vast amounts of biomedical data, identify novel targets, and then uses generative AI to design potential drug molecules for those targets.\n*   **Relay Therapeutics:** Focuses on understanding protein motion using experimental and computational methods, including AI, to design molecules that precisely target these dynamic proteins.\n*   **AbCellera:** While often associated with antibody discovery, AbCellera also has AI capabilities that can inform and guide the design of therapeutic molecules.\n*   **Schrödinger:** A long-standing player in computational chemistry, Schrödinger has significantly enhanced its platform with AI and machine learning for molecular design and property prediction.\n\n**Large Pharmaceutical Companies (Investing and Partnering):**\n\nMany major pharma companies are not just adopting these technologies but are also investing in or partnering with AI startups. They often build their own internal AI teams and platforms. Examples include:\n\n*   **Pfizer:** Actively uses AI across its R&D pipeline, including in drug design.\n*   **Novartis:** Has made significant investments in AI and machine learning for drug discovery, including de novo design capabilities.\n*   **Roche/Genentech:** Utilizes AI for various aspects of drug discovery and development.\n*   **Merck:** Has been exploring AI for target identification and molecule design.\n*   **AstraZeneca:** Collaborates with AI companies and builds internal AI expertise.\n*   **Johnson & Johnson:** Integrates AI and machine learning into its pharmaceutical research.\n*   **Bayer:** Leverages AI for drug discovery and development.\n\n**Academic Institutions and Research Efforts:**\n\nMany groundbreaking advancements in generative AI for molecule design originate from academic labs. These institutions often publish their research and their alumni go on to found or join AI drug discovery companies.\n\n*   **MIT (Massachusetts Institute of Technology):** Researchers here have been instrumental in developing some of the foundational generative AI models for chemistry.\n*   **Stanford University:** Also a hub for AI research in chemistry and biology.\n*   **University of Toronto:** Home to leading researchers in AI and drug discovery.\n*   **Numerous others:** Many universities globally have strong computational chemistry and AI labs contributing to this field.\n\n**Key Trends to Note:**\n\n*   **Partnerships and Acquisitions:** Established pharma companies are increasingly partnering with or acquiring specialized AI drug discovery firms.\n*   **Platform Integration:** The trend is towards companies developing comprehensive AI platforms that cover the entire drug discovery pipeline, from target identification to clinical trial design, with de novo design as a core component.\n*   **Focus on Specific Modalities:** While many focus on small molecules, AI is also being applied to design other therapeutic modalities like peptides and even antibodies.\n\nThis is not an exhaustive list, and new companies emerge regularly. The key takeaway is that AI-driven de novo molecule design is no longer a fringe concept; it's a central and rapidly advancing area of modern pharmaceutical R&D.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.3 Verifying Compaction in the Session History\n",
        "\n",
        "The conversation above looks normal, but the history has been changed behind the scenes. How can we prove it?\n",
        "\n",
        "We can inspect the `events` list from our session. The compaction process **doesn't delete old events; it replaces them with a single, new `Event` that contains the summary.** Let's find it."
      ],
      "metadata": {
        "id": "jVXlRhsqx6Fi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Get the final session state\n",
        "final_session = await session_service.get_session(\n",
        "    app_name=research_runner_compacting.app_name,\n",
        "    user_id=USER_ID,\n",
        "    session_id=\"compaction_demo\",\n",
        ")\n",
        "\n",
        "print(\"--- Searching for Compaction Summary Event ---\")\n",
        "found_summary = False\n",
        "for event in final_session.events:\n",
        "    # Compaction events have a 'compaction' attribute\n",
        "    if event.actions and event.actions.compaction:\n",
        "        print(\"\\n✅ SUCCESS! Found the Compaction Event:\")\n",
        "        print(f\"  Author: {event.author}\")\n",
        "        print(f\"\\n Compacted information: {event}\")\n",
        "        found_summary = True\n",
        "        break\n",
        "\n",
        "if not found_summary:\n",
        "    print(\n",
        "        \"\\n❌ No compaction event found. Try increasing the number of turns in the demo.\"\n",
        "    )"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T13:52:24.918109Z",
          "iopub.execute_input": "2025-11-13T13:52:24.918465Z",
          "iopub.status.idle": "2025-11-13T13:52:24.933909Z",
          "shell.execute_reply.started": "2025-11-13T13:52:24.918433Z",
          "shell.execute_reply": "2025-11-13T13:52:24.932668Z"
        },
        "id": "-lrG7N_ox6Fi",
        "outputId": "214770d2-fd8a-4fe6-f10e-4f32197fec0b"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "--- Searching for Compaction Summary Event ---\n\n✅ SUCCESS! Found the Compaction Event:\n  Author: user\n\n Compacted information: model_version=None content=None grounding_metadata=None partial=None turn_complete=None finish_reason=None error_code=None error_message=None interrupted=None custom_metadata=None usage_metadata=None live_session_resumption_update=None input_transcription=None output_transcription=None avg_logprobs=None logprobs_result=None cache_metadata=None citation_metadata=None invocation_id='f29b1c9a-4f25-4e85-bb1c-d7ab1af15508' author='user' actions=EventActions(skip_summarization=None, state_delta={}, artifact_delta={}, transfer_to_agent=None, escalate=None, requested_auth_configs={}, requested_tool_confirmations={}, compaction={'start_timestamp': 1763041926.332496, 'end_timestamp': 1763041935.579341, 'compacted_content': {'parts': [{'function_call': None, 'code_execution_result': None, 'executable_code': None, 'file_data': None, 'function_response': None, 'inline_data': None, 'text': 'The user asked for the latest news on AI in healthcare. The AI agent provided a comprehensive overview covering key areas like drug discovery, diagnostic imaging, personalized medicine, virtual assistants, administrative efficiency, predictive analytics, and surgical robotics. It also highlighted recent trends such as the impact of generative AI, regulatory scrutiny, interoperability challenges, the focus on explainability (XAI), and AI for mental health. The agent then recommended several sources for staying updated.\\n\\nFollowing this, the user inquired about new developments specifically in drug discovery. The AI agent detailed advancements in target identification, novel molecule design and generation (focusing on Generative AI for De Novo Design), enhanced preclinical testing, improved clinical trial design, and drug repurposing. It mentioned key AI-powered companies in this space and outlined remaining challenges.\\n\\nFinally, the user asked for more information about the second development mentioned previously, which was \"Novel Molecule Design and Generation\" with a focus on \"Generative AI for De Novo Design.\" The AI agent explained what de novo design is, how generative AI techniques like GANs and VAEs are used to learn molecular grammar and generate new structures, and why this approach is a significant development due to its speed, scale, and ability to design for specific properties, thereby transforming how medicines are designed.', 'thought': None, 'thought_signature': None, 'video_metadata': None}], 'role': 'model'}}, end_of_agent=None, agent_state=None, rewind_before_invocation_id=None) long_running_tool_ids=set() branch=None id='50495cdf-7bf1-4cb5-a604-b76b4b5947e0' timestamp=1763041941.893244\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.4 What you've accomplished: Automatic Context Management\n",
        "\n",
        "You just found the proof! The presence of that special summary `Event` in your session's history is the tangible result of the compaction process.\n",
        "\n",
        "**Let's recap what you just witnessed:**\n",
        "\n",
        "1.  **Silent Operation**: You ran a standard conversation, and from the outside, nothing seemed different.\n",
        "2.  **Background Compaction**: Because you configured the `App` with `EventsCompactionConfig`, the ADK `Runner` automatically monitored the conversation length. Once the threshold was met, it triggered the summarization process in the background.\n",
        "3.  **Verified Result**: By inspecting the session's events, you found the summary that the LLM generated. This summary now replaces the older, more verbose turns in the agent's active context.\n",
        "\n",
        "**For all future turns in this conversation, the agent will be given this concise summary instead of the full history.** This saves costs, improves performance, and helps the agent stay focused on what's most important.\n"
      ],
      "metadata": {
        "id": "1OkggqEex6Fi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.5 More Context Engineering options in ADK\n",
        "\n",
        "#### 👉 Custom Compaction\n",
        "In this example, we used ADK's default summarizer. For more advanced use cases, you can provide your own by defining a custom `SlidingWindowCompactor` and passing it to the config. This allows you to control the summarization prompt or even use a different, specialized LLM for the task. You can read more about it in the [official documentation](https://google.github.io/adk-docs/context/compaction/).\n",
        "\n",
        "#### 👉 Context Caching\n",
        "ADK also provides **Context Caching** to help reduce the token size of the static instructions that are fed to the LLM by caching the request data. Read more about it [here](https://google.github.io/adk-docs/context/caching/)."
      ],
      "metadata": {
        "id": "ra19kHu9x6Fi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### The Problem\n",
        "\n",
        "While we can do Context Compaction and use a database to resume a session, we face new challenges now. In some cases, **we have key information or preferences that we want to share across other sessions.**\n",
        "\n",
        "In these scenarios, instead of sharing the entire session history, transferring information from a few key variables can improve the session experience. Let's see how to do it!"
      ],
      "metadata": {
        "id": "0u5JhjFRx6Fi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🤝 Section 5: Working with Session State\n",
        "\n",
        "### 5.1 Creating custom tools for Session state management\n",
        "\n",
        "Let's explore how to manually manage session state through custom tools. In this example, we'll identify a **transferable characteristic**, like a user's name and their country, and create tools to capture and save it.\n",
        "\n",
        "**Why This Example?**\n",
        "\n",
        "The username is a perfect example of information that:\n",
        "\n",
        "- Is introduced once but referenced multiple times\n",
        "- Should persist throughout a conversation\n",
        "- Represents a user-specific characteristic that enhances personalization\n",
        "\n",
        "Here, for demo purposes, we'll create two tools that can store and retrieve user name and country from the Session State. **Note that all tools have access to the `ToolContext` object.** You don't have to create separate tools for each piece of information you want to share."
      ],
      "metadata": {
        "id": "e2Uy-Mh-x6Fi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define scope levels for state keys (following best practices)\n",
        "USER_NAME_SCOPE_LEVELS = (\"temp\", \"user\", \"app\")\n",
        "\n",
        "\n",
        "# This demonstrates how tools can write to session state using tool_context.\n",
        "# The 'user:' prefix indicates this is user-specific data.\n",
        "def save_userinfo(\n",
        "    tool_context: ToolContext, user_name: str, country: str\n",
        ") -> Dict[str, Any]:\n",
        "    \"\"\"\n",
        "    Tool to record and save user name and country in session state.\n",
        "\n",
        "    Args:\n",
        "        user_name: The username to store in session state\n",
        "        country: The name of the user's country\n",
        "    \"\"\"\n",
        "    # Write to session state using the 'user:' prefix for user data\n",
        "    tool_context.state[\"user:name\"] = user_name\n",
        "    tool_context.state[\"user:country\"] = country\n",
        "\n",
        "    return {\"status\": \"success\"}\n",
        "\n",
        "\n",
        "# This demonstrates how tools can read from session state.\n",
        "def retrieve_userinfo(tool_context: ToolContext) -> Dict[str, Any]:\n",
        "    \"\"\"\n",
        "    Tool to retrieve user name and country from session state.\n",
        "    \"\"\"\n",
        "    # Read from session state\n",
        "    user_name = tool_context.state.get(\"user:name\", \"Username not found\")\n",
        "    country = tool_context.state.get(\"user:country\", \"Country not found\")\n",
        "\n",
        "    return {\"status\": \"success\", \"user_name\": user_name, \"country\": country}\n",
        "\n",
        "\n",
        "print(\"✅ Tools created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T14:22:43.083944Z",
          "iopub.execute_input": "2025-11-13T14:22:43.085585Z",
          "iopub.status.idle": "2025-11-13T14:22:43.10007Z",
          "shell.execute_reply.started": "2025-11-13T14:22:43.085544Z",
          "shell.execute_reply": "2025-11-13T14:22:43.097757Z"
        },
        "id": "-9OldsMzx6Fj",
        "outputId": "0a5a26c2-4e32-4291-eefe-0853b96bd5d9"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Tools created.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Key Concepts:**\n",
        "- Tools can access `tool_context.state` to read/write session state\n",
        "- Use descriptive key prefixes (`user:`, `app:`, `temp:`) for organization\n",
        "- State persists across conversation turns within the same session"
      ],
      "metadata": {
        "id": "D5iFqViax6Fj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.2 Creating an Agent with Session State Tools\n",
        "\n",
        "Now let's create a new agent that has access to our session state management tools:"
      ],
      "metadata": {
        "id": "lrCPu4inx6Fj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Configuration\n",
        "APP_NAME = \"default\"\n",
        "USER_ID = \"default\"\n",
        "MODEL_NAME = \"gemini-2.5-flash-lite\"\n",
        "\n",
        "# Create an agent with session state tools\n",
        "root_agent = LlmAgent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"text_chat_bot\",\n",
        "    description=\"\"\"A text chatbot.\n",
        "    Tools for managing user context:\n",
        "    * To record username and country when provided use `save_userinfo` tool.\n",
        "    * To fetch username and country when required use `retrieve_userinfo` tool.\n",
        "    \"\"\",\n",
        "    tools=[save_userinfo, retrieve_userinfo],  # Provide the tools to the agent\n",
        ")\n",
        "\n",
        "# Set up session service and runner\n",
        "session_service = InMemorySessionService()\n",
        "runner = Runner(agent=root_agent, session_service=session_service, app_name=\"default\")\n",
        "\n",
        "print(\"✅ Agent with session state tools initialized!\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T14:23:17.37393Z",
          "iopub.execute_input": "2025-11-13T14:23:17.374301Z",
          "iopub.status.idle": "2025-11-13T14:23:17.387663Z",
          "shell.execute_reply.started": "2025-11-13T14:23:17.374274Z",
          "shell.execute_reply": "2025-11-13T14:23:17.386407Z"
        },
        "id": "OWCas1m8x6Fj",
        "outputId": "18139e8a-d2a3-4ab7-c012-0fea3fadb04e"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Agent with session state tools initialized!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.3 Testing Session State in Action\n",
        "\n",
        "Let's test how the agent uses session state to remember information across conversation turns:"
      ],
      "metadata": {
        "id": "SajJ7RDVx6Fj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Test conversation demonstrating session state\n",
        "await run_session(\n",
        "    runner,\n",
        "    [\n",
        "        \"Hi there, how are you doing today? What is my name?\",  # Agent shouldn't know the name yet\n",
        "        \"My name is Sam. I'm from Poland.\",  # Provide name - agent should save it\n",
        "        \"What is my name? Which country am I from?\",  # Agent should recall from session state\n",
        "    ],\n",
        "    \"state-demo-session\",\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T14:23:25.077798Z",
          "iopub.execute_input": "2025-11-13T14:23:25.078202Z",
          "iopub.status.idle": "2025-11-13T14:23:28.260608Z",
          "shell.execute_reply.started": "2025-11-13T14:23:25.078176Z",
          "shell.execute_reply": "2025-11-13T14:23:28.259565Z"
        },
        "id": "dcvcEEGex6Fk",
        "outputId": "d008fb1e-cdc1-45ec-dfa3-4db36cca3e08"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n ### Session: state-demo-session\n\nUser > Hi there, how are you doing today? What is my name?\ngemini-2.5-flash-lite >  Hello! I'm doing well, thank you for asking. I can't tell you your name just yet, as I don't have that information stored. If you'd like to tell me your name, I can remember it for you!\n\nUser > My name is Sam. I'm from Poland.\n",
          "output_type": "stream"
        },
        {
          "name": "stderr",
          "text": "WARNING:google_genai.types:Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.\n",
          "output_type": "stream"
        },
        {
          "name": "stdout",
          "text": "gemini-2.5-flash-lite >  It's nice to meet you, Sam! I'll save your name and country.\ngemini-2.5-flash-lite >  I have saved that you are Sam from Poland.\n\nUser > What is my name? Which country am I from?\n",
          "output_type": "stream"
        },
        {
          "name": "stderr",
          "text": "WARNING:google_genai.types:Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.\n",
          "output_type": "stream"
        },
        {
          "name": "stdout",
          "text": "gemini-2.5-flash-lite >  Your name is Sam and you are from Poland.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.4 Inspecting Session State\n",
        "\n",
        "Let's directly inspect the session state to see what's stored:"
      ],
      "metadata": {
        "id": "sXsPMDg-x6Fk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Retrieve the session and inspect its state\n",
        "session = await session_service.get_session(\n",
        "    app_name=APP_NAME, user_id=USER_ID, session_id=\"state-demo-session\"\n",
        ")\n",
        "\n",
        "print(\"Session State Contents:\")\n",
        "print(session.state)\n",
        "print(\"\\n🔍 Notice the 'user:name' and 'user:country' keys storing our data!\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T14:23:53.072714Z",
          "iopub.execute_input": "2025-11-13T14:23:53.073677Z",
          "iopub.status.idle": "2025-11-13T14:23:53.081746Z",
          "shell.execute_reply.started": "2025-11-13T14:23:53.073631Z",
          "shell.execute_reply": "2025-11-13T14:23:53.080565Z"
        },
        "id": "EfSy0guXx6Fk",
        "outputId": "adf14488-d63e-4d15-ed36-ef3e967e3f2b"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Session State Contents:\n{'user:name': 'Sam', 'user:country': 'Poland'}\n\n🔍 Notice the 'user:name' and 'user:country' keys storing our data!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.5 Session State Isolation\n",
        "\n",
        "As we've already seen, an important characteristic of session state is that it's isolated per session. Let's demonstrate this by starting a new session:"
      ],
      "metadata": {
        "id": "I8Y6gnvdx6Fk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Start a completely new session - the agent won't know our name\n",
        "await run_session(\n",
        "    runner,\n",
        "    [\"Hi there, how are you doing today? What is my name?\"],\n",
        "    \"new-isolated-session\",\n",
        ")\n",
        "\n",
        "# Expected: The agent won't know the name because this is a different session"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T14:24:41.081814Z",
          "iopub.execute_input": "2025-11-13T14:24:41.082155Z",
          "iopub.status.idle": "2025-11-13T14:24:41.707478Z",
          "shell.execute_reply.started": "2025-11-13T14:24:41.082131Z",
          "shell.execute_reply": "2025-11-13T14:24:41.706411Z"
        },
        "id": "B6AwtTDnx6Fk",
        "outputId": "50863d6a-170c-44b4-be70-89cdeb0b44a9"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n ### Session: new-isolated-session\n\nUser > Hi there, how are you doing today? What is my name?\ngemini-2.5-flash-lite >  Hello! I'm doing great. I'm a text chatbot, so I don't have feelings, but I'm ready to help.\n\nI don't know your name yet. Can you tell me what it is? If you'd like, you can also tell me your country, and I can remember it for next time.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.6 Cross-Session State Sharing\n",
        "\n",
        "While sessions are isolated by default, you might notice something interesting. Let's check the state of our new session (`new-isolated-session`):"
      ],
      "metadata": {
        "id": "M3koiW_mx6Fk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Check the state of the new session\n",
        "session = await session_service.get_session(\n",
        "    app_name=APP_NAME, user_id=USER_ID, session_id=\"new-isolated-session\"\n",
        ")\n",
        "\n",
        "print(\"New Session State:\")\n",
        "print(session.state)\n",
        "\n",
        "# Note: Depending on implementation, you might see shared state here.\n",
        "# This is where the distinction between session-specific and user-specific state becomes important."
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T14:25:46.577791Z",
          "iopub.execute_input": "2025-11-13T14:25:46.578199Z",
          "iopub.status.idle": "2025-11-13T14:25:46.58519Z",
          "shell.execute_reply.started": "2025-11-13T14:25:46.578173Z",
          "shell.execute_reply": "2025-11-13T14:25:46.583767Z"
        },
        "id": "_bDEAJ4bx6Fk",
        "outputId": "58d0ccd9-94dd-413d-a8bd-81d7dc5a3fbb"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "New Session State:\n{'user:name': 'Sam', 'user:country': 'Poland'}\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 🧹 Cleanup"
      ],
      "metadata": {
        "id": "lehgpLbTx6Fl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Clean up any existing database to start fresh (if Notebook is restarted)\n",
        "import os\n",
        "\n",
        "if os.path.exists(\"my_agent_data.db\"):\n",
        "    os.remove(\"my_agent_data.db\")\n",
        "print(\"✅ Cleaned up old database files\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T14:25:56.844757Z",
          "iopub.execute_input": "2025-11-13T14:25:56.845252Z",
          "iopub.status.idle": "2025-11-13T14:25:56.851976Z",
          "shell.execute_reply.started": "2025-11-13T14:25:56.845217Z",
          "shell.execute_reply": "2025-11-13T14:25:56.850651Z"
        },
        "id": "qPohz_zux6Fl",
        "outputId": "ed513f10-6e6a-4162-d0dc-eafb41167b9b"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Cleaned up old database files\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 📊 Summary\n",
        "\n",
        "🎉 Congratulations! You've learned the fundamentals of building stateful AI agents:\n",
        "\n",
        "- ✅ **Context Engineering** - You understand how to assemble context for LLMs using Context Compaction\n",
        "- ✅ **Sessions & Events** - You can maintain conversation history across multiple turns\n",
        "- ✅ **Persistent Storage** - You know how to make conversations survive restarts\n",
        "- ✅ **Session State** - You can track structured data during conversations\n",
        "- ✅ **Manual State Management** - You've experienced both the power and limitations of manual approaches\n",
        "- ✅ **Production Considerations** - You're ready to handle real-world challenges\n"
      ],
      "metadata": {
        "id": "mzK0Puyrx6Fl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## ✅ Congratulations! You did it 🎉\n",
        "\n",
        "**ℹ️ Note: No submission required!**\n",
        "\n",
        "This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "### 📚 Learn More\n",
        "\n",
        "Refer to the following documentation to learn more:\n",
        "\n",
        "- [ADK Documentation](https://google.github.io/adk-docs/)\n",
        "- [ADK Sessions](https://google.github.io/adk-docs/)\n",
        "- [ADK Session-State](https://medium.com/google-cloud/2-minute-adk-manage-context-efficiently-with-artifacts-6fcc6683d274)\n",
        "- [ADK Session Compaction](https://google.github.io/adk-docs/context/compaction/#define-compactor)\n",
        "\n",
        "### 🎯 Next Steps - Long Term Memory Systems (Part 2)\n",
        "\n",
        "#### Why do we need memory?\n",
        "In this notebook, we manually identified a couple characteristic (username and country) and built tools to manage it. But real conversations involve hundreds of such characteristics:\n",
        "- User preferences and habits\n",
        "- Past interactions and their outcomes\n",
        "- Domain knowledge and expertise levels\n",
        "- Communication styles and patterns\n",
        "- Contextual relationships between topics\n",
        "\n",
        "**The Memory System in ADK automates this entire process**, making it a valuable asset for building truly Context-Aware Agents that can accommodate any user's current and future needs.\n",
        "\n",
        "In the next notebook (Part 2: Memory Management), you'll learn how to:\n",
        "- Enable automatic memory extraction from conversations\n",
        "- Build agents that learn and adapt over time\n",
        "- Create truly personalized experiences at scale\n",
        "- Manage long-term knowledge across sessions\n",
        "\n",
        "Ready to transform your manual state management into an intelligent, automated Memory system? Let's continue to Part 2!"
      ],
      "metadata": {
        "id": "0RdOMBPmx6Fl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "| Authors |\n",
        "| --- |\n",
        "| [Sampath M](https://www.linkedin.com/in/msampathkumar/) |"
      ],
      "metadata": {
        "id": "oOEaN0iHx6Fl"
      }
    }
  ]
}

---



# Log: Day_3b_Agent_Memory.txt

{
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.13",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [],
      "isInternetEnabled": true,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "##### Copyright 2025 Google LLC."
      ],
      "metadata": {
        "id": "Gj_iNrkUyMBT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-11T06:24:39.733202Z",
          "iopub.execute_input": "2025-11-11T06:24:39.733552Z",
          "iopub.status.idle": "2025-11-11T06:24:39.739735Z",
          "shell.execute_reply.started": "2025-11-11T06:24:39.733524Z",
          "shell.execute_reply": "2025-11-11T06:24:39.738304Z"
        },
        "id": "h0z0ZMB-yMBU"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 🧠 Memory Management - Part 2 - Memory\n",
        "\n",
        "**Welcome to Day 3 of the Kaggle 5-day Agents course!**\n",
        "\n",
        "In the previous notebook, you learned how **Sessions** manage conversation threads. Now you'll add **Memory** - a searchable, long-term knowledge store that persists across multiple conversations.\n",
        "\n",
        "### What is Memory ❓\n",
        "\n",
        "Memory is a service that provides long-term knowledge storage for your agents. The key distinction:\n",
        "\n",
        "> **Session = Short-term memory** (single conversation)\n",
        ">\n",
        "> **Memory = Long-term knowledge** (across multiple conversations)\n",
        "\n",
        "Think of it in software engineering terms: **Session** is like application state (temporary), while **Memory** is like a database (persistent)."
      ],
      "metadata": {
        "id": "73BhgjquyMBV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 🤔 Why Memory?\n",
        "\n",
        "Memory provides capabilities that Sessions alone cannot:\n",
        "\n",
        "| Capability | What It Means | Example |\n",
        "|------------|---------------|---------|\n",
        "| **Cross-Conversation Recall** | Access information from any past conversation | \"What preferences has this user mentioned across all chats?\" |\n",
        "| **Intelligent Extraction** | LLM-powered consolidation extracts key facts | Stores \"allergic to peanuts\" instead of 50 raw messages |\n",
        "| **Semantic Search** | Meaning-based retrieval, not just keyword matching | Query \"preferred hue\" matches \"favorite color is blue\" |\n",
        "| **Persistent Storage** | Survives application restarts | Build knowledge that grows over time |\n",
        "\n",
        "**Example:** Imagine talking to a personal assistant:\n",
        "- 🗣️ **Session**: They remember what you said 10 minutes ago in THIS conversation\n",
        "- 🧠 **Memory**: They remember your preferences from conversations LAST WEEK"
      ],
      "metadata": {
        "id": "J_QEwOLUyMBW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 🎯 What you'll learn:\n",
        "\n",
        "- ✅ Initialize MemoryService and integrate with your agent\n",
        "- ✅ Transfer session data to memory storage\n",
        "- ✅ Search and retrieve memories\n",
        "- ✅ Automate memory storage and retrieval\n",
        "- ✅ Understand memory consolidation (conceptual overview)\n",
        "\n",
        "#### 📝 Implementation Note\n",
        "\n",
        "> This notebook uses `InMemoryMemoryService` for learning - it performs keyword matching and doesn't persist data.\n",
        ">\n",
        "> For production applications, use **Vertex AI Memory Bank** (covered in Day 5), which provides LLM-powered consolidation and semantic search with persistent cloud storage."
      ],
      "metadata": {
        "id": "J2rskHIhyMBW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ‼️ Please Read\n",
        "\n",
        "\n",
        "> ❌ **ℹ️ Note: No submission required!**\n",
        "> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n",
        "\n",
        "> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n",
        "\n",
        "**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**"
      ],
      "metadata": {
        "id": "P5XlIoUbyMBX"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "9XfWvbAtyMBY"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 📖 Get started with Kaggle Notebooks\n",
        "\n",
        "If this is your first time using Kaggle Notebooks, welcome! You can learn more about using Kaggle Notebooks [in the documentation](https://www.kaggle.com/docs/notebooks).\n",
        "\n",
        "Here's how to get started:\n",
        "\n",
        "**1. Verify Your Account (Required)**\n",
        "\n",
        "To use the Kaggle Notebooks in this course, you'll need to verify your account with a phone number.\n",
        "\n",
        "You can do this in your [Kaggle settings](https://www.kaggle.com/settings).\n",
        "\n",
        "**2. Make Your Own Copy**\n",
        "\n",
        "To run any code in this notebook, you first need your own editable copy.\n",
        "\n",
        "Click the `Copy and Edit` button in the top-right corner.\n",
        "\n",
        "![Copy and Edit button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_1.png)\n",
        "\n",
        "This creates a private copy of the notebook just for you.\n",
        "\n",
        "**3. Run Code Cells**\n",
        "\n",
        "Once you have your copy, you can run code.\n",
        "\n",
        "Click the ▶️ Run button next to any code cell to execute it.\n",
        "\n",
        "![Run cell button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_2.png)\n",
        "\n",
        "Run the cells in order from top to bottom.\n",
        "\n",
        "**4. If You Get Stuck**\n",
        "\n",
        "To restart: Select `Factory reset` from the `Run` menu.\n",
        "\n",
        "For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server."
      ],
      "metadata": {
        "id": "piluvEUEyMBZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## ⚙️ Section 1: Setup\n",
        "\n",
        "### 1.1: Install dependencies\n",
        "\n",
        "The Kaggle Notebooks environment includes a pre-installed version of the [google-adk](https://google.github.io/adk-docs/) library for Python and its required dependencies, so you don't need to install additional packages in this notebook.\n",
        "\n",
        "To install and use ADK in your own Python development environment outside of this course, you can do so by running:\n",
        "\n",
        "```\n",
        "pip install google-adk\n",
        "```"
      ],
      "metadata": {
        "id": "tX_0NV-ayMBZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.2: Configure your Gemini API Key\n",
        "\n",
        "This notebook uses the [Gemini API](https://ai.google.dev/gemini-api/docs), which requires authentication.\n",
        "\n",
        "**1. Get your API key**\n",
        "\n",
        "If you don't have one already, create an [API key in Google AI Studio](https://aistudio.google.com/app/api-keys).\n",
        "\n",
        "**2. Add the key to Kaggle Secrets**\n",
        "\n",
        "Next, you will need to add your API key to your Kaggle Notebook as a Kaggle User Secret.\n",
        "\n",
        "1. In the top menu bar of the notebook editor, select `Add-ons` then `Secrets`.\n",
        "2. Create a new secret with the label `GOOGLE_API_KEY`.\n",
        "3. Paste your API key into the \"Value\" field and click \"Save\".\n",
        "4. Ensure that the checkbox next to `GOOGLE_API_KEY` is selected so that the secret is attached to the notebook.\n",
        "\n",
        "**3. Authenticate in the notebook**\n",
        "\n",
        "Run the cell below to complete authentication."
      ],
      "metadata": {
        "id": "mpoi7jBoyMBa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from kaggle_secrets import UserSecretsClient\n",
        "\n",
        "try:\n",
        "    GOOGLE_API_KEY = UserSecretsClient().get_secret(\"GOOGLE_API_KEY\")\n",
        "    os.environ[\"GOOGLE_API_KEY\"] = GOOGLE_API_KEY\n",
        "    print(\"✅ Gemini API key setup complete.\")\n",
        "except Exception as e:\n",
        "    print(\n",
        "        f\"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}\"\n",
        "    )"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:06:16.278807Z",
          "iopub.execute_input": "2025-11-13T16:06:16.279289Z",
          "iopub.status.idle": "2025-11-13T16:06:16.350494Z",
          "shell.execute_reply.started": "2025-11-13T16:06:16.279264Z",
          "shell.execute_reply": "2025-11-13T16:06:16.349588Z"
        },
        "id": "Hafs_1AeyMBb",
        "outputId": "b99dc5d3-a1ab-4939-97c6-ce5f36e9910c"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Gemini API key setup complete.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.3: Import ADK components\n",
        "\n",
        "Now, import the specific components you'll need from the Agent Development Kit and the Generative AI library. This keeps your code organized and ensures we have access to the necessary building blocks."
      ],
      "metadata": {
        "id": "yVOVNfRsyMBb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.adk.agents import LlmAgent\n",
        "from google.adk.models.google_llm import Gemini\n",
        "from google.adk.runners import Runner\n",
        "from google.adk.sessions import InMemorySessionService\n",
        "from google.adk.memory import InMemoryMemoryService\n",
        "from google.adk.tools import load_memory, preload_memory\n",
        "from google.genai import types\n",
        "\n",
        "print(\"✅ ADK components imported successfully.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:06:21.502805Z",
          "iopub.execute_input": "2025-11-13T16:06:21.503121Z",
          "iopub.status.idle": "2025-11-13T16:07:05.100012Z",
          "shell.execute_reply.started": "2025-11-13T16:06:21.503094Z",
          "shell.execute_reply": "2025-11-13T16:07:05.099199Z"
        },
        "id": "5Mjw0vdTyMBc",
        "outputId": "04b43fe2-a441-4328-e88d-94ce18a06881"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ ADK components imported successfully.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.4: Helper functions\n",
        "\n",
        "This helper function manages a complete conversation session, handling session creation/retrieval, query processing, and response streaming."
      ],
      "metadata": {
        "id": "vpIs1TrEyMBd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "async def run_session(\n",
        "    runner_instance: Runner, user_queries: list[str] | str, session_id: str = \"default\"\n",
        "):\n",
        "    \"\"\"Helper function to run queries in a session and display responses.\"\"\"\n",
        "    print(f\"\\n### Session: {session_id}\")\n",
        "\n",
        "    # Create or retrieve session\n",
        "    try:\n",
        "        session = await session_service.create_session(\n",
        "            app_name=APP_NAME, user_id=USER_ID, session_id=session_id\n",
        "        )\n",
        "    except:\n",
        "        session = await session_service.get_session(\n",
        "            app_name=APP_NAME, user_id=USER_ID, session_id=session_id\n",
        "        )\n",
        "\n",
        "    # Convert single query to list\n",
        "    if isinstance(user_queries, str):\n",
        "        user_queries = [user_queries]\n",
        "\n",
        "    # Process each query\n",
        "    for query in user_queries:\n",
        "        print(f\"\\nUser > {query}\")\n",
        "        query_content = types.Content(role=\"user\", parts=[types.Part(text=query)])\n",
        "\n",
        "        # Stream agent response\n",
        "        async for event in runner_instance.run_async(\n",
        "            user_id=USER_ID, session_id=session.id, new_message=query_content\n",
        "        ):\n",
        "            if event.is_final_response() and event.content and event.content.parts:\n",
        "                text = event.content.parts[0].text\n",
        "                if text and text != \"None\":\n",
        "                    print(f\"Model: > {text}\")\n",
        "\n",
        "\n",
        "print(\"✅ Helper functions defined.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:08:05.843945Z",
          "iopub.execute_input": "2025-11-13T16:08:05.845627Z",
          "iopub.status.idle": "2025-11-13T16:08:05.854214Z",
          "shell.execute_reply.started": "2025-11-13T16:08:05.845596Z",
          "shell.execute_reply": "2025-11-13T16:08:05.853452Z"
        },
        "id": "SBNtzvKCyMBd",
        "outputId": "51fae04b-30d3-4711-c692-15f8facccc27"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Helper functions defined.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.5: Configure Retry Options\n",
        "\n",
        "When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff."
      ],
      "metadata": {
        "id": "TJDLZc5UyMBd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "retry_config = types.HttpRetryOptions(\n",
        "    attempts=5,  # Maximum retry attempts\n",
        "    exp_base=7,  # Delay multiplier\n",
        "    initial_delay=1,\n",
        "    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:23:51.643248Z",
          "iopub.execute_input": "2025-11-13T16:23:51.646004Z",
          "iopub.status.idle": "2025-11-13T16:23:51.657416Z",
          "shell.execute_reply.started": "2025-11-13T16:23:51.645923Z",
          "shell.execute_reply": "2025-11-13T16:23:51.656322Z"
        },
        "id": "Ob_A3BF_yMBe"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🤓 Section 2: Memory Workflow\n",
        "\n",
        "From the Introduction section, you now know why we need Memory. In order to integrate Memory into your Agents, there are **three high-level steps.**\n",
        "\n",
        "**Three-step integration process:**\n",
        "\n",
        "1. **Initialize** → Create a `MemoryService` and provide it to your agent via the `Runner`\n",
        "2. **Ingest** → Transfer session data to memory using `add_session_to_memory()`\n",
        "3. **Retrieve** → Search stored memories using `search_memory()`\n",
        "\n",
        "Let's explore each step in the following sections."
      ],
      "metadata": {
        "id": "NUbr4HH1yMBe"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day3/memory-workflow.png\" width=\"1400\" alt=\"Memory workflow\">"
      ],
      "metadata": {
        "id": "zQyq8IkPyMBe"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🧠 Section 3: Initialize MemoryService"
      ],
      "metadata": {
        "id": "CSiUfJzOyMBe"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.1 Initialize Memory\n",
        "\n",
        "ADK provides multiple `MemoryService` implementations through the `BaseMemoryService` interface:\n",
        "\n",
        "- **`InMemoryMemoryService`** - Built-in service for prototyping and testing (keyword matching, no persistence)\n",
        "- **`VertexAiMemoryBankService`** - Managed cloud service with LLM-powered consolidation and semantic search\n",
        "- **Custom implementations** - You can build your own using databases, though managed services are recommended\n",
        "\n",
        "For this notebook, we'll use `InMemoryMemoryService` to learn the core mechanics. The same methods work identically with production-ready services like Vertex AI Memory Bank."
      ],
      "metadata": {
        "id": "p64WibTZyMBe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "memory_service = (\n",
        "    InMemoryMemoryService()\n",
        ")  # ADK's built-in Memory Service for development and testing"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:23:56.857992Z",
          "iopub.execute_input": "2025-11-13T16:23:56.858603Z",
          "iopub.status.idle": "2025-11-13T16:23:56.862614Z",
          "shell.execute_reply.started": "2025-11-13T16:23:56.858579Z",
          "shell.execute_reply": "2025-11-13T16:23:56.861544Z"
        },
        "id": "XOY7U5VlyMBe"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.2 Add Memory to Agent\n",
        "\n",
        "Next, create a simple agent to answer user queries."
      ],
      "metadata": {
        "id": "TL3IQuZmyMBf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define constants used throughout the notebook\n",
        "APP_NAME = \"MemoryDemoApp\"\n",
        "USER_ID = \"demo_user\"\n",
        "\n",
        "# Create agent\n",
        "user_agent = LlmAgent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"MemoryDemoAgent\",\n",
        "    instruction=\"Answer user questions in simple words.\",\n",
        ")\n",
        "\n",
        "print(\"✅ Agent created\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:24:09.219894Z",
          "iopub.execute_input": "2025-11-13T16:24:09.220256Z",
          "iopub.status.idle": "2025-11-13T16:24:09.227429Z",
          "shell.execute_reply.started": "2025-11-13T16:24:09.220233Z",
          "shell.execute_reply": "2025-11-13T16:24:09.226453Z"
        },
        "id": "iB9mkNZWyMBf",
        "outputId": "826ca1df-961e-4543-a3e4-84af49982c04"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Agent created\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### **Create Runner**\n",
        "\n",
        "Now provide both Session and Memory services to the `Runner`.\n",
        "\n",
        "**Key configuration:**\n",
        "\n",
        "The `Runner` requires both services to enable memory functionality:\n",
        "- **`session_service`** → Manages conversation threads and events\n",
        "- **`memory_service`** → Provides long-term knowledge storage\n",
        "\n",
        "Both services work together: Sessions capture conversations, Memory stores knowledge for retrieval across sessions."
      ],
      "metadata": {
        "id": "ijV3O85YyMBf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Create Session Service\n",
        "session_service = InMemorySessionService()  # Handles conversations\n",
        "\n",
        "# Create runner with BOTH services\n",
        "runner = Runner(\n",
        "    agent=user_agent,\n",
        "    app_name=\"MemoryDemoApp\",\n",
        "    session_service=session_service,\n",
        "    memory_service=memory_service,  # Memory service is now available!\n",
        ")\n",
        "\n",
        "print(\"✅ Agent and Runner created with memory support!\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:25:01.741079Z",
          "iopub.execute_input": "2025-11-13T16:25:01.741618Z",
          "iopub.status.idle": "2025-11-13T16:25:01.7483Z",
          "shell.execute_reply.started": "2025-11-13T16:25:01.741592Z",
          "shell.execute_reply": "2025-11-13T16:25:01.747465Z"
        },
        "id": "ASXXKeYqyMBf",
        "outputId": "4db44c74-83dc-4a64-e58a-1095a515105c"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Agent and Runner created with memory support!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### ‼️ Important\n",
        "\n",
        "**💡 Configuration vs. Usage:** Adding `memory_service` to the `Runner` makes memory *available* to your agent, but doesn't automatically use it. You must explicitly:\n",
        "1. **Ingest data** using `add_session_to_memory()`\n",
        "2. **Enable retrieval** by giving your agent memory tools (`load_memory` or `preload_memory`)\n",
        "\n",
        "Let's learn these steps next!"
      ],
      "metadata": {
        "id": "8224I4GOyMBf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.3 MemoryService Implementation Options\n",
        "\n",
        "**This notebook: `InMemoryMemoryService`**\n",
        "- Stores raw conversation events without consolidation\n",
        "- Keyword-based search (simple word matching)\n",
        "- In-memory storage (resets on restart)\n",
        "- Ideal for learning and local development\n",
        "\n",
        "**Production: `VertexAiMemoryBankService` (You'll learn this on Day 5)**\n",
        "- LLM-powered extraction of key facts\n",
        "- Semantic search (meaning-based retrieval)\n",
        "- Persistent cloud storage\n",
        "- Integrates external knowledge sources\n",
        "\n",
        "**💡 API Consistency:** Both implementations use identical methods (`add_session_to_memory()`, `search_memory()`). The workflow you learn here applies to all memory services!"
      ],
      "metadata": {
        "id": "3Z0GPp5OyMBf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 💾 Section 4: Ingest Session Data into Memory"
      ],
      "metadata": {
        "id": "pZ8K2QoFyMBf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Why should you transfer Session data to Memory?**\n",
        "\n",
        "Now that memory is initialized, you need to populate it with knowledge. When you initialize a MemoryService, it starts completely empty. All your conversations are stored in Sessions, which contain raw events including every message, tool call, and metadata. To make this information available for long-term recall, you explicitly transfer it to memory using `add_session_to_memory()`.\n",
        "\n",
        "Here's where managed memory services like Vertex AI Memory Bank shine. **During transfer, they perform intelligent consolidation - extracting key facts while discarding conversational noise.** The `InMemoryMemoryService` we're using stores everything without consolidation, which is sufficient for learning the mechanics."
      ],
      "metadata": {
        "id": "1wqgvnRCyMBf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Before we can transfer anything, we need data. Let's have a conversation with our agent to populate the session. This conversation will be stored in the SessionService just like you learned in the previous notebook."
      ],
      "metadata": {
        "id": "8eeUkixByMBf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# User tells agent about their favorite color\n",
        "await run_session(\n",
        "    runner,\n",
        "    \"My favorite color is blue-green. Can you write a Haiku about it?\",\n",
        "    \"conversation-01\",  # Session ID\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:27:10.268701Z",
          "iopub.execute_input": "2025-11-13T16:27:10.269033Z",
          "iopub.status.idle": "2025-11-13T16:27:11.7Z",
          "shell.execute_reply.started": "2025-11-13T16:27:10.269009Z",
          "shell.execute_reply": "2025-11-13T16:27:11.698991Z"
        },
        "id": "k9T4U6f2yMBg",
        "outputId": "414db77a-1f04-4f49-f56c-8c5873dcc365"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n### Session: conversation-01\n\nUser > My favorite color is blue-green. Can you write a Haiku about it?\nModel: > Sure, here is a haiku about your favorite color:\n\nSea and sky's soft blend,\nNature's calm and cool embrace,\nPeaceful, deep, and true.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let's verify the conversation was captured in the session. You should see the session events containing both the user's prompt and the model's response."
      ],
      "metadata": {
        "id": "hYRcf0u0yMBg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "session = await session_service.get_session(\n",
        "    app_name=APP_NAME, user_id=USER_ID, session_id=\"conversation-01\"\n",
        ")\n",
        "\n",
        "# Let's see what's in the session\n",
        "print(\"📝 Session contains:\")\n",
        "for event in session.events:\n",
        "    text = (\n",
        "        event.content.parts[0].text[:60]\n",
        "        if event.content and event.content.parts\n",
        "        else \"(empty)\"\n",
        "    )\n",
        "    print(f\"  {event.content.role}: {text}...\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:27:32.645976Z",
          "iopub.execute_input": "2025-11-13T16:27:32.646303Z",
          "iopub.status.idle": "2025-11-13T16:27:32.652968Z",
          "shell.execute_reply.started": "2025-11-13T16:27:32.646273Z",
          "shell.execute_reply": "2025-11-13T16:27:32.651659Z"
        },
        "id": "Ba0iF79yyMBg",
        "outputId": "29992766-f3a5-4294-bc15-3cff5f908eaa"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "📝 Session contains:\n  user: My favorite color is blue-green. Can you write a Haiku about...\n  model: Sure, here is a haiku about your favorite color:\n\nSea and sk...\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Perfect! The session contains our conversation. Now we're ready to transfer it to memory. Call `add_session_to_memory()` and pass the session object. This ingests the conversation into the memory store, making it available for future searches."
      ],
      "metadata": {
        "id": "W7ftSU8SyMBg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# This is the key method!\n",
        "await memory_service.add_session_to_memory(session)\n",
        "\n",
        "print(\"✅ Session added to memory!\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:27:47.054383Z",
          "iopub.execute_input": "2025-11-13T16:27:47.05474Z",
          "iopub.status.idle": "2025-11-13T16:27:47.060283Z",
          "shell.execute_reply.started": "2025-11-13T16:27:47.054716Z",
          "shell.execute_reply": "2025-11-13T16:27:47.059167Z"
        },
        "id": "n0VeIdTAyMBh",
        "outputId": "781e69d8-2ad6-4a27-a249-9bf3b4512286"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Session added to memory!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🔎 Section 5: Enable Memory Retrieval in Your Agent\n",
        "\n",
        "You've successfully transferred session data to memory, but there's one crucial step remaining. **Agents can't directly access the MemoryService - they need tools to search it.**\n",
        "\n",
        "This is by design: it gives you control over when and how memory is retrieved."
      ],
      "metadata": {
        "id": "voQE10YiyMBh"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.1 Memory Retrieval in ADK\n",
        "\n",
        "ADK provides two built-in tools for memory retrieval:\n",
        "\n",
        "**`load_memory` (Reactive)**\n",
        "- Agent decides when to search memory\n",
        "- Only retrieves when the agent thinks it's needed\n",
        "- More efficient (saves tokens)\n",
        "- Risk: Agent might forget to search\n",
        "\n",
        "**`preload_memory` (Proactive)**\n",
        "- Automatically searches before every turn\n",
        "- Memory always available to the agent\n",
        "- Guaranteed context, but less efficient\n",
        "- Searches even when not needed\n",
        "\n",
        "Think of it like studying for an exam: `load_memory` is looking things up only when you need them, while `preload_memory` is reading all your notes before answering each question."
      ],
      "metadata": {
        "id": "Zri5yLFAyMBh"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.2 Add Load Memory Tool to Agent\n",
        "\n",
        "Let's start by implementing the reactive pattern. We'll recreate the agent from Section 3, this time adding the `load_memory` tool to its toolkit. Since this is a built-in ADK tool, you simply include it in the tools array without any custom implementation."
      ],
      "metadata": {
        "id": "5xbWFOOHyMBh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Create agent\n",
        "user_agent = LlmAgent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"MemoryDemoAgent\",\n",
        "    instruction=\"Answer user questions in simple words. Use load_memory tool if you need to recall past conversations.\",\n",
        "    tools=[\n",
        "        load_memory\n",
        "    ],  # Agent now has access to Memory and can search it whenever it decides to!\n",
        ")\n",
        "\n",
        "print(\"✅ Agent with load_memory tool created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:28:02.68519Z",
          "iopub.execute_input": "2025-11-13T16:28:02.685557Z",
          "iopub.status.idle": "2025-11-13T16:28:02.691434Z",
          "shell.execute_reply.started": "2025-11-13T16:28:02.68553Z",
          "shell.execute_reply": "2025-11-13T16:28:02.690353Z"
        },
        "id": "DktKMWTgyMBh",
        "outputId": "2108cdce-bd43-4bae-d083-8d0125efd69e"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Agent with load_memory tool created.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.3 Update the Runner and Test\n",
        "\n",
        "Let's now update the Runner to use our new `user_agent` that has the `load_memory` tool. And we'll ask the Agent about the favorite color which we had stored previously in another session.\n",
        "\n",
        "**👉 Since sessions don't share conversation history, the only way the agent can answer correctly is by using the `load_memory` tool** to retrieve the information from long-term memory that we manually stored."
      ],
      "metadata": {
        "id": "LSnxH-lnyMBi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a new runner with the updated agent\n",
        "runner = Runner(\n",
        "    agent=user_agent,\n",
        "    app_name=APP_NAME,\n",
        "    session_service=session_service,\n",
        "    memory_service=memory_service,\n",
        ")\n",
        "\n",
        "await run_session(runner, \"What is my favorite color?\", \"color-test\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:28:12.5197Z",
          "iopub.execute_input": "2025-11-13T16:28:12.520338Z",
          "iopub.status.idle": "2025-11-13T16:28:13.688953Z",
          "shell.execute_reply.started": "2025-11-13T16:28:12.520311Z",
          "shell.execute_reply": "2025-11-13T16:28:13.688107Z"
        },
        "id": "pCNJ_ZnFyMBi",
        "outputId": "4ddfda14-c027-41bb-bd31-5a305e43d8fd"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n### Session: color-test\n\nUser > What is my favorite color?\n",
          "output_type": "stream"
        },
        {
          "name": "stderr",
          "text": "WARNING:google_genai.types:Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.4 Complete Manual Workflow Test\n",
        "\n",
        "Let's see the complete workflow in action. We'll have a conversation about a birthday, manually save it to memory, then test retrieval in a new session. This demonstrates the full cycle: **ingest → store → retrieve**."
      ],
      "metadata": {
        "id": "P8SNAjxJyMBi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "await run_session(runner, \"My birthday is on March 15th.\", \"birthday-session-01\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:28:27.124987Z",
          "iopub.execute_input": "2025-11-13T16:28:27.125567Z",
          "iopub.status.idle": "2025-11-13T16:28:27.593111Z",
          "shell.execute_reply.started": "2025-11-13T16:28:27.125543Z",
          "shell.execute_reply": "2025-11-13T16:28:27.59222Z"
        },
        "id": "NliqHx-1yMBj",
        "outputId": "eecc3a07-db4e-4af0-b453-60d38fd703f5"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n### Session: birthday-session-01\n\nUser > My birthday is on March 15th.\nModel: > Okay, I will remember that your birthday is on March 15th.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Now manually save this session to memory. This is the crucial step that transfers the conversation from short-term session storage to long-term memory storage."
      ],
      "metadata": {
        "id": "dPal_fOWyMBj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Manually save the session to memory\n",
        "birthday_session = await session_service.get_session(\n",
        "    app_name=APP_NAME, user_id=USER_ID, session_id=\"birthday-session-01\"\n",
        ")\n",
        "\n",
        "await memory_service.add_session_to_memory(birthday_session)\n",
        "\n",
        "print(\"✅ Birthday session saved to memory!\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:28:35.776022Z",
          "iopub.execute_input": "2025-11-13T16:28:35.77634Z",
          "iopub.status.idle": "2025-11-13T16:28:35.781846Z",
          "shell.execute_reply.started": "2025-11-13T16:28:35.776318Z",
          "shell.execute_reply": "2025-11-13T16:28:35.781025Z"
        },
        "id": "kw7ZbAdEyMBj",
        "outputId": "4415e874-ddc8-47fc-f941-96669c4434ee"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Birthday session saved to memory!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "Here's the crucial test: we'll start a completely new session with a different session ID and ask the agent to recall the birthday."
      ],
      "metadata": {
        "id": "39HYr4MQyMBk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Test retrieval in a NEW session\n",
        "await run_session(\n",
        "    runner, \"When is my birthday?\", \"birthday-session-02\"  # Different session ID\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:28:40.387172Z",
          "iopub.execute_input": "2025-11-13T16:28:40.387515Z",
          "iopub.status.idle": "2025-11-13T16:28:41.43821Z",
          "shell.execute_reply.started": "2025-11-13T16:28:40.387494Z",
          "shell.execute_reply": "2025-11-13T16:28:41.437288Z"
        },
        "id": "wWIvIgDFyMBk",
        "outputId": "345aaead-bc48-45e1-a45c-e5eb3569a461"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n### Session: birthday-session-02\n\nUser > When is my birthday?\n",
          "output_type": "stream"
        },
        {
          "name": "stderr",
          "text": "WARNING:google_genai.types:Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.\n",
          "output_type": "stream"
        },
        {
          "name": "stdout",
          "text": "Model: > I was born on March 15th.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**What happens:**\n",
        "\n",
        "1. Agent receives: \"When is my birthday?\"\n",
        "2. Agent recognizes: This requires past conversation context\n",
        "3. Agent calls: `load_memory(\"birthday\")`\n",
        "4. Memory returns: Previous conversation containing \"March 15th\"\n",
        "5. Agent responds: \"Your birthday is on March 15th\"\n",
        "\n",
        "The memory retrieval worked even though this is a completely different session!"
      ],
      "metadata": {
        "id": "tu-8fpT1yMBk"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### 🚀 Your Turn: Experiment with Both Patterns\n",
        "\n",
        "Try swapping `load_memory` with `preload_memory` by changing the tools array to `tools=[preload_memory]`.\n",
        "\n",
        "**What changes:**\n",
        "- `load_memory` (reactive): Agent decides when to search\n",
        "- `preload_memory` (proactive): Automatically loads memory before every turn\n",
        "\n",
        "**Test it:**\n",
        "1. Ask \"What is my favorite color?\" in a new session\n",
        "2. Ask \"Tell me a joke\" - notice that `preload_memory` still searches memory even though it's unnecessary\n",
        "3. Which pattern is better for different use cases?"
      ],
      "metadata": {
        "id": "yMVhpOm9yMBl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.5 Manual Memory Search\n",
        "\n",
        "Beyond agent tools, you can also search memories directly in your code. This is useful for:\n",
        "- Debugging memory contents\n",
        "- Building analytics dashboards  \n",
        "- Creating custom memory management UIs\n",
        "\n",
        "The `search_memory()` method takes a text query and returns a `SearchMemoryResponse` with matching memories."
      ],
      "metadata": {
        "id": "s2iSDbshyMBl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Search for color preferences\n",
        "search_response = await memory_service.search_memory(\n",
        "    app_name=APP_NAME, user_id=USER_ID, query=\"What is the user's favorite color?\"\n",
        ")\n",
        "\n",
        "print(\"🔍 Search Results:\")\n",
        "print(f\"  Found {len(search_response.memories)} relevant memories\")\n",
        "print()\n",
        "\n",
        "for memory in search_response.memories:\n",
        "    if memory.content and memory.content.parts:\n",
        "        text = memory.content.parts[0].text[:80]\n",
        "        print(f\"  [{memory.author}]: {text}...\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:29:12.816064Z",
          "iopub.execute_input": "2025-11-13T16:29:12.816455Z",
          "iopub.status.idle": "2025-11-13T16:29:12.822705Z",
          "shell.execute_reply.started": "2025-11-13T16:29:12.816381Z",
          "shell.execute_reply": "2025-11-13T16:29:12.821935Z"
        },
        "id": "yaolDs0IyMBl",
        "outputId": "256fe8a7-5e11-4633-d933-ae0a3e86aef0"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "🔍 Search Results:\n  Found 4 relevant memories\n\n  [user]: My favorite color is blue-green. Can you write a Haiku about it?...\n  [MemoryDemoAgent]: Sure, here is a haiku about your favorite color:\n\nSea and sky's soft blend,\nNatu...\n  [user]: My birthday is on March 15th....\n  [MemoryDemoAgent]: Okay, I will remember that your birthday is on March 15th....\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### **🚀 Your Turn: Test Different Queries**\n",
        "\n",
        "Try these searches to understand how keyword matching works with `InMemoryMemoryService`:\n",
        "\n",
        "1. **\"what color does the user like\"**\n",
        "2. **\"haiku\"**\n",
        "3. **\"age\"**\n",
        "4. **\"preferred hue\"**\n",
        "\n",
        "Notice which queries return results and which don't. What pattern do you observe?\n",
        "\n",
        "**💡 Key Insight:** Memory search is grounded in reality - agents can't hallucinate memories that don't exist."
      ],
      "metadata": {
        "id": "KNeDkCjWyMBl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5.6 How Search Works\n",
        "\n",
        "**InMemoryMemoryService (this notebook):**\n",
        "- **Method:** Keyword matching\n",
        "- **Example:** \"favorite color\" matches because those exact words exist\n",
        "- **Limitation:** \"preferred hue\" won't match\n",
        "\n",
        "**VertexAiMemoryBankService (Day 5):**\n",
        "- **Method:** Semantic search via embeddings\n",
        "- **Example:** \"preferred hue\" WILL match \"favorite color\"\n",
        "- **Advantage:** Understands meaning, not just keywords\n",
        "\n",
        "You'll explore semantic search in Day 5!"
      ],
      "metadata": {
        "id": "nYqtM9EeyMBm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🤖 Section 6: Automating Memory Storage"
      ],
      "metadata": {
        "id": "K8LgVR8ryMBm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "So far, we've **manually** called `add_session_to_memory()` to transfer data to long-term storage. Production systems need this to happen **automatically**."
      ],
      "metadata": {
        "id": "6dB5jdwByMBm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 6.1 Callbacks\n",
        "\n",
        "ADK's callback system lets you hook into key execution moments. Callbacks are **Python functions** you define and attach to agents - ADK automatically calls them at specific stages, acting like checkpoints during the agent's execution flow.\n",
        "\n",
        "**Think of callbacks as event listeners in your agent's lifecycle.** When an agent processes a request, it goes through multiple stages: receiving the input, calling the LLM, invoking tools, and generating the response. Callbacks let you insert custom logic at each of these stages without modifying the core agent code.\n",
        "\n",
        "**Available callback types:**\n",
        "\n",
        "- `before_agent_callback` → Runs before agent starts processing a request\n",
        "- `after_agent_callback` → Runs after agent completes its turn  \n",
        "- `before_tool_callback` / `after_tool_callback` → Around tool invocations\n",
        "- `before_model_callback` / `after_model_callback` → Around LLM calls\n",
        "- `on_model_error_callback` → When errors occur\n",
        "\n",
        "**Common use cases:**\n",
        "\n",
        "- Logging and observability (track what the agent does)\n",
        "- Automatic data persistence (like saving to memory)\n",
        "- Custom validation or filtering\n",
        "- Performance monitoring\n",
        "\n",
        "**📚 Learn More:** [ADK Callbacks Documentation](https://google.github.io/adk-docs/agents/callbacks/)"
      ],
      "metadata": {
        "id": "glIxe9MlyMBm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "![image.png](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/types_of_callbacks.png)"
      ],
      "metadata": {
        "id": "6S0oH7bxyMBm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 6.2 Automatic Memory Storage with Callbacks\n",
        "\n",
        "For automatic memory storage, we'll use `after_agent_callback`. This function triggers every time the agent finishes a turn, then calls `add_session_to_memory()` to persist the conversation automatically.\n",
        "\n",
        "But here's the challenge: how does our callback function actually access the memory service and current session? That's where `callback_context` comes in.\n",
        "\n",
        "When you define a callback function, ADK automatically passes a special parameter called `callback_context` to it. The `callback_context` provides access to the Memory Service and other runtime components.\n",
        "\n",
        "**How we'll use it:** In our callback, we'll access the memory service and current session to automatically save conversation data after each turn.\n",
        "\n",
        "**💡 Important:** You don't create this context - ADK creates it and passes it to your callback automatically when the callback runs."
      ],
      "metadata": {
        "id": "xip-mBkMyMBm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "async def auto_save_to_memory(callback_context):\n",
        "    \"\"\"Automatically save session to memory after each agent turn.\"\"\"\n",
        "    await callback_context._invocation_context.memory_service.add_session_to_memory(\n",
        "        callback_context._invocation_context.session\n",
        "    )\n",
        "\n",
        "\n",
        "print(\"✅ Callback created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:29:41.448076Z",
          "iopub.execute_input": "2025-11-13T16:29:41.448373Z",
          "iopub.status.idle": "2025-11-13T16:29:41.453978Z",
          "shell.execute_reply.started": "2025-11-13T16:29:41.448354Z",
          "shell.execute_reply": "2025-11-13T16:29:41.453122Z"
        },
        "id": "5pG9spEEyMBn",
        "outputId": "b840c236-829a-4e06-90fc-b90a9fc59a11"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Callback created.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 6.3 Create an Agent: Callback and PreLoad Memory Tool\n",
        "\n",
        "Now create an agent that combines:\n",
        "- **Automatic storage:** `after_agent_callback` saves conversations\n",
        "- **Automatic retrieval:** `preload_memory` loads memories\n",
        "\n",
        "This creates a fully automated memory system with zero manual intervention."
      ],
      "metadata": {
        "id": "R93mT2dzyMBn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Agent with automatic memory saving\n",
        "auto_memory_agent = LlmAgent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"AutoMemoryAgent\",\n",
        "    instruction=\"Answer user questions.\",\n",
        "    tools=[preload_memory],\n",
        "    after_agent_callback=auto_save_to_memory,  # Saves after each turn!\n",
        ")\n",
        "\n",
        "print(\"✅ Agent created with automatic memory saving!\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:29:48.004349Z",
          "iopub.execute_input": "2025-11-13T16:29:48.004732Z",
          "iopub.status.idle": "2025-11-13T16:29:48.010617Z",
          "shell.execute_reply.started": "2025-11-13T16:29:48.004706Z",
          "shell.execute_reply": "2025-11-13T16:29:48.009779Z"
        },
        "id": "ZLD3VCdqyMBn",
        "outputId": "8bac01d9-6004-4db5-a441-16541f8d9443"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Agent created with automatic memory saving!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**What happens automatically:**\n",
        "\n",
        "- After every agent response → callback triggers\n",
        "- Session data → transferred to memory\n",
        "- No manual `add_session_to_memory()` calls needed\n",
        "\n",
        "The framework handles everything!"
      ],
      "metadata": {
        "id": "-LDdoU9IyMBn"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 6.4 Create a Runner and Test The Agent\n",
        "\n",
        "Time to test! Create a Runner with the auto-memory agent, connecting the session and memory services."
      ],
      "metadata": {
        "id": "MSqBhrMayMBo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a runner for the auto-save agent\n",
        "# This connects our automated agent to the session and memory services\n",
        "auto_runner = Runner(\n",
        "    agent=auto_memory_agent,  # Use the agent with callback + preload_memory\n",
        "    app_name=APP_NAME,\n",
        "    session_service=session_service,  # Same services from Section 3\n",
        "    memory_service=memory_service,\n",
        ")\n",
        "\n",
        "print(\"✅ Runner created.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:29:55.392471Z",
          "iopub.execute_input": "2025-11-13T16:29:55.393164Z",
          "iopub.status.idle": "2025-11-13T16:29:55.399258Z",
          "shell.execute_reply.started": "2025-11-13T16:29:55.393133Z",
          "shell.execute_reply": "2025-11-13T16:29:55.398364Z"
        },
        "id": "MGGIeqNHyMBo",
        "outputId": "c6c0ba69-9e98-4258-ab02-0623ce9d2d4f"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "✅ Runner created.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Test 1: Tell the agent about a gift (first conversation)\n",
        "# The callback will automatically save this to memory when the turn completes\n",
        "await run_session(\n",
        "    auto_runner,\n",
        "    \"I gifted a new toy to my nephew on his 1st birthday!\",\n",
        "    \"auto-save-test\",\n",
        ")\n",
        "\n",
        "# Test 2: Ask about the gift in a NEW session (second conversation)\n",
        "# The agent should retrieve the memory using preload_memory and answer correctly\n",
        "await run_session(\n",
        "    auto_runner,\n",
        "    \"What did I gift my nephew?\",\n",
        "    \"auto-save-test-2\",  # Different session ID - proves memory works across sessions!\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T16:30:13.085009Z",
          "iopub.execute_input": "2025-11-13T16:30:13.085366Z",
          "iopub.status.idle": "2025-11-13T16:30:14.305512Z",
          "shell.execute_reply.started": "2025-11-13T16:30:13.085342Z",
          "shell.execute_reply": "2025-11-13T16:30:14.30443Z"
        },
        "id": "eHCAgGRFyMBo",
        "outputId": "4e9dc682-c360-45f1-9df7-89116883dacd"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\n### Session: auto-save-test\n\nUser > I gifted a new toy to my nephew on his 1st birthday!\nModel: > That's wonderful! A first birthday is such a special milestone. I hope your nephew enjoys his new toy!\n\n### Session: auto-save-test-2\n\nUser > What did I gift my nephew?\nModel: > You gifted your nephew a new toy for his 1st birthday.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**What just happened:**\n",
        "\n",
        "1. **First conversation:** Mentioned gift to nephew\n",
        "   - Callback automatically saved to memory ✅\n",
        "2. **Second conversation (new session):** Asked about the gift  \n",
        "   - `preload_memory` automatically retrieved the memory ✅\n",
        "   - Agent answered correctly ✅\n",
        "\n",
        "**Zero manual memory calls!** This is automated memory management in action."
      ],
      "metadata": {
        "id": "SrlcRMm6yMBo"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 6.5 How often should you save Sessions to Memory?\n",
        "\n",
        "**Options:**\n",
        "\n",
        "| Timing | Implementation | Best For |\n",
        "|--------|----------------|----------|\n",
        "| **After every turn** | `after_agent_callback` | Real-time memory updates |\n",
        "| **End of conversation** | Manual call when session ends | Batch processing, reduce API calls |\n",
        "| **Periodic intervals** | Timer-based background job | Long-running conversations |"
      ],
      "metadata": {
        "id": "zZsXvqSQyMBo"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 🧩 Section 7: Memory Consolidation"
      ],
      "metadata": {
        "id": "4oBvDLDpyMBo"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 7.1 The Limitation of Raw Storage\n",
        "\n",
        "**What we've stored so far:**\n",
        "- Every user message\n",
        "- Every agent response  \n",
        "- Every tool call\n",
        "\n",
        "**The problem:**\n",
        "```\n",
        "Session: 50 messages = 10,000 tokens\n",
        "Memory:  All 50 messages stored\n",
        "Search:  Returns all 50 messages → Agent must process 10,000 tokens\n",
        "```\n",
        "\n",
        "This doesn't scale. We need **consolidation**."
      ],
      "metadata": {
        "id": "6Kuvvs_pyMBo"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 7.2 What is Memory Consolidation?\n",
        "\n",
        "**Memory Consolidation** = Extracting **only important facts** while discarding conversational noise.\n",
        "\n",
        "**Before (Raw Storage):**\n",
        "\n",
        "```\n",
        "User: \"My favorite color is BlueGreen. I also like purple.\n",
        "       Actually, I prefer BlueGreen most of the time.\"\n",
        "Agent: \"Great! I'll remember that.\"\n",
        "User: \"Thanks!\"\n",
        "Agent: \"You're welcome!\"\n",
        "\n",
        "→ Stores ALL 4 messages (redundant, verbose)\n",
        "```\n",
        "\n",
        "**After (Consolidation):**\n",
        "\n",
        "```\n",
        "Extracted Memory: \"User's favorite color: BlueGreen\"\n",
        "\n",
        "→ Stores 1 concise fact\n",
        "```\n",
        "\n",
        "**Benefits:** Less storage, faster retrieval, more accurate answers."
      ],
      "metadata": {
        "id": "qYjo3WOgyMBp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day3/memory-consolidation.png\" width=\"1400\" alt=\"Memory consolidation\">"
      ],
      "metadata": {
        "id": "aZ4YzW2fyMBp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 7.3 How Consolidation Works (Conceptual)\n",
        "\n",
        "**The pipeline:**\n",
        "\n",
        "```\n",
        "1. Raw Session Events\n",
        "   ↓\n",
        "2. LLM analyzes conversation\n",
        "   ↓\n",
        "3. Extracts key facts\n",
        "   ↓\n",
        "4. Stores concise memories\n",
        "   ↓\n",
        "5. Merges with existing memories (deduplication)\n",
        "```\n",
        "\n",
        "**Example transformation:**\n",
        "\n",
        "```\n",
        "Input:  \"I'm allergic to peanuts. I can't eat anything with nuts.\"\n",
        "\n",
        "Output: Memory {\n",
        "  allergy: \"peanuts, tree nuts\"\n",
        "  severity: \"avoid completely\"\n",
        "}\n",
        "```\n",
        "\n",
        "Natural language → Structured, actionable data."
      ],
      "metadata": {
        "id": "5ayze_V3yMBp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 7.4 Next Steps for Memory Consolidation\n",
        "\n",
        "**💡 Key Point:** Managed Memory Services handle consolidation **automatically**.\n",
        "\n",
        "**You use the same API:**\n",
        "- `add_session_to_memory()` ← Same method\n",
        "- `search_memory()` ← Same method\n",
        "\n",
        "**The difference:** What happens behind the scenes.\n",
        "- **InMemoryMemoryService:** Stores raw events\n",
        "- **VertexAiMemoryBankService:** Intelligently consolidates before storing\n",
        "\n",
        "**📚 Learn More:**\n",
        "- [Vertex AI Memory Bank: Memory Consolidation Guide](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/memory-bank/generate-memories) -> You'll explore this in Day 5!\n"
      ],
      "metadata": {
        "id": "9i_6h-9jyMBp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 📊 Summary"
      ],
      "metadata": {
        "id": "Kx-amjqmyMBp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "You've learned the **core mechanics** of Memory in ADK:\n",
        "\n",
        "1. **✅ Adding Memory**\n",
        "   - Initialize `MemoryService` alongside `SessionService`\n",
        "   - Both services are provided to the `Runner`\n",
        "\n",
        "2. **✅ Storing Information**\n",
        "   - `await memory_service.add_session_to_memory(session)`\n",
        "   - Transfers session data to long-term storage\n",
        "   - Can be automated with callbacks\n",
        "\n",
        "3. **✅ Searching Memory**\n",
        "   - `await memory_service.search_memory(app_name, user_id, query)`\n",
        "   - Returns relevant memories from past conversations\n",
        "\n",
        "4. **✅ Retrieving in Agents**\n",
        "   - **Reactive:** `load_memory` tool (agent decides when to use memory)\n",
        "   - **Proactive:** `preload_memory` tool (always loads memory into LLM's system instructions)\n",
        "\n",
        "5. **✅ Memory Consolidation**\n",
        "   - Extracts key information from Session data\n",
        "   - Provided by managed memory services such as Vertex AI Memory Bank"
      ],
      "metadata": {
        "id": "paC0BRMRyMBp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🎉 **Congratulations!** You've learned Memory Management in ADK!"
      ],
      "metadata": {
        "id": "5hqHWKRMyMBq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**📚 Learn More:**\n",
        "- [ADK Memory Documentation](https://google.github.io/adk-docs/sessions/memory/)\n",
        "- [Vertex AI Memory Bank](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/memory-bank/overview)\n",
        "- [Memory Consolidation Guide](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/memory-bank/generate-memories)\n",
        "\n",
        "**🎯 Next Steps:**\n",
        "\n",
        "Ready for Day 4? Learn how to **implement Observability and Evaluate your agents** to ensure they're working as intended in production!"
      ],
      "metadata": {
        "id": "5U_LpM_UyMBq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## Authors\n",
        "\n",
        "| Authors |\n",
        "| --- |\n",
        "| [Sampath M](https://www.linkedin.com/in/msampathkumar/) |"
      ],
      "metadata": {
        "id": "4eFjJp5dyMBq"
      }
    }
  ]
}

---



# Log: Day_4a-agent-observability.txt

{"metadata":{"kernelspec":{"name":"python3","display_name":"Python 3","language":"python"},"language_info":{"name":"python","version":"3.11.13","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"},"kaggle":{"accelerator":"none","dataSources":[],"isInternetEnabled":true,"language":"python","sourceType":"notebook","isGpuEnabled":false}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"markdown","source":"Copyright 2025 Google LLC.","metadata":{}},{"cell_type":"code","source":"# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n# https://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an \"AS IS\" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:15:08.149281Z","iopub.execute_input":"2025-11-12T19:15:08.149605Z","iopub.status.idle":"2025-11-12T19:15:08.155172Z","shell.execute_reply.started":"2025-11-12T19:15:08.149581Z","shell.execute_reply":"2025-11-12T19:15:08.154081Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"# 🔎 Agent Observability - Logs, Traces & Metrics\n\n**Welcome to Day 4 of the Kaggle 5-day Agents course!**\n\nIn Day 3, you learned the **\"What, Why & How\" of Session and Memory management**, focusing on long-term, short-term, and shared memory (state). \n\nToday, you'll learn:\n- How to add observability to the agent you've built and\n- How to evaluate if the agents are working as expected\n\nIn this notebook, we'll focus on the first part - **Agent Observability!**\n\n## What is Agent Observability?\n\n**🚨 The challenge:** Unlike traditional software that fails predictably, AI agents can fail mysteriously. Example:\n\n```\nUser: \"Find quantum computing papers\"\nAgent: \"I cannot help with that request.\"\nYou: 😭 WHY?? Is it the prompt? Missing tools? API error?\n```\n\n**💡 The Solution:** Agent observability gives you complete visibility into your agent's decision-making process. You'll see exactly what prompts are sent to the LLM, which tools are available, how the model responds, and where failures occur.\n\n```\nDEBUG Log: LLM Request shows \"Functions: []\" (no tools!)\nYou: 🎯 Aha! Missing google_search tool - easy fix!\n```\n\n## Foundational pillars of Agent Observability\n\n1. **Logs:** A log is a record of a single event, telling you **what** happened at a specific moment.\n2. **Traces:** A trace connects the logs into a single story, showing you **why** a final result occurred by revealing the entire sequence of steps.\n3. **Metrics:** Metrics are the summary numbers (like averages and error rates) that tell you **how** well the agent is performing overall.\n\n<center>\n    <img src=\"https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/observability-intro.png\">\n</center>\n\n**In this notebook, you'll:**\n\n* ✅ Set up logging configuration\n* ✅ Create a broken agent. Use `adk web` UI & logs to identify exactly why the agent fails\n* ✅ Understand how to implement logging in production\n* ✅ Learn when to use built-in logging vs custom solutions","metadata":{}},{"cell_type":"markdown","source":"## ‼️ Please Read\n\n> ❌ **ℹ️ Note: No submission required!**\n> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n\n> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n\n> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n\n**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**","metadata":{}},{"cell_type":"markdown","source":"## ⚙️ Section 1: Setup\n\n### 1.1: Install dependencies\n\nThe Kaggle Notebooks environment includes a pre-installed version of the [google-adk](https://google.github.io/adk-docs/) library for Python and its required dependencies, so you don't need to install additional packages in this notebook.\n\nTo install and use ADK in your own Python development environment outside of this course, you can do so by running:\n\n```\npip install google-adk\n```","metadata":{}},{"cell_type":"markdown","source":"### 🔑 1.2: Configure your Gemini API Key\n\nThis notebook uses the [Gemini API](https://ai.google.dev/gemini-api/), which requires an API key.\n\n**1. Get your API key**\n\nIf you don't have one already, create an [API key in Google AI Studio](https://aistudio.google.com/app/api-keys).\n\n**2. Add the key to Kaggle Secrets**\n\nNext, you will need to add your API key to your Kaggle Notebook as a Kaggle User Secret.\n\n1. In the top menu bar of the notebook editor, select `Add-ons` then `Secrets`.\n2. Create a new secret with the label `GOOGLE_API_KEY`.\n3. Paste your API key into the \"Value\" field and click \"Save\".\n4. Ensure that the checkbox next to `GOOGLE_API_KEY` is selected so that the secret is attached to the notebook.\n\n**3. Authenticate in the notebook**\n\nRun the cell below to access the `GOOGLE_API_KEY` you just saved and set it as an environment variable for the notebook to use:","metadata":{}},{"cell_type":"code","source":"import os\nfrom kaggle_secrets import UserSecretsClient\n\ntry:\n    GOOGLE_API_KEY = UserSecretsClient().get_secret(\"GOOGLE_API_KEY\")\n    os.environ[\"GOOGLE_API_KEY\"] = GOOGLE_API_KEY\n    print(\"✅ Setup and authentication complete.\")\nexcept Exception as e:\n    print(\n        f\"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}\"\n    )","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:15:08.156609Z","iopub.execute_input":"2025-11-12T19:15:08.156979Z","iopub.status.idle":"2025-11-12T19:15:08.278839Z","shell.execute_reply.started":"2025-11-12T19:15:08.156958Z","shell.execute_reply":"2025-11-12T19:15:08.277826Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"### ✍️ 1.3: Set up logging and cleanup old files\nLet's configure logging for our debugging session. The following cell makes sure we also capture other log levels, like DEBUG.","metadata":{}},{"cell_type":"code","source":"import logging\nimport os\n\n# Clean up any previous logs\nfor log_file in [\"logger.log\", \"web.log\", \"tunnel.log\"]:\n    if os.path.exists(log_file):\n        os.remove(log_file)\n        print(f\"🧹 Cleaned up {log_file}\")\n\n# Configure logging with DEBUG log level.\nlogging.basicConfig(\n    filename=\"logger.log\",\n    level=logging.DEBUG,\n    format=\"%(filename)s:%(lineno)s %(levelname)s:%(message)s\",\n)\n\nprint(\"✅ Logging configured\")","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:15:08.280623Z","iopub.execute_input":"2025-11-12T19:15:08.280848Z","iopub.status.idle":"2025-11-12T19:15:08.287816Z","shell.execute_reply.started":"2025-11-12T19:15:08.28083Z","shell.execute_reply":"2025-11-12T19:15:08.286586Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"### 💻 1.4: Set up proxy and tunneling\n\nWe'll use a proxy to access the ADK web UI from within the Kaggle Notebooks environment. If you are running this outside the Kaggle environment, you don't need to do this.","metadata":{}},{"cell_type":"code","source":"from IPython.core.display import display, HTML\nfrom jupyter_server.serverapp import list_running_servers\n\n\n# Gets the proxied URL in the Kaggle Notebooks environment\ndef get_adk_proxy_url():\n    PROXY_HOST = \"https://kkb-production.jupyter-proxy.kaggle.net\"\n    ADK_PORT = \"8000\"\n\n    servers = list(list_running_servers())\n    if not servers:\n        raise Exception(\"No running Jupyter servers found.\")\n\n    baseURL = servers[0][\"base_url\"]\n\n    try:\n        path_parts = baseURL.split(\"/\")\n        kernel = path_parts[2]\n        token = path_parts[3]\n    except IndexError:\n        raise Exception(f\"Could not parse kernel/token from base URL: {baseURL}\")\n\n    url_prefix = f\"/k/{kernel}/{token}/proxy/proxy/{ADK_PORT}\"\n    url = f\"{PROXY_HOST}{url_prefix}\"\n\n    styled_html = f\"\"\"\n    <div style=\"padding: 15px; border: 2px solid #f0ad4e; border-radius: 8px; background-color: #fef9f0; margin: 20px 0;\">\n        <div style=\"font-family: sans-serif; margin-bottom: 12px; color: #333; font-size: 1.1em;\">\n            <strong>⚠️ IMPORTANT: Action Required</strong>\n        </div>\n        <div style=\"font-family: sans-serif; margin-bottom: 15px; color: #333; line-height: 1.5;\">\n            The ADK web UI is <strong>not running yet</strong>. You must start it in the next cell.\n            <ol style=\"margin-top: 10px; padding-left: 20px;\">\n                <li style=\"margin-bottom: 5px;\"><strong>Run the next cell</strong> (the one with <code>!adk web ...</code>) to start the ADK web UI.</li>\n                <li style=\"margin-bottom: 5px;\">Wait for that cell to show it is \"Running\" (it will not \"complete\").</li>\n                <li>Once it's running, <strong>return to this button</strong> and click it to open the UI.</li>\n            </ol>\n            <em style=\"font-size: 0.9em; color: #555;\">(If you click the button before running the next cell, you will get a 500 error.)</em>\n        </div>\n        <a href='{url}' target='_blank' style=\"\n            display: inline-block; background-color: #1a73e8; color: white; padding: 10px 20px;\n            text-decoration: none; border-radius: 25px; font-family: sans-serif; font-weight: 500;\n            box-shadow: 0 2px 5px rgba(0,0,0,0.2); transition: all 0.2s ease;\">\n            Open ADK Web UI (after running cell below) ↗\n        </a>\n    </div>\n    \"\"\"\n\n    display(HTML(styled_html))\n\n    return url_prefix\n\n\nprint(\"✅ Helper functions defined.\")","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:15:08.288658Z","iopub.execute_input":"2025-11-12T19:15:08.288913Z","iopub.status.idle":"2025-11-12T19:15:10.114729Z","shell.execute_reply.started":"2025-11-12T19:15:08.288892Z","shell.execute_reply":"2025-11-12T19:15:10.113583Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"---\n## 🐞 Section 2: Hands-On Debugging with ADK Web UI","metadata":{}},{"cell_type":"markdown","source":"### 2.1: Create a \"Research Paper Finder\" Agent\n\n\n**Our goal:** Build a research paper finder agent that helps users find academic papers on any topic.\n\nBut first, let's intentionally create an incorrect version of the agent to practice debugging! We'll start by creating a new agent folder using the `adk create` CLI command.","metadata":{}},{"cell_type":"code","source":"!adk create research-agent --model gemini-2.5-flash-lite --api_key $GOOGLE_API_KEY","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:15:10.116101Z","iopub.execute_input":"2025-11-12T19:15:10.116471Z","iopub.status.idle":"2025-11-12T19:15:57.917412Z","shell.execute_reply.started":"2025-11-12T19:15:10.116449Z","shell.execute_reply":"2025-11-12T19:15:57.916363Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"### Agent definition\n\nNext, let's create our root agent. \n- We'll configure it as an `LlmAgent`, give it a name, model and instruction.\n- The `root_agent` gets the user prompt and delegates the search to the `google_search_agent`.\n- Then, the agent uses the `count_papers` tool to count the number of papers returned.\n\n**👉 Pay attention to the root agent's instructions and the `count_papers` tool parameter!**","metadata":{}},{"cell_type":"code","source":"%%writefile research-agent/agent.py\n\nfrom google.adk.agents import LlmAgent\nfrom google.adk.models.google_llm import Gemini\nfrom google.adk.tools.agent_tool import AgentTool\nfrom google.adk.tools.google_search_tool import google_search\n\nfrom google.genai import types\nfrom typing import List\n\nretry_config = types.HttpRetryOptions(\n    attempts=5,  # Maximum retry attempts\n    exp_base=7,  # Delay multiplier\n    initial_delay=1,\n    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors\n)\n\n# ---- Intentionally pass incorrect datatype - `str` instead of `List[str]` ----\ndef count_papers(papers: str):\n    \"\"\"\n    This function counts the number of papers in a list of strings.\n    Args:\n      papers: A list of strings, where each string is a research paper.\n    Returns:\n      The number of papers in the list.\n    \"\"\"\n    return len(papers)\n\n\n# Google Search agent\ngoogle_search_agent = LlmAgent(\n    name=\"google_search_agent\",\n    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n    description=\"Searches for information using Google search\",\n    instruction=\"\"\"Use the google_search tool to find information on the given topic. Return the raw search results.\n    If the user asks for a list of papers, then give them the list of research papers you found and not the summary.\"\"\",\n    tools=[google_search]\n)\n\n\n# Root agent\nroot_agent = LlmAgent(\n    name=\"research_paper_finder_agent\",\n    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n    instruction=\"\"\"Your task is to find research papers and count them. \n\n    You MUST ALWAYS follow these steps:\n    1) Find research papers on the user provided topic using the 'google_search_agent'. \n    2) Then, pass the papers to 'count_papers' tool to count the number of papers returned.\n    3) Return both the list of research papers and the total number of papers.\n    \"\"\",\n    tools=[AgentTool(agent=google_search_agent), count_papers]\n)","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:15:57.920313Z","iopub.execute_input":"2025-11-12T19:15:57.920709Z","iopub.status.idle":"2025-11-12T19:15:57.929037Z","shell.execute_reply.started":"2025-11-12T19:15:57.920678Z","shell.execute_reply":"2025-11-12T19:15:57.928058Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"### 2.2: Run the agent\n\nLet's now run our agent with the `adk web --log_level DEBUG` CLI command.\n\n**📍 The key here is `--log_level DEBUG`** - this shows us:\n\n\n* **Full LLM Prompts:** The complete request sent to the language model, including system instructions, history, and tools.\n* Detailed API responses from services.\n* Internal state transitions and variable values.\n\nOther log levels include: INFO, ERROR and WARNING.","metadata":{}},{"cell_type":"markdown","source":"Get the proxied URL to access the ADK web UI in the Kaggle Notebooks environment:","metadata":{}},{"cell_type":"code","source":"url_prefix = get_adk_proxy_url()","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:15:57.92998Z","iopub.execute_input":"2025-11-12T19:15:57.930262Z","iopub.status.idle":"2025-11-12T19:15:57.954484Z","shell.execute_reply.started":"2025-11-12T19:15:57.930231Z","shell.execute_reply":"2025-11-12T19:15:57.953584Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"Now you can start the ADK web UI with the `--log_level` parameter.\n\n👉 **Note:** The following cell will not \"complete\", but will remain running and serving the ADK web UI until you manually stop the cell.","metadata":{}},{"cell_type":"code","source":"!adk web --log_level DEBUG --url_prefix {url_prefix}","metadata":{"scrolled":true,"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:15:57.955496Z","iopub.execute_input":"2025-11-12T19:15:57.955806Z","iopub.status.idle":"2025-11-12T19:16:28.225932Z","shell.execute_reply.started":"2025-11-12T19:15:57.955775Z","shell.execute_reply":"2025-11-12T19:16:28.224851Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"Once the ADK web UI starts, open the proxy link using the button in the previous cell.\n\nAs you start chatting with the agent, you should see the DEBUG logs appear in the output cell below!\n\n‼️ **IMPORTANT: DO NOT SHARE THE PROXY LINK** with anyone - treat it as sensitive data as it contains your authentication token in the URL.","metadata":{}},{"cell_type":"markdown","source":"### 📝 2.3: Test the agent in ADK web UI\n\n#### **👉 Do: In the ADK web UI**\n\n1. Select \"research-agent\" from the dropdown in the top-left.\n2. In the chat interface, type: `Find latest quantum computing papers`\n3. Send the message and observe the response. The agent should return a list of research papers and their count.\n\nIt looks like our agent works and we got a response! 🤔 **But wait, isn't the count of papers unusually large? Let's look at the logs and trace.** ","metadata":{}},{"cell_type":"markdown","source":"#### **👉 Do: Events tab - Traces in detail**\n\n1. In the web UI, click the **\"Events\"** tab on the left sidebar\n2. You'll see a chronological list of all agent actions\n3. Click on any event to expand its details in the bottom panel\n4. Try clicking the **\"Trace\"** button to see timing information for each step.\n5. **Click the `execute_tool count_papers` span. You'll see that the function call to `count_papers` returns the large number as the response**.\n6. Let's look at what was passed as input to this function. \n7. **Find the `call_llm` span corresponding to the `count_papers` function call**.","metadata":{}},{"cell_type":"markdown","source":"#### **👉 Do: Inspect the Function call in Events:**\n\n- Click on the specific span to open the Events tab.\n- Examine the `function_call`, focusing on the `papers` argument.\n- Notice that `root_agent` passes the list of `papers` as a **str** instead of a **List[str]** - there's our bug! ","metadata":{}},{"cell_type":"markdown","source":"![Demo](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/observability-demo.gif)","metadata":{}},{"cell_type":"markdown","source":"### 2.4: Your Turn - fix it! 👾 \n\nUpdate the datatype of the `papers` argument in the `count_papers` tool to a `List[str]` and rerun the `adk web` command!","metadata":{}},{"cell_type":"markdown","source":"---\n\n## ‼️ **Stop the ADK web UI** 🛑\n\n**In order to run cells in the remainder of this notebook,** please stop the running cell where you started `adk web` in Section 3.1.\n\nOtherwise that running cell will block / prevent other cells from running as long as the ADK web UI is running.\n\n---","metadata":{}},{"cell_type":"markdown","source":"### 2.5: Debug through local Logs\n\nOptionally, you can also examine the local DEBUG logs to find the root cause. Run the following cell to print the contents of the log file. Look for detailed logs like:\n```\nDEBUG - google_adk.models.google_llm - LLM Request: ...\nDEBUG - google_adk.models.google_llm - LLM Response: ...\n```","metadata":{}},{"cell_type":"code","source":"# Check the DEBUG logs from the broken agent\nprint(\"🔍 Examining web server logs for debugging clues...\\n\")\n!cat logger.log","metadata":{"scrolled":true,"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:16:28.227335Z","iopub.execute_input":"2025-11-12T19:16:28.227808Z","iopub.status.idle":"2025-11-12T19:16:28.351612Z","shell.execute_reply.started":"2025-11-12T19:16:28.22777Z","shell.execute_reply":"2025-11-12T19:16:28.350387Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"**Other Observability questions you can now answer from logs and adk web:**\n- **Efficiency**: Is the agent making optimal tool choices?\n- **Reasoning Quality**: Are the prompts well-structured and context-appropriate?\n- **Performance**: Look at the traces to identify which steps take the longest?\n- **Failure Diagnosis**: When something goes wrong, where exactly did it fail?\n\n**Key Learning:** Core debugging pattern: `symptom → logs → root cause → fix`.\n\n**Debugging Victory:** You just went from \"Agent mysteriously failed\" to \"I know exactly why and how to fix it!\" This is the power of observability!\n","metadata":{}},{"cell_type":"markdown","source":"---\n## 🧑‍💻 Section 3: Logging in production\n\n**🎯 Great! You can now debug agent failures using ADK web UI and DEBUG logs.**\n\nBut what happens when you move beyond development? Real-world scenarios where you need to move beyond the web UI:\n\n**❌ Problem 1: Production Deployment**\n```\nYou: \"Let me open the ADK web UI to check why the agent failed\"\nDevOps: \"Um... this is a production server. No web UI access.\"\nYou: 😱 \"How do I debug production issues?\"\n```\n\n**❌ Problem 2: Automated Systems** \n```\nYou: \"The agent runs 1000 times per day in our pipeline\"\nBoss: \"Which runs are slow? What's our success rate?\"\nYou: 😰 \"I'd have to manually check the web UI 1000 times...\"\n```\n\n**💡 The Solution:**\n\nWe need a way to capture observability data or in other words, **add logs to our code**. \n\n👉 In traditional software development, this is done by adding log statements in Python functions - **and agents are no different!** We need to add log statements to our agent and a common approach is to add log statements to **Plugins**.\n","metadata":{}},{"cell_type":"markdown","source":"### 3.1: How to add logs for production observability?\n\nA Plugin is a custom code module that runs automatically at various stages of your agent's lifecycle. Plugins are composed of \"**Callbacks**\" which provide the hooks to interrupt an agent's flow. Think of it like this:\n\n- **Your agent workflow**: User message → Agent thinks → Calls tools → Returns response\n- **Plugin hooks into this**: Before agent starts → After tool runs → When LLM responds → etc.\n- **Plugin contains your custom code**: Logging, monitoring, security checks, caching, etc.","metadata":{}},{"cell_type":"markdown","source":"![image.png](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/plugins-callbacks.png)","metadata":{}},{"cell_type":"markdown","source":"#### Callbacks\n\nCallbacks are the **atomic components inside a Plugin** - these are just Python functions that run at specific points in an agent's lifecycle! **Callbacks are grouped together to create a Plugin.**\n\nThere are different kinds of callbacks such as:\n* **before/after_agent_callbacks** - runs before/after an agent is invoked\n* **before/after_tool_callbacks** - runs before/after a tool is called\n* **before/after_model_callbacks** - similarly, runs before/after the LLM model is called\n* **on_model_error_callback** - which runs when a model error is encountered","metadata":{}},{"cell_type":"markdown","source":"![image.png](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/types_of_callbacks.png)","metadata":{}},{"cell_type":"markdown","source":"### 3.2: To make things more concrete, what does a Plugin look like?","metadata":{}},{"cell_type":"code","source":"print(\"----- EXAMPLE PLUGIN - DOES NOTHING ----- \")\n\nimport logging\nfrom google.adk.agents.base_agent import BaseAgent\nfrom google.adk.agents.callback_context import CallbackContext\nfrom google.adk.models.llm_request import LlmRequest\nfrom google.adk.plugins.base_plugin import BasePlugin\n\n\n# Applies to all agent and model calls\nclass CountInvocationPlugin(BasePlugin):\n    \"\"\"A custom plugin that counts agent and tool invocations.\"\"\"\n\n    def __init__(self) -> None:\n        \"\"\"Initialize the plugin with counters.\"\"\"\n        super().__init__(name=\"count_invocation\")\n        self.agent_count: int = 0\n        self.tool_count: int = 0\n        self.llm_request_count: int = 0\n\n    # Callback 1: Runs before an agent is called. You can add any custom logic here.\n    async def before_agent_callback(\n        self, *, agent: BaseAgent, callback_context: CallbackContext\n    ) -> None:\n        \"\"\"Count agent runs.\"\"\"\n        self.agent_count += 1\n        logging.info(f\"[Plugin] Agent run count: {self.agent_count}\")\n\n    # Callback 2: Runs before a model is called. You can add any custom logic here.\n    async def before_model_callback(\n        self, *, callback_context: CallbackContext, llm_request: LlmRequest\n    ) -> None:\n        \"\"\"Count LLM requests.\"\"\"\n        self.llm_request_count += 1\n        logging.info(f\"[Plugin] LLM request count: {self.llm_request_count}\")","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:16:28.352812Z","iopub.execute_input":"2025-11-12T19:16:28.353204Z","iopub.status.idle":"2025-11-12T19:16:50.525358Z","shell.execute_reply.started":"2025-11-12T19:16:28.353111Z","shell.execute_reply":"2025-11-12T19:16:50.524461Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"**Key insight**: You register a plugin **once** on your runner, and it automatically applies to **every agent, tool call, and LLM request** in your system as per your definition. Read more about Plugin hooks [here](https://google.github.io/adk-docs/plugins/#plugin-callback-hooks).","metadata":{}},{"cell_type":"markdown","source":"You can follow along with the numbers in the diagram below to understand the flow.","metadata":{}},{"cell_type":"markdown","source":"![image.png](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/count-invocation-plugin.png)","metadata":{}},{"cell_type":"markdown","source":"### 3.3: ADK's built-in `LoggingPlugin`\n\nBut you don't have to define all the callbacks and plugins to capture *standard* Observability data in ADK. Instead, ADK provides a built-in **LoggingPlugin** that automatically captures all agent activity:\n\n- 🚀 User messages and agent responses\n- ⏱️ Timing data for performance analysis\n- 🧠 LLM requests and responses for debugging\n- 🔧 Tool calls and results\n- ✅ Complete execution traces","metadata":{}},{"cell_type":"markdown","source":"#### Agent definition\n\nLet's use the same agent from the previous demo - the Research paper finder!","metadata":{}},{"cell_type":"code","source":"from google.adk.agents import LlmAgent\nfrom google.adk.models.google_llm import Gemini\nfrom google.adk.tools.agent_tool import AgentTool\nfrom google.adk.tools.google_search_tool import google_search\n\nfrom google.genai import types\nfrom typing import List\n\nretry_config = types.HttpRetryOptions(\n    attempts=5,  # Maximum retry attempts\n    exp_base=7,  # Delay multiplier\n    initial_delay=1,\n    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors\n)\n\n\ndef count_papers(papers: List[str]):\n    \"\"\"\n    This function counts the number of papers in a list of strings.\n    Args:\n      papers: A list of strings, where each string is a research paper.\n    Returns:\n      The number of papers in the list.\n    \"\"\"\n    return len(papers)\n\n\n# Google search agent\ngoogle_search_agent = LlmAgent(\n    name=\"google_search_agent\",\n    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n    description=\"Searches for information using Google search\",\n    instruction=\"Use the google_search tool to find information on the given topic. Return the raw search results.\",\n    tools=[google_search],\n)\n\n# Root agent\nresearch_agent_with_plugin = LlmAgent(\n    name=\"research_paper_finder_agent\",\n    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n    instruction=\"\"\"Your task is to find research papers and count them. \n   \n   You must follow these steps:\n   1) Find research papers on the user provided topic using the 'google_search_agent'. \n   2) Then, pass the papers to 'count_papers' tool to count the number of papers returned.\n   3) Return both the list of research papers and the total number of papers.\n   \"\"\",\n    tools=[AgentTool(agent=google_search_agent), count_papers],\n)\n\nprint(\"✅ Agent created\")","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:16:50.52641Z","iopub.execute_input":"2025-11-12T19:16:50.527099Z","iopub.status.idle":"2025-11-12T19:16:50.536674Z","shell.execute_reply.started":"2025-11-12T19:16:50.527068Z","shell.execute_reply":"2025-11-12T19:16:50.535658Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"### 3.4: Add LoggingPlugin to Runner\n\nThe following code creates the `InMemoryRunner`. This is used to programmatically invoke the agent.\n\n**To use `LoggingPlugin` in the above research agent,**\n1) Import the plugin\n2) Add it when initializing the `InMemoryRunner`.\n","metadata":{}},{"cell_type":"code","source":"from google.adk.runners import InMemoryRunner\nfrom google.adk.plugins.logging_plugin import (\n    LoggingPlugin,\n)  # <---- 1. Import the Plugin\nfrom google.genai import types\nimport asyncio\n\nrunner = InMemoryRunner(\n    agent=research_agent_with_plugin,\n    plugins=[\n        LoggingPlugin()\n    ],  # <---- 2. Add the plugin. Handles standard Observability logging across ALL agents\n)\n\nprint(\"✅ Runner configured\")","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:16:50.537622Z","iopub.execute_input":"2025-11-12T19:16:50.537912Z","iopub.status.idle":"2025-11-12T19:16:50.56708Z","shell.execute_reply.started":"2025-11-12T19:16:50.537892Z","shell.execute_reply":"2025-11-12T19:16:50.566104Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"Let's now run the agent using `run_debug` function.","metadata":{}},{"cell_type":"code","source":"print(\"🚀 Running agent with LoggingPlugin...\")\nprint(\"📊 Watch the comprehensive logging output below:\\n\")\n\nresponse = await runner.run_debug(\"Find recent papers on quantum computing\")","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T19:16:50.568034Z","iopub.execute_input":"2025-11-12T19:16:50.568333Z","iopub.status.idle":"2025-11-12T19:16:57.577725Z","shell.execute_reply.started":"2025-11-12T19:16:50.568307Z","shell.execute_reply":"2025-11-12T19:16:57.576751Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"---\n\n## 📊 Summary\n\n**❓ When to use which type of Logging?**\n1. **Development debugging?** → Use `adk web --log_level DEBUG`\n2. **Common production observability?** → Use `LoggingPlugin()` \n3. **Custom requirements?** → Build Custom Callbacks and Plugins\n\n### Try it out!\n\n👉 Extend the agent's observability by implementing a **custom ADK plugin** that tracks and reports the total number of tool calls made during a session.","metadata":{}},{"cell_type":"markdown","source":"## 🎯 Congratulations!\n\n**You now know how to:**\n\n- ✅ Debug agent failures through DEBUG logs and the ADK web UI\n- ✅ Use the core debugging pattern: symptom → logs → root cause → fix  \n- ✅ Scale observability with `LoggingPlugin` for production systems\n- ✅ Understand when to use the different logging types\n\n**ℹ️ Note: No submission required!**\n\nThis notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.","metadata":{}},{"cell_type":"markdown","source":"### 📚 Resources\n\n**Refer to the ADK documentation to learn more about observability:**\n\n- [ADK Observability Documentation](https://google.github.io/adk-docs/observability/logging/) - Complete guide to logging in ADK\n- [Custom Plugin](https://google.github.io/adk-docs/plugins/) - Build your own Plugins\n- [External Integrations](https://google.github.io/adk-docs/observability/cloud-trace/) - Explore external third-party observability integrations with ADK\n\n### 🎯 Next Steps\n\nReady for the next challenge? Continue to the next notebook to learn how to **Evaluate an Agent** and ensure it's working as expected in production.","metadata":{"execution":{"iopub.execute_input":"2025-10-24T01:50:15.542601Z","iopub.status.busy":"2025-10-24T01:50:15.542221Z","iopub.status.idle":"2025-10-24T01:50:15.548614Z","shell.execute_reply":"2025-10-24T01:50:15.547556Z","shell.execute_reply.started":"2025-10-24T01:50:15.542577Z"}}},{"cell_type":"markdown","source":"---\n\n<div align=\"center\">\n  <table>\n    <tr>\n      <th style=\"text-align:center\">Authors</th>\n    </tr>\n    <tr>\n      <td style=\"text-align:center\"><a href=\"https://www.linkedin.com/in/sitalakshmi04/\">Sita Lakshmi Sangameswaran</a></td>\n    </tr>\n  </table>\n</div>","metadata":{}}]}

---



# Log: Day_4b-agent-evaluation.txt

{"metadata":{"kernelspec":{"name":"python3","display_name":"Python 3","language":"python"},"language_info":{"name":"python","version":"3.11.13","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"},"kaggle":{"accelerator":"none","dataSources":[],"isInternetEnabled":true,"language":"python","sourceType":"notebook","isGpuEnabled":false}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"markdown","source":"Copyright 2025 Google LLC.","metadata":{}},{"cell_type":"code","source":"# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n# https://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an \"AS IS\" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:38:28.606824Z","iopub.execute_input":"2025-11-12T18:38:28.607103Z","iopub.status.idle":"2025-11-12T18:38:28.612472Z","shell.execute_reply.started":"2025-11-12T18:38:28.607068Z","shell.execute_reply":"2025-11-12T18:38:28.611559Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"# 📝 Agent Evaluation\n\n\n**Welcome to Day 4 of the Kaggle 5-day Agents course!**\n\nIn the previous notebook, we explored how to implement Observability in AI agents. This approach is primarily **reactive**; it comes into play after an issue has surfaced, providing the necessary data to debug and understand the root cause.\n\nIn this notebook, we'll complement those observability practices with a **proactive** approach using **Agent Evaluation.** By continuously evaluating our agent's performance, we can catch any quality degradations much earlier!\n\n```\n                            Observability + Agent Evaluation\n                            (reactive)      (proactive)\n```","metadata":{}},{"cell_type":"markdown","source":"## **What is Agent Evaluation?**\n\nIt is the systematic process of testing and measuring how well an AI agent performs across different scenarios and quality dimensions.","metadata":{}},{"cell_type":"markdown","source":"\n## **🤖 The story**\n\nYou've built a home automation agent. It works perfectly in your tests, so you launch it confidently...\n\n\n* **Week 1:** 🚨 \"Agent turned on the fireplace when I asked for lights!\"\n* **Week 2:** 🚨 \"Agent won't respond to commands in the guest room!\"\n* **Week 3:** 🚨 \"Agent gives rude responses when devices are unavailable!\"\n\n**The Problem:** `Standard testing ≠ Evaluation`\n\nAgents are different from traditional software:\n- They are non-deterministic\n- Users give unpredictable, ambiguous commands\n- Small prompt changes cause dramatic behavior shifts and different tool calls \n\nTo accommodate all these differences, agents need systematic evaluation, not just \"happy path\" testing. **Which means assessing the agent's entire decision-making process - including the final response and the path it took to get the response (trajectory)!**","metadata":{}},{"cell_type":"markdown","source":"By the end of this notebook, you will be able to:\n\n* ✅ Understand what agent evaluation is and how to use it\n* ✅ Run evaluations and analyze results directly in the ADK web UI\n* ✅ Detect regression in the agent's performance over a period of time\n* ✅ Understand and create the necessary evaluation files (`*.test.json`, `*.evalset.json`, `test_config.json`).\n","metadata":{}},{"cell_type":"markdown","source":"## ‼️ Please Read\n\n> ❌ **ℹ️ Note: No submission required!**\n> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n\n> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n\n> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n\n**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**","metadata":{}},{"cell_type":"markdown","source":"---\n## ⚙️ Section 1: Setup\n\nBefore we begin our evaluation journey, let's set up our environment.\n\n### 1.1: Install dependencies\n\nThe Kaggle Notebooks environment includes a pre-installed version of the [google-adk](https://google.github.io/adk-docs/) library for Python and its required dependencies, so you don't need to install additional packages in this notebook.\n\nTo install and use ADK in your own Python development environment outside of this course, you can do so by running:\n\n```\npip install google-adk\n```","metadata":{}},{"cell_type":"markdown","source":"### 🔑 1.2: Configure your Gemini API Key\n\nThis notebook uses the [Gemini API](https://ai.google.dev/gemini-api/), which requires an API key.\n\n**1. Get your API key**\n\nIf you don't have one already, create an [API key in Google AI Studio](https://aistudio.google.com/app/api-keys).\n\n**2. Add the key to Kaggle Secrets**\n\nNext, you will need to add your API key to your Kaggle Notebook as a Kaggle User Secret.\n\n1. In the top menu bar of the notebook editor, select `Add-ons` then `Secrets`.\n2. Create a new secret with the label `GOOGLE_API_KEY`.\n3. Paste your API key into the \"Value\" field and click \"Save\".\n4. Ensure that the checkbox next to `GOOGLE_API_KEY` is selected so that the secret is attached to the notebook.\n\n**3. Authenticate in the notebook**\n\nRun the cell below to access the `GOOGLE_API_KEY` you just saved and set it as an environment variable for the notebook to use:","metadata":{}},{"cell_type":"code","source":"import os\nfrom kaggle_secrets import UserSecretsClient\n\ntry:\n    GOOGLE_API_KEY = UserSecretsClient().get_secret(\"GOOGLE_API_KEY\")\n    os.environ[\"GOOGLE_API_KEY\"] = GOOGLE_API_KEY\n    print(\"✅ Setup and authentication complete.\")\nexcept Exception as e:\n    print(\n        f\"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}\"\n    )","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:38:28.614278Z","iopub.execute_input":"2025-11-12T18:38:28.614575Z","iopub.status.idle":"2025-11-12T18:38:28.699613Z","shell.execute_reply.started":"2025-11-12T18:38:28.614555Z","shell.execute_reply":"2025-11-12T18:38:28.698431Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"### 💻 1.3: Set up proxy and tunneling\n\nWe'll use a proxy to access the ADK web UI from within the Kaggle Notebooks environment. If you are running this outside the Kaggle environment, you don't need to do this.","metadata":{}},{"cell_type":"code","source":"from IPython.core.display import display, HTML\nfrom jupyter_server.serverapp import list_running_servers\n\n\n# Gets the proxied URL in the Kaggle Notebooks environment\ndef get_adk_proxy_url():\n    PROXY_HOST = \"https://kkb-production.jupyter-proxy.kaggle.net\"\n    ADK_PORT = \"8000\"\n\n    servers = list(list_running_servers())\n    if not servers:\n        raise Exception(\"No running Jupyter servers found.\")\n\n    baseURL = servers[0][\"base_url\"]\n\n    try:\n        path_parts = baseURL.split(\"/\")\n        kernel = path_parts[2]\n        token = path_parts[3]\n    except IndexError:\n        raise Exception(f\"Could not parse kernel/token from base URL: {baseURL}\")\n\n    url_prefix = f\"/k/{kernel}/{token}/proxy/proxy/{ADK_PORT}\"\n    url = f\"{PROXY_HOST}{url_prefix}\"\n\n    styled_html = f\"\"\"\n    <div style=\"padding: 15px; border: 2px solid #f0ad4e; border-radius: 8px; background-color: #fef9f0; margin: 20px 0;\">\n        <div style=\"font-family: sans-serif; margin-bottom: 12px; color: #333; font-size: 1.1em;\">\n            <strong>⚠️ IMPORTANT: Action Required</strong>\n        </div>\n        <div style=\"font-family: sans-serif; margin-bottom: 15px; color: #333; line-height: 1.5;\">\n            The ADK web UI is <strong>not running yet</strong>. You must start it in the next cell.\n            <ol style=\"margin-top: 10px; padding-left: 20px;\">\n                <li style=\"margin-bottom: 5px;\"><strong>Run the next cell</strong> (the one with <code>!adk web ...</code>) to start the ADK web UI.</li>\n                <li style=\"margin-bottom: 5px;\">Wait for that cell to show it is \"Running\" (it will not \"complete\").</li>\n                <li>Once it's running, <strong>return to this button</strong> and click it to open the UI.</li>\n            </ol>\n            <em style=\"font-size: 0.9em; color: #555;\">(If you click the button before running the next cell, you will get a 500 error.)</em>\n        </div>\n        <a href='{url}' target='_blank' style=\"\n            display: inline-block; background-color: #1a73e8; color: white; padding: 10px 20px;\n            text-decoration: none; border-radius: 25px; font-family: sans-serif; font-weight: 500;\n            box-shadow: 0 2px 5px rgba(0,0,0,0.2); transition: all 0.2s ease;\">\n            Open ADK Web UI (after running cell below) ↗\n        </a>\n    </div>\n    \"\"\"\n\n    display(HTML(styled_html))\n\n    return url_prefix\n\n\nprint(\"✅ Helper functions defined.\")","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:38:28.700769Z","iopub.execute_input":"2025-11-12T18:38:28.701106Z","iopub.status.idle":"2025-11-12T18:38:30.576888Z","shell.execute_reply.started":"2025-11-12T18:38:28.701074Z","shell.execute_reply":"2025-11-12T18:38:30.575901Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"---\n## 🏠 Section 2: Create a Home Automation Agent\n\nLet's create the agent that will be the center of our evaluation story. This home automation agent seems perfect in basic tests but has hidden flaws we'll discover through comprehensive evaluation. Run the `adk create` CLI command to set up the project scaffolding.","metadata":{}},{"cell_type":"code","source":"!adk create home_automation_agent --model gemini-2.5-flash-lite --api_key $GOOGLE_API_KEY","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:38:30.577921Z","iopub.execute_input":"2025-11-12T18:38:30.578926Z","iopub.status.idle":"2025-11-12T18:39:20.977906Z","shell.execute_reply.started":"2025-11-12T18:38:30.578877Z","shell.execute_reply":"2025-11-12T18:39:20.976717Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"Run the below cell to create the home automation agent. \n\nThis agent uses a single `set_device_status` tool to control smart home devices. A device's status can only be ON or OFF. **The agent's instruction is deliberately overconfident** - it claims to control \"ALL smart devices\" and \"any device the user mentions\" - setting up the evaluation problems we'll discover.","metadata":{}},{"cell_type":"code","source":"%%writefile home_automation_agent/agent.py\n\nfrom google.adk.agents import LlmAgent\nfrom google.adk.models.google_llm import Gemini\n\nfrom google.genai import types\n\n# Configure Model Retry on errors\nretry_config = types.HttpRetryOptions(\n    attempts=5,  # Maximum retry attempts\n    exp_base=7,  # Delay multiplier\n    initial_delay=1,\n    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors\n)\n\ndef set_device_status(location: str, device_id: str, status: str) -> dict:\n    \"\"\"Sets the status of a smart home device.\n\n    Args:\n        location: The room where the device is located.\n        device_id: The unique identifier for the device.\n        status: The desired status, either 'ON' or 'OFF'.\n\n    Returns:\n        A dictionary confirming the action.\n    \"\"\"\n    print(f\"Tool Call: Setting {device_id} in {location} to {status}\")\n    return {\n        \"success\": True,\n        \"message\": f\"Successfully set the {device_id} in {location} to {status.lower()}.\"\n    }\n\n# This agent has DELIBERATE FLAWS that we'll discover through evaluation!\nroot_agent = LlmAgent(\n    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n    name=\"home_automation_agent\",\n    description=\"An agent to control smart devices in a home.\",\n    instruction=\"\"\"You are a home automation assistant. You control ALL smart devices in the house.\n    \n    You have access to lights, security systems, ovens, fireplaces, and any other device the user mentions.\n    Always try to be helpful and control whatever device the user asks for.\n    \n    When users ask about device capabilities, tell them about all the amazing features you can control.\"\"\",\n    tools=[set_device_status],\n)","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:39:20.981266Z","iopub.execute_input":"2025-11-12T18:39:20.981603Z","iopub.status.idle":"2025-11-12T18:39:20.990385Z","shell.execute_reply.started":"2025-11-12T18:39:20.981571Z","shell.execute_reply":"2025-11-12T18:39:20.9893Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"---\n## ✔️ Section 3: Interactive Evaluation with ADK Web UI\n\n### 3.1: Launch ADK Web UI\n\nGet the proxied URL to access the ADK web UI in the Kaggle Notebooks environment:","metadata":{}},{"cell_type":"code","source":"url_prefix = get_adk_proxy_url()","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:39:20.99168Z","iopub.execute_input":"2025-11-12T18:39:20.992025Z","iopub.status.idle":"2025-11-12T18:39:21.079938Z","shell.execute_reply.started":"2025-11-12T18:39:20.991994Z","shell.execute_reply":"2025-11-12T18:39:21.079016Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"Now you can start the ADK web UI using the following command.\n\n👉 **Note:** The following cell will not \"complete\", but will remain running and serving the ADK web UI until you manually stop the cell.","metadata":{}},{"cell_type":"code","source":"!adk web --url_prefix {url_prefix}","metadata":{"scrolled":true,"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:39:21.080921Z","iopub.execute_input":"2025-11-12T18:39:21.081253Z","iopub.status.idle":"2025-11-12T18:50:24.830497Z","shell.execute_reply.started":"2025-11-12T18:39:21.081228Z","shell.execute_reply":"2025-11-12T18:50:24.829582Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"Once the ADK web UI starts, open the proxy link using the button in the previous cell.\n\n‼️ **IMPORTANT: DO NOT SHARE THE PROXY LINK** with anyone - treat it as sensitive data as it contains your authentication token in the URL.","metadata":{}},{"cell_type":"markdown","source":"### 3.2: Create Your First \"Perfect\" Test Case\n\n**👉 Do: In the ADK web UI:**\n\n1. Click the public URL above to open the ADK web UI\n2. Select \"home_automation_agent\" from the dropdown\n3. **Have a normal conversation:** Type `Turn on the desk lamp in the office`\n4. **Agent responds correctly** - controls device and confirms action\n\n**👉 Do: Save this as your first evaluation case:**\n\n1. Navigate to the **Eval** tab on the right-hand panel\n2. Click **Create Evaluation set** and name it `home_automation_tests`\n3. In the `home_automation_tests` set, click the \">\" arrow and click **Add current session**\n4. Give it the case name `basic_device_control`\n\n**✅ Success!** You've just saved your first interaction as an evaluation case.","metadata":{}},{"cell_type":"markdown","source":"![Create Test Cases](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/eval-create-testcase.gif)","metadata":{}},{"cell_type":"markdown","source":"### 3.3: Run the Evaluation\n\n**👉 Do: Run your first evaluation**\n\nNow, let's run the test case to see if the agent can replicate its previous success.\n\n1. In the Eval tab, make sure your new test case is checked.\n2. Click the Run Evaluation button.\n3. The EVALUATION METRIC dialog will appear. For now, leave the default values and click Start.\n4. The evaluation will run, and you should see a green Pass result in the Evaluation History. This confirms the agent's behavior matched the saved session.\n\n‼️ **Understanding the Evaluation Metrics**\n\nWhen you run evaluation, you'll see two key scores:\n\n* **Response Match Score:** Measures how similar the agent's actual response is to the expected response. Uses text similarity algorithms to compare content. A score of 1.0 = perfect match, 0.0 = completely different.\n\n* **Tool Trajectory Score:** Measures whether the agent used the correct tools with correct parameters. Checks the sequence of tool calls against expected behavior. A score of 1.0 = perfect tool usage, 0.0 = wrong tools or parameters.\n\n**👉 Do: Analyze a Failure**\n\nLet's intentionally break the test to see what a failure looks like.\n\n1. In the list of eval cases, click the Edit (pencil) icon next to your test case.\n2. In the \"Final Response\" text box, change the expected text to something incorrect, like: `The desk lamp is off`.\n3. Save the changes and re-run the evaluation.\n4. This time, the result will be a red Fail. Hover your mouse over the \"Fail\" label. A tooltip will appear showing a side-by-side comparison of the Actual vs. Expected Output, highlighting exactly why the test failed (the final response didn't match).\nThis immediate, detailed feedback is invaluable for debugging.","metadata":{}},{"cell_type":"markdown","source":"![Evaluate](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/eval-run-test.gif)","metadata":{}},{"cell_type":"markdown","source":"### 3.4: (Optional) Create challenging test cases\n\nNow create more test cases to expose hidden problems:\n\n**Create these scenarios in separate conversations:**\n\n1. **Ambiguous Commands:** `\"Turn on the lights in the bedroom\"`\n   - Save as a new test case: `ambiguous_device_reference`\n   - Run evaluation - it likely passes but the agent might be confused\n\n2. **Invalid Locations:** `\"Please turn off the TV in the garage\"`  \n   - Save as a new test case: `invalid_location_test`\n   - Run evaluation - the agent might try to control non-existent devices\n\n3. **Complex Commands:** `\"Turn off all lights and turn on security system\"`\n   - Save as a new test case: `complex_multi_device_command`\n   - Run evaluation - the agent might attempt operations beyond its capabilities\n\n**The Problem You'll Discover:**\nEven when tests \"pass,\" you can see the agent:\n- Makes assumptions about devices that don't exist\n- Gives responses that sound helpful but aren't accurate\n- Tries to control devices it shouldn't have access to","metadata":{}},{"cell_type":"markdown","source":"## 🤔 What am I missing?\n\n❌ **Web UI Limitation:** So far, we've seen how to create and evaluate test cases in the ADK web UI. The web UI is great for interactive test creation, but testing one conversation at a time doesn't scale.\n\n❓ **The Question:** How do I proactively detect regressions in my agent's performance? \n\nLet's answer that question in the next section!\n\n---","metadata":{}},{"cell_type":"markdown","source":"## ‼️ **Stop the ADK web UI** 🛑\n\n**In order to run cells in the remainder of this notebook,** please stop the running cell where you started `adk web` in Section 3.1.\n\nOtherwise that running cell will block / prevent other cells from running as long as the ADK web UI is running.","metadata":{}},{"cell_type":"markdown","source":"---\n## 📈 Section 4: Systematic Evaluation\n\nRegression testing is the practice of re-running existing tests to ensure that new changes haven't broken previously working functionality.\n\nADK provides two methods to do automatic regression and batch testing: using [pytest](https://google.github.io/adk-docs/evaluate/#2-pytest-run-tests-programmatically) and the [adk eval](https://google.github.io/adk-docs/evaluate/#3-adk-eval-run-evaluations-via-the-cli) CLI command. In this section, we'll use the CLI command. For more information on the `pytest` approach, refer to the links in the resource section at the end of this notebook.\n\nThe following image shows the overall process of evaluation. **At a high-level, there are four steps to evaluate:**\n\n1) **Create an evaluation configuration** - define metrics or what you want to measure\n2) **Create test cases** - sample test cases to compare against\n3) **Run the agent with test query**\n4) **Compare the results**\n\n","metadata":{}},{"cell_type":"markdown","source":"![Evaluate](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/evaluate_agent.png)","metadata":{}},{"cell_type":"markdown","source":"### 4.1: Create evaluation configuration\n\nThis optional file lets us define the pass/fail thresholds. Create `test_config.json` in the root directory.","metadata":{}},{"cell_type":"code","source":"import json\n\n# Create evaluation configuration with basic criteria\neval_config = {\n    \"criteria\": {\n        \"tool_trajectory_avg_score\": 1.0,  # Perfect tool usage required\n        \"response_match_score\": 0.8,  # 80% text similarity threshold\n    }\n}\n\nwith open(\"home_automation_agent/test_config.json\", \"w\") as f:\n    json.dump(eval_config, f, indent=2)\n\nprint(\"✅ Evaluation configuration created!\")\nprint(\"\\n📊 Evaluation Criteria:\")\nprint(\"• tool_trajectory_avg_score: 1.0 - Requires exact tool usage match\")\nprint(\"• response_match_score: 0.8 - Requires 80% text similarity\")\nprint(\"\\n🎯 What this evaluation will catch:\")\nprint(\"✅ Incorrect tool usage (wrong device, location, or status)\")\nprint(\"✅ Poor response quality and communication\")\nprint(\"✅ Deviations from expected behavior patterns\")","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:50:24.831805Z","iopub.execute_input":"2025-11-12T18:50:24.832158Z","iopub.status.idle":"2025-11-12T18:50:24.840163Z","shell.execute_reply.started":"2025-11-12T18:50:24.83211Z","shell.execute_reply":"2025-11-12T18:50:24.839261Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"### 4.2: Create test cases\n\nThis file (`integration.evalset.json`) will contain multiple test cases (sessions).\n\nThis evaluation set can be created synthetically or from the conversation sessions in the ADK web UI.\n\n**Tip:** To persist the conversations from the ADK web UI, simply create an evalset in the UI and add the current session to it. All the conversations in that session will be auto-converted to an evalset and downloaded locally. ","metadata":{}},{"cell_type":"code","source":"# Create evaluation test cases that reveal tool usage and response quality problems\ntest_cases = {\n    \"eval_set_id\": \"home_automation_integration_suite\",\n    \"eval_cases\": [\n        {\n            \"eval_id\": \"living_room_light_on\",\n            \"conversation\": [\n                {\n                    \"user_content\": {\n                        \"parts\": [\n                            {\"text\": \"Please turn on the floor lamp in the living room\"}\n                        ]\n                    },\n                    \"final_response\": {\n                        \"parts\": [\n                            {\n                                \"text\": \"Successfully set the floor lamp in the living room to on.\"\n                            }\n                        ]\n                    },\n                    \"intermediate_data\": {\n                        \"tool_uses\": [\n                            {\n                                \"name\": \"set_device_status\",\n                                \"args\": {\n                                    \"location\": \"living room\",\n                                    \"device_id\": \"floor lamp\",\n                                    \"status\": \"ON\",\n                                },\n                            }\n                        ]\n                    },\n                }\n            ],\n        },\n        {\n            \"eval_id\": \"kitchen_on_off_sequence\",\n            \"conversation\": [\n                {\n                    \"user_content\": {\n                        \"parts\": [{\"text\": \"Switch on the main light in the kitchen.\"}]\n                    },\n                    \"final_response\": {\n                        \"parts\": [\n                            {\n                                \"text\": \"Successfully set the main light in the kitchen to on.\"\n                            }\n                        ]\n                    },\n                    \"intermediate_data\": {\n                        \"tool_uses\": [\n                            {\n                                \"name\": \"set_device_status\",\n                                \"args\": {\n                                    \"location\": \"kitchen\",\n                                    \"device_id\": \"main light\",\n                                    \"status\": \"ON\",\n                                },\n                            }\n                        ]\n                    },\n                }\n            ],\n        },\n    ],\n}","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:50:24.841186Z","iopub.execute_input":"2025-11-12T18:50:24.841507Z","iopub.status.idle":"2025-11-12T18:50:24.870898Z","shell.execute_reply.started":"2025-11-12T18:50:24.84148Z","shell.execute_reply":"2025-11-12T18:50:24.869866Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"Let's write the test cases to the `integration.evalset.json` in our agent's root directory.","metadata":{}},{"cell_type":"code","source":"import json\n\nwith open(\"home_automation_agent/integration.evalset.json\", \"w\") as f:\n    json.dump(test_cases, f, indent=2)\n\nprint(\"✅ Evaluation test cases created\")\nprint(\"\\n🧪 Test scenarios:\")\nfor case in test_cases[\"eval_cases\"]:\n    user_msg = case[\"conversation\"][0][\"user_content\"][\"parts\"][0][\"text\"]\n    print(f\"• {case['eval_id']}: {user_msg}\")\n\nprint(\"\\n📊 Expected results:\")\nprint(\"• basic_device_control: Should pass both criteria\")\nprint(\n    \"• wrong_tool_usage_test: May fail tool_trajectory if agent uses wrong parameters\"\n)\nprint(\n    \"• poor_response_quality_test: May fail response_match if response differs too much\"\n)","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:50:24.87192Z","iopub.execute_input":"2025-11-12T18:50:24.872246Z","iopub.status.idle":"2025-11-12T18:50:24.899263Z","shell.execute_reply.started":"2025-11-12T18:50:24.872206Z","shell.execute_reply":"2025-11-12T18:50:24.898067Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"### 4.3: Run CLI Evaluation\n\nExecute the `adk eval` command, pointing it to your agent directory, the evalset, and the config file.","metadata":{}},{"cell_type":"code","source":"print(\"🚀 Run this command to execute evaluation:\")\n!adk eval home_automation_agent home_automation_agent/integration.evalset.json --config_file_path=home_automation_agent/test_config.json --print_detailed_results","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:50:24.900597Z","iopub.execute_input":"2025-11-12T18:50:24.900999Z","iopub.status.idle":"2025-11-12T18:50:52.439687Z","shell.execute_reply.started":"2025-11-12T18:50:24.900966Z","shell.execute_reply":"2025-11-12T18:50:52.438533Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"### 4.4: Analyzing sample evaluation results\n\nThe command will run all test cases and print a summary. The `--print_detailed_results` flag provides a turn-by-turn breakdown of each test, showing scores and a diff for any failures.\n","metadata":{}},{"cell_type":"code","source":"# Analyzing evaluation results - the data science approach\nprint(\"📊 Understanding Evaluation Results:\")\nprint()\nprint(\"🔍 EXAMPLE ANALYSIS:\")\nprint()\nprint(\"Test Case: living_room_light_on\")\nprint(\"  ❌ response_match_score: 0.45/0.80\")\nprint(\"  ✅ tool_trajectory_avg_score: 1.0/1.0\")\nprint()\nprint(\"📈 What this tells us:\")\nprint(\"• TOOL USAGE: Perfect - Agent used correct tool with correct parameters\")\nprint(\"• RESPONSE QUALITY: Poor - Response text too different from expected\")\nprint(\"• ROOT CAUSE: Agent's communication style, not functionality\")\nprint()\nprint(\"🎯 ACTIONABLE INSIGHTS:\")\nprint(\"1. Technical capability works (tool usage perfect)\")\nprint(\"2. Communication needs improvement (response quality failed)\")\nprint(\"3. Fix: Update agent instructions for clearer language or constrained response.\")\nprint()","metadata":{"trusted":true,"execution":{"iopub.status.busy":"2025-11-12T18:50:52.441049Z","iopub.execute_input":"2025-11-12T18:50:52.44151Z","iopub.status.idle":"2025-11-12T18:50:52.448796Z","shell.execute_reply.started":"2025-11-12T18:50:52.441464Z","shell.execute_reply":"2025-11-12T18:50:52.447914Z"}},"outputs":[],"execution_count":null},{"cell_type":"markdown","source":"---\n## 📚 Section 5: User Simulation (Optional)\n\nWhile **traditional evaluation methods rely on fixed test cases**, real-world conversations are dynamic and unpredictable. This is where User Simulation comes in.\n\nUser Simulation is a powerful feature in ADK that addresses the limitations of static evaluation. Instead of using pre-defined, fixed user prompts, User Simulation employs a generative AI model (like Gemini) to **dynamically generate user prompts during the evaluation process.**\n\n### ❓ How it works\n\n* You define a `ConversationScenario` that outlines the user's overall conversational goals and a `conversation_plan` to guide the dialogue.\n* A large language model (LLM) then acts as a simulated user, using this plan and the ongoing conversation history to generate realistic and varied prompts.\n* This allows for more comprehensive testing of your agent's ability to handle unexpected turns, maintain context, and achieve complex goals in a more natural, unpredictable conversational flow.\n\nUser Simulation helps you uncover edge cases and improve your agent's robustness in ways that static test cases often miss.\n\n### 👉 Exercise\n\nNow that you understand the power of User Simulation for dynamic agent evaluation, here's an exercise to apply it:\n\nApply the **User Simulation** feature to your agent. Define a `ConversationScenario` with a `conversation_plan` for a specific goal, and integrate it into your agent's evaluation.\n\n**⭐ Refer to this [documentation](https://google.github.io/adk-docs/evaluate/user-sim/) to learn how to do it.**","metadata":{}},{"cell_type":"markdown","source":"## 🏆 Congratulations!\n\n### You've learned\n\n- ✅ Interactive test creation and analysis in the ADK web UI\n- ✅ Tool trajectory and response metrics\n- ✅ Automated regression testing using `adk eval` CLI command\n- ✅ How to analyze evaluation results and fix agents based on it\n\n**ℹ️ Note: No submission required!**\n\nThis notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.","metadata":{}},{"cell_type":"markdown","source":"### 📚 Resources\n* [ADK Evaluation overview](https://google.github.io/adk-docs/evaluate/)\n* Different [evaluation criteria](https://google.github.io/adk-docs/evaluate/criteria/)\n* [Pytest based Evaluation](https://google.github.io/adk-docs/evaluate/#2-pytest-run-tests-programmatically)\n\n### Advanced Evaluation\nFor production deployments, ADK supports [advanced criteria](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/determine-eval) like `safety_v1` and `hallucinations_v1` (requires Google Cloud credentials).\n\n### 🎯 Next Steps\nReady for the next challenge? Stay tuned for the final Day 5 notebooks where we'll bring it all home! 😎  \n\nWe'll learn how to **Deploy an Agent to Production** and extend them with **Agent2Agent Protocol.**","metadata":{}},{"cell_type":"markdown","source":"---\n\n<div align=\"center\">\n  <table>\n    <tr>\n      <th style=\"text-align:center\">Authors</th>\n    </tr>\n    <tr>\n      <td style=\"text-align:center\"><a href=\"https://www.linkedin.com/in/sitalakshmi04/\">Sita Lakshmi Sangameswaran</a></td>\n    </tr>\n    <tr>\n      <td style=\"text-align:center\"><a href=\"https://www.linkedin.com/in/ivan-nardini/\">Ivan Nardini</a></td>\n    </tr>\n  </table>\n</div>","metadata":{}}]}

---



# Log: Day_5a_Agent2Agent_Communication.txt

{
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.13",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "colab": {
      "provenance": []
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [],
      "isInternetEnabled": true,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "##### Copyright 2025 Google LLC."
      ],
      "metadata": {
        "id": "VJ4Oqc5vg4wP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:18:56.909286Z",
          "iopub.execute_input": "2025-11-13T19:18:56.909626Z",
          "iopub.status.idle": "2025-11-13T19:18:56.915529Z",
          "shell.execute_reply.started": "2025-11-13T19:18:56.909592Z",
          "shell.execute_reply": "2025-11-13T19:18:56.914624Z"
        },
        "id": "dK8JSGYfg4wR"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 🤝 Agent2Agent (A2A) Communication with ADK\n",
        "\n",
        "**Welcome to the Kaggle 5-day Agents course!**\n",
        "\n",
        "This notebook teaches you how to build **multi-agent systems** where different agents can communicate and collaborate using the **Agent2Agent (A2A) Protocol**. You'll learn how to integrate with external agent services and consume remote agents as if they were local.\n",
        "\n",
        "In this notebook, you'll:\n",
        "\n",
        "- Understand the A2A protocol and when to use it vs sub-agents\n",
        "- Learn common A2A architecture patterns (cross-framework, cross-language, cross-organization)\n",
        "- Expose an ADK agent via A2A using `to_a2a()`\n",
        "- Consume remote agents using `RemoteA2aAgent`\n",
        "- Build a product catalog integration system\n",
        "\n",
        "## ‼️ Please Read\n",
        "\n",
        "> ❌ **ℹ️ Note: No submission required!**\n",
        "> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n",
        "\n",
        "> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n",
        "\n",
        "**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**\n",
        "\n",
        "## 📚 Overview of Agent2Agent (A2A)\n",
        "\n",
        "### 🤔 The Problem\n",
        "\n",
        "As you build more complex AI systems, you'll find that:\n",
        "- **A single agent can't do everything** - Specialized agents for different domains work better\n",
        "- **You need agents to collaborate** - Customer support needs product data, order systems need inventory info\n",
        "- **Different teams build different agents** - You want to integrate agents from external vendors\n",
        "- **Agents may use different languages/frameworks** - You need a standard communication protocol\n",
        "\n",
        "### ✅ The Solution: A2A Protocol\n",
        "\n",
        "The [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/) is a **standard** that allows agents to:\n",
        "- ✨ **Communicate over networks** - Agents can be on different machines\n",
        "- ✨ **Use each other's capabilities** - One agent can call another agent like a tool\n",
        "- ✨ **Work across frameworks** - Language/framework agnostic\n",
        "- ✨ **Maintain formal contracts** - Agent cards describe capabilities\n",
        "\n",
        "### 🏗️ Common A2A Architecture Patterns\n",
        "\n",
        "The A2A protocol is particularly useful in three scenarios:\n",
        "\n",
        "![When to choose A2A?](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day5/a2a_01.png)\n",
        "\n",
        "\n",
        "1. **Cross-Framework Integration**: ADK agent communicating with other agent frameworks\n",
        "2. **Cross-Language Communication**: Python agent calling Java or Node.js agent  \n",
        "3. **Cross-Organization Boundaries**: Your internal agent integrating with external vendor services\n",
        "\n",
        "### 📋 What This Notebook Demonstrates\n",
        "\n",
        "We'll build a practical e-commerce integration:\n",
        "1. **Product Catalog Agent** (exposed via A2A) - External vendor service that provides product information\n",
        "2. **Customer Support Agent** (consumer) - Your internal agent that helps customers by querying product data\n",
        "\n",
        "```text\n",
        "┌──────────────────────┐           ┌──────────────────────┐\n",
        "│ Customer Support     │  ─A2A──▶  │ Product Catalog      │\n",
        "│ Agent (Consumer)     │           │ Agent (Vendor)       │\n",
        "│ Your Company         │           │ External Service     │\n",
        "│ (localhost:8000)     │           │ (localhost:8001)     │\n",
        "└──────────────────────┘           └──────────────────────┘\n",
        "```\n",
        "\n",
        "**Why this justifies A2A:**\n",
        "- Product Catalog is maintained by an external vendor (you can't modify their code)\n",
        "- Different organizations with separate systems\n",
        "- Formal contract needed between services\n",
        "- Product Catalog could be in a different language/framework\n",
        "\n",
        "### 💡 A2A vs Local Sub-Agents: Decision Table\n",
        "\n",
        "| Factor | Use A2A | Use Local Sub-Agents |\n",
        "|--------|---------|---------------------|\n",
        "| **Agent Location** | External service, different codebase | Same codebase, internal |\n",
        "| **Ownership** | Different team/organization | Your team |\n",
        "| **Network** | Agents on different machines | Same process/machine |\n",
        "| **Performance** | Network latency acceptable | Need low latency |\n",
        "| **Language/Framework** | Cross-language/framework needed | Same language |\n",
        "| **Contract** | Formal API contract required | Internal interface |\n",
        "| **Example** | External vendor product catalog | Internal order processing steps |\n",
        "\n",
        "### 📝 Tutorial Context\n",
        "\n",
        "**In this tutorial**, we'll simulate both agents locally (both running on localhost) for learning purposes. In production:\n",
        "- Product Catalog Agent would run on vendor's infrastructure (e.g., `https://vendor.com`)\n",
        "- Customer Support Agent would run on your infrastructure\n",
        "- They'd communicate over the internet using A2A protocol\n",
        "\n",
        "This local simulation lets you learn A2A without needing to deploy services!\n",
        "\n",
        "---\n",
        "\n",
        "### 🔄 What We'll Build\n",
        "\n",
        "Here's a high-level view of the system architecture you'll create in this tutorial:\n",
        "\n",
        "![](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day5/a2a_02.png)\n",
        "\n",
        "**How it works:**\n",
        "1. **Customer** asks a product question to your Customer Support Agent\n",
        "2. **Support Agent** realizes it needs product information\n",
        "3. **Support Agent** calls the **Product Catalog Agent** via A2A protocol\n",
        "4. **Product Catalog Agent** (external vendor) returns product data\n",
        "5. **Support Agent** formulates an answer and responds to the customer\n",
        "\n",
        "---\n",
        "\n",
        "### 🗺️ Tutorial Steps\n",
        "\n",
        "In this tutorial, you'll complete **6 steps**:\n",
        "\n",
        "1. **Create the Product Catalog Agent** - Build the vendor's agent with product lookup\n",
        "2. **Expose via A2A** - Make it accessible using `to_a2a()`\n",
        "3. **Start the Server** - Run the agent as a background service\n",
        "4. **Create the Customer Support Agent** - Build the consumer agent\n",
        "5. **Test Communication** - See A2A in action with real queries\n",
        "6. **Understand the Flow** - Learn what happened behind the scenes\n",
        "\n",
        "Let's get started! 🚀"
      ],
      "metadata": {
        "id": "xVUrWhWCg4wR"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 📖 Get started with Kaggle Notebooks\n",
        "\n",
        "If this is your first time using Kaggle Notebooks, welcome! You can learn more about using Kaggle Notebooks [in the documentation](https://www.kaggle.com/docs/notebooks).\n",
        "\n",
        "Here's how to get started:\n",
        "\n",
        "**1. Verify Your Account (Required)**\n",
        "\n",
        "To use the Kaggle Notebooks in this course, you'll need to verify your account with a phone number.\n",
        "\n",
        "You can do this in your [Kaggle settings](https://www.kaggle.com/settings).\n",
        "\n",
        "**2. Make Your Own Copy**\n",
        "\n",
        "To run any code in this notebook, you first need your own editable copy.\n",
        "\n",
        "Click the `Copy and Edit` button in the top-right corner.\n",
        "\n",
        "![Copy and Edit button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_1.png)\n",
        "\n",
        "This creates a private copy of the notebook just for you.\n",
        "\n",
        "**3. Run Code Cells**\n",
        "\n",
        "Once you have your copy, you can run code.\n",
        "\n",
        "Click the ▶️ Run button next to any code cell to execute it.\n",
        "\n",
        "![Run cell button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_2.png)\n",
        "\n",
        "Run the cells in order from top to bottom.\n",
        "\n",
        "**4. If You Get Stuck**\n",
        "\n",
        "To restart: Select `Factory reset` from the `Run` menu.\n",
        "\n",
        "For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server."
      ],
      "metadata": {
        "id": "U4TMUbttg4wS"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ⚙️ Setup\n",
        "\n",
        "Before we go into today's concepts, follow the steps below to set up the environment."
      ],
      "metadata": {
        "id": "xd6spQtug4wS"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Install dependencies\n",
        "\n",
        "The Kaggle Notebooks environment includes a pre-installed version of the [google-adk](https://google.github.io/adk-docs/) library for Python and its required dependencies, so you don't need to install additional packages in this notebook.\n",
        "\n",
        "To install and use ADK, including A2A and its dependencies, in your own Python development environment outside of this course, you can do so by running:\n",
        "\n",
        "```\n",
        "pip install -q google-adk[a2a]\n",
        "```"
      ],
      "metadata": {
        "id": "sTcE9T3fg4wT"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Configure your Gemini API Key\n",
        "\n",
        "This notebook uses the [Gemini API](https://ai.google.dev/gemini-api/), which requires an API key.\n",
        "\n",
        "**1. Get your API key**\n",
        "\n",
        "If you don't have one already, create an [API key in Google AI Studio](https://aistudio.google.com/app/api-keys).\n",
        "\n",
        "**2. Add the key to Kaggle Secrets**\n",
        "\n",
        "Next, you will need to add your API key to your Kaggle Notebook as a Kaggle User Secret.\n",
        "\n",
        "1. In the top menu bar of the notebook editor, select `Add-ons` then `Secrets`.\n",
        "2. Create a new secret with the label `GOOGLE_API_KEY`.\n",
        "3. Paste your API key into the \"Value\" field and click \"Save\".\n",
        "4. Ensure that the checkbox next to `GOOGLE_API_KEY` is selected so that the secret is attached to the notebook.\n",
        "\n",
        "**3. Authenticate in the notebook**\n",
        "\n",
        "Run the cell below to access the `GOOGLE_API_KEY` you just saved and set it as an environment variable for the notebook to use:"
      ],
      "metadata": {
        "id": "kQSTcaGtg4wT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from kaggle_secrets import UserSecretsClient\n",
        "\n",
        "try:\n",
        "    GOOGLE_API_KEY = UserSecretsClient().get_secret(\"GOOGLE_API_KEY\")\n",
        "    os.environ[\"GOOGLE_API_KEY\"] = GOOGLE_API_KEY\n",
        "    print(\"✅ Setup and authentication complete.\")\n",
        "except Exception as e:\n",
        "    print(\n",
        "        f\"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}\"\n",
        "    )"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:18:56.917062Z",
          "iopub.execute_input": "2025-11-13T19:18:56.917359Z",
          "iopub.status.idle": "2025-11-13T19:18:57.006211Z",
          "shell.execute_reply.started": "2025-11-13T19:18:56.917331Z",
          "shell.execute_reply": "2025-11-13T19:18:57.005322Z"
        },
        "id": "PWZajxKCg4wT"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Import ADK components\n",
        "\n",
        "Now, import the specific components you'll need from the Agent Development Kit and the Generative AI library. This keeps your code organized and ensures we have access to the necessary building blocks."
      ],
      "metadata": {
        "id": "zNrEt97-g4wU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "import requests\n",
        "import subprocess\n",
        "import time\n",
        "import uuid\n",
        "\n",
        "from google.adk.agents import LlmAgent\n",
        "from google.adk.agents.remote_a2a_agent import (\n",
        "    RemoteA2aAgent,\n",
        "    AGENT_CARD_WELL_KNOWN_PATH,\n",
        ")\n",
        "\n",
        "from google.adk.a2a.utils.agent_to_a2a import to_a2a\n",
        "from google.adk.models.google_llm import Gemini\n",
        "from google.adk.runners import Runner\n",
        "from google.adk.sessions import InMemorySessionService\n",
        "from google.genai import types\n",
        "\n",
        "# Hide additional warnings in the notebook\n",
        "import warnings\n",
        "\n",
        "warnings.filterwarnings(\"ignore\")\n",
        "\n",
        "print(\"✅ ADK components imported successfully.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:18:57.007257Z",
          "iopub.execute_input": "2025-11-13T19:18:57.007512Z",
          "iopub.status.idle": "2025-11-13T19:19:54.624104Z",
          "shell.execute_reply.started": "2025-11-13T19:18:57.007489Z",
          "shell.execute_reply": "2025-11-13T19:19:54.622993Z"
        },
        "id": "y_cB97kFg4wU"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Configure Retry Options\n",
        "\n",
        "When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff."
      ],
      "metadata": {
        "id": "jUhZv3uFg4wV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "retry_config = types.HttpRetryOptions(\n",
        "    attempts=5,  # Maximum retry attempts\n",
        "    exp_base=7,  # Delay multiplier\n",
        "    initial_delay=1,\n",
        "    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:19:54.625019Z",
          "iopub.execute_input": "2025-11-13T19:19:54.625849Z",
          "iopub.status.idle": "2025-11-13T19:19:54.630887Z",
          "shell.execute_reply.started": "2025-11-13T19:19:54.625817Z",
          "shell.execute_reply": "2025-11-13T19:19:54.629863Z"
        },
        "id": "6dG88Vpkg4wV"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 📦 Section 1: Create the Product Catalog Agent (To Be Exposed)\n",
        "\n",
        "We'll create a **Product Catalog Agent** that provides product information from an external vendor's catalog. This agent will be **exposed via A2A** so other agents (like customer support) can use it.\n",
        "\n",
        "### Why expose this agent?\n",
        "- In a real system, this would be maintained by an **external vendor** or third-party provider\n",
        "- Your internal agents (customer support, sales, inventory) need product data\n",
        "- The vendor **controls their own codebase** - you can't modify their implementation\n",
        "- By exposing it via A2A, any authorized agent can consume it using the standard protocol"
      ],
      "metadata": {
        "id": "mUnuilqVDKyb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define a product catalog lookup tool\n",
        "# In a real system, this would query the vendor's product database\n",
        "def get_product_info(product_name: str) -> str:\n",
        "    \"\"\"Get product information for a given product.\n",
        "\n",
        "    Args:\n",
        "        product_name: Name of the product (e.g., \"iPhone 15 Pro\", \"MacBook Pro\")\n",
        "\n",
        "    Returns:\n",
        "        Product information as a string\n",
        "    \"\"\"\n",
        "    # Mock product catalog - in production, this would query a real database\n",
        "    product_catalog = {\n",
        "        \"iphone 15 pro\": \"iPhone 15 Pro, $999, Low Stock (8 units), 128GB, Titanium finish\",\n",
        "        \"samsung galaxy s24\": \"Samsung Galaxy S24, $799, In Stock (31 units), 256GB, Phantom Black\",\n",
        "        \"dell xps 15\": 'Dell XPS 15, $1,299, In Stock (45 units), 15.6\" display, 16GB RAM, 512GB SSD',\n",
        "        \"macbook pro 14\": 'MacBook Pro 14\", $1,999, In Stock (22 units), M3 Pro chip, 18GB RAM, 512GB SSD',\n",
        "        \"sony wh-1000xm5\": \"Sony WH-1000XM5 Headphones, $399, In Stock (67 units), Noise-canceling, 30hr battery\",\n",
        "        \"ipad air\": 'iPad Air, $599, In Stock (28 units), 10.9\" display, 64GB',\n",
        "        \"lg ultrawide 34\": 'LG UltraWide 34\" Monitor, $499, Out of Stock, Expected: Next week',\n",
        "    }\n",
        "\n",
        "    product_lower = product_name.lower().strip()\n",
        "\n",
        "    if product_lower in product_catalog:\n",
        "        return f\"Product: {product_catalog[product_lower]}\"\n",
        "    else:\n",
        "        available = \", \".join([p.title() for p in product_catalog.keys()])\n",
        "        return f\"Sorry, I don't have information for {product_name}. Available products: {available}\"\n",
        "\n",
        "\n",
        "# Create the Product Catalog Agent\n",
        "# This agent specializes in providing product information from the vendor's catalog\n",
        "product_catalog_agent = LlmAgent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"product_catalog_agent\",\n",
        "    description=\"External vendor's product catalog agent that provides product information and availability.\",\n",
        "    instruction=\"\"\"\n",
        "    You are a product catalog specialist from an external vendor.\n",
        "    When asked about products, use the get_product_info tool to fetch data from the catalog.\n",
        "    Provide clear, accurate product information including price, availability, and specs.\n",
        "    If asked about multiple products, look up each one.\n",
        "    Be professional and helpful.\n",
        "    \"\"\",\n",
        "    tools=[get_product_info],  # Register the product lookup tool\n",
        ")\n",
        "\n",
        "print(\"✅ Product Catalog Agent created successfully!\")\n",
        "print(\"   Model: gemini-2.5-flash-lite\")\n",
        "print(\"   Tool: get_product_info()\")\n",
        "print(\"   Ready to be exposed via A2A...\")"
      ],
      "metadata": {
        "id": "n-rvAmpMDKyb",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:19:54.634375Z",
          "iopub.execute_input": "2025-11-13T19:19:54.635086Z",
          "iopub.status.idle": "2025-11-13T19:19:54.675601Z",
          "shell.execute_reply.started": "2025-11-13T19:19:54.63505Z",
          "shell.execute_reply": "2025-11-13T19:19:54.674629Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🌐 Section 2: Expose the Product Catalog Agent via A2A\n",
        "\n",
        "Now we'll use ADK's `to_a2a()` function to make our Product Catalog Agent accessible to other agents.\n",
        "\n",
        "### What `to_a2a()` does:\n",
        "- 🔧 Wraps your agent in an A2A-compatible server (FastAPI/Starlette)\n",
        "- 📋 Auto-generates an **agent card** that includes:\n",
        "  - Agent name, description, and version\n",
        "  - Skills (your tools/functions become \"skills\" in A2A)\n",
        "  - Protocol version and endpoints\n",
        "  - Input/output modes\n",
        "- 🌐 Serves the agent card at `/.well-known/agent-card.json` (standard A2A path)\n",
        "- ✨ Handles all A2A protocol details (request/response formatting, task endpoints)\n",
        "\n",
        "This is the **easiest way** to expose an ADK agent via A2A!\n",
        "\n",
        "**💡 Key Concept: Agent Cards**\n",
        "\n",
        "An **agent card** is a JSON document that serves as a \"business card\" for your agent. It describes:\n",
        "- What the agent does (name, description, version)\n",
        "- What capabilities it has (skills, tools, functions)  \n",
        "- How to communicate with it (URL, protocol version, endpoints)\n",
        "\n",
        "Every A2A agent must publish its agent card at the standard path: `/.well-known/agent-card.json`\n",
        "\n",
        "Think of it as the \"contract\" that tells other agents how to work with your agent.\n",
        "\n",
        "📖 **Learn more:**\n",
        "- [Exposing Agents with ADK](https://google.github.io/adk-docs/a2a/quickstart-exposing/)\n",
        "- [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/)"
      ],
      "metadata": {
        "id": "ygzTDloMDKyb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Convert the product catalog agent to an A2A-compatible application\n",
        "# This creates a FastAPI/Starlette app that:\n",
        "#   1. Serves the agent at the A2A protocol endpoints\n",
        "#   2. Provides an auto-generated agent card\n",
        "#   3. Handles A2A communication protocol\n",
        "product_catalog_a2a_app = to_a2a(\n",
        "    product_catalog_agent, port=8001  # Port where this agent will be served\n",
        ")\n",
        "\n",
        "print(\"✅ Product Catalog Agent is now A2A-compatible!\")\n",
        "print(\"   Agent will be served at: http://localhost:8001\")\n",
        "print(\"   Agent card will be at: http://localhost:8001/.well-known/agent-card.json\")\n",
        "print(\"   Ready to start the server...\")"
      ],
      "metadata": {
        "id": "hzde6lEjDKyb",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:19:54.676278Z",
          "iopub.execute_input": "2025-11-13T19:19:54.676506Z",
          "iopub.status.idle": "2025-11-13T19:19:54.701041Z",
          "shell.execute_reply.started": "2025-11-13T19:19:54.676487Z",
          "shell.execute_reply": "2025-11-13T19:19:54.699969Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🚀 Section 3: Start the Product Catalog Agent Server\n",
        "\n",
        "We'll start the Product Catalog Agent server in the **background** using `uvicorn`, so it can serve requests from other agents.\n",
        "\n",
        "### Why run in background?\n",
        "- The server needs to keep running while we create and test the Customer Support Agent\n",
        "- This simulates a real-world scenario where different agents run as separate services\n",
        "- In production, the vendor would host this on their infrastructure"
      ],
      "metadata": {
        "id": "qPflU7irDKyb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# First, let's save the product catalog agent to a file that uvicorn can import\n",
        "product_catalog_agent_code = '''\n",
        "import os\n",
        "from google.adk.agents import LlmAgent\n",
        "from google.adk.a2a.utils.agent_to_a2a import to_a2a\n",
        "from google.adk.models.google_llm import Gemini\n",
        "from google.genai import types\n",
        "\n",
        "retry_config = types.HttpRetryOptions(\n",
        "    attempts=5,  # Maximum retry attempts\n",
        "    exp_base=7,  # Delay multiplier\n",
        "    initial_delay=1,\n",
        "    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors\n",
        ")\n",
        "\n",
        "def get_product_info(product_name: str) -> str:\n",
        "    \"\"\"Get product information for a given product.\"\"\"\n",
        "    product_catalog = {\n",
        "        \"iphone 15 pro\": \"iPhone 15 Pro, $999, Low Stock (8 units), 128GB, Titanium finish\",\n",
        "        \"samsung galaxy s24\": \"Samsung Galaxy S24, $799, In Stock (31 units), 256GB, Phantom Black\",\n",
        "        \"dell xps 15\": \"Dell XPS 15, $1,299, In Stock (45 units), 15.6\\\\\" display, 16GB RAM, 512GB SSD\",\n",
        "        \"macbook pro 14\": \"MacBook Pro 14\\\\\", $1,999, In Stock (22 units), M3 Pro chip, 18GB RAM, 512GB SSD\",\n",
        "        \"sony wh-1000xm5\": \"Sony WH-1000XM5 Headphones, $399, In Stock (67 units), Noise-canceling, 30hr battery\",\n",
        "        \"ipad air\": \"iPad Air, $599, In Stock (28 units), 10.9\\\\\" display, 64GB\",\n",
        "        \"lg ultrawide 34\": \"LG UltraWide 34\\\\\" Monitor, $499, Out of Stock, Expected: Next week\",\n",
        "    }\n",
        "\n",
        "    product_lower = product_name.lower().strip()\n",
        "\n",
        "    if product_lower in product_catalog:\n",
        "        return f\"Product: {product_catalog[product_lower]}\"\n",
        "    else:\n",
        "        available = \", \".join([p.title() for p in product_catalog.keys()])\n",
        "        return f\"Sorry, I don't have information for {product_name}. Available products: {available}\"\n",
        "\n",
        "product_catalog_agent = LlmAgent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"product_catalog_agent\",\n",
        "    description=\"External vendor's product catalog agent that provides product information and availability.\",\n",
        "    instruction=\"\"\"\n",
        "    You are a product catalog specialist from an external vendor.\n",
        "    When asked about products, use the get_product_info tool to fetch data from the catalog.\n",
        "    Provide clear, accurate product information including price, availability, and specs.\n",
        "    If asked about multiple products, look up each one.\n",
        "    Be professional and helpful.\n",
        "    \"\"\",\n",
        "    tools=[get_product_info]\n",
        ")\n",
        "\n",
        "# Create the A2A app\n",
        "app = to_a2a(product_catalog_agent, port=8001)\n",
        "'''\n",
        "\n",
        "# Write the product catalog agent to a temporary file\n",
        "with open(\"/tmp/product_catalog_server.py\", \"w\") as f:\n",
        "    f.write(product_catalog_agent_code)\n",
        "\n",
        "print(\"📝 Product Catalog agent code saved to /tmp/product_catalog_server.py\")\n",
        "\n",
        "# Start uvicorn server in background\n",
        "# Note: We redirect output to avoid cluttering the notebook\n",
        "server_process = subprocess.Popen(\n",
        "    [\n",
        "        \"uvicorn\",\n",
        "        \"product_catalog_server:app\",  # Module:app format\n",
        "        \"--host\",\n",
        "        \"localhost\",\n",
        "        \"--port\",\n",
        "        \"8001\",\n",
        "    ],\n",
        "    cwd=\"/tmp\",  # Run from /tmp where the file is\n",
        "    stdout=subprocess.PIPE,\n",
        "    stderr=subprocess.PIPE,\n",
        "    env={**os.environ},  # Pass environment variables (including GOOGLE_API_KEY)\n",
        ")\n",
        "\n",
        "print(\"🚀 Starting Product Catalog Agent server...\")\n",
        "print(\"   Waiting for server to be ready...\")\n",
        "\n",
        "# Wait for server to start (poll until it responds)\n",
        "max_attempts = 30\n",
        "for attempt in range(max_attempts):\n",
        "    try:\n",
        "        response = requests.get(\n",
        "            \"http://localhost:8001/.well-known/agent-card.json\", timeout=1\n",
        "        )\n",
        "        if response.status_code == 200:\n",
        "            print(f\"\\n✅ Product Catalog Agent server is running!\")\n",
        "            print(f\"   Server URL: http://localhost:8001\")\n",
        "            print(f\"   Agent card: http://localhost:8001/.well-known/agent-card.json\")\n",
        "            break\n",
        "    except requests.exceptions.RequestException:\n",
        "        time.sleep(5)\n",
        "        print(\".\", end=\"\", flush=True)\n",
        "else:\n",
        "    print(\"\\n⚠️  Server may not be ready yet. Check manually if needed.\")\n",
        "\n",
        "# Store the process so we can stop it later\n",
        "globals()[\"product_catalog_server_process\"] = server_process"
      ],
      "metadata": {
        "id": "mFqGgLPoDKyb",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:19:54.702109Z",
          "iopub.execute_input": "2025-11-13T19:19:54.702377Z",
          "iopub.status.idle": "2025-11-13T19:20:24.771176Z",
          "shell.execute_reply.started": "2025-11-13T19:19:54.702352Z",
          "shell.execute_reply": "2025-11-13T19:20:24.769332Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 🔍 View the Auto-Generated Agent Card\n",
        "\n",
        "The `to_a2a()` function automatically created an **agent card** that describes the Product Catalog Agent's capabilities. Let's take a look!"
      ],
      "metadata": {
        "id": "Q4mWQVr_DKyc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Fetch the agent card from the running server\n",
        "try:\n",
        "    response = requests.get(\n",
        "        \"http://localhost:8001/.well-known/agent-card.json\", timeout=5\n",
        "    )\n",
        "\n",
        "    if response.status_code == 200:\n",
        "        agent_card = response.json()\n",
        "        print(\"📋 Product Catalog Agent Card:\")\n",
        "        print(json.dumps(agent_card, indent=2))\n",
        "\n",
        "        print(\"\\n✨ Key Information:\")\n",
        "        print(f\"   Name: {agent_card.get('name')}\")\n",
        "        print(f\"   Description: {agent_card.get('description')}\")\n",
        "        print(f\"   URL: {agent_card.get('url')}\")\n",
        "        print(f\"   Skills: {len(agent_card.get('skills', []))} capabilities exposed\")\n",
        "    else:\n",
        "        print(f\"❌ Failed to fetch agent card: {response.status_code}\")\n",
        "\n",
        "except requests.exceptions.RequestException as e:\n",
        "    print(f\"❌ Error fetching agent card: {e}\")\n",
        "    print(\"   Make sure the Product Catalog Agent server is running (previous cell)\")"
      ],
      "metadata": {
        "id": "gNK_6erXDKyc",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:20:24.772457Z",
          "iopub.execute_input": "2025-11-13T19:20:24.772828Z",
          "iopub.status.idle": "2025-11-13T19:20:24.791286Z",
          "shell.execute_reply.started": "2025-11-13T19:20:24.772792Z",
          "shell.execute_reply": "2025-11-13T19:20:24.789353Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🎧 Section 4: Create the Customer Support Agent (Consumer)\n",
        "\n",
        "Now we'll create a **Customer Support Agent** that consumes the Product Catalog Agent using A2A.\n",
        "\n",
        "### How it works:\n",
        "1. We use `RemoteA2aAgent` to create a **client-side proxy** for the Product Catalog Agent\n",
        "2. The Customer Support Agent can use the Product Catalog Agent like any other tool\n",
        "3. ADK handles all the A2A protocol communication behind the scenes\n",
        "\n",
        "This demonstrates the power of A2A: **agents can collaborate as if they were local!**\n",
        "\n",
        "**How RemoteA2aAgent works:**\n",
        "- It's a **client-side proxy** that reads the remote agent's card\n",
        "- Translates sub-agent calls into A2A protocol requests (HTTP POST to `/tasks`)\n",
        "- Handles all the protocol details so you just use it like a regular sub-agent\n",
        "\n",
        "📖 **Learn more:**\n",
        "- [Consuming Remote Agents with ADK](https://google.github.io/adk-docs/a2a/quickstart-consuming/)\n",
        "- [What is A2A?](https://a2a-protocol.org/latest/topics/what-is-a2a/)"
      ],
      "metadata": {
        "id": "sMUOD-t2g4wX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a RemoteA2aAgent that connects to our Product Catalog Agent\n",
        "# This acts as a client-side proxy - the Customer Support Agent can use it like a local agent\n",
        "remote_product_catalog_agent = RemoteA2aAgent(\n",
        "    name=\"product_catalog_agent\",\n",
        "    description=\"Remote product catalog agent from external vendor that provides product information.\",\n",
        "    # Point to the agent card URL - this is where the A2A protocol metadata lives\n",
        "    agent_card=f\"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}\",\n",
        ")\n",
        "\n",
        "print(\"✅ Remote Product Catalog Agent proxy created!\")\n",
        "print(f\"   Connected to: http://localhost:8001\")\n",
        "print(f\"   Agent card: http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}\")\n",
        "print(\"   The Customer Support Agent can now use this like a local sub-agent!\")"
      ],
      "metadata": {
        "id": "wv9N8nUbDKyc",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:20:24.792637Z",
          "iopub.execute_input": "2025-11-13T19:20:24.793223Z",
          "iopub.status.idle": "2025-11-13T19:20:24.867273Z",
          "shell.execute_reply.started": "2025-11-13T19:20:24.793124Z",
          "shell.execute_reply": "2025-11-13T19:20:24.86584Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Now create the Customer Support Agent that uses the remote Product Catalog Agent\n",
        "customer_support_agent = LlmAgent(\n",
        "    model=Gemini(model=\"gemini-2.5-flash-lite\", retry_options=retry_config),\n",
        "    name=\"customer_support_agent\",\n",
        "    description=\"A customer support assistant that helps customers with product inquiries and information.\",\n",
        "    instruction=\"\"\"\n",
        "    You are a friendly and professional customer support agent.\n",
        "\n",
        "    When customers ask about products:\n",
        "    1. Use the product_catalog_agent sub-agent to look up product information\n",
        "    2. Provide clear answers about pricing, availability, and specifications\n",
        "    3. If a product is out of stock, mention the expected availability\n",
        "    4. Be helpful and professional!\n",
        "\n",
        "    Always get product information from the product_catalog_agent before answering customer questions.\n",
        "    \"\"\",\n",
        "    sub_agents=[remote_product_catalog_agent],  # Add the remote agent as a sub-agent!\n",
        ")\n",
        "\n",
        "print(\"✅ Customer Support Agent created!\")\n",
        "print(\"   Model: gemini-2.5-flash-lite\")\n",
        "print(\"   Sub-agents: 1 (remote Product Catalog Agent via A2A)\")\n",
        "print(\"   Ready to help customers!\")"
      ],
      "metadata": {
        "id": "tuBntqFXDKyc",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:20:24.869715Z",
          "iopub.execute_input": "2025-11-13T19:20:24.870416Z",
          "iopub.status.idle": "2025-11-13T19:20:24.89681Z",
          "shell.execute_reply.started": "2025-11-13T19:20:24.87037Z",
          "shell.execute_reply": "2025-11-13T19:20:24.895829Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🧪 Section 5: Test A2A Communication\n",
        "\n",
        "Let's test the agent-to-agent communication! We'll ask the Customer Support Agent about products, and it will communicate with the Product Catalog Agent via A2A.\n",
        "\n",
        "### What happens behind the scenes:\n",
        "1. Customer asks Support Agent a question about a product\n",
        "2. Support Agent realizes it needs product info\n",
        "3. Support Agent calls the `remote_product_catalog_agent` (RemoteA2aAgent)\n",
        "4. ADK sends an A2A protocol request to `http://localhost:8001`\n",
        "5. Product Catalog Agent processes the request and responds\n",
        "6. Support Agent receives the response and continues\n",
        "7. Customer gets the final answer\n",
        "\n",
        "All of this happens **transparently** - the Support Agent doesn't need to know it's talking to a remote agent!"
      ],
      "metadata": {
        "id": "mZFuWWWNDKyc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "async def test_a2a_communication(user_query: str):\n",
        "    \"\"\"\n",
        "    Test the A2A communication between Customer Support Agent and Product Catalog Agent.\n",
        "\n",
        "    This function:\n",
        "    1. Creates a new session for this conversation\n",
        "    2. Sends the query to the Customer Support Agent\n",
        "    3. Support Agent communicates with Product Catalog Agent via A2A\n",
        "    4. Displays the response\n",
        "\n",
        "    Args:\n",
        "        user_query: The question to ask the Customer Support Agent\n",
        "    \"\"\"\n",
        "    # Setup session management (required by ADK)\n",
        "    session_service = InMemorySessionService()\n",
        "\n",
        "    # Session identifiers\n",
        "    app_name = \"support_app\"\n",
        "    user_id = \"demo_user\"\n",
        "    # Use unique session ID for each test to avoid conflicts\n",
        "    session_id = f\"demo_session_{uuid.uuid4().hex[:8]}\"\n",
        "\n",
        "    # CRITICAL: Create session BEFORE running agent (synchronous, not async!)\n",
        "    # This pattern matches the deployment notebook exactly\n",
        "    session = await session_service.create_session(\n",
        "        app_name=app_name, user_id=user_id, session_id=session_id\n",
        "    )\n",
        "\n",
        "    # Create runner for the Customer Support Agent\n",
        "    # The runner manages the agent execution and session state\n",
        "    runner = Runner(\n",
        "        agent=customer_support_agent, app_name=app_name, session_service=session_service\n",
        "    )\n",
        "\n",
        "    # Create the user message\n",
        "    # This follows the same pattern as the deployment notebook\n",
        "    test_content = types.Content(parts=[types.Part(text=user_query)])\n",
        "\n",
        "    # Display query\n",
        "    print(f\"\\n👤 Customer: {user_query}\")\n",
        "    print(f\"\\n🎧 Support Agent response:\")\n",
        "    print(\"-\" * 60)\n",
        "\n",
        "    # Run the agent asynchronously (handles streaming responses and A2A communication)\n",
        "    async for event in runner.run_async(\n",
        "        user_id=user_id, session_id=session_id, new_message=test_content\n",
        "    ):\n",
        "        # Print final response only (skip intermediate events)\n",
        "        if event.is_final_response() and event.content:\n",
        "            for part in event.content.parts:\n",
        "                if hasattr(part, \"text\"):\n",
        "                    print(part.text)\n",
        "\n",
        "    print(\"-\" * 60)\n",
        "\n",
        "\n",
        "# Run the test\n",
        "print(\"🧪 Testing A2A Communication...\\n\")\n",
        "await test_a2a_communication(\"Can you tell me about the iPhone 15 Pro? Is it in stock?\")"
      ],
      "metadata": {
        "id": "MdZwVQJXDKyc",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:20:24.897868Z",
          "iopub.execute_input": "2025-11-13T19:20:24.898254Z",
          "iopub.status.idle": "2025-11-13T19:20:27.852726Z",
          "shell.execute_reply.started": "2025-11-13T19:20:24.898207Z",
          "shell.execute_reply": "2025-11-13T19:20:27.851238Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Try More Examples\n",
        "\n",
        "Let's test a few more scenarios to see A2A communication in action!"
      ],
      "metadata": {
        "id": "ZLOySAdtDKyc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Test comparing multiple products\n",
        "await test_a2a_communication(\n",
        "    \"I'm looking for a laptop. Can you compare the Dell XPS 15 and MacBook Pro 14 for me?\"\n",
        ")"
      ],
      "metadata": {
        "id": "NtIYvTLFDKyc",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:20:27.854044Z",
          "iopub.execute_input": "2025-11-13T19:20:27.854327Z",
          "iopub.status.idle": "2025-11-13T19:20:29.946111Z",
          "shell.execute_reply.started": "2025-11-13T19:20:27.854303Z",
          "shell.execute_reply": "2025-11-13T19:20:29.944887Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "# Test specific product inquiry\n",
        "await test_a2a_communication(\n",
        "    \"Do you have the Sony WH-1000XM5 headphones? What's the price?\"\n",
        ")"
      ],
      "metadata": {
        "id": "ssynCwqjDKyc",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T19:20:29.947261Z",
          "iopub.execute_input": "2025-11-13T19:20:29.947568Z",
          "iopub.status.idle": "2025-11-13T19:20:31.499058Z",
          "shell.execute_reply.started": "2025-11-13T19:20:29.947537Z",
          "shell.execute_reply": "2025-11-13T19:20:31.497703Z"
        }
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🔍 Section 6: Understanding What Just Happened\n",
        "\n",
        "### A2A Communication Flow\n",
        "\n",
        "When you ran the tests above, here's the detailed step-by-step flow of how the agents communicated:\n",
        "\n",
        "![](https://storage.googleapis.com/github-repo/kaggle-5days-ai/day5/a2a_03.png)\n",
        "\n",
        "**A2A Protocol Communication:**\n",
        "\n",
        "Behind the scenes, here's what happens at the protocol level:\n",
        "- **RemoteA2aAgent** sends HTTP POST requests to the `/tasks` endpoint on `http://localhost:8001`\n",
        "- Request and response data follow the [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/)\n",
        "- Data is exchanged in standardized JSON format\n",
        "- The protocol ensures any A2A-compatible agent (regardless of language/framework) can communicate\n",
        "\n",
        "This standardization is what makes cross-organization, cross-language agent communication possible!\n",
        "\n",
        "---\n",
        "\n",
        "**What happened:**\n",
        "1. **Customer** asked about the iPhone 15 Pro\n",
        "2. **Customer Support Agent** (LlmAgent) received the question and decided it needs product information\n",
        "3. **Support Agent** delegated to the `product_catalog_agent` sub-agent\n",
        "4. **RemoteA2aAgent** (client-side proxy) translated this into an A2A protocol request\n",
        "5. The A2A request was sent over HTTP to `http://localhost:8001` (highlighted in yellow)\n",
        "6. **Product Catalog Agent** (server) received the request and called `get_product_info(\"iPhone 15 Pro\")`\n",
        "7. **Product Catalog Agent** returned the product information via A2A response\n",
        "8. **RemoteA2aAgent** received the response and passed it back to the Support Agent\n",
        "9. **Support Agent** formulated a final answer with the product details\n",
        "10. **Customer** received the complete, helpful response\n",
        "\n",
        "### Key Benefits Demonstrated\n",
        "\n",
        "1. **Transparency**: Support Agent doesn't \"know\" Product Catalog Agent is remote\n",
        "2. **Standard Protocol**: Uses A2A standard - any A2A-compatible agent works\n",
        "3. **Easy Integration**: Just one line: `sub_agents=[remote_product_catalog_agent]`\n",
        "4. **Separation of Concerns**: Product data lives in Catalog Agent (vendor), support logic in Support Agent (your company)\n",
        "\n",
        "### Real-World Applications\n",
        "\n",
        "This pattern enables:\n",
        "- **Microservices**: Each agent is an independent service\n",
        "- **Third-party Integration**: Consume agents from external vendors (e.g., product catalogs, payment processors)\n",
        "- **Cross-language**: Product Catalog Agent could be Java, Support Agent Python\n",
        "- **Specialized Teams**: Vendor maintains catalog, your team maintains support agent\n",
        "- **Cross-Organization**: Vendor hosts catalog on their infrastructure, you integrate via A2A"
      ],
      "metadata": {
        "id": "tt2REOwBg4wZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🎓 Next Steps and Learning Resources\n",
        "\n",
        "### 🚀 Enhancement Ideas\n",
        "\n",
        "Now that you understand A2A basics, try extending this example:\n",
        "\n",
        "1. **Add More Agents**:\n",
        "   - Create an **Inventory Agent** that checks stock levels and restocking schedules\n",
        "   - Create a **Shipping Agent** that provides delivery estimates and tracking\n",
        "   - Have Customer Support Agent coordinate all three via A2A\n",
        "\n",
        "2. **Real Data Sources**:\n",
        "   - Replace mock product catalog with real database (PostgreSQL, MongoDB)\n",
        "   - Add real inventory tracking system integration\n",
        "   - Connect to real payment gateway APIs\n",
        "\n",
        "3. **Advanced A2A Features**:\n",
        "   - Implement authentication between agents (API keys, OAuth)\n",
        "   - Add error handling and retries for network failures\n",
        "   - Use the alternative `adk api_server --a2a` approach\n",
        "\n",
        "4. **Deploy to Production**:\n",
        "   - Deploy Product Catalog Agent to Agent Engine\n",
        "   - Update agent card URL to point to production server (e.g., `https://vendor-catalog.example.com`)\n",
        "   - Consumer agents can now access it over the internet!\n",
        "\n",
        "### 📚 Documentation\n",
        "\n",
        "**A2A Protocol**:\n",
        "\n",
        "- [Official A2A Protocol Website](https://a2a-protocol.org/)\n",
        "- [A2A Protocol Specification](https://a2a-protocol.org/latest/spec/)\n",
        "\n",
        "**ADK A2A Guides**:\n",
        "\n",
        "- [Introduction to A2A in ADK](https://google.github.io/adk-docs/a2a/intro/)\n",
        "- [Exposing Agents Quickstart](https://google.github.io/adk-docs/a2a/quickstart-exposing/)\n",
        "- [Consuming Agents Quickstart](https://google.github.io/adk-docs/a2a/quickstart-consuming/)\n",
        "\n",
        "**Other Deployment Options**:\n",
        "\n",
        "- [Deploy ADK Agents to Cloud Run](https://google.github.io/adk-docs/deploy/cloud-run/)\n",
        "- [Deploy to Agent Engine](https://google.github.io/adk-docs/deploy/agent-engine/)\n",
        "- [Deploy to GKE](https://google.github.io/adk-docs/deploy/gke/)"
      ],
      "metadata": {
        "id": "Gjs0ZY1YDKyc"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 📊 Summary - A2A Communication Patterns\n",
        "\n",
        "### Key Takeaways\n",
        "\n",
        "In this notebook, you learned how to build multi-agent systems with A2A:\n",
        "\n",
        "- **A2A Protocol**: Standardized protocol for agent-to-agent communication across networks and frameworks\n",
        "- **Exposing Agents**: Use `to_a2a()` to make your agents accessible to others with auto-generated agent cards\n",
        "- **Consuming Agents**: Use `RemoteA2aAgent` to integrate remote agents as if they were local sub-agents\n",
        "- **Use Cases**: Best for microservices architectures, cross-team integrations, and third-party agent consumption"
      ],
      "metadata": {
        "id": "WWQ-dyMyg4wZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## ✅ Congratulations! You're an A2A Expert\n",
        "\n",
        "You've successfully learned how to build multi-agent systems using the A2A protocol!\n",
        "\n",
        "You now know how to expose agents as services, consume remote agents, and build collaborative multi-agent systems that can scale across teams and organizations.\n",
        "\n",
        "**ℹ️ Note: No submission required!**\n",
        "\n",
        "This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "### 📚 Learn More\n",
        "\n",
        "Refer to the following documentation to learn more:\n",
        "\n",
        "- [ADK Documentation](https://google.github.io/adk-docs/)\n",
        "- [A2A Protocol Official Website](https://a2a-protocol.org/)\n",
        "- [A2A Tutorials](https://a2a-protocol.org/latest/tutorials/)\n",
        "- [Introduction to A2A in ADK](https://google.github.io/adk-docs/a2a/intro/)\n",
        "- [Exposing Agents Quickstart](https://google.github.io/adk-docs/a2a/quickstart-exposing/)\n",
        "- [Consuming Agents Quickstart](https://google.github.io/adk-docs/a2a/quickstart-consuming/)\n",
        "\n",
        "### 🎯 Next Steps\n",
        "\n",
        "Now that you understand A2A communication, you can build complex multi-agent systems where specialized agents collaborate to solve real-world problems. Consider deploying your agents to production using Cloud Run or Agent Engine to make them accessible over the internet!\n",
        "\n",
        "Ready for more? Explore advanced ADK features like custom agents, streaming, and production deployment patterns!"
      ],
      "metadata": {
        "id": "4W174mzCg4wa"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "| Authors |\n",
        "| --- |\n",
        "| [Lavi Nigam](https://www.linkedin.com/in/lavinigam/) |"
      ],
      "metadata": {
        "id": "SQCPNPteg4wa"
      }
    }
  ]
}

---



# Log: Day_5b_Agent_Deployment.txt

{
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.13",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [],
      "isInternetEnabled": true,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    },
    "colab": {
      "name": "Day 5b - Agent Deployment",
      "provenance": []
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Copyright 2025 Google LLC."
      ],
      "metadata": {
        "id": "8seCLBkPiC1I"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:33:46.135726Z",
          "iopub.execute_input": "2025-11-13T21:33:46.136045Z",
          "iopub.status.idle": "2025-11-13T21:33:46.143045Z",
          "shell.execute_reply.started": "2025-11-13T21:33:46.136013Z",
          "shell.execute_reply": "2025-11-13T21:33:46.141924Z"
        },
        "id": "Pki1GMv2iC1J"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 🚀 Deploy ADK Agent to Vertex AI Agent Engine\n",
        "\n",
        "**Welcome to the final day of the Kaggle 5-day Agents course!**\n",
        "\n",
        "In the previous notebook you learned how to use Agent2Agent Protocol to make your agents interoperable.\n",
        "\n",
        "Now, let's take the final step: deploying your agents to production using [Vertex AI Agent Engine](https://docs.cloud.google.com/agent-builder/agent-engine/overview).\n",
        "\n",
        "## 💡 Scaling Your Agent\n",
        "\n",
        "You've built an amazing AI agent. It works perfectly on your machine. You can chat with it, it responds intelligently, and everything seems ready. But there's a problem.\n",
        "\n",
        "> **Your agent is not publicly available!**\n",
        "\n",
        "It only lives in your notebook and development environment. When you stop your notebook session, it stops working. Your teammates can't access it. Your users can't interact with it. And this is precisely why we need to deploy the agents!"
      ],
      "metadata": {
        "id": "joEibZg3iC1J"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 🎯 What You'll Learn\n",
        "\n",
        "In this notebook, you'll:\n",
        "\n",
        "- ✅ Build a production-ready ADK agent\n",
        "- ✅ Deploy your agent to [**Vertex AI Agent Engine**](https://docs.cloud.google.com/agent-builder/agent-engine/overview) using the ADK CLI\n",
        "- ✅ Test your deployed agent with Python SDK\n",
        "- ✅ Monitor and manage deployed agents in Google Cloud Console\n",
        "- ✅ Understand how to add Memory to your Agent using Vertex AI Memory Bank\n",
        "- ✅ Understand cost management and cleanup best practices"
      ],
      "metadata": {
        "id": "0mYMtiRDiC1K"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ‼️ Please Read\n",
        "\n",
        "> ❌ **ℹ️ Note: No submission required!**\n",
        "> This notebook is for your hands-on practice and learning only. You **do not** need to submit it anywhere to complete the course.\n",
        "\n",
        "> ⏸️ **Note:**  When you first start the notebook via running a cell you might see a banner in the notebook header that reads **\"Waiting for the next available notebook\"**. The queue should drop rapidly; however, during peak bursts you might have to wait a few minutes.\n",
        "\n",
        "> ❌ **Note:** Avoid using the **Run all** cells command as this can trigger a QPM limit resulting in 429 errors when calling the backing model. Suggested flow is to run each cell in order - one at a time. [See FAQ on 429 errors for more information.](https://www.kaggle.com/code/kaggle5daysofai/day-0-troubleshooting-and-faqs)\n",
        "\n",
        "**For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server.**"
      ],
      "metadata": {
        "id": "SVlTwk9iiC1K"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 📖 Get started with Kaggle Notebooks\n",
        "\n",
        "If this is your first time using Kaggle Notebooks, welcome! You can learn more about using Kaggle Notebooks [in the documentation](https://www.kaggle.com/docs/notebooks).\n",
        "\n",
        "Here's how to get started:\n",
        "\n",
        "**1. Verify Your Account (Required)**\n",
        "\n",
        "To use the Kaggle Notebooks in this course, you'll need to verify your account with a phone number.\n",
        "\n",
        "You can do this in your [Kaggle settings](https://www.kaggle.com/settings).\n",
        "\n",
        "**2. Make Your Own Copy**\n",
        "\n",
        "To run any code in this notebook, you first need your own editable copy.\n",
        "\n",
        "Click the `Copy and Edit` button in the top-right corner.\n",
        "\n",
        "![Copy and Edit button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_1.png)\n",
        "\n",
        "This creates a private copy of the notebook just for you.\n",
        "\n",
        "**3. Run Code Cells**\n",
        "\n",
        "Once you have your copy, you can run code.\n",
        "\n",
        "Click the ▶️ Run button next to any code cell to execute it.\n",
        "\n",
        "![Run cell button](https://storage.googleapis.com/kaggle-media/Images/5gdai_sc_2.png)\n",
        "\n",
        "Run the cells in order from top to bottom.\n",
        "\n",
        "**4. If You Get Stuck**\n",
        "\n",
        "To restart: Select `Factory reset` from the `Run` menu.\n",
        "\n",
        "For help: Ask questions on the [Kaggle Discord](https://discord.com/invite/kaggle) server."
      ],
      "metadata": {
        "id": "KS9OP-w8iC1L"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ⚙️ Section 1: Setup\n"
      ],
      "metadata": {
        "id": "3zLdEBePiC1M"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.1: ⚠️ **Important: Prerequisites**\n",
        "\n",
        "This notebook requires a **Google Cloud account** to deploy agents to Vertex AI Agent Engine.\n",
        "\n",
        "**If you don't have a GCP account yet:**\n",
        "\n",
        " ✅ Step 1. **Create a free Google Cloud account** - [Sign up here](https://cloud.google.com/free)\n",
        "- New users get **$300 in free credits** valid for 90 days on Google Cloud\n",
        "- No charges during the free trial period\n",
        "\n",
        " ✅ Step 2. **Enable billing on your account** - Required even for free trial\n",
        "- A credit card is needed for verification\n",
        "- You won't be charged unless you explicitly upgrade\n",
        "- This demo stays within the free tier of Agent Engine if you clean up resources promptly\n",
        "\n",
        "\n",
        " ✅ Step 3. **Understand the free trial** - Know what's included\n",
        "- Check [free trial details of Google Cloud](https://cloud.google.com/free/docs/free-cloud-features#free-trial)\n",
        "- Review [common questions about the free trial for Google Cloud](https://cloud.google.com/signup-faqs?hl=en#google-cloud-free-trial-faqs)\n",
        "\n",
        "**💡 Quick Setup Guide:** Watch this [3-minute setup video](https://youtu.be/-nUAQq_evxc) for a walkthrough"
      ],
      "metadata": {
        "id": "ovlcyNX_iC1M"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.2: Import components\n",
        "\n",
        "Now, import the specific components you'll need for this notebook. This keeps your code organized and ensures we have access to the necessary building blocks."
      ],
      "metadata": {
        "id": "uc5Hi_XLiC1M"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import random\n",
        "import time\n",
        "import vertexai\n",
        "from kaggle_secrets import UserSecretsClient\n",
        "from vertexai import agent_engines\n",
        "\n",
        "print(\"✅ Imports completed successfully\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:33:46.145438Z",
          "iopub.execute_input": "2025-11-13T21:33:46.145732Z",
          "iopub.status.idle": "2025-11-13T21:34:30.80119Z",
          "shell.execute_reply.started": "2025-11-13T21:33:46.145709Z",
          "shell.execute_reply": "2025-11-13T21:34:30.799583Z"
        },
        "id": "h7JPJ-F3iC1M"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.3: Add Cloud Credentials to Secrets\n",
        "\n",
        "1. In the top menu bar of the notebook editor, select `Add-ons` then `Google Cloud SDK`.\n",
        "2. Click on `Link Account`\n",
        "3. Select your Google Cloud Account\n",
        "4. Attach to the notebook\n",
        "   \n",
        "This cell retrieves your Google Cloud credentials from Kaggle Secrets and configures them for use. These credentials allow the notebook to authenticate with Google Cloud services like Vertex AI Agent Engine."
      ],
      "metadata": {
        "id": "qUfH6MUbiC1O"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Set up Cloud Credentials in Kaggle\n",
        "user_secrets = UserSecretsClient()\n",
        "user_credential = user_secrets.get_gcloud_credential()\n",
        "user_secrets.set_tensorflow_credential(user_credential)\n",
        "\n",
        "print(\"✅ Cloud credentials configured\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:34:30.802351Z",
          "iopub.execute_input": "2025-11-13T21:34:30.803106Z",
          "iopub.status.idle": "2025-11-13T21:34:30.976716Z",
          "shell.execute_reply.started": "2025-11-13T21:34:30.803076Z",
          "shell.execute_reply": "2025-11-13T21:34:30.975649Z"
        },
        "id": "AbIVPV39iC1O"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.4: Set your PROJECT_ID\n",
        "\n",
        "**Important:** Make sure to replace `\"your-project-id\"` with your actual Google Cloud project ID. You can find your project ID in the [Google Cloud Console](https://console.cloud.google.com/)."
      ],
      "metadata": {
        "id": "F7cTa9cSiC1O"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Set your PROJECT_ID\n",
        "PROJECT_ID = \"your-project-id\"  # TODO: Replace with your project ID\n",
        "os.environ[\"GOOGLE_CLOUD_PROJECT\"] = PROJECT_ID\n",
        "\n",
        "if PROJECT_ID == \"your-project-id\" or not PROJECT_ID:\n",
        "    raise ValueError(\"⚠️ Please replace 'your-project-id' with your actual Google Cloud Project ID.\")\n",
        "\n",
        "print(f\"✅ Project ID set to: {PROJECT_ID}\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:39:02.29647Z",
          "iopub.execute_input": "2025-11-13T21:39:02.296792Z",
          "iopub.status.idle": "2025-11-13T21:39:02.302855Z",
          "shell.execute_reply.started": "2025-11-13T21:39:02.296772Z",
          "shell.execute_reply": "2025-11-13T21:39:02.301659Z"
        },
        "id": "WMMyW4kviC1O"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1.5: Enable Google Cloud APIs\n",
        "\n",
        "For this tutorial, you'll need to enable the following APIs in the Google Cloud Console.\n",
        "\n",
        "- Vertex AI API\n",
        "- Cloud Storage API\n",
        "- Cloud Logging API\n",
        "- Cloud Monitoring API\n",
        "- Cloud Trace API\n",
        "- Telemetry API\n",
        "\n",
        "You can [use this link to open the Google Cloud Console](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com,storage.googleapis.com,logging.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com,telemetry.googleapis.com) and follow the steps there to enable these APIs."
      ],
      "metadata": {
        "id": "4p1AZ5dJiC1P"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 🏗️ Section 2: Create Your Agent with ADK\n",
        "\n",
        "Before we deploy, we need a functional agent to host. We'll build a **Weather Assistant** designed to serve as our sample agent.\n",
        "\n",
        "This agent is optimized for production testing with the following configuration:\n",
        "\n",
        "- **Model:** Uses gemini-2.5-flash-lite for low latency and cost-efficiency.\n",
        "- **Tools:** Includes a `get_weather` function to demonstrate tool execution.\n",
        "- **Persona:** Responds conversationally to prove the instruction-following capabilities.\n",
        "\n",
        "This demonstrates the foundational ADK architecture we are about to package: **Agent + Tools + Instructions**.\n",
        "\n",
        "We'll create the following files and directory structure:\n",
        "\n",
        "```\n",
        "sample_agent/\n",
        "├── agent.py                  # The logic\n",
        "├── requirements.txt          # The libraries\n",
        "├── .env                      # The secrets/config\n",
        "└── .agent_engine_config.json # The hardware specs\n",
        "```"
      ],
      "metadata": {
        "id": "OKmX_UHViC1P"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.1: Create agent directory\n",
        "\n",
        "We need a clean workspace to package our agent for deployment. We will create a directory named `sample_agent`.\n",
        "\n",
        "All necessary files - including the agent code, dependencies, and configuration—will be written into this folder to prepare it for the `adk deploy` command."
      ],
      "metadata": {
        "id": "MfAXwNaHiC1P"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Create simple agent - all code for the agent will live in this directory\n",
        "!mkdir -p sample_agent\n",
        "\n",
        "print(f\"✅ Sample Agent directory created\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:34:30.985515Z",
          "iopub.execute_input": "2025-11-13T21:34:30.985771Z",
          "iopub.status.idle": "2025-11-13T21:34:31.1364Z",
          "shell.execute_reply.started": "2025-11-13T21:34:30.985723Z",
          "shell.execute_reply": "2025-11-13T21:34:31.135026Z"
        },
        "id": "Njh6dLQjiC1P"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.2: Create requirements file\n",
        "\n",
        "The Agent Engine builds a dedicated environment for your agent. To ensure it runs correctly, we must declare our dependencies.\n",
        "\n",
        "We will write a `requirements.txt` file containing the Python packages needed for the agent."
      ],
      "metadata": {
        "id": "vybeUigQiC1Q"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile sample_agent/requirements.txt\n",
        "\n",
        "google-adk\n",
        "opentelemetry-instrumentation-google-genai"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:34:31.139468Z",
          "iopub.execute_input": "2025-11-13T21:34:31.139797Z",
          "iopub.status.idle": "2025-11-13T21:34:31.147811Z",
          "shell.execute_reply.started": "2025-11-13T21:34:31.139765Z",
          "shell.execute_reply": "2025-11-13T21:34:31.146539Z"
        },
        "id": "JuAoEO2iiC1Q"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.3: Create environment configuration\n",
        "\n",
        "We need to provide the agent with the necessary cloud configuration settings.\n",
        "\n",
        "We will write a `.env` file that sets the cloud location to `global` and explicitly enables the Vertex AI backend for the ADK SDK."
      ],
      "metadata": {
        "id": "BRrHtzIYiC1Q"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile sample_agent/.env\n",
        "\n",
        "# https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#global-endpoint\n",
        "GOOGLE_CLOUD_LOCATION=\"global\"\n",
        "\n",
        "# Set to 1 to use Vertex AI, or 0 to use Google AI Studio\n",
        "GOOGLE_GENAI_USE_VERTEXAI=1"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:34:31.148584Z",
          "iopub.execute_input": "2025-11-13T21:34:31.148857Z",
          "iopub.status.idle": "2025-11-13T21:34:31.171757Z",
          "shell.execute_reply.started": "2025-11-13T21:34:31.148836Z",
          "shell.execute_reply": "2025-11-13T21:34:31.170056Z"
        },
        "id": "iGcwEPHBiC1Q"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Configuration explained:**\n",
        "\n",
        "- `GOOGLE_CLOUD_LOCATION=\"global\"` - Uses the `global` endpoint for Gemini API calls\n",
        "- `GOOGLE_GENAI_USE_VERTEXAI=1` - Configures ADK to use Vertex AI instead of Google AI Studio"
      ],
      "metadata": {
        "id": "FBXMIisZiC1Q"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2.4: Create agent code\n",
        "\n",
        "We will now generate the `agent.py` file. This script defines the behavior of our **Weather Assistant**.\n",
        "\n",
        "Agent Configuration:\n",
        "\n",
        "- 🧠 Model: Uses `gemini-2.5-flash-lite` for low latency and cost-efficiency.\n",
        "- 🛠️ Tools: Accesses a `get_weather` function to retrieve data.\n",
        "- 📝 Instructions: Follows a system prompt to identify cities and respond in a friendly tone."
      ],
      "metadata": {
        "id": "Y11QyrLkiC1Q"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile sample_agent/agent.py\n",
        "from google.adk.agents import Agent\n",
        "import vertexai\n",
        "import os\n",
        "\n",
        "vertexai.init(\n",
        "    project=os.environ[\"GOOGLE_CLOUD_PROJECT\"],\n",
        "    location=os.environ[\"GOOGLE_CLOUD_LOCATION\"],\n",
        ")\n",
        "\n",
        "def get_weather(city: str) -> dict:\n",
        "    \"\"\"\n",
        "    Returns weather information for a given city.\n",
        "\n",
        "    This is a TOOL that the agent can call when users ask about weather.\n",
        "    In production, this would call a real weather API (e.g., OpenWeatherMap).\n",
        "    For this demo, we use mock data.\n",
        "\n",
        "    Args:\n",
        "        city: Name of the city (e.g., \"Tokyo\", \"New York\")\n",
        "\n",
        "    Returns:\n",
        "        dict: Dictionary with status and weather report or error message\n",
        "    \"\"\"\n",
        "    # Mock weather database with structured responses\n",
        "    weather_data = {\n",
        "        \"san francisco\": {\"status\": \"success\", \"report\": \"The weather in San Francisco is sunny with a temperature of 72°F (22°C).\"},\n",
        "        \"new york\": {\"status\": \"success\", \"report\": \"The weather in New York is cloudy with a temperature of 65°F (18°C).\"},\n",
        "        \"london\": {\"status\": \"success\", \"report\": \"The weather in London is rainy with a temperature of 58°F (14°C).\"},\n",
        "        \"tokyo\": {\"status\": \"success\", \"report\": \"The weather in Tokyo is clear with a temperature of 70°F (21°C).\"},\n",
        "        \"paris\": {\"status\": \"success\", \"report\": \"The weather in Paris is partly cloudy with a temperature of 68°F (20°C).\"}\n",
        "    }\n",
        "\n",
        "    city_lower = city.lower()\n",
        "    if city_lower in weather_data:\n",
        "        return weather_data[city_lower]\n",
        "    else:\n",
        "        available_cities = \", \".join([c.title() for c in weather_data.keys()])\n",
        "        return {\n",
        "            \"status\": \"error\",\n",
        "            \"error_message\": f\"Weather information for '{city}' is not available. Try: {available_cities}\"\n",
        "        }\n",
        "\n",
        "root_agent = Agent(\n",
        "    name=\"weather_assistant\",\n",
        "    model=\"gemini-2.5-flash-lite\",  # Fast, cost-effective Gemini model\n",
        "    description=\"A helpful weather assistant that provides weather information for cities.\",\n",
        "    instruction=\"\"\"\n",
        "    You are a friendly weather assistant. When users ask about the weather:\n",
        "\n",
        "    1. Identify the city name from their question\n",
        "    2. Use the get_weather tool to fetch current weather information\n",
        "    3. Respond in a friendly, conversational tone\n",
        "    4. If the city isn't available, suggest one of the available cities\n",
        "\n",
        "    Be helpful and concise in your responses.\n",
        "    \"\"\",\n",
        "    tools=[get_weather]\n",
        ")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:34:31.172879Z",
          "iopub.execute_input": "2025-11-13T21:34:31.173227Z",
          "iopub.status.idle": "2025-11-13T21:34:31.193238Z",
          "shell.execute_reply.started": "2025-11-13T21:34:31.173194Z",
          "shell.execute_reply": "2025-11-13T21:34:31.191853Z"
        },
        "id": "hvU8RKEoiC1Q"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## ☁️ Section 3: Deploy to Agent Engine\n",
        "\n",
        "ADK supports multiple deployment platforms. Learn more in the [ADK deployment documentation](https://google.github.io/adk-docs/deploy/).\n",
        "\n",
        "You'll be deploying to [Vertex AI Agent Engine](https://docs.cloud.google.com/agent-builder/agent-engine/overview) in this notebook.\n",
        "\n",
        "### 🔷 Vertex AI Agent Engine\n",
        "\n",
        "- **Fully managed** service specifically for AI agents\n",
        "- **Auto-scaling** with session management built-in\n",
        "- **Easy deployment** using [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)\n",
        "- 📚 [Deploy to Agent Engine Guide](https://google.github.io/adk-docs/deploy/agent-engine/)\n",
        "\n",
        "**Note**: To help you get started with the runtime, Agent Engine offers a monthly free tier, which you can learn more about in the [documentation](https://docs.cloud.google.com/agent-builder/agent-engine/overview#pricing). The agent deployed in this notebook should stay within the free tier if cleaned up promptly. Note that you can incur costs if the agent is left running.\n",
        "\n",
        "### 🚢 Other Deployment Options\n",
        "\n",
        "### 🔷 Cloud Run\n",
        "\n",
        "- Serverless, easiest to start\n",
        "- Perfect for demos and small-to-medium workloads\n",
        "- 📚 [Deploy to Cloud Run Guide](https://google.github.io/adk-docs/deploy/cloud-run/)\n",
        "\n",
        "### 🔷 Google Kubernetes Engine (GKE)\n",
        "\n",
        "- Full control over containerized deployments\n",
        "- Best for complex multi-agent systems\n",
        "- 📚 [Deploy to GKE Guide](https://google.github.io/adk-docs/deploy/gke/)"
      ],
      "metadata": {
        "id": "LKYRkcBDiC1R"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.1: Create deployment configuration\n",
        "\n",
        "The `.agent_engine_config.json` file controls the deployment settings."
      ],
      "metadata": {
        "id": "DTB1erPeiC1R"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile sample_agent/.agent_engine_config.json\n",
        "{\n",
        "    \"min_instances\": 0,\n",
        "    \"max_instances\": 1,\n",
        "    \"resource_limits\": {\"cpu\": \"1\", \"memory\": \"1Gi\"}\n",
        "}"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:34:31.194206Z",
          "iopub.execute_input": "2025-11-13T21:34:31.194529Z",
          "iopub.status.idle": "2025-11-13T21:34:31.218987Z",
          "shell.execute_reply.started": "2025-11-13T21:34:31.194504Z",
          "shell.execute_reply": "2025-11-13T21:34:31.21765Z"
        },
        "id": "YwnnuIDViC1R"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Configuration explained:**\n",
        "\n",
        "- `\"min_instances\": 0` - Scales down to zero when not in use (saves costs)\n",
        "- `\"max_instances\": 1` - Maximum of 1 instance running (sufficient for this demo)\n",
        "- `\"cpu\": \"1\"` - 1 CPU core per instance\n",
        "- `\"memory\": \"1Gi\"` - 1 GB of memory per instance\n",
        "\n",
        "These settings keep costs minimal while providing adequate resources for our weather agent."
      ],
      "metadata": {
        "id": "LB-v11OyiC1R"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.2: Select deployment region\n",
        "\n",
        "Agent Engine is available in specific regions. We'll randomly select one for this demo."
      ],
      "metadata": {
        "id": "RiH0djNJiC1R"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "regions_list = [\"europe-west1\", \"europe-west4\", \"us-east4\", \"us-west1\"]\n",
        "deployed_region = random.choice(regions_list)\n",
        "\n",
        "print(f\"✅ Selected deployment region: {deployed_region}\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:34:31.220181Z",
          "iopub.execute_input": "2025-11-13T21:34:31.220521Z",
          "iopub.status.idle": "2025-11-13T21:34:31.243332Z",
          "shell.execute_reply.started": "2025-11-13T21:34:31.220468Z",
          "shell.execute_reply": "2025-11-13T21:34:31.242014Z"
        },
        "id": "C8wfBpN-iC1R"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**About regions:**\n",
        "\n",
        "Agent Engine is available in multiple regions. For production:\n",
        "\n",
        "- Choose a region close to your users for lower latency\n",
        "- Consider data residency requirements\n",
        "- Check the [Agent Engine locations documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview#locations)"
      ],
      "metadata": {
        "id": "wdAFJlChiC1S"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3.3: Deploy the agent\n",
        "\n",
        "This uses the ADK CLI to deploy your agent to Agent Engine."
      ],
      "metadata": {
        "id": "ryoSZNlKiC1S"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!adk deploy agent_engine --project=$PROJECT_ID --region=$deployed_region sample_agent --agent_engine_config_file=sample_agent/.agent_engine_config.json"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:34:31.244157Z",
          "iopub.execute_input": "2025-11-13T21:34:31.244395Z",
          "iopub.status.idle": "2025-11-13T21:37:36.468795Z",
          "shell.execute_reply.started": "2025-11-13T21:34:31.244377Z",
          "shell.execute_reply": "2025-11-13T21:37:36.467104Z"
        },
        "id": "1fR6kUQ1iC1S"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**What just happened:**\n",
        "\n",
        "The `adk deploy agent_engine` command:\n",
        "\n",
        "1. Packages your agent code (`sample_agent/` directory)\n",
        "2. Uploads it to Agent Engine\n",
        "3. Creates a containerized deployment\n",
        "4. Outputs a resource name like: `projects/PROJECT_NUMBER/locations/REGION/reasoningEngines/ID`\n",
        "\n",
        "**Note:** Deployment typically takes 2-5 minutes."
      ],
      "metadata": {
        "id": "0LUPcYU8iC1S"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 🤖 Section 4: Retrieve and Test Your Deployed Agent"
      ],
      "metadata": {
        "id": "cVdlITBQiC1S"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.1: Retrieve the deployed agent\n",
        "\n",
        "After deploying with the CLI, we need to retrieve the agent object to interact with it."
      ],
      "metadata": {
        "id": "9MiVNozXiC1S"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Initialize Vertex AI\n",
        "vertexai.init(project=PROJECT_ID, location=deployed_region)\n",
        "\n",
        "# Get the most recently deployed agent\n",
        "agents_list = list(agent_engines.list())\n",
        "if agents_list:\n",
        "    remote_agent = agents_list[0]  # Get the first (most recent) agent\n",
        "    client = agent_engines\n",
        "    print(f\"✅ Connected to deployed agent: {remote_agent.resource_name}\")\n",
        "else:\n",
        "    print(\"❌ No agents found. Please deploy first.\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:37:36.470508Z",
          "iopub.execute_input": "2025-11-13T21:37:36.470852Z",
          "iopub.status.idle": "2025-11-13T21:37:37.045605Z",
          "shell.execute_reply.started": "2025-11-13T21:37:36.470816Z",
          "shell.execute_reply": "2025-11-13T21:37:37.044477Z"
        },
        "id": "R_IJKWXKiC1T"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**What happened:**\n",
        "\n",
        "This cell retrieves your deployed agent:\n",
        "\n",
        "1. Initializes the Vertex AI SDK with your project and region\n",
        "2. Lists all deployed agents in that region\n",
        "3. Gets the first one (most recently deployed)\n",
        "4. Stores it as `remote_agent` for testing"
      ],
      "metadata": {
        "id": "WK0OLzfWiC1T"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4.2: Test the deployed agent\n",
        "\n",
        "Now let's send a query to your deployed agent!"
      ],
      "metadata": {
        "id": "_8QiAC1ZiC1T"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "async for item in remote_agent.async_stream_query(\n",
        "    message=\"What is the weather in Tokyo?\",\n",
        "    user_id=\"user_42\",\n",
        "):\n",
        "    print(item)"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:37:37.046943Z",
          "iopub.execute_input": "2025-11-13T21:37:37.047231Z",
          "iopub.status.idle": "2025-11-13T21:37:41.472923Z",
          "shell.execute_reply.started": "2025-11-13T21:37:37.047202Z",
          "shell.execute_reply": "2025-11-13T21:37:41.472044Z"
        },
        "id": "MD9uKejyiC1T"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**What happened:**\n",
        "\n",
        "This cell tests your deployed agent:\n",
        "\n",
        "1. Sends the query \"What is the weather in Tokyo?\"\n",
        "2. Streams the response from the agent\n",
        "\n",
        "**Understanding the output:**\n",
        "\n",
        "You'll see multiple items printed:\n",
        "\n",
        "1. **Function call** - Agent decides to call `get_weather` tool\n",
        "2. **Function response** - Result from the tool (weather data)\n",
        "3. **Final response** - Agent's natural language answer"
      ],
      "metadata": {
        "id": "7ec7UhN5iC1T"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 🧠 Section 5: Long-Term Memory with Vertex AI Memory Bank\n",
        "\n",
        "### What Problem Does Memory Bank Solve?\n",
        "\n",
        "Your deployed agent has **session memory** - it remembers the conversation while you're chatting. But once the session ends, it forgets everything. Each new conversation starts from scratch.\n",
        "\n",
        "**The problem:**\n",
        "\n",
        "- User tells agent \"I prefer Celsius\" today\n",
        "- Tomorrow, user asks about weather → Agent gives Fahrenheit (forgot preference)\n",
        "- User has to repeat preferences every time\n",
        "\n",
        "### 💡 What is Vertex AI Memory Bank?\n",
        "\n",
        "Memory Bank gives your agent **long-term memory across sessions**:\n",
        "\n",
        "| Session Memory | Memory Bank |\n",
        "|---------------|-------------|\n",
        "| Single conversation | All conversations |\n",
        "| Forgets when session ends | Remembers permanently |\n",
        "| \"What did I just say?\" | \"What's my favorite city?\" |\n",
        "\n",
        "**How it works:**\n",
        "\n",
        "1. **During conversations** - Agent uses memory tools to search past facts\n",
        "2. **After conversations** - Agent Engine extracts key information (\"User prefers Celsius\")\n",
        "3. **Next session** - Agent automatically recalls and uses that information\n",
        "\n",
        "**Example:**\n",
        "\n",
        "- **Session 1:** User: \"I prefer Celsius\"\n",
        "- **Session 2 (days later):** User: \"Weather in Tokyo?\" → Agent responds in Celsius automatically ✨\n",
        "\n",
        "### 🔧 Memory Bank & Your Deployment\n",
        "\n",
        "Your Agent Engine deployment **provides the infrastructure** for Memory Bank, but it's not enabled by default.\n",
        "\n",
        "**To use Memory Bank:**\n",
        "\n",
        "1. Add memory tools to your agent code (`PreloadMemoryTool`)\n",
        "2. Add a callback to save conversations to Memory Bank\n",
        "3. Redeploy your agent\n",
        "\n",
        "Once configured, Memory Bank works automatically - no additional infrastructure needed!\n",
        "\n",
        "### 📚 Learn More\n",
        "\n",
        "- **[ADK Memory Guide](https://google.github.io/adk-docs/sessions/memory/)** - Complete guide with code examples\n",
        "- **[Memory Tools](https://google.github.io/adk-docs/tools/built-in-tools/)** - PreloadMemory and LoadMemory documentation\n",
        "- **[Get started with Memory Bank on ADK](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/memory_bank/get_started_with_memory_bank_on_adk.ipynb)** - Sample notebook that demonstrates how to build ADK agents with memory"
      ],
      "metadata": {
        "id": "FHQ7Giw2iC1U"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## 🧹 Section 6: Cleanup\n",
        "\n",
        "**⚠️ IMPORTANT: Prevent unexpected charges: Always delete resources when done testing!**\n",
        "\n",
        "**Cost Reminders**\n",
        "\n",
        "As a reminder, leaving the agent running can incur costs. Agent Engine offers a monthly free tier, which you can learn more about in the [documentation](https://docs.cloud.google.com/agent-builder/agent-engine/overview#pricing).\n",
        "\n",
        "**Always delete resources when done testing!**\n",
        "\n",
        "When you're done testing and querying your deployed agent, it's recommended to delete your remote agent to avoid incurring additional costs:"
      ],
      "metadata": {
        "id": "1Ul22EqLiC1U"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "agent_engines.delete(resource_name=remote_agent.resource_name, force=True)\n",
        "\n",
        "print(\"✅ Agent successfully deleted\")"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2025-11-13T21:37:41.474198Z",
          "iopub.execute_input": "2025-11-13T21:37:41.474513Z",
          "iopub.status.idle": "2025-11-13T21:37:41.634969Z",
          "shell.execute_reply.started": "2025-11-13T21:37:41.474491Z",
          "shell.execute_reply": "2025-11-13T21:37:41.634056Z"
        },
        "id": "mZp1wGUniC1U"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": [
        "**What happened:**\n",
        "\n",
        "This cell deletes your deployed agent:\n",
        "\n",
        "- `resource_name=remote_agent.resource_name` - Identifies which agent to delete\n",
        "- `force=True` - Forces deletion even if the agent is running\n",
        "\n",
        "The deletion process typically takes 1-2 minutes. You can verify deletion in the [Agent Engine Console](https://console.cloud.google.com/vertex-ai/agents/agent-engines)."
      ],
      "metadata": {
        "id": "J-EC2ypSiC1V"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "## ✅ Congratulations! You're Ready for Production Deployment\n",
        "\n",
        "You've successfully learned how to deploy ADK agents to Vertex AI Agent Engine - taking your agents from development to production!\n",
        "\n",
        "You now know how to deploy agents with enterprise-grade infrastructure, manage costs, and test production deployments.\n",
        "\n",
        "### 📚 Learn More\n",
        "\n",
        "Refer to the following documentation to learn more:\n",
        "\n",
        "- [ADK Documentation](https://google.github.io/adk-docs/)\n",
        "- [Agent Engine Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)\n",
        "- [ADK Deployment Guide](https://google.github.io/adk-docs/deploy/agent-engine/)\n",
        "\n",
        "**Other Deployment Options:**\n",
        "\n",
        "- [Cloud Run Deployment](https://google.github.io/adk-docs/deploy/cloud-run/)\n",
        "- [GKE Deployment](https://google.github.io/adk-docs/deploy/gke/)\n",
        "\n",
        "**Production Best Practices:**\n",
        "\n",
        "- Delete test deployments when finished to avoid costs\n",
        "- Enable tracing (`enable_tracing=True`) for debugging\n",
        "- Monitor via [Vertex AI Console](https://console.cloud.google.com/vertex-ai/agents/agent-engines)\n",
        "- Follow [security best practices](https://google.github.io/adk-docs/safety/)\n",
        "\n",
        "## 🎯 Course Recap: Your 5-Day Journey\n",
        "\n",
        "Over the past 5 days, you've learned:\n",
        "\n",
        "- **Day 1:** Agent fundamentals - Building your first agent with tools and instructions\n",
        "- **Day 2:** Advanced tools - Custom tools, built-in tools, and best practices\n",
        "- **Day 3:** Sessions & Memory - Managing conversations and long-term knowledge storage\n",
        "- **Day 4:** Observability & Evaluation - Monitoring agents and measuring performance\n",
        "- **Day 5:** Production Deployment - Taking your agents live with Agent Engine\n",
        "\n",
        "You now have the complete toolkit to build, test, and deploy production-ready AI agents!\n",
        "\n",
        "### 🚀 What's Next?\n",
        "\n",
        "**Thank you for completing the 5-day AI Agents course!**\n",
        "\n",
        "Now it's your turn to build:\n",
        "- Start creating your own AI agents with ADK\n",
        "- Share your projects with the community on [Kaggle Discord](https://discord.com/invite/kaggle)\n",
        "- Explore advanced patterns in the [ADK documentation](https://google.github.io/adk-docs/)\n",
        "\n",
        "**Happy building! 🚀**"
      ],
      "metadata": {
        "id": "izb4vdaHiC1V"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "| Authors |\n",
        "| --- |\n",
        "| [Lavi Nigam](https://www.linkedin.com/in/lavinigam/) |"
      ],
      "metadata": {
        "id": "a-7UBHnJiC1V"
      }
    }
  ]
}

---

