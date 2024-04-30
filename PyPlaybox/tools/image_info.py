from PIL import Image

# Percorso dell'immagine
IMAGE_PATH = r"C:\Users\salva\Documents\VS Code\pysandbox\scrolling world\autumn.png"

# Dimensioni delle tiles
TILE_SIZE = 16

def count_tiles(image, tile_size):
    image_width, image_height = image.size
    num_tiles_x = image_width // tile_size
    num_tiles_y = image_height // tile_size
    total_tiles = num_tiles_x * num_tiles_y
    return total_tiles, num_tiles_x, num_tiles_y

def main():
    # Carica l'immagine "autumn"
    try:
        autumn = Image.open(IMAGE_PATH)
    except IOError:
        print("Errore: Impossibile aprire l'immagine.")
        return

    # Dividi "autumn" in tiles
    total_tiles, num_tiles_x, num_tiles_y = count_tiles(autumn, TILE_SIZE)

    # Stampa le informazioni
    print("Dimensione dell'immagine:", autumn.size[0], autumn.size[1])
    print("Numero di tiles presenti in autumn:", total_tiles)
    print("Numero di colonne di tiles in autumn:", num_tiles_x)
    print("Numero di righe di tiles in autumn:", num_tiles_y)

if __name__ == "__main__":
    main()
