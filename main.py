from database.conexao import Conexao
def main():
    conexao = Conexao()
    print("CONEXÃO REALIZADA COM SUCESSO! :)")
    
    conexao.close()

if __name__ == "__main__":
    main()  