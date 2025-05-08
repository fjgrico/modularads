import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openai

# Configuración de acceso a la API de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Conectar con el documento
spreadsheet = client.open("modularads_creativo")

# Obtener o crear hojas
try:
    hoja_piezas = spreadsheet.worksheet("Piezas")
except:
    hoja_piezas = spreadsheet.add_worksheet(title="Piezas", rows="1000", cols="10")
    hoja_piezas.append_row(["Tipo", "Texto", "Tono", "Fecha", "ID generación"])

# Clasificador simple de tono
def clasificar_tono(texto):
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en marketing que clasifica el tono de un texto como emocional, profesional, enérgico o alegre."},
            {"role": "user", "content": f"¿Qué tono tiene este texto?

"{texto}"?
Solo responde con una palabra: emocional, profesional, enérgico o alegre."}
        ],
        temperature=0.2
    )
    tono = respuesta["choices"][0]["message"]["content"].strip().lower()
    return tono

# Exportar datos
def exportar_a_sheets(modulos):
    fecha = datetime.date.today().isoformat()
    id_gen = os.urandom(4).hex()

    for tipo in ["hooks", "cuerpos", "ctas"]:
        textos = modulos[tipo].split("\n")
        for texto in textos:
            if texto.strip():
                tono = clasificar_tono(texto)
                hoja_piezas.append_row([
                    tipo[:-1].capitalize(),  # Hook, Cuerpo, CTA
                    texto.strip(),
                    tono,
                    fecha,
                    id_gen
                ])