import tkinter as tk
from EnzoGame import EnzoGame


class EnzoGUI:
    def __init__(self, root, enzo_path):
        self.root = root
        self.root.geometry("400x620")
        self.root.resizable(False, False)
        self.root.title("Trova Enzo")
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)
        self.root.configure(bg="#f0f0f0")

        # gioco
        self.game = EnzoGame()

        # frame bottoni
        self.buttons_frame = tk.Frame(root, bg="white")
        self.buttons_frame.grid(row=0, column=0, columnspan=4)
        self.create_buttons()

        # immagini
        self.enzo_image_orig = tk.PhotoImage(file=enzo_path)
        self.enzo_image = self.enzo_image_orig.subsample(4,4)
        # placeholder vuoto delle stesse dimensioni
        self.blank_img = tk.PhotoImage(width=self.enzo_image.width(), height=self.enzo_image.height())

        # frame messaggio + immagine
        self.message_frame = tk.Frame(root, bg="white")
        self.message_frame.grid(row=5, column=0, columnspan=4, pady=10)

        # label testo
        self.text_output = tk.Label(
            self.message_frame,
            text="",
            fg="red",
            font=("Helvetica", 14),
            bg="white",
            wraplength=self.enzo_image.width(),  # larghezza massima in pixel
            width=30,  # in caratteri
            height=3  # in righe
        )
        self.text_output.pack()

        # label immagine
        self.image_label = tk.Label(self.message_frame, image=self.blank_img, bg="white")
        self.image_label.pack(pady=5)

        # frame reset
        self.reset_frame = tk.Frame(root, bg="white")
        self.reset_frame.grid(row=6, column=0, columnspan=4, pady=5)
        self.btn_reset = tk.Button(
            self.reset_frame,
            text="Reset",
            bg="#4CAF50",
            fg="white",
            width=10,
            height=3,
            font=("Helvetica", 12, "bold"),
            activebackground="#45a049",
            activeforeground="white",
            command=self.reset_game
        )
        self.btn_reset.grid(row=0, column=0, padx=5)

        # Pulsante Chiudi
        self.btn_chiudi = tk.Button(
            self.reset_frame,
            text="Chiudi",
            bg="#f44336",  # rosso
            fg="white",
            width=10,
            height=3,
            font=("Helvetica", 12, "bold"),
            activebackground="#d32f2f",
            activeforeground="white",
            command=self.close_game  # chiude la finestra
        )
        self.btn_chiudi.grid(row=0, column=1, padx=5)

    def create_buttons(self):
        button_number = 1
        for row in range(4):
            for col in range(4):
                btn = tk.Button(
                    self.buttons_frame,
                    text=str(button_number),
                    width=10,
                    height=3,
                    bg="#2196F3",
                    fg="white",
                    font=("Helvetica", 10, "bold"),
                    activebackground="#1976D2",
                    activeforeground="white",
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                btn.grid(row=row, column=col, padx=5, pady=5)
                button_number += 1


    def on_click(self, row, col):
        found = self.game.check_enzo(row, col)
        if found:
            self.text_output.config(text="Hai Trovato Enzo!")
            self.image_label.config(image=self.enzo_image)
        else:
            self.text_output.config(text="Enzo non trovato, continua a cercare")
            self.image_label.config(image=self.blank_img)

    def reset_game(self):
        self.game.grid = self.game.draw_enzo()
        self.text_output.config(text="")
        self.image_label.config(image=self.blank_img)


    def close_game(self):
        self.game.grid = self.root.destroy()


