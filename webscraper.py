import requests
from bs4 import BeautifulSoup

# URL de la página de la que queremos hacer scraping
url = "https://www.bbc.com/news"

# Realizamos la petición HTTP a la página
response = requests.get(url)

# Verificamos que la petición haya sido exitosa
if response.status_code == 200:
    # Creamos el objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscamos todos los elementos que contengan los titulares
    # Ajusta este selector según la estructura de la página y tus necesidades
    headlines = soup.find_all('h3')
    
    # Imprimimos los titulares encontrados
    for headline in headlines:
        print(headline.text.strip())
else:
    print("Error en la petición:", response.status_code)
