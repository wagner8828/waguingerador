

import subprocess

# Chamar o executável gerado pelo PyInstaller
subprocess.run(["dist/gerador_waguin.exe"])

# Pausar para permitir que você veja a saída antes de fechar a janela
input("Pressione Enter para sair...")