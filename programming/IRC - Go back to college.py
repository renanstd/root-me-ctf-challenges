import math
from irc import IRC

# Inicializa a conexão
irc = IRC()
ep = '!ep1'

# Faz contato com o bot
irc.send_private_message(ep)
question = irc.listen()
print(question)

# Calcula resultado
question = question.split(':')[2]
a, b = question.split('/')
a, b = int(a), int(b)
result = math.sqrt(a) * b
result = round(result, 2)

# Envia resposta
irc.send_private_message(f"{ep} -rep {result}")

# Recebe a flag
print(irc.listen())
