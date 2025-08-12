import sys
from   os.path import splitext
from  PIL import ImageOps,Image

def main():
    try:
        if argument_check():
            source1 = splitext(sys.argv[1])
            file1 =  (f'{source1[0]}' + '.jpg')

            source2 = splitext(sys.argv[2])
            file2 = (f'{source2[0]}' + '.jpg')

            img2 = Image.open("shirt.png")
            size2 = img2.size

            img1 = Image.open(file1)
            img_resized = ImageOps.fit(img1,size2)

            img_resized.paste(img2,img2)
            img_resized.save(file2)

    except FileNotFoundError:
            sys.exit(f"Could not read ")

def argument_check():

        valid_extensions = ('.jpg', '.jpeg', '.png')
        if len(sys.argv) < 3:
            sys.exit(f'Too few command-line arguments')
        elif len(sys.argv) > 3:
            sys.exit(f'Too many command-line arguments')

        if not (sys.argv[1].lower().endswith(valid_extensions) and sys.argv[2].lower().endswith(valid_extensions)):
            sys.exit('Invalid file extension')

        elif sys.argv[1][-3:].lower() != sys.argv[2][-3:].lower():
            sys.exit('Invalid input')
        else:
            return True

if __name__ == "__main__":
    main()



