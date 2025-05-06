import openai

def generar_modulos(sector, objetivo, mercado, avatar):
    prompt_hooks = open("prompts/hooks.txt").read() + f"\nSector: {sector}, Objetivo: {objetivo}, Mercado: {mercado}, Avatar: {avatar}"
    prompt_cuerpos = open("prompts/cuerpos.txt").read() + f"\nSector: {sector}, Objetivo: {objetivo}, Mercado: {mercado}, Avatar: {avatar}"
    prompt_ctas = open("prompts/ctas.txt").read() + f"\nSector: {sector}, Objetivo: {objetivo}, Mercado: {mercado}, Avatar: {avatar}"

    def pedir(prompt):
        respuesta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return respuesta["choices"][0]["message"]["content"]

    return {
        "hooks": pedir(prompt_hooks),
        "cuerpos": pedir(prompt_cuerpos),
        "ctas": pedir(prompt_ctas)
    }