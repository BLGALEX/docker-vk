from PIL import Image
import media
import os

def scale_image(image, scale=1):
    os.makedirs('media/scaled',exist_ok=True)
    image_path = image.image.url
    size = round(image.image.width*scale), round(image.image.height*scale)

    img = Image.open(image_path[1:])
    img = img.resize(size, Image.ANTIALIAS)
    save_path = 'media/scaled/{}_{}_{}.jpg'.format(image.id, size[0], size[1])
    img.save(save_path)
    
    return '/'+save_path