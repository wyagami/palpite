import streamlit as st
import random

# Função principal do jogo
def adivinhe_o_numero():
    st.title("🎮 Adivinhe o Número 🎮")
    
    # Inicializa o estado da sessão para armazenar o número secreto e o número de tentativas
    if 'numero_secreto' not in st.session_state:
        st.session_state.numero_secreto = random.randint(1, 100)
        st.session_state.tentativas = 0
    
    # Exibe instruções
    st.write("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

    # Entrada do usuário
    palpite = st.number_input("Digite seu palpite:", min_value=1, max_value=100, step=1)

    # Botão para confirmar o palpite
    if st.button("Confirmar Palpite"):
        st.session_state.tentativas += 1

        if palpite < st.session_state.numero_secreto:
            st.warning(f"Seu palpite ({palpite}) é muito baixo! Tente novamente.")
        elif palpite > st.session_state.numero_secreto:
            st.warning(f"Seu palpite ({palpite}) é muito alto! Tente novamente.")
        else:
            st.success(f"Parabéns! Você acertou o número {st.session_state.numero_secreto} em {st.session_state.tentativas} tentativas!")
            # Reinicia o jogo
            st.session_state.numero_secreto = random.randint(1, 100)
            st.session_state.tentativas = 0

    # Botão para reiniciar o jogo
    if st.button("Reiniciar Jogo"):
        st.session_state.numero_secreto = random.randint(1, 100)
        st.session_state.tentativas = 0
        st.rerun()

# Executa o jogo
if __name__ == "__main__":
    adivinhe_o_numero()