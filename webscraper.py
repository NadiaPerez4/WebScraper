import requests
from bs4 import BeautifulSoup

def scrape_bbc_headlines(url):
    try:
        # Realizamos la petición HTTP a la página
        response = requests.get(url)
        
        # Verificamos que la petición haya sido exitosa
        if response.status_code == 200:
            print("Conexión exitosa. Procesando página...")
            # Creamos el objeto BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Buscamos todos los elementos que contengan los titulares
            headlines = soup.find_all('h3')  # Ajustar según la estructura de la página
            
            # Preparamos un archivo para guardar los titulares
            with open("headlines.txt", "w", encoding="utf-8") as file:
                # Imprimimos y guardamos los titulares encontrados
                for headline in headlines:
                    headline_text = headline.text.strip()
                    print(headline_text)
                    file.write(headline_text + "\n")
            print("Los titulares han sido guardados en 'headlines.txt'.")
        else:
            print("Error en la petición HTTP:", response.status_code)
    except requests.RequestException as e:
        print("Error al conectar con la página:", e)

# Solicitamos al usuario la URL
url = input("Escribe la URL de la página de noticias de BBC: ")

# Llamamos a la función con la URL proporcionada
scrape_bbc_headlines(url)
    