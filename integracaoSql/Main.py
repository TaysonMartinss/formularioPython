import streamlit as st
from Database import Database
from dotenv import load_dotenv

load_dotenv()

def main():

    db_manager = Database()

    st.title("Formulário de Cadastro")


    with st.form("formulario"):
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        endereco = st.text_input("Endereço")
        cpf = st.text_input("CPF")


        submit_button = st.form_submit_button("Enviar")


    if submit_button:
        if nome and email and telefone and endereco and cpf:

            db_manager.insert_data(nome, email, telefone, endereco, cpf)
            st.success("Dados inseridos com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")


    st.subheader("Dados no Banco de Dados")
    data = db_manager.fetch_data()

    if data:

        st.table(data)
    else:
        st.write("Nenhum dado encontrado.")


    db_manager.close()

if __name__ == "__main__":
    main()