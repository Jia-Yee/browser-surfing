import asyncio
import os
import sys

from langchain_ollama import ChatOllama

sys.path.append("../../")

from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig

llm = ChatOllama(base_url=os.environ.get("OLLAMA_API_BASE", "http://192.168.1.4:11434"), model='qwen2.5')
browser = Browser(
	config=BrowserConfig(
		headless=False,
		disable_security=False,
		keep_alive=True,
		new_context_config=BrowserContextConfig(
			keep_alive=True,
			disable_security=False,
		),
	)
)


async def main():
	agent = Agent(
		task="""
            Go to https://bot-detector.rebrowser.net/ and verify that all the bot checks are passed.
        """,
		llm=llm,
		browser=browser,
	)
	await agent.run()
	input('Press Enter to continue to the next test...')

	agent = Agent(
		task="""
            Go to https://www.webflow.com/ and verify that the page is not blocked by a bot check.
        """,
		llm=llm,
		browser=browser,
	)
	await agent.run()
	input('Press Enter to continue to the next test...')

	agent = Agent(
		task="""
            Go to https://www.okta.com/ and verify that the page is not blocked by a bot check.
        """,
		llm=llm,
		browser=browser,
	)
	await agent.run()

	agent = Agent(
		task="""
            Go to https://abrahamjuliot.github.io/creepjs/ and verify that the detection score is >50%.
        """,
		llm=llm,
		browser=browser,
	)
	await agent.run()

	input('Press Enter to close the browser...')

	agent = Agent(
		task="""
            Go to https://nowsecure.nl/ check the "I'm not a robot" checkbox.
        """,
		llm=llm,
		browser=browser,
	)
	await agent.run()

	input('Press Enter to close the browser...')


if __name__ == '__main__':
	asyncio.run(main())
