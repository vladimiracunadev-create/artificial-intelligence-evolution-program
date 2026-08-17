
from __future__ import annotations

import json
import sys
import tkinter as tk
import webbrowser
from pathlib import Path
from tkinter import ttk


ROOT = Path(__file__).resolve().parents[2]
CATALOG = json.loads((ROOT / "site" / "data" / "catalog.json").read_text(encoding="utf-8"))


class ProgramApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Artificial Intelligence Evolution Program")
        self.geometry("1280x760")
        self.minsize(1040, 620)
        self.configure(bg="#0b1020")

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", rowheight=28, background="#111831", fieldbackground="#111831", foreground="#e8ecff")
        style.configure("Treeview.Heading", background="#171f3b", foreground="#ffffff")

        left = ttk.Frame(self)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=12, pady=12)
        right = tk.Frame(self, bg="#0b1020")
        right.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=12, pady=12)

        self.search_var = tk.StringVar()
        search = ttk.Entry(left, textvariable=self.search_var, width=42)
        search.pack(fill=tk.X, pady=(0, 8))
        search.bind("<KeyRelease>", lambda _event: self.populate())

        # el arbol necesita ancho propio: los titulos de parte y clase se
        # cortaban a la mitad y no habia forma de leerlos enteros
        arbol = tk.Frame(left, bg="#0b1020")
        arbol.pack(fill=tk.BOTH, expand=True)
        self.tree = ttk.Treeview(arbol, show="tree", height=24)
        barra_x = ttk.Scrollbar(arbol, orient=tk.HORIZONTAL, command=self.tree.xview)
        barra_y = ttk.Scrollbar(arbol, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(xscrollcommand=barra_x.set, yscrollcommand=barra_y.set)
        self.tree.column("#0", width=380, minwidth=380, stretch=False)
        barra_y.pack(side=tk.RIGHT, fill=tk.Y)
        barra_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.select_lesson)

        self.title_label = tk.Label(right, text="Selecciona una clase", font=("Segoe UI", 22, "bold"), bg="#0b1020", fg="#ffffff", anchor="w")
        self.title_label.pack(fill=tk.X)
        self.meta_label = tk.Label(right, text="", font=("Segoe UI", 11), bg="#0b1020", fg="#91a7ff", anchor="w")
        self.meta_label.pack(fill=tk.X, pady=(6, 14))
        self.body = tk.Text(right, wrap=tk.WORD, font=("Segoe UI", 11), bg="#111831", fg="#e8ecff", insertbackground="#ffffff", relief=tk.FLAT, padx=18, pady=18)
        self.body.pack(expand=True, fill=tk.BOTH)
        self.body.configure(state=tk.DISABLED)

        buttons = tk.Frame(right, bg="#0b1020")
        buttons.pack(fill=tk.X, pady=(10, 0))
        ttk.Button(buttons, text="Abrir README", command=self.open_readme).pack(side=tk.LEFT)
        ttk.Button(buttons, text="Abrir sitio", command=self.open_site).pack(side=tk.LEFT, padx=8)
        self.selected: dict | None = None
        self.populate()

    def populate(self) -> None:
        query = self.search_var.get().strip().lower()
        self.tree.delete(*self.tree.get_children())
        for part in CATALOG["parts"]:
            matching = [
                lesson for lesson in part["lessons"]
                if not query or query in lesson["title"].lower() or query in " ".join(lesson["keywords"]).lower()
            ]
            if not matching:
                continue
            parent = self.tree.insert("", tk.END, text=f"{part['id']} · {part['title']}", open=bool(query))
            for lesson in matching:
                self.tree.insert(parent, tk.END, iid=f"lesson-{lesson['id']}", text=f"{lesson['id']} · {lesson['title']}")

    def select_lesson(self, _event=None) -> None:
        selection = self.tree.selection()
        if not selection or not selection[0].startswith("lesson-"):
            return
        lesson_id = selection[0].split("-", 1)[1]
        for part in CATALOG["parts"]:
            for lesson in part["lessons"]:
                if lesson["id"] == lesson_id:
                    self.selected = lesson
                    self.title_label.configure(text=f"{lesson['id']} · {lesson['title']}")
                    self.meta_label.configure(text=f"Parte {part['id']} · {part['title']} · laboratorio {lesson['lab_kind']}")
                    body = (
                        "Conceptos\n\n"
                        + " · ".join(lesson["keywords"])
                        + "\n\nPropósito\n\n"
                        + lesson["summary"]
                        + "\n\nRuta local\n\n"
                        + lesson["path"]
                    )
                    self.body.configure(state=tk.NORMAL)
                    self.body.delete("1.0", tk.END)
                    self.body.insert("1.0", body)
                    self.body.configure(state=tk.DISABLED)
                    return

    def open_readme(self) -> None:
        if self.selected:
            webbrowser.open((ROOT / self.selected["path"] / "README.md").as_uri())

    def open_site(self) -> None:
        webbrowser.open((ROOT / "site" / "index.html").as_uri())


if __name__ == "__main__":
    ProgramApp().mainloop()
