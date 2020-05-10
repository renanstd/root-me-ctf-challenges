import base64
from irc import IRC

# Inicializa a conexão
irc = IRC()
ep = '!ep2'

# Faz contato com o bot
irc.send_private_message(ep)
question = irc.listen()
question = question.split(':')[2]

# Calcula resultado
result = base64.b64decode(question).decode('utf-8')

# Envia resposta
irc.send_private_message(f"{ep} -rep {result}")

# Recebe a flag
print(irc.listen())
