from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import sys
import os
import asyncio
sys.path.append("../../")

if sys.platform == "darwin":
	print("Setting event loop policy for macOS")
	asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

load_dotenv()

from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig

llm = ChatOllama(base_url=os.environ.get("OLLAMA_API_BASE", "http://192.168.1.4:11434"), model='qwen2.5')


initial_actions = [
	{'open_tab': {'url': 'https://www.google.com'}},
	{'open_tab': {'url': 'https://en.wikipedia.org/wiki/Randomness'}},
	{'scroll_down': {'amount': 1000}},
]



async def main():
	agent = Agent(
		task='What theories are displayed on the page?',
		initial_actions=initial_actions,
		llm=llm,
	)
	await agent.run(max_steps=10)


if __name__ == '__main__':
	asyncio.run(main())
