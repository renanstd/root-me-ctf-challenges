import base64
import zlib
from irc import IRC

# Inicializa a conexão
irc = IRC()
ep = '!ep4'

# Faz contato com o bot
irc.send_private_message(ep)
question = irc.listen()
question = question.split(':')[2]
print(question)
# question = str(question)

# Calcula resultado
decoded_question = base64.b64decode(question)
unpacked_result = zlib.decompress(decoded_question).decode('utf-8')

# Envia resposta
irc.send_private_message(f"{ep} -rep {unpacked_result}")

# Recebe a flag
print(irc.listen())
