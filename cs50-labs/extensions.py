fileExt = {
    "gif": "image/gif",
    "jpeg": "image/jpeg",
    "jpg": "image/jpg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

userFile = input("File name: ").lower().strip()
userFileExt = userFile.split(".")
test = (len(userFileExt) - 1)


if userFileExt[test] in fileExt:
    print(fileExt[userFileExt[test]])
else:
    print("application/octet-stream")


