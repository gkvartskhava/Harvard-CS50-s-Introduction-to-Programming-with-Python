def main():
    name = input("File name: ").lower().strip()
    print(type(name))

def type(x):
    if x.endswith(".gif"):
        return "image/gif"
    elif x.endswith(".jpg"):
        return "image/jpeg"
    elif x.endswith(".jpeg"):
        return "image/jpeg"
    elif x.endswith(".png"):
        return "image/png"
    elif x.endswith(".pdf"):
        return "application/pdf"
    elif x.endswith(".zip"):
        return "application/zip"
    elif x.endswith(".txt"):
        return "text/plain"
    else:
        return "application/octet-stream"

main()
