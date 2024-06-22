import os

from PIL import Image  # pillow==10.3.0


def main():
    for file in os.listdir('game/images/'):
        if file == 'bg letistenara.jpg':
            continue
        f_path = os.path.join('game/images', file)
        Image.open(f_path).resize((1920, 1080)).save(f_path)


if __name__ == "__main__":
    main()
