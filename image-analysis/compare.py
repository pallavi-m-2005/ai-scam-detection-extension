from PIL import Image
import imagehash

def compare_images(real, suspicious):

    hash1 = imagehash.phash(
        Image.open(real)
    )

    hash2 = imagehash.phash(
        Image.open(suspicious)
    )

    difference = hash1 - hash2

    return difference
