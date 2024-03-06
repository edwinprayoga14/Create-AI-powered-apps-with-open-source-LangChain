# Menggunakan Hugging FaceHub
import os
from langchain_community.llms import HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "..."
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")
text = "Tell me a fun fact about potato!"
result = llm.invoke(text)
print(result)