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
      if self.check_workspace():
        try:
            try:  
                for file in os.listdir(self.folder_temp_path):
                    path_file = os.path.join(self.folder_temp_path, file)
                    os.remove(path_file)
                    print(f'Arquivos {path_file} removido com seucesso.')
                print('Arquivos removidos com sucesso.')    
            except OSError as o:
                print(f'Erros ao remover os arquivos {o}')
        except:
            print('Error Workscpace')
    
    # def clean_folder_temp_porcent(self):
    #     if self.check_workspace:
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
    #             print('Error Workspace.')            
    
    def clean_folder_prefetch(self):
        try:
            try:
                for file in os.listdir(self.folder_prefetch_path):
                    path_file = os.path.join(self.folder_prefetch_path, file)
                    os.remove(path_file)
                    print(f"Arquivo {path_file} removido com sucesso.")      
            except OSError as o:
                print(f'Erro {o} ao apagar os arquivos')
        except:
            print('Error Workspace')

    def clean_folder_trash(self):
        if self.check_workspace():
            try:
                subprocess.run(self.folder_trash_path, shell=True)
            except:
                print('Error Workscpace')    

    def check_workspace(self):
       if os.name == self.workspace:
          return True
       else:
          return False
       
