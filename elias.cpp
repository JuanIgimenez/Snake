#include <windows.h>

int main() {
    // Especifica la URL de la página web que deseas abrir
    const char* url = "https://www.ejemplo.com";

    // Abre la página web en el navegador predeterminado
    ShellExecute(NULL, "open", url, NULL, NULL, SW_SHOWNORMAL);

    return 0;
}
