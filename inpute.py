
def input_genre():
    genre_list = ['Drama', 'Comedy', 'Musical',
                  'Detective', 'Action', 'Horror']
    while True:
        genre = input('Введите название категории: ')
        if genre in genre_list:
            return genre
        else:
            print(f'Название категории должно быть из списка {genre_list}')
