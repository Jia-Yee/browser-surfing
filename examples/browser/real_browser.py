import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

import dotenv
from langchain_ollama import ChatOllama

sys.path.append("../../")

from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig

llm = ChatOllama(base_url=os.environ.get("OLLAMA_API_BASE", "http://192.168.1.4:11434"), model='qwen2.5')

dotenv.load_dotenv()

browser = Browser(
	config=BrowserConfig(
		# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
		browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
		extra_browser_args=[
            "--user-data-dir=remote-debug-profile",
        ],
        headless=False,
	)
)


async def main():
	agent = Agent(
		task='In docs.google.com write my Papa a quick letter',
		llm=llm,
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())
