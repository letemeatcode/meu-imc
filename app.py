import streamlit as st

# Configuració de la pàgina (títol que surt a la pestanya del navegador)
st.set_page_config(page_title="Calculadora IMC Pro", page_icon="⚖️")

# Títol principal amb estil
st.title("Calculadora d'Índex de Massa Corporal")
st.markdown("---")

# Secció d'entrada de dades
st.subheader("Introdueix les teves dades:")
nom = st.text_input("Com et dius, gilipollas?", placeholder="Escriu el teu nom...")

col1, col2 = st.columns(2)
with col1:
    pes = st.number_input("El teu pes (en kg)", value="1", min_value=1.0, max_value=250.0, step=0.1)
with col2:
    alcada_cm = st.number_input("La teva altura (en cm)", min_value=50, max_value=250, value=170)

# Botó de càlcul
if st.button("Calcular el meu estat 🚀"):
    if nom:
        # Càlcul de l'IMC
        alcada_m = alcada_cm / 100
        imc = pes / (alcada_m ** 2)
        
        st.divider()
        st.header(f"Resultats per a {nom}")
        
        # Mostrem el número de l'IMC de forma visual
        st.metric(label="El teu IMC és de:", value=f"{imc:.2f}")

        # Lògica amb colors i missatges
        if imc < 18.5:
            st.warning("⚠️ **Estat: Baix pes.**")
            st.info("Hauries de guanyar una mica de pes per estar en el rang saludable.")
        
        elif 18.5 <= imc <= 24.9:
            st.success("✅ **Estat: Pes ideal!**")
            st.write("Estàs en un rang de pes saludable. Continua cuidant-te!")
            st.balloons() # <--- Això llança els globus!
            
        else:
            st.error("⚠️ **Estat: Sobrepès.**")
            st.info("Hauries de considerar perdre una mica de pes per millorar la teva salut.")
            
        # Nota a peu de pàgina
        st.caption("Nota: L'IMC és orientatiu. Consulta sempre a un professional de la salut.")
    else:
        st.error("Si us plau, posa el teu nom per personalitzar el resultat.")

