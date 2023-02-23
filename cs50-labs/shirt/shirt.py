import sys
from PIL import Image, ImageOps

def main():
    verify_image_file()
    try:
        before_img = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")    
    shirt_img = Image.open("shirt.png")
    
    # Resize before_img to fit that of shirt_img as it is smaller.
        # 1) obtain size of shirt_img
    size = shirt_img.size
        # 2) Create a new image of the "before_img" with size of "shirt_img"
    after_img = ImageOps.fit(before_img, size) 
        # 3) Paste shirt_img over newly created after_img
    after_img.paste(shirt_img, shirt_img)
        # 4) Save new image with name entered by user in second argument
    after_img.save(sys.argv[2])
        # Display new image - file name in file system is based on argument provided by user.
    after_img.show()
   
def verify_image_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".jpg" in sys.argv[1].lower() and ".png" in sys.argv[2].lower():
        sys.exit("Input and output have different extensions")
    if sys.argv[2].endswith(".jpg") == False and sys.argv[2].endswith(".jpeg") == False and sys.argv[2].endswith(".png") == False and sys.argv[1].endswith(".jpg") == False and sys.argv[1].endswith(".jpeg") == False and sys.argv[1].endswith(".png") == False:
        sys.exit("Invalid output")

if __name__ == "__main__":
    main()