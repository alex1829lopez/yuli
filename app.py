import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(page_title="ATS Inteligente", layout="wide")

st.title("🧠 Sistema de Reclutamiento Inteligente (ATS)")

# -----------------------------
# GENERAR DATOS SIMULADOS
# -----------------------------
def generar_datos(n=50):
    np.random.seed(42)

    data = {
        "nombre": [f"Candidato {i}" for i in range(n)],
        "experiencia": np.random.randint(0, 15, n),
        "skills_tech": np.random.randint(1, 10, n),
        "entrevista": np.random.randint(1, 10, n),
        "ingles": np.random.randint(1, 10, n),
    }

    df = pd.DataFrame(data)

    # score base
    df["score"] = (
        df["experiencia"] * 3 +
        df["skills_tech"] * 4 +
        df["entrevista"] * 2 +
        df["ingles"] * 2
    )

    # normalizar 0-100
    scaler = MinMaxScaler(feature_range=(0, 100))
    df["score"] = scaler.fit_transform(df[["score"]])

    return df

df = generar_datos()

# -----------------------------
# SIDEBAR FILTROS
# -----------------------------
st.sidebar.header("⚙️ Filtros")

min_score = st.sidebar.slider("Score mínimo", 0, 100, 50)

df_filtrado = df[df["score"] >= min_score]

# -----------------------------
# KPIs
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("👥 Candidatos", len(df_filtrado))
col2.metric("🏆 Mejor Score", round(df_filtrado["score"].max(), 2))
col3.metric("📊 Promedio", round(df_filtrado["score"].mean(), 2))

# -----------------------------
# TABLA
# -----------------------------
st.subheader("📋 Ranking de candidatos")

df_filtrado = df_filtrado.sort_values(by="score", ascending=False)

st.dataframe(df_filtrado, use_container_width=True)

# -----------------------------
# GRÁFICA 1
# -----------------------------
st.subheader("📈 Distribución de Scores")

fig = px.histogram(df_filtrado, x="score", nbins=20)
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# GRÁFICA 2
# -----------------------------
st.subheader("📊 Comparación de habilidades")

fig2 = px.bar(
    df_filtrado.head(10),
    x="nombre",
    y="score",
    color="score"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# EXPORTAR CSV
# -----------------------------
csv = df_filtrado.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Descargar candidatos filtrados",
    data=csv,
    file_name="candidatos_filtrados.csv",
    mime="text/csv"
)