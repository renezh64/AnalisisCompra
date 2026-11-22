import streamlit as st


st.set_page_config(
    page_title="Comparador de Audífonos",
    layout="wide"
)


st.title("Comparador de Audífonos")

st.write(
    "Aplicación para consultar y comparar audífonos "
    "disponibles en diferentes tiendas en línea."
)

st.subheader("Tiendas analizadas")

st.write("- Ktronix")
st.write("- Alkosto")
st.write("- Falabella")

st.info(
    "La aplicación utilizará los módulos de scraping "
    "y procesamiento desarrollados en el proyecto."
)