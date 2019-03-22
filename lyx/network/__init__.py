def aria_format(url):
    path, filename = os.path.split(url)

    path = path.lstrip(r'https://').lstrip(r'http://')

    result = url + '\n dir=' + path + '\n out=' + filename + '\n'
    return result
