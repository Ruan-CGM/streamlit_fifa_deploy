import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🤖",
    layout="wide",
)

# if "data" not in st.session_state:
#     st.error("Dados não carregados. Redirecionando para a página inicial.")
#     st.query_params.from_dict(page="1_🏡_home.py")
# else:
    df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)

players_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(players_stats["Photo"])
st.title(players_stats["Name"])

st.markdown(f"**Clube:** {players_stats['Club']}")
st.markdown(f"**Nacionalidade:** {players_stats['Nationality']}")
st.markdown(f"**Posição:** {players_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {players_stats['Age']}")
col2.markdown(f"**Altura:** {players_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {players_stats['Weight(lbs.)'] * 0.453:.2f}")
st.divider()


st.subheader(f"Overall {players_stats['Overall']}")
st.progress(int(players_stats["Overall"]) / 100)

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de Mercado", value=f"£ {players_stats['Value(£)']:.2f}")
col2.metric(label="Remuneração Semanal", value=f"£ {players_stats['Wage(£)']:.2f}")
col3.metric(label="Cláusula de rescisão", value=f"£ {players_stats['Release Clause(£)']:.2f}")
