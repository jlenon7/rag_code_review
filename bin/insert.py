from src.vector import insert_chunks
from langchain_text_splitters import Language
from src.models import create_embedding_model
from src.langchain import load_code_folder_chunks 

insert_chunks(
  embedding=create_embedding_model(),
  chunks=load_code_folder_chunks(
    path="langchain/libs/core/langchain_core/",
    glob="**/*",
    suffixes=[".py"],
    exclude=["**/non-utf-8-encoding.py"],
    language=Language.PYTHON
  )
)
