from presentacion.presentacion_usuarios import login_usuario
from presentacion.menu import menu_principal

usuario = login_usuario()
if usuario:
    menu_principal()