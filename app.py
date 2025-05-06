import streamlit as st
from utils.generator import generar_modulos
from utils.zip_creator import crear_zip_entrega

st.set_page_config(page_title="ModularAds", layout="wide")

st.title("🧠 ModularAds – Generador de Anuncios con IA")

with st.form("form_datos"):
    sector = st.text_input("🔧 Sector o actividad del cliente")
    objetivo = st.text_input("🎯 Objetivo de la campaña")
    mercado = st.text_input("🌍 Tipo de mercado (B2B, local, etc.)")
    avatar = st.text_area("🧑‍🎤 Avatar o público objetivo")
    submit = st.form_submit_button("🚀 Generar contenido modular")

if submit:
    from utils.audio import generar_audios  # 🔄 Import moved inside the block

    with st.spinner("Generando Hooks, Cuerpos y CTAs..."):
        modulos = generar_modulos(sector, objetivo, mercado, avatar)
        st.success("✅ Generado con éxito")

        st.subheader("🧲 Hooks")
        st.write(modulos["hooks"])

        st.subheader("🧠 Cuerpos de texto")
        st.write(modulos["cuerpos"])

        st.subheader("📢 CTAs")
        st.write(modulos["ctas"])

    with st.spinner("🎧 Generando audios..."):
        generar_audios(modulos)

    with st.spinner("📦 Empaquetando ZIP final..."):
        zip_path = crear_zip_entrega(modulos)
        st.success("✅ Entregable generado")
        st.download_button("⬇ Descargar ZIP", open(zip_path, "rb"), file_name="entrega_modular.zip")
