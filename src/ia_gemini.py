from google import genai

cliente = genai.Client()


def perguntar_ia(pergunta):
    resposta = cliente.interactions.create(
        model="gemini-3.8-flash",
        input=pergunta
    )

    return resposta.output_text