import streamlit as st

# Títol i configuració de la pàgina
st.set_page_config(page_title="Calculadora IMC", page_icon="⚖️")
st.title("⚖️ Calculadora d'IMC")

# Formulari d'entrada
with st.container():
    nom = st.text_input("Com et dius?", placeholder="Escriu el teu nom aquí")
    
    col1, col2 = st.columns(2)
    with col1:
        pes = st.number_input("Pes (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
    with col2:
        alcada_cm = st.number_input("Altura (cm)", min_value=50.0, max_value=250.0, value=170.0, step=1.0)

# Botó per calcular
if st.button("Calcular el meu estat"):
    if nom:
        alcada_m = alcada_cm / 100
        imc = pes / (alcada_m ** 2)
        
        st.divider()
        st.subheader(f"Resultats per a {nom}:")
        st.metric(label="El teu IMC", value=f"{imc:.2f}")
        
        if imc < 18.5:
            st.warning("Hauries de guanyar pes. Estàs per sota del pes recomanat.")
        elif 18.5 <= imc <= 24.9:
            st.success("Estàs en el teu pes ideal. Molt bé!")
        else:
            st.error("Hauries de perdre pes. Estàs per sobre del pes recomanat.")
    else:
        st.info("Si us plau, introdueix el teu nom per continuar.")