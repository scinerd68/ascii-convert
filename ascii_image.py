from PIL import Image

img = Image.open("car.jpg")

print("Successfully loaded image")
print("Size of image:", img.size[0], "x", img.size[1])

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_pixel_matrix(img, height):
    img.thumbnail((height, 120))
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

def get_brightness(pixel):
    return sum(pixel)//len(pixel)

def map_brightness_to_ascii(pixel):
    ascii_index = round((pixel * len(ascii_chars))/255)
    if ascii_index >= len(ascii_chars):
        ascii_index = len(ascii_chars) - 1
    return ascii_chars[ascii_index]

def print_matrix(img):
    pixel_matrix = get_pixel_matrix(img, 1000)
    for x in range(len(pixel_matrix)):
        for y in range(len(pixel_matrix[x])):
            pixel_brightness = get_brightness(pixel_matrix[x][y])
            pixel = map_brightness_to_ascii(pixel_brightness)
            pixel_matrix[x][y] = pixel
    for i in range(len(pixel_matrix)):
        print(''.join(pixel_matrix[i]))

print_matrix(img)
