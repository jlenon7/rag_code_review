from collections.abc import Sequence
from langchain_community.document_loaders import PyPDFLoader 
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser 
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

def load_pdf_chunks(file_name: str):
  loader = PyPDFLoader(f"storage/{file_name}.pdf", extract_images=False)
  pages = loader.load_and_split()

  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000,
    chunk_overlap=20,
    length_function=len,
    add_start_index=True
  )

  return text_splitter.split_documents(pages)

def load_code_folder_chunks(path: str, glob: str, suffixes: Sequence[str], exclude: Sequence[str], language: Language):
  loader = GenericLoader.from_filesystem(
    f"storage/repositories/{path}",
    glob=glob,
    suffixes=suffixes,
    exclude=exclude,
    parser=LanguageParser(language=language, parser_threshold=500)
  )

  documents = loader.load()
  splitter = RecursiveCharacterTextSplitter.from_language(
    language=language,
    chunk_size=2000,
    chunk_overlap=200
  )

  return splitter.split_documents(documents)
