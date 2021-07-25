import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from Guess_revert import game_reverse
from guess_the_number import game

save_info('старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутсвует название')
        else:
            copy_file(name, new_name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название')
        else:
            change_dir(name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создать файл')
        print('create_folder - создать папку')
        print('delete - удаление папки или файла')
        print('copy - копирование файла или папки')
    elif command == 'reverse':
        game_reverse()
    elif command == 'game':
        game()

    save_info("конец")
