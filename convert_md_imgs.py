import re
import pyperclip

def md_to_img_empty_alt(md_text: str, width: int = 400) -> str:
    """
    Convierte imágenes estilo markdown ![alt](src)
    a etiquetas HTML <img ... width='...' alt=''>
    """
    pattern = r'!\[[^\]]*\]\((\/uploads\/[^\s)]+)\)'
    replacement = lambda m: f"<img src='{m.group(1)}' alt='' width='{width}'/>"
    return re.sub(pattern, replacement, md_text)

def main():
    print("📥 Pegá el markdown que quieras convertir (ENTER para terminar):")
    lines = []
    while True:
        try:
            line = input()
            if not line:
                break
            lines.append(line)
        except EOFError:
            break

    md_text = "\n".join(lines)
    converted = md_to_img_empty_alt(md_text)

    # Copiar al portapapeles
    pyperclip.copy(converted)

    print("\n✅ Conversión terminada y copiada al portapapeles.")
    print("Ahora podés pegarla donde quieras (Cmd+V / Ctrl+V).")
    print("\nResultado:\n")
    print(converted)

if __name__ == "__main__":
    main()

# crear venv e instalacion
# python3 -m venv venv
# source venv/bin/activate
# python -m pip install pyperclip
# python convert_md_imgs.py


# Activar el venv
# source venv/bin/activate
# python3 convert_md_imgs.py

# Desactivar el venv
# deactivate