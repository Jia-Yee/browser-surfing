import asyncio
import json
from typing import List
import os
import sys
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

from pydantic import BaseModel
sys.path.append("../../")

load_dotenv()

from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig, Controller

llm = ChatOllama(base_url=os.environ.get("OLLAMA_API_BASE", "http://192.168.1.4:11434"), model='qwen2.5')


links = [
	'https://docs.mem0.ai/components/llms/models/litellm',
	'https://docs.mem0.ai/components/llms/models/mistral_AI',
	'https://docs.mem0.ai/components/llms/models/ollama',
	'https://docs.mem0.ai/components/llms/models/openai',
	'https://docs.mem0.ai/components/llms/models/together',
	'https://docs.mem0.ai/components/llms/models/xAI',
	'https://docs.mem0.ai/components/llms/overview',
	'https://docs.mem0.ai/components/vectordbs/config',
	'https://docs.mem0.ai/components/vectordbs/dbs/azure_ai_search',
	'https://docs.mem0.ai/components/vectordbs/dbs/chroma',
	'https://docs.mem0.ai/components/vectordbs/dbs/elasticsearch',
	'https://docs.mem0.ai/components/vectordbs/dbs/milvus',
	'https://docs.mem0.ai/components/vectordbs/dbs/opensearch',
	'https://docs.mem0.ai/components/vectordbs/dbs/pgvector',
	'https://docs.mem0.ai/components/vectordbs/dbs/pinecone',
	'https://docs.mem0.ai/components/vectordbs/dbs/qdrant',
	'https://docs.mem0.ai/components/vectordbs/dbs/redis',
	'https://docs.mem0.ai/components/vectordbs/dbs/supabase',
	'https://docs.mem0.ai/components/vectordbs/dbs/vertex_ai_vector_search',
	'https://docs.mem0.ai/components/vectordbs/dbs/weaviate',
	'https://docs.mem0.ai/components/vectordbs/overview',
	'https://docs.mem0.ai/contributing/development',
	'https://docs.mem0.ai/contributing/documentation',
	'https://docs.mem0.ai/core-concepts/memory-operations',
	'https://docs.mem0.ai/core-concepts/memory-types',
]


class Link(BaseModel):
	url: str
	title: str
	summary: str


class Links(BaseModel):
	links: List[Link]


initial_actions = [
	{'open_tab': {'url': 'https://docs.mem0.ai/'}},
]
controller = Controller(output_model=Links)
task_description = f"""
Visit all the links provided in {links} and summarize the content of the page with url and title. There are {len(links)} links to visit. Make sure to visit all the links. Return a json with the following format: [{{url: <url>, title: <title>, summary: <summary>}}].

Guidelines:
1. Strictly stay on the domain https://docs.mem0.ai
2. Do not visit any other websites.
3. Ignore the links that are hashed (#) or javascript (:), or mailto, or tel, or other protocols
4. Don't visit any other url other than the ones provided above.
5. Capture the unique urls which are not already visited.
6. If you visit any page that doesn't have host name docs.mem0.ai, then do not visit it and come back to the page with host name docs.mem0.ai.
"""


async def main(max_steps=500):
	config = BrowserConfig(headless=True)
	browser = Browser(config=config)

	agent = Agent(
		task=task_description,
		llm=llm,
		controller=controller,
		initial_actions=initial_actions,
		enable_memory=True,
		browser=browser,
	)
	history = await agent.run(max_steps=max_steps)
	result = history.final_result()
	parsed_result = []
	if result:
		parsed: Links = Links.model_validate_json(result)
		print(f'Total parsed links: {len(parsed.links)}')
		for link in parsed.links:
			parsed_result.append({'title': link.title, 'url': link.url, 'summary': link.summary})
	else:
		print('No result')

	with open('result.json', 'w+') as f:
		f.write(json.dumps(parsed_result, indent=4))


if __name__ == '__main__':
	asyncio.run(main())
