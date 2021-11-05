from PIL import Image, ImageChops
import media
import os


def scale_image(image, scale=1):
    os.makedirs('media/scaled',exist_ok=True)
    image_path = image.image.url
    size = round(image.image.width*scale), round(image.image.height*scale)

    img = Image.open(image_path[1:])
    img = img.resize(size, Image.ANTIALIAS)
    save_path = 'media/scaled/{}_{}_{}.jpg'.format(image.id, size[0], size[1])
    img = img.convert('RGB')
    img.save(save_path)
    
    return '/'+save_path


def get_diff(upload_image, exists_image):
    if abs((upload_image.image.height/upload_image.image.width) - (exists_image.image.height/exists_image.image.width)) >= 0.01:
        return 1

    upload = Image.open(upload_image.image)
    exists = Image.open(exists_image.image.url[1:])
    upload = upload.convert('RGB')
    exists = exists.convert('RGB')
    if upload_image.image.height > exists_image.image.height:
        upload = upload.resize(exists.size, Image.ANTIALIAS)
    else:
        exists = exists.resize(upload.size, Image.ANTIALIAS)
    diff = ImageChops.difference(upload, exists)
    black = 0
    other = 0
    for pixel in diff.getdata():
        if pixel[0] < 10 and pixel[1] < 10 and pixel[2] < 10:
            black += 1
        else:
            other += 1
    print(black)
    print(other)
    print(other/(black+other))
    if other/(black+other) < 0.1:
        print(exists_image.id)
    return other/(black+other)