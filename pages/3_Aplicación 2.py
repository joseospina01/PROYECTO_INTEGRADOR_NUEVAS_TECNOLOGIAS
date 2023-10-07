import streamlit as st
from googletrans import Translator

st.title("Traductor de Texto")

translator = Translator()

texto_a_traducir = st.text_area("Introduce el texto que deseas traducir", height=200)

idioma_destino = st.selectbox("Selecciona el idioma al que deseas traducir", ["Español", "Inglés", "Francés", "Alemán"])

if st.button("Traducir"):
    if texto_a_traducir:
        try:
           
            idioma_destino = idioma_destino.lower()
            idioma_destino = "es" if idioma_destino == "español" else idioma_destino
            idioma_destino = "en" if idioma_destino == "inglés" else idioma_destino
            idioma_destino = "fr" if idioma_destino == "francés" else idioma_destino
            idioma_destino = "de" if idioma_destino == "alemán" else idioma_destino

            traduccion = translator.translate(texto_a_traducir, dest=idioma_destino)
            st.write(f"Texto traducido ({idioma_destino}): {traduccion.text}")
        except Exception as e:
            st.error("Hubo un error al traducir el texto. Por favor, intenta de nuevo.")


st.sidebar.markdown("Hecho por tu nombre")

