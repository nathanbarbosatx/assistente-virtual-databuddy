from conhecimento import carregar_conhecimento
from prompt import montar_prompt
from ia_gemini import perguntar_ia

print("DataBuddy iniciado!")

conhecimento = carregar_conhecimento()

pergunta = input("Digite sua pergunta: ")

prompt_completo = montar_prompt(pergunta, conhecimento)

resposta = perguntar_ia(prompt_completo)

print("\n--- DataBuddy ---")
print(resposta)