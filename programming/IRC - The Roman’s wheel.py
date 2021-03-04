import codecs
from irc import IRC

# Inicializa a conexão
irc = IRC()
ep = '!ep3'

# Faz contato com o bot
irc.send_private_message(ep)
question = irc.listen()
question = question.split(':')[2]
print(question)
question = str(question)

# Calcula resultado
result = codecs.encode(question, 'rot_13')
print(result)

# Envia resposta
irc.send_private_message(f"{ep} -rep {result}")

# Recebe a flag
print(irc.listen())
