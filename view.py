def index():
    with open('templase/index.html') as templase:
        return templase.read()


def blog():
    with open('templase/blog.html') as templase:
        return templase.read()