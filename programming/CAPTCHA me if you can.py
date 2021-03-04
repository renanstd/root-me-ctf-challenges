import json
import base64
import requests
import pytesseract
from html.parser import HTMLParser
from PIL import Image


URL = 'http://challenge01.root-me.org/programmation/ch8/'

class MyHTMLparser(HTMLParser):
    """
    Classe que fiz usando o HTMLParser nativo para localizar uma imagem
    em um conteúdo HTML
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.encoded_image = None

    def handle_starttag(self, tag, attr):
        """
        Sobrescrevo essa função para pegar somente a tag que eu quero
        """
        for tag, content in attr:
            if tag == 'src' and 'image' in content:
                encoded_image = content.split(',')[1]
                self.encoded_image = encoded_image

    def get_encoded_image(self):
        """
        Retorno a imagem base64 encontrado na página
        """
        return self.encoded_image.encode()


# Acessa a página e pega o conteúdo
session = requests.Session()
# content = requests.get(URL)
content = session.get(URL)

# Inicializo o parser e passo o conteúdo pra ele extrair a imagem
parser = MyHTMLparser()
parser.feed(content.text)
encoded_image = parser.get_encoded_image()

# A imagem está em base64, então eu crio ela em png para ser analisada
with open("image.png", "wb") as file:
    file.write(base64.decodebytes(encoded_image))

# Pega a imagem que acabou de ser criada
img = Image.open("image.png")

# Usa o tesseract para identificar o texto
captcha = pytesseract.image_to_string(img, lang='eng')

# Para o tesseract funcionar, é necessário a instalação de um binário
# Para baixar este binário: https://tesseract-ocr.github.io/tessdoc/Home.html

# Remove caracteres de espaço para eviar erros
captcha = captcha.replace(' ', '')

# Monta e envia os dados
data = {'cametu': captcha}
response = session.post(URL, data)

# Printa o resultado
print(response.text)

# Foi necessário a execução contínua do script até dar certo
