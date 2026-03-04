import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Estudiantes", layout="wide")

@st.cache_data
def load_data():
    # Buscamos el archivo CSV en la carpeta actual
    import os
    for file in os.listdir('.'):
        if file.endswith('.csv'):
            return pd.read_csv(file)
    return None

df = load_data()

if df is not None:
    st.title("🎓 Dashboard de Rendimiento Estudiantil")
    
    # 1. Gráfico Numérico vs Numérico
    st.subheader("Análisis Numérico")
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    col1, col2 = st.columns(2)
    x_n = col1.selectbox("Variable X:", num_cols, index=0)
    y_n = col2.selectbox("Variable Y:", num_cols, index=num_cols.index('Exam_Score') if 'Exam_Score' in num_cols else 0)
    
    fig1 = px.scatter(df, x=x_n, y=y_n, trendline="ols")
    st.plotly_chart(fig1, use_container_width=True)

    # 2. Gráfico Categórico
    st.subheader("Análisis por Categorías")
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    col3, col4 = st.columns(2)
    x_c = col3.selectbox("Categoría:", cat_cols, index=0)
    fig2 = px.box(df, x=x_c, y=y_n, color=x_c)
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.error("No se encontró el archivo CSV. Asegúrate de que el archivo esté en la carpeta del proyecto.")
