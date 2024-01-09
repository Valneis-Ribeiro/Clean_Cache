import os
import subprocess
import tempfile

class Clean_Cache:

    def __init__(self):
        self.workspace = "nt" # Windows
        self.folder_temp_path = "C:\Windows\Temp"
        # self.folder_temp_porcent_path = tempfile.gettempdir()
        self.folder_prefetch_path = os.path.join(os.environ['SystemRoot'], 'prefetch')
        self.folder_trash_path = 'rd /s /q C:\\$Recycle.Bin'
    
    def clean_folder_temp(self):
        try:
            if self.check_computer_system():
                try:  
                    for file in os.listdir(self.folder_temp_path):
                        path_file = os.path.join(self.folder_temp_path, file)
                        os.remove(path_file)
                        print(f'Arquivos {path_file} removido com seucesso.')
                    print('Arquivos removidos com sucesso.')    
                except OSError as o:
                    print(f'Erros ao remover os arquivos {o}')
        except:
            print('Error system')
    # def clean_folder_temp_porcent(self):
    #     if self.check_computer_system:
    #         try:
    #             try:   
    #                 for file in os.listdir(self.folder_temp_porcent_path):
    #                     path_file = os.path.join(self.folder_temp_porcent_path, file)
    #                     os.remove(path_file)
    #                     os.rmdir(path_file)
    #                     print(f'Arquivo {path_file} removido com sucesso.')
    #                 print("Arquivos removidos com suceso.")   
    #             except OSError as o:
    #                 print(f'Erro eo remover {o}')
    #         except:
    #             print('Error system.')            
    
    def clean_folder_prefetch(self):
            try:
                if self.check_computer_system():
                    try:
                        for file in os.listdir(self.folder_prefetch_path):
                            path_file = os.path.join(self.folder_prefetch_path, file)
                            os.remove(path_file)
                            print(f"Arquivo {path_file} removido com sucesso.")      
                    except OSError as o:
                        print(f'Erro {o} ao apagar os arquivos')
            except:
                print('Error system')

    def clean_folder_trash(self):
            try:
                if self.check_computer_system():
                    try:
                        subprocess.run(self.folder_trash_path, shell=True)
                    except OSError as o:
                        print(f'Erro {o} ao apgar os arquivos')    
            except:
                print('Error system')

    def check_computer_system(self):
       if os.name == self.workspace:
          return True
       else:
          return False

    def check_amount_files_cache_for_clean(self):
        path_temp = os.listdir(self.folder_temp_path)
        path_prefetch = os.listdir(self.folder_prefetch_path)
        amount_files_temp = len(path_temp)
        amount_files_prefetch = len(path_prefetch)
        all_files_sum = amount_files_temp + amount_files_prefetch
        return path_temp, path_prefetch, all_files_sum

    def get_files_size(self):   
        amount_kb  = 0
        for files in os.listdir(self.folder_temp_path):
            path_files = os.path.join(self.folder_temp_path, files) 
            size_files = os.path.getsize(path_files)
            amount_kb += size_files
        conversion_factor = 1024
        amount_mb = amount_kb / conversion_factor 
        print(amount_mb)            
        return amount_mb

