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
    nuevos_elements = elements_por_category.get(category, [])
    element_var.set("")
    element_menu["menu"].delete(0, "end")
    for element in new_elements:
        element_menu["menu"].add_command(
            label=element,
            command=lambda value=element: element_var.set(value)
        )

# Function to display a message informing the user that they must first choose a category if they try
# to select a main element without selecting a category.
def mostrar_advertencia_element(event):
    if not category_var.get():
        messagebox.showwarning("Warning", "You must choose a category first.")
        
# Function to construct the prompt based on the selected options.
def generate_prompt():
    category = category_var.get()
    element = element_var.get()
    style = style_var.get()
    lighting = lighting_var.get()
    composition = composition_var.get()

    if not (category and element and style and iluminacion and composicion):
        resultado_label.config(
            text="Complete all options before generating the prompt.",
            fg="#ff5555"
        )
        return

   #Writing adjustments according to the selected options.
    if category == "Anime":
        text_environment = (
            "represented in a clean, expressive, and visually balanced anime style"
        )
    elif category == "Realistic":
        text_environment = (
            "interpreted with a realistic aesthetic, prioritizing natural proportions and authentic detail"
        )
    elif category == "Abstract":
        text_environment = (
            "conceived from an abstract perspective, with expressive forms and conceptual symbolism"
        )
    else:
        text_environment = (
            f"set in a universe of {category.lower()}, with a defined visual identity and aesthetic richness"
        )

    lightning_l = lightning.lower()

    if lightning_l == "sunset":
        light_text = (
            "illuminated by a warm sunset glow that enhances soft shadows"
        )
    elif lightning_l == "natural light":
        light_text = (
            "bathed in balanced natural light that brings clarity and volume"
        )
    elif lightning_l == "neon":
        light_text = (
            "with vibrant neon lighting that creates intense reflections and a modern atmosphere"
        )
    elif lightning_l == "night shift":
        light_text = (
            "set with nighttime lighting that produces marked contrasts and a deep atmosphere"
        )
    elif lightning_l == "dramatic":
        light_text = (
            "with dramatic lighting that emphasizes contrast and visual tension"
        )
    else:
        light_text = (
            f"with {lightning_l} lighting applied harmoniously"
        )
        
    style_text = (
        f"done in style {style.lower()}, with attention to color, shape and composition"
    )

    text_composition = f"following a composition in {composition.lower()}"

    # Professional detail layer to improve prompt quality.
    details = (
        "Include defined textures, atmospheric depth, precise light handling, "
        "chromatic harmony, and a professional finish designed for high-quality results."
    )

    # Final prompt.
    prompt = (
        f"{element} {environment_text}, {lighting_text}, {style_text}, "
        f"{composition_text}. {details}"
    )
    
    resultado_label.config(text=prompt, fg="white")

# Function for the "Copy Prompt" option.
def copy_prompt():
    text = result_label.cget("text")
    if not text:
        messagebox.showinfo("Information", "First generate a prompt to copy it.")
        return
    window.clipboard_clear()
    window.clipboard_append(text)
    messagebox.showinfo("Copied", "Prompt copied to clipboard.")

# Basic interface configuration.
ventana = tk.Tk()
ventana.title("Prompt Generator")
ventana.geometry("1080x670")
ventana.configure(bg="#0d0d0d")
ventana.minsize(960, 580)

# We center the window based on the screen size.
ancho_ventana = 1080
alto_ventana = 670
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
pos_x = int((screen_width / 2) - (window_width / 2))
pos_y = int((screen_height / 2) - (window_height / 2))
ventana.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

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
    text="Prompt Generator",
    font=("Segoe UI", 22, "bold"),
    fg="#b19cd9",
    bg="#0d0d0d"
)
titulo.pack(pady=(15, 10))

# Main frame configuration.
main_frame = tk.Frame(window, bg="#0d0d0d")
main_frame.pack(fill="both", expand=True)

# Configuration of the frame with the "Generation Options" section.
frame_izq = tk.Frame(main_frame, bg="#0d0d0d", width=420)
frame_izq.pack(side="left", fill="y", padx=25, pady=20)
frame_izq.pack_propagate(False)

# Configuration of the frame with the "Prompt Result" section (in addition to the brief application description).
frame_der = tk.Frame(main_frame, bg="#0d0d0d", width=420)
frame_der.pack(side="right", fill="both", expand=True, padx=25, pady=20)
frame_der.pack_propagate(False)

# Variables to store the options selected by the user.
category_var = tk.StringVar()
element_var = tk.StringVar()
style_var = tk.StringVar()
lightning_var = tk.StringVar()
composicion_var = tk.StringVar()

# Basic configuration of the left panel "Generation Options".
tk.Label(
    frame_izq,
    text="Generation Options",
    font=("Segoe UI", 15, "bold"),
    fg="#b19cd9",
    bg="#0d0d0d"
).pack(pady=(0, 15))

# Function to create dropdown menus for the options in the "Generation Options" section.
def create_menu(label, variable, options, command=None, warning=False):
    ttk.Label(left_frame, text=label).pack(anchor="w", pady=(5, 0))
    menu = ttk.OptionMenu(left_frame, variable, "", *options, command=command)
    menu.pack(fill="x", pady=5)
    if warning:
        menu.bind("<Button-1>", show_warning_element)
    return menu

# Creation of each dropdown menu using the "create_menu()" function according to each option.
create_menu("Category:", category_var, elements_by_category.keys(), update_elements)
element_menu = create_menu("Main Element:", element_var, [], warning=True)
create_menu("Visual Style:", style_var, visual_styles)
create_menu("Lighting:", lighting_var, lightings)
create_menu("Composition:", composition_var, compositions)

# Configuration of buttons for "Generate Prompt" and "Copy Prompt".
ttk.Button(frame_izq, text="Generar Prompt", command=generar_prompt).pack(fill="x", pady=(20, 5))
ttk.Button(frame_izq, text="Copiar Prompt", command=copiar_prompt).pack(fill="x", pady=5)


# Basic configuration of the right panel "Prompt Result".
tk.Label(
    right_frame,
    text="Prompt Result",
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

# Brief description of the app.   
description = tk.Label(
    right_frame,
    text="This application allows you to combine categories, styles, and compositions "
         "to generate coherent and creative prompts for visual AI models.",
    bg="#0d0d0d",
    fg="#aaaaaa",
    wraplength=400,
    justify="left",
    font=("Segoe UI", 10, "italic")
)
descripcion.pack(pady=(5, 0))

# We start the main loop of the graphical interface, keeping the window open and
# handling user events until it is closed using Tkinter's mainloop function.
ventana.mainloop()
