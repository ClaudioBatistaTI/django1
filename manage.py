import os

def main():
    # Obtém o endereço do servidor e da porta da variável de ambiente
    server_address = os.getenv("RAILWAY_SERVER_ADDR")

    # Imprime o endereço do servidor e da porta
    print(server_address)

if __name__ == "__main__":
    main()
