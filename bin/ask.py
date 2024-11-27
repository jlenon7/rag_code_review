from src.vector import ask
from src.models import create_llm_model, create_embedding_model

llm = create_llm_model()
embedding = create_embedding_model()

result, context = ask(
  llm=llm, 
  embedding=embedding, 
  question="Você pode revisar e sugerir melhorias para o código de RunnableBinding?"
)

print(result["answer"])
