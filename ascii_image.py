from PIL import Image

img = Image.open("car.jpg")

print("Successfully loaded image")
print("Size of image:", img.size[0], "x", img.size[1])

ascii_chars = r"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_pixel_matrix(img, height):
    img.thumbnail((height, 120))
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

def get_brightness(pixel, brightness_type):
    if brightness_type == 'average':
        return sum(pixel)//len(pixel)
    elif brightness_type == 'luminosity':
        return 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]
    elif brightness_type == 'lightness':
        return (max(pixel) + min(pixel))/2

def map_brightness_to_ascii(pixel):
    ascii_index = round((pixel * len(ascii_chars))/255)
    if ascii_index >= len(ascii_chars):
        ascii_index = len(ascii_chars) - 1
    return ascii_chars[ascii_index]

def print_matrix(img, brightness_type):
    pixel_matrix = get_pixel_matrix(img, 1000)
    for x in range(len(pixel_matrix)):
        for y in range(len(pixel_matrix[x])):
            pixel_brightness = get_brightness(pixel_matrix[x][y], brightness_type)
            pixel = map_brightness_to_ascii(pixel_brightness)
            pixel_matrix[x][y] = pixel
    for i in range(len(pixel_matrix)):
        print(''.join(pixel_matrix[i]))

brightness_type = input("which type of brightness (average, luminosity, lightness)? ")
print_matrix(img, brightness_type)
