import socket

class IRC:
    """
    Classe que faz a conexão com o IRC utilizado nos challenges de
    programação do root-me.org
    https://www.root-me.org/en/Challenges/Programming/
    """
    def __init__(self):
        self.HOST = 'irc.root-me.org'
        self.PORT = 6667
        self.CHANNEL = '#root-me_challenge'
        self.BOT = 'candy'
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.HOST, self.PORT))
        self.listen()
        self.send("NICK DOC")
        self.send("USER Pizebot Pibot Pibot :Python IRC")
        self.listen()
        self.send(f"JOIN {self.CHANNEL}")
        self.listen()

    def listen(self):
        """
        Recebe e converte uma mensagem
        """
        response = self.irc.recv(20140000).decode("utf-8")
        return response

    def send(self, message):
        """
        Converte e envia uma mensagem genérica para o canal
        """
        self.irc.send(f"{message}\r\n".encode('utf-8'))

    def send_private_message(self, message):
        """
        Converte e envia uma mensagem privada para o bot
        """
        self.send(f"PRIVMSG {self.BOT} {message}")
