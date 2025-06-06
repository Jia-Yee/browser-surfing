import asyncio
import os
import sys

from langchain_ollama import ChatOllama

sys.path.append("../../")

os.environ["LANG"] = "en_US.UTF-8"
os.environ["LC_ALL"] = "en_US.UTF-8"

from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig

llm = ChatOllama(base_url=os.environ.get("OLLAMA_API_BASE", "http://192.168.1.4:11434"), model='qwen2.5')
browser = Browser(
	config=BrowserConfig(
		headless=False,
		disable_security=False,
		keep_alive=True,
		chromium_args=[
            "--lang=en-US",
            "--accept-lang=en-US",
            "--disable-features=Translate"
        ],
		new_context_config=BrowserContextConfig(
			keep_alive=True,
			disable_security=False,
			locale="en-US",  # Add this line if supported
			extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
		),
	)
)


async def main():
	agent = Agent(
		task="""
            Go to https://www.google.com and check the language in the page.
        """,
		llm=llm,
		browser=browser,
	)
	await agent.run()
	input('Press Enter to complete the test...')

if __name__ == '__main__':
	asyncio.run(main())
