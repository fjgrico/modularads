import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_modulos(sector, objetivo, mercado, avatar):
    def pedir(prompt):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en copywriting, persuasión y guiones de anuncios estilo Hormozi"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

    prompt_hooks = open("prompts/hooks.txt").read() + f"\n\nSector: {sector}\nObjetivo: {objetivo}\nMercado: {mercado}\nAvatar: {avatar}"
    prompt_cuerpos = open("prompts/cuerpos.txt").read() + f"\n\nSector: {sector}\nObjetivo: {objetivo}\nMercado: {mercado}\nAvatar: {avatar}"
    prompt_ctas = open("prompts/ctas.txt").read() + f"\n\nSector: {sector}\nObjetivo: {objetivo}\nMercado: {mercado}\nAvatar: {avatar}"

    return {
        "hooks": pedir(prompt_hooks),
        "cuerpos": pedir(prompt_cuerpos),
        "ctas": pedir(prompt_ctas)
    }
