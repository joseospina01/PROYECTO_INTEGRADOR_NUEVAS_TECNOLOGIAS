import streamlit as st
import webcolors 

st.title("Buscador de Colores")

rgb_value = st.text_input("Introduce el valor RGB (ejemplo: 255, 0, 0):")

if rgb_value:
    try:
        
        rgb_values = tuple(map(int, rgb_value.split(',')))

        
        color_name = webcolors.rgb_to_name(rgb_values)

       
        st.write(f"Nombre del color: {color_name}")
    except ValueError:
        st.error("Entrada no válida. Asegúrate de usar el formato correcto (ejemplo: 255, 0, 0).")


st.sidebar.markdown("Hecho por tu nombre")
