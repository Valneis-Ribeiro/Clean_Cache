import PySimpleGUI as sg
from clean_cache import Clean_Cache
import time

sg.theme('DarkPurple5')

clean_layout = [[sg.Button('Check files', font=('Arial', 20),size=(70,1), button_color='orange')],
                [sg.Text('Arquivos temporários que estão enchendo a memória cache',font=('Arial', 15) ),sg.Text(key='-STATUS_CHECK-',font=('Arial', 15) )],
                [sg.Button('Clean cache', font=('Arial', 12),size=(15,2))]
]

window_clean = sg.Window('Clean cache v. 1.3', clean_layout, size=(700,180) )


while True:

    event, value = window_clean.read()

    clean_cache = Clean_Cache()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Check files':
        check_size_files = clean_cache.get_files_size()
        if check_size_files == 0:
            window_clean['-STATUS_CHECK-'].update(background_color='green')
            window_clean['-STATUS_CHECK-'].update(check_size_files)
            sg.popup_ok('Precesso de verificação concluído.')
        elif check_size_files > 0:
            window_clean['-STATUS_CHECK-'].update(background_color='red')
            window_clean['-STATUS_CHECK-'].update(check_size_files)
            sg.popup_ok('Precesso de verificação concluído.')    
    elif event == 'Clean cache':
        clean_cache.clean_folder_temp()
        clean_cache.clean_folder_prefetch()
        window_clean['-STATUS_CHECK-'].update(background_color='green')
        window_clean['-STATUS_CHECK-'].update(check_size_files)




window_clean.close()
