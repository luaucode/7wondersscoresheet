from PIL import Image

path = 'Wonder-scoring-card.jpg'


def main():
    try:
        img = Image.open(path)
        width, height = img.size
        img = img.resize((width // 7, height // 7))
        img.show()
    except IOError:
        pass


if __name__ == "__main__":
    main()
