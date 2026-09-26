from openai import OpenAI

cliente = OpenAI()


def perguntar_ia(prompt):
    resposta = cliente.responses.create(
        model="gpt-5.6",
        input=prompt
    )

    return resposta.output_text