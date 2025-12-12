import tkinter as tk
from tkinter import ttk, messagebox


#Base data for the prompt structure.
elements_by_category = {
    "Fantasy": ["Wizard", "Dragon", "Warrior", "Castle", "Spell"],
    "Futuristic": ["Robot", "Neon City", "Spaceship", "Cyborg"],
    "Historical": ["Samurai", "Knight", "Queen", "Temple"],
    "Anime": ["Student", "Hero", "Demon", "Idol"],
    "Nature": ["Forest", "Mountain", "Lake", "Waterfall"],
    "Realistic": ["Portrait", "Urban Scene", "Model", "City"],
    "Abstract": ["Energy", "Light", "Chaos", "Emotion"]
}

visual_styles = [
    "Digital illustration", "Realistic oil painting", "Cyberpunk",
    "Watercolor", "Concept art", "Manga"
]

lighting_effects = [
    "Dramatic", "Neon", "Warm", "Cool",
    "Sunset", "Nocturnal", "Natural light"
]

compositions = [
    "Close-up", "Medium shot", "Full shot",
    "Low-angle view", "Aerial view"
]

# Function definitions.

#Function to display the options of elements according to the chosen category.
def update_elements(event=None):
    category = category_var.get()
    nuevos_elementos = elementos_por_category.get(category, [])
    elemento_var.set("")
    elemento_menu["menu"].delete(0, "end")
    for elemento in nuevos_elementos:
        elemento_menu["menu"].add_command(
            label=elemento,
            command=lambda value=elemento: elemento_var.set(value)
        )

#Función para mostrar un mensaje que señale al usuario que primero debe escoger una categoría si intenta
#escoger un elemento principal sin seleccionar la categoría.
def mostrar_advertencia_elemento(event):
    if not category_var.get():
        messagebox.showwarning("Advertencia", "Primero debes escoger una categoría.")

#Función para la construcción del prompt en base a las opciones escogidas.
def generar_prompt():
    category = category_var.get()
    elemento = elemento_var.get()
    estilo = estilo_var.get()
    iluminacion = iluminacion_var.get()
    composicion = composicion_var.get()

    if not (category and elemento and estilo and iluminacion and composicion):
        resultado_label.config(
            text="Completa todas las opciones antes de generar el prompt.",
            fg="#ff5555"
        )
        return

    #Ajustes de redacción según las opciones seleccionadas.
    if category == "Anime":
        entorno_texto = (
            "representado en un estilo anime limpio, expresivo y visualmente equilibrado"
        )
    elif category == "Realista":
        entorno_texto = (
            "interpretado con estética realista, priorizando proporciones naturales y detalle auténtico"
        )
    elif category == "Abstracto":
        entorno_texto = (
            "concebido desde una perspectiva abstracta, con formas expresivas y simbolismo conceptual"
        )
    else:
        entorno_texto = (
            f"ambientado en un universo de {category.lower()}, con identidad visual definida y riqueza estética"
        )

    iluminacion_l = iluminacion.lower()

    if iluminacion_l == "atardecer":
        luz_texto = (
            "iluminado por un cálido resplandor de atardecer que realza sombras suaves"
        )
    elif iluminacion_l == "luz natural":
        luz_texto = (
            "bañado por luz natural equilibrada que aporta claridad y volumen"
        )
    elif iluminacion_l == "neón":
        luz_texto = (
            "con iluminación neón vibrante que genera reflejos intensos y ambiente moderno"
        )
    elif iluminacion_l == "nocturna":
        luz_texto = (
            "ambientado con iluminación nocturna que produce contrastes marcados y atmósfera profunda"
        )
    elif iluminacion_l == "dramática":
        luz_texto = (
            "con una iluminación dramática que enfatiza contraste y tensión visual"
        )
    else:
        luz_texto = (
            f"con iluminación {iluminacion_l} aplicada de forma armoniosa"
        )
        
    estilo_texto = (
        f"realizado en estilo {estilo.lower()}, con atención a color, forma y composición"
    )

    composicion_texto = f"siguiendo una composición en {composicion.lower()}"

    #Capa profesional de detalles para mejorar la calidad del prompt.
    detalles = (
        "Incluye texturas definidas, profundidad atmosférica, manejo preciso de la luz, "
        "armonía cromática y un acabado profesional pensado para resultados de alta calidad."
    )

    #Prompt final.
    prompt = (
        f"{elemento} {entorno_texto}, {luz_texto}, {estilo_texto}, "
        f"{composicion_texto}. {detalles}"
    )

    resultado_label.config(text=prompt, fg="white")

#Función para la opción "Copiar Prompt".
def copiar_prompt():
    texto = resultado_label.cget("text")
    if not texto:
        messagebox.showinfo("Información", "Primero genera un prompt para copiarlo.")
        return
    ventana.clipboard_clear()
    ventana.clipboard_append(texto)
    messagebox.showinfo("Copiado", "Prompt copiado al portapapeles.")

#Configuración básica de interfaz.

ventana = tk.Tk()
ventana.title("Generador de Prompts")
ventana.geometry("1080x670")
ventana.configure(bg="#0d0d0d")
ventana.minsize(960, 580)

#Centramos la ventana en función del tamaño de la pantalla.
ancho_ventana = 1080
alto_ventana = 670
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
pos_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
pos_y = int((alto_pantalla / 2) - (alto_ventana / 2))
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TLabel",
    background="#0d0d0d",
    foreground="white",
    font=("Segoe UI", 11)
)
style.configure(
    "TMenubutton",
    background="#1a1a1a",
    foreground="white",
    font=("Segoe UI", 11),
    relief="flat",
    padding=6
)
style.map("TMenubutton", background=[("active", "#292929")])
style.configure(
    "TButton",
    background="#2b2bff",
    foreground="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    padding=8
)
style.map("TButton", background=[("active", "#4c4cff")])

titulo = tk.Label(
    ventana,
    text="Generador de Prompts",
    font=("Segoe UI", 22, "bold"),
    fg="#b19cd9",
    bg="#0d0d0d"
)
titulo.pack(pady=(15, 10))

#Configuración del frame principal.
main_frame = tk.Frame(ventana, bg="#0d0d0d")
main_frame.pack(fill="both", expand=True)

#Configuración del frame con el apartado "Opciones de Generación".
frame_izq = tk.Frame(main_frame, bg="#0d0d0d", width=420)
frame_izq.pack(side="left", fill="y", padx=25, pady=20)
frame_izq.pack_propagate(False)

#Configuración del frame con el apartado "Resultado del Prompt" (además de la breve descripción de la aplicación).
frame_der = tk.Frame(main_frame, bg="#0d0d0d", width=420)
frame_der.pack(side="right", fill="both", expand=True, padx=25, pady=20)
frame_der.pack_propagate(False)

# Variables para guardar las opciones seleccionadas por el usuario.
category_var = tk.StringVar()
elemento_var = tk.StringVar()
estilo_var = tk.StringVar()
iluminacion_var = tk.StringVar()
composicion_var = tk.StringVar()

#Configuración básica del panel izquierdo "Opciones de Generación".
tk.Label(
    frame_izq,
    text="Opciones de Generación",
    font=("Segoe UI", 15, "bold"),
    fg="#b19cd9",
    bg="#0d0d0d"
).pack(pady=(0, 15))

#Función para crear los menús desplegables para las opciones dentro del apartado de "Opciones de Generación".
def crear_menu(etiqueta, variable, opciones, comando=None, advertencia=False):
    ttk.Label(frame_izq, text=etiqueta).pack(anchor="w", pady=(5, 0))
    menu = ttk.OptionMenu(frame_izq, variable, "", *opciones, command=comando)
    menu.pack(fill="x", pady=5)
    if advertencia:
        menu.bind("<Button-1>", mostrar_advertencia_elemento)
    return menu

#Creación de cada menú desplegable con la función "crear_menu()" según cada opción.
crear_menu("Categoría:", category_var, elementos_por_category.keys(), update_elements)
elemento_menu = crear_menu("Elemento principal:", elemento_var, [], advertencia=True)
crear_menu("Estilo visual:", estilo_var, estilos_visuales)
crear_menu("Iluminación:", iluminacion_var, iluminaciones)
crear_menu("Composición:", composicion_var, composiciones)

#Configuración de botones para "Generar Prompt" y "Copiar Prompt".
ttk.Button(frame_izq, text="Generar Prompt", command=generar_prompt).pack(fill="x", pady=(20, 5))
ttk.Button(frame_izq, text="Copiar Prompt", command=copiar_prompt).pack(fill="x", pady=5)


#Configuración básica del panel derecho "Resultado del Prompt".
tk.Label(
    frame_der,
    text="Resultado del Prompt",
    font=("Segoe UI", 15, "bold"),
    fg="#b19cd9",
    bg="#0d0d0d"
).pack(pady=(0, 10))

resultado_frame = tk.Frame(frame_der, bg="#161616", bd=2, relief="flat")
resultado_frame.pack(fill="both", expand=True, padx=10, pady=10)

resultado_label = tk.Label(
    resultado_frame,
    text="",
    bg="#161616",
    fg="white",
    wraplength=380,
    justify="left",
    font=("Segoe UI", 12),
    padx=15,
    pady=15
)
resultado_label.pack(fill="both", expand=True)

#Breve descripción de la app.   
descripcion = tk.Label(
    frame_der,
    text="Esta aplicación te permite combinar categorías, estilos y composiciones "
        "para generar prompts coherentes y creativos para modelos de IA visual.",
    bg="#0d0d0d",
    fg="#aaaaaa",
    wraplength=400,
    justify="left",
    font=("Segoe UI", 10, "italic")
)
descripcion.pack(pady=(5, 0))

#Iniciamos el bucle principal de la interfaz gráfica, manteniendo la ventana abierta y 
#gestionando los eventos del usuario hasta que se cierre mediante la función mainloop de Tkinter.
ventana.mainloop()
