from PIL import Image

# Open the image file
im = Image.open("pan.png")

# Convert the image to grayscale
im = im.convert("L")

# Set a threshold value for the image
threshold = 100

# Get the image's width and height
width, height = im.size

# Create a new image with the same size
new_im = Image.new("L", (width, height),     255)

# Iterate through the pixels in the image
for x in range(width):
    for y in range(height):
        # Get the pixel's value
        pix = im.getpixel((x, y))
        # If the pixel's value is less than the threshold,
        # set the pixel's value in the new image to 0
        if pix < threshold:
            print(pix)
            new_im.putpixel((x, y), 0)

# Crop the image based on the bounding box of the non-white pixels
bbox = new_im.getbbox()
if bbox:
    cropped = im.crop(bbox)
    cropped.save("cropped.png")
    new_im.save("cropped.png")
