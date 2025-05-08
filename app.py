import streamlit as st
from utils.generator import generar_modulos
from utils.zip_creator import crear_zip_entrega
from exportar_a_sheets import exportar_a_sheets
import pandas as pd

st.set_page_config(page_title="ModularAds", layout="wide")

st.title("🧠 ModularAds – Generador de Anuncios con IA")

with st.form("form_datos"):
    sector = st.text_input("🔧 Sector o actividad del cliente")
    objetivo = st.text_input("🎯 Objetivo de la campaña")
    mercado = st.text_input("🌍 Tipo de mercado (B2B, local, etc.)")
    avatar = st.text_area("🧑‍🎤 Avatar o público objetivo")
    submit = st.form_submit_button("🚀 Generar contenido modular")

if submit:
    with st.spinner("Generando Hooks, Cuerpos y CTAs..."):
        modulos = generar_modulos(sector, objetivo, mercado, avatar)
        st.success("✅ Generado con éxito")

        st.subheader("🧲 Hooks")
        st.write(modulos["hooks"])

        st.subheader("🧠 Cuerpos de texto")
        st.write(modulos["cuerpos"])

        st.subheader("📢 CTAs")
        st.write(modulos["ctas"])

    # Comentar o eliminar la parte de generación de audios
    # with st.spinner("🎧 Generando audios..."):
    #     generar_audios(modulos)

    with st.spinner("📦 Empaquetando ZIP final..."):
        zip_path = crear_zip_entrega(modulos)
        st.success("✅ Entregable generado")
        st.download_button("⬇ Descargar ZIP", open(zip_path, "rb"), file_name="entregable_modular.zip")

    # Botón para exportar a Google Sheets
    if st.button("📤 Exportar a Google Sheets"):
        exportar_a_sheets(modulos)
        st.success("✅ Datos exportados con éxito a Google Sheets")

    # Botón para descargar archivo local (CSV o Excel)
    if st.button("💾 Descargar como archivo local"):
        # Convertir las piezas a DataFrame
        piezas_data = {
            "Tipo": ["Hook", "Cuerpo", "CTA"],
            "Texto": modulos["hooks"] + modulos["cuerpos"] + modulos["ctas"],
            "Tono": ["emocional"] * len(modulos["hooks"]) + ["profesional"] * len(modulos["cuerpos"]) + ["energético"] * len(modulos["ctas"]),
            "Fecha": ["2024-05-06"] * (len(modulos["hooks"]) + len(modulos["cuerpos"]) + len(modulos["ctas"])),
            "ID generación": [os.urandom(4).hex()] * (len(modulos["hooks"]) + len(modulos["cuerpos"]) + len(modulos["ctas"]))
        }
        df = pd.DataFrame(piezas_data)
        
        # Guardar como Excel
        file_path = "/mnt/data/piezas_generadas.xlsx"
        df.to_excel(file_path, index=False)

        st.download_button(
            label="Descargar archivo de Piezas (Excel)",
            data=open(file_path, "rb"),
            file_name="piezas_generadas.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
