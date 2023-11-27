from class_pars import Parser


def main():
    pars = Parser('https://wargm.ru/','server/66235/votes', 'text_steam.txt')
    pars.run()


if __name__ == '__main__':
    main()