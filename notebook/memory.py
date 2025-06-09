# %%
import os
import sys

sys.path.insert(0, os.path.abspath('../'))
from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from browser_use.agent.memory import Memory, MemorySettings

# %%


# %%
os.environ['HF_ENDPOINT']='https://hf-mirror.com'

# %%
from langchain_ollama import ChatOllama
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import (
	BaseMessage,
	HumanMessage,
)
from mem0 import Memory as Mem0Memory
from pydantic import BaseModel

from browser_use.agent.message_manager.service import MessageManager
from browser_use.agent.message_manager.views import ManagedMessage, MessageMetadata


llm = ChatOllama(base_url=os.environ.get("OLLAMA_API_BASE", "http://192.168.1.4:11434"), model='qwen2.5')


# %%
'''
# Default configuration values as class constants
DEFAULT_VECTOR_STORE = {'provider': 'faiss', 'config': {'embedding_model_dims': 384}}
DEFAULT_EMBEDDER = {'provider': 'huggingface', 'config': {'model': 'all-MiniLM-L6-v2'}}

@staticmethod
def _get_default_config(llm: BaseChatModel) -> dict:
    """Returns the default configuration for memory."""
    return {
        'vector_store': Memory.DEFAULT_VECTOR_STORE,
        'llm': {'provider': 'langchain', 'config': {'model': llm}},
        'embedder': Memory.DEFAULT_EMBEDDER,
    }
'''

_memory_config = Memory._get_default_config(llm)
print(_memory_config)
mem0 = Mem0Memory.from_config(config_dict=_memory_config)
all_memory = mem0.get_all()

print(f"All memories: {all_memory.keys()}")
print(f"Number of memories: {len(all_memory.get('results', []))}")
relevant_memories = mem0.search(query="hello", user_id='default_user', limit=3)

print(f"Relevant memories: {relevant_memories}")





