from google_images_download import google_images_download  # importing the library

response = google_images_download.googleimagesdownload()  # class instantiation

arguments = {"keywords": "Tree yoga pose", "limit": 100, "print_urls": True, "format": "png",
             "output_directory": "/home/aakash/Downloads/dataset/", "size": ">640*480", "type": "photo"}
paths = response.download(arguments)
print(paths)


