<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./static/browser-surfing.jpg">
  <source media="(prefers-color-scheme: light)" srcset="./static/browser-surfing.jpg">
  <img alt="Shows a black Browser Use Logo in light color mode and a white one in dark color mode." src="./static/browser-surfing.jpg"  width="full">
</picture>

<h1 align="center">Browser Surfing 🤖</h1>


🌐 Browser is surfing the internet.

# Quick start

With pip (Python>=3.11):

```bash
pip install browser-surfing
```

Install Playwright:
```bash
playwright install chromium
```

Spin up your agent:

```python
from langchain_openai import ChatOpenAI
from browser_surfing import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())
```

Add your API keys for the provider you want to use to your `.env` file.

```bash
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
AZURE_ENDPOINT=
AZURE_OPENAI_API_KEY=
GEMINI_API_KEY=
DEEPSEEK_API_KEY=
GROK_API_KEY=
NOVITA_API_KEY=
```


##  Set up environment variables:
   ```bash
   cp .env-example .env
   ```
   Then edit the `.env` file to add your OpenAI and/or Anthropic API keys.

## Running the Service

1. Start the FastAPI server:
   ```bash
   python app.py
   ```

2. The server will start at http://localhost:8000 by default.

3. You can access the API documentation at http://localhost:8000/docs

## API Endpoints

| Method | Endpoint                      | Description                  |
|--------|-------------------------------|------------------------------|
| POST   | /api/v1/run-task              | Start a new browser task     |
| GET    | /api/v1/task/{task_id}        | Get task details             |
| GET    | /api/v1/task/{task_id}/status | Get task status              |
| PUT    | /api/v1/stop-task/{task_id}   | Stop a running task          |
| PUT    | /api/v1/pause-task/{task_id}  | Pause a running task         |
| PUT    | /api/v1/resume-task/{task_id} | Resume a paused task         |
| GET    | /api/v1/list-tasks            | List all tasks               |

## Usage Examples

### Starting a Task

```bash
curl -X POST http://localhost:8000/api/v1/run-task \
  -H "Content-Type: application/json" \
  -d '{"task": "Go to google.com and search for n8n automation", "ai_provider": "ollama","save_browser_data": false, "headful": true, "use_custom_chrome": false}'
```
### use custom chrome error now
### Checking Task Status

```bash
curl -X GET http://localhost:8000/api/v1/task/{task_id}/status
```

### Stopping a Task

```bash
curl -X PUT http://localhost:8000/api/v1/stop-task/{task_id}
```

## Configuration Options

You can configure the service by editing the `.env` file.  Available options are grouped below:

### API Configuration

- `PORT`: The port the service will run on (default: 8000).


### Test with UI
simply run the gradio example:

```
uv pip install gradio
```

```bash
python examples/ui/gradio_demo.py
```

# Vision

Tell your computer what to do, and it gets it done.

## Roadmap

### Agent

- [ ] Improve agent memory (summarize, compress, RAG, etc.)
- [ ] Enhance planning capabilities (load website specific context)
- [ ] Reduce token consumption (system prompt, DOM state)

### DOM Extraction

- [ ] Improve extraction for datepickers, dropdowns, special elements
- [ ] Improve state representation for UI elements

### Rerunning tasks

- [ ] LLM as fallback
- [ ] Make it easy to define workflow templates where LLM fills in the details
- [ ] Return playwright script from the agent

### Datasets

- [ ] Create datasets for complex tasks
- [ ] Benchmark various models against each other
- [ ] Fine-tuning models for specific tasks

### User Experience

- [ ] Human-in-the-loop execution
- [ ] Improve the generated GIF quality
- [ ] Create various demos for tutorial execution, job application, QA testing, social media, etc.

## Contributing

We love contributions! Feel free to open issues for bugs or feature requests. To contribute to the docs, check out the `/docs` folder.



## Thanks

Thanks for creating and sharing  [browser-use](https://github.com/browser-use)!‌ 🙌
Forked to explore and build on your work—appreciate the clean code and useful setup. Will credit you if I adapt/modify anything. Keep up the awesome work!

 </div>
