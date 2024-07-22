from cx_Freeze import setup, Executable

# Opções adicionais podem ser necessárias dependendo das bibliotecas que seu script usa
options = {
    'build_exe': {
        'packages': ['pynput','queue'],  # Inclua pacotes adicionais necessários aqui
        'excludes': ['tkinter'],  # Exclua pacotes que não são necessários
        'include_files': ['log_teclas.txt']  # Inclua arquivos adicionais necessários
    }
}



# Configuração do executável
executables = [
    Executable(
        script='teclado.py',  # Substitua pelo nome do seu script
        base='Console',  # Use 'Win32GUI' se o seu script tiver uma interface gráfica
        target_name='teclado.exe'  # Substitua pelo nome desejado para o executável
    )
]

# Chamada de setup para criar o executável
setup(
    name='teclado',
    version='0.1',
    description='Teclado Win',
    options=options,
    executables=executables
)
