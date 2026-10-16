"""
NEXORA — Modern AI Chat Desktop App
Exact-style target:
- Dark glassmorphism desktop UI
- White/Dark theme switch
- Left navigation + recent chats
- Center chat
- Right prompts panel
- Large glass composer
- Keyboard shortcuts
- Gemini API via .env
- Persistent chat history
- Search
- New/Delete/Clear chat
"""

import os
import json
import time
import threading
from datetime import datetime

import customtkinter as ctk
from tkinter import messagebox
from dotenv import load_dotenv
from google import genai


# ============================================================
# CONFIG
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

# Gemini 3.6 Flash is a current stable model.
# You can override it in .env with GEMINI_MODEL=...
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash").strip()

HISTORY_FILE = "chat_history.json"

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing.\n\n"
        "Open your existing .env file and add:\n\n"
        "GEMINI_API_KEY=YOUR_API_KEY"
    )

client = genai.Client(api_key=API_KEY)


# ============================================================
# THEMES
# ============================================================

DARK = {
    "bg": "#070A10",
    "sidebar": "#0B0F17",
    "panel": "#0C111A",
    "card": "#111722",
    "card2": "#151B26",
    "input": "#111722",
    "border": "#242D3A",
    "border2": "#303B4B",
    "text": "#F5F7FB",
    "muted": "#9AA4B4",
    "subtle": "#687386",
    "hover": "#171F2D",
    "selected": "#191633",
    "accent": "#725BFF",
    "accent2": "#9B6CFF",
    "user": "#4C3DD4",
    "user2": "#624CEB",
    "assistant": "#121821",
    "code": "#080B10",
    "success": "#36D399",
    "danger": "#F87171",
}

LIGHT = {
    "bg": "#F5F7FB",
    "sidebar": "#FFFFFF",
    "panel": "#FFFFFF",
    "card": "#FFFFFF",
    "card2": "#F7F9FD",
    "input": "#FFFFFF",
    "border": "#E1E6EF",
    "border2": "#CDD5E2",
    "text": "#171A21",
    "muted": "#6E7787",
    "subtle": "#9AA3B2",
    "hover": "#F0F3F8",
    "selected": "#EEF0FF",
    "accent": "#5D4FE8",
    "accent2": "#7B61FF",
    "user": "#6556E9",
    "user2": "#7B61FF",
    "assistant": "#FFFFFF",
    "code": "#F3F5F8",
    "success": "#20A36A",
    "danger": "#D94E5F",
}

dark_mode = True
C = DARK


# ============================================================
# DATA
# ============================================================

chats = {}
current_chat_id = None
current_page = "AI Chat"


def save_history():
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(chats, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("History save error:", e)


def load_history():
    global chats

    if not os.path.exists(HISTORY_FILE):
        chats = {}
        return

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            chats = json.load(f)
    except Exception:
        chats = {}


def now_text():
    return datetime.now().strftime("%I:%M %p").lstrip("0")


# ============================================================
# APP
# ============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Nexora — AI Chat")
app.geometry("1500x900")
app.minsize(1120, 720)
app.configure(fg_color=C["bg"])


# ============================================================
# HELPERS
# ============================================================

def glass_frame(parent, **kwargs):
    defaults = {
        "fg_color": C["card"],
        "corner_radius": 16,
        "border_width": 1,
        "border_color": C["border"],
    }
    defaults.update(kwargs)
    return ctk.CTkFrame(parent, **defaults)


def clear_widget(parent):
    for child in parent.winfo_children():
        child.destroy()


def safe_after(ms, fn):
    try:
        if app.winfo_exists():
            app.after(ms, fn)
    except Exception:
        pass


# ============================================================
# ROOT LAYOUT
# ============================================================

root = ctk.CTkFrame(
    app,
    fg_color=C["bg"],
    corner_radius=0
)
root.pack(fill="both", expand=True)


# ============================================================
# LEFT SIDEBAR
# ============================================================

sidebar = ctk.CTkFrame(
    root,
    width=300,
    fg_color=C["sidebar"],
    corner_radius=0,
    border_width=1,
    border_color=C["border"]
)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)


brand = ctk.CTkFrame(
    sidebar,
    height=70,
    fg_color="transparent"
)
brand.pack(fill="x", padx=18, pady=(10, 0))
brand.pack_propagate(False)

ctk.CTkLabel(
    brand,
    text="✦",
    font=("Segoe UI", 27, "bold"),
    text_color=C["accent2"]
).pack(side="left", padx=(2, 8))

ctk.CTkLabel(
    brand,
    text="Nexora",
    font=("Segoe UI", 23, "bold"),
    text_color=C["text"]
).pack(side="left")


# Search
search_entry = ctk.CTkEntry(
    sidebar,
    height=42,
    corner_radius=12,
    border_width=1,
    border_color=C["border"],
    fg_color=C["input"],
    text_color=C["text"],
    placeholder_text="⌕  Search chats",
    placeholder_text_color=C["muted"],
    font=("Segoe UI", 11)
)
search_entry.pack(fill="x", padx=18, pady=(3, 14))


# Navigation
nav_buttons = {}


def set_nav_style():
    for name, button in nav_buttons.items():
        selected = name == current_page
        button.configure(
            fg_color=C["selected"] if selected else "transparent",
            text_color=C["text"] if selected else C["muted"],
            hover_color=C["hover"]
        )


def show_page(name):
    global current_page
    current_page = name
    set_nav_style()

    if name == "AI Chat":
        show_chat_page()
    elif name == "History":
        show_history_page()
    elif name == "Settings":
        show_settings_page()
    elif name == "Help & Support":
        show_help_page()
    else:
        show_simple_page(name)


def add_nav(name, icon):
    button = ctk.CTkButton(
        sidebar,
        text=f"{icon}   {name}",
        height=43,
        corner_radius=11,
        anchor="w",
        fg_color=C["selected"] if name == "AI Chat" else "transparent",
        hover_color=C["hover"],
        text_color=C["text"] if name == "AI Chat" else C["muted"],
        font=("Segoe UI", 13),
        command=lambda n=name: show_page(n)
    )
    button.pack(fill="x", padx=12, pady=2)
    nav_buttons[name] = button


add_nav("AI Chat", "●")
add_nav("Projects", "□")
add_nav("Templates", "▣")
add_nav("Documents", "▤")
add_nav("Community", "♧")
add_nav("History", "◷")


ctk.CTkLabel(
    sidebar,
    text="",
    height=8
).pack()


ctk.CTkLabel(
    sidebar,
    text="Settings & Help",
    font=("Segoe UI", 10, "bold"),
    text_color=C["subtle"]
).pack(anchor="w", padx=22, pady=(8, 5))

add_nav("Settings", "⚙")
add_nav("Help & Support", "?")


# Recent chats section
ctk.CTkLabel(
    sidebar,
    text="Recent Chats",
    font=("Segoe UI", 11, "bold"),
    text_color=C["text"]
).pack(anchor="w", padx=22, pady=(18, 6))


recent_area = ctk.CTkScrollableFrame(
    sidebar,
    height=230,
    fg_color="transparent",
    scrollbar_button_color=C["border"]
)
recent_area.pack(fill="x", padx=10)


def refresh_recent():
    clear_widget(recent_area)

    items = list(chats.items())[-8:][::-1]

    for cid, data in items:
        title = data.get("title", "New Chat")
        if len(title) > 28:
            title = title[:28] + "..."

        row = ctk.CTkFrame(
            recent_area,
            fg_color=C["card2"] if cid == current_chat_id else "transparent",
            corner_radius=10
        )
        row.pack(fill="x", pady=2)

        ctk.CTkButton(
            row,
            text="▱  " + title,
            height=40,
            anchor="w",
            corner_radius=10,
            fg_color="transparent",
            hover_color=C["hover"],
            text_color=C["text"],
            font=("Segoe UI", 10),
            command=lambda x=cid: open_chat(x)
        ).pack(side="left", fill="x", expand=True)

        ctk.CTkButton(
            row,
            text="⋮",
            width=28,
            height=32,
            corner_radius=8,
            fg_color="transparent",
            hover_color=C["hover"],
            text_color=C["muted"],
            command=lambda x=cid: delete_chat(x)
        ).pack(side="right", padx=3)


# Bottom user profile
sidebar_spacer = ctk.CTkFrame(sidebar, fg_color="transparent")
sidebar_spacer.pack(fill="both", expand=True)

profile = glass_frame(
    sidebar,
    fg_color=C["card"],
    corner_radius=14
)
profile.pack(fill="x", padx=14, pady=14)

ctk.CTkLabel(
    profile,
    text="N",
    width=40,
    height=40,
    corner_radius=20,
    fg_color=C["selected"],
    text_color=C["accent2"],
    font=("Segoe UI", 16, "bold")
).pack(side="left", padx=10, pady=9)

profile_text = ctk.CTkFrame(profile, fg_color="transparent")
profile_text.pack(side="left")

ctk.CTkLabel(
    profile_text,
    text="Nexora User",
    font=("Segoe UI", 11, "bold"),
    text_color=C["text"]
).pack(anchor="w")

ctk.CTkLabel(
    profile_text,
    text="Personal workspace",
    font=("Segoe UI", 9),
    text_color=C["muted"]
).pack(anchor="w")


# ============================================================
# MAIN AREA
# ============================================================

main = ctk.CTkFrame(
    root,
    fg_color=C["bg"],
    corner_radius=0
)
main.pack(side="left", fill="both", expand=True)


# Top bar
topbar = ctk.CTkFrame(
    main,
    height=76,
    fg_color=C["panel"],
    corner_radius=0,
    border_width=1,
    border_color=C["border"]
)
topbar.pack(fill="x")
topbar.pack_propagate(False)


top_title = ctk.CTkLabel(
    topbar,
    text="AI Chat",
    font=("Segoe UI", 18, "bold"),
    text_color=C["text"]
)
top_title.pack(side="left", padx=25)


# Search shortcut button
def focus_search():
    search_entry.focus()
    search_entry.select_range(0, "end")


ctk.CTkButton(
    topbar,
    text="⌕   Search    Ctrl K",
    width=150,
    height=38,
    corner_radius=11,
    fg_color=C["card"],
    hover_color=C["hover"],
    border_width=1,
    border_color=C["border"],
    text_color=C["muted"],
    font=("Segoe UI", 10),
    command=focus_search
).pack(side="right", padx=8)


def toggle_theme():
    global dark_mode, C

    dark_mode = not dark_mode
    C = DARK if dark_mode else LIGHT

    apply_theme()


theme_button = ctk.CTkButton(
    topbar,
    text="☾",
    width=44,
    height=38,
    corner_radius=11,
    fg_color=C["card"],
    hover_color=C["hover"],
    border_width=1,
    border_color=C["border"],
    text_color=C["text"],
    font=("Segoe UI", 17),
    command=toggle_theme
)
theme_button.pack(side="right", padx=5)


def new_chat():
    global current_chat_id

    current_chat_id = str(time.time())

    chats[current_chat_id] = {
        "title": "New Chat",
        "created": now_text(),
        "messages": []
    }

    save_history()
    refresh_recent()
    show_chat_page()
    composer_entry.focus()


ctk.CTkButton(
    topbar,
    text="＋  New Chat",
    width=125,
    height=38,
    corner_radius=11,
    fg_color=C["accent"],
    hover_color=C["accent2"],
    text_color="#FFFFFF",
    font=("Segoe UI", 11, "bold"),
    command=new_chat
).pack(side="right", padx=8)


# ============================================================
# CENTER + RIGHT CONTENT
# ============================================================

workspace = ctk.CTkFrame(
    main,
    fg_color=C["bg"]
)
workspace.pack(fill="both", expand=True)

# Center chat
center = ctk.CTkFrame(
    workspace,
    fg_color=C["panel"],
    corner_radius=0
)
center.pack(side="left", fill="both", expand=True)


# Right prompts
right = ctk.CTkFrame(
    workspace,
    width=285,
    fg_color=C["sidebar"],
    corner_radius=0,
    border_width=1,
    border_color=C["border"]
)
right.pack(side="right", fill="y")
right.pack_propagate(False)


# Chat header
chat_header = ctk.CTkFrame(
    center,
    height=72,
    fg_color=C["panel"],
    corner_radius=0,
    border_width=1,
    border_color=C["border"]
)
chat_header.pack(fill="x")
chat_header.pack_propagate(False)

ctk.CTkLabel(
    chat_header,
    text="✦",
    width=42,
    height=42,
    corner_radius=21,
    fg_color=C["selected"],
    text_color=C["accent2"],
    font=("Segoe UI", 20, "bold")
).pack(side="left", padx=(22, 10), pady=14)

chat_identity = ctk.CTkFrame(
    chat_header,
    fg_color="transparent"
)
chat_identity.pack(side="left")

ctk.CTkLabel(
    chat_identity,
    text="Nexora",
    font=("Segoe UI", 14, "bold"),
    text_color=C["text"]
).pack(anchor="w")

status_label = ctk.CTkLabel(
    chat_identity,
    text="● Online",
    font=("Segoe UI", 9),
    text_color=C["success"]
)
status_label.pack(anchor="w")


# ============================================================
# MESSAGE AREA
# ============================================================

message_area = ctk.CTkScrollableFrame(
    center,
    fg_color=C["panel"],
    scrollbar_button_color=C["border"],
    scrollbar_button_hover_color=C["border2"]
)
message_area.pack(fill="both", expand=True, padx=12, pady=5)


def scroll_bottom():
    try:
        message_area._parent_canvas.yview_moveto(1.0)
    except Exception:
        pass


def add_message(role, text, timestamp=None):
    row = ctk.CTkFrame(
        message_area,
        fg_color="transparent"
    )
    row.pack(fill="x", pady=7, padx=7)

    if role == "user":
        bubble = ctk.CTkFrame(
            row,
            fg_color=C["user"],
            corner_radius=17,
            border_width=1,
            border_color=C["accent2"]
        )
        bubble.pack(side="right", padx=(150, 5))

        ctk.CTkLabel(
            bubble,
            text=text,
            font=("Segoe UI", 15),
            text_color="#FFFFFF",
            justify="left",
            wraplength=620
        ).pack(padx=17, pady=(13, 5))

        ctk.CTkLabel(
            bubble,
            text=f"{timestamp or now_text()}  ✓✓",
            font=("Segoe UI", 8),
            text_color="#DDD9FF"
        ).pack(anchor="e", padx=15, pady=(0, 10))

    else:
        avatar = ctk.CTkLabel(
            row,
            text="✦",
            width=38,
            height=38,
            corner_radius=19,
            fg_color=C["selected"],
            text_color=C["accent2"],
            font=("Segoe UI", 17, "bold")
        )
        avatar.pack(side="left", padx=(5, 9), anchor="n")

        bubble = ctk.CTkFrame(
            row,
            fg_color=C["assistant"],
            corner_radius=17,
            border_width=1,
            border_color=C["border"]
        )
        bubble.pack(side="left", padx=(0, 100))

        ctk.CTkLabel(
            bubble,
            text=text,
            font=("Segoe UI", 15),
            text_color=C["text"],
            justify="left",
            wraplength=680
        ).pack(padx=18, pady=(14, 5))

        ctk.CTkLabel(
            bubble,
            text=timestamp or now_text(),
            font=("Segoe UI", 8),
            text_color=C["muted"]
        ).pack(anchor="w", padx=18, pady=(0, 7))

        actions = ctk.CTkFrame(
            bubble,
            fg_color="transparent"
        )
        actions.pack(anchor="w", padx=10, pady=(0, 8))

        for icon in ["□", "♡", "⌁", "↻"]:
            ctk.CTkButton(
                actions,
                text=icon,
                width=27,
                height=25,
                corner_radius=7,
                fg_color="transparent",
                hover_color=C["hover"],
                text_color=C["muted"],
                font=("Segoe UI", 11)
            ).pack(side="left", padx=1)

    safe_after(80, scroll_bottom)


# ============================================================
# WELCOME
# ============================================================

def show_welcome():
    clear_widget(message_area)

    box = ctk.CTkFrame(
        message_area,
        fg_color="transparent"
    )
    box.pack(fill="both", expand=True, pady=90)

    ctk.CTkLabel(
        box,
        text="✦",
        width=70,
        height=70,
        corner_radius=35,
        fg_color=C["selected"],
        text_color=C["accent2"],
        font=("Segoe UI", 34, "bold")
    ).pack(pady=(10, 18))

    ctk.CTkLabel(
        box,
        text="Welcome to Nexora",
        font=("Segoe UI", 29, "bold"),
        text_color=C["text"]
    ).pack()

    ctk.CTkLabel(
        box,
        text="Your personal AI workspace",
        font=("Segoe UI", 13),
        text_color=C["muted"]
    ).pack(pady=(8, 25))

    quick = ctk.CTkFrame(box, fg_color="transparent")
    quick.pack()

    for title, prompt in [
        ("Write copy", "Write a professional paragraph about artificial intelligence."),
        ("Explain simply", "Explain computer networks in very simple terms."),
        ("Help with code", "Help me write a Python program."),
        ("Give project ideas", "Give me five AI project ideas for a CSE student."),
    ]:
        ctk.CTkButton(
            quick,
            text=title,
            width=180,
            height=44,
            corner_radius=12,
            fg_color=C["card"],
            hover_color=C["hover"],
            border_width=1,
            border_color=C["border"],
            text_color=C["text"],
            font=("Segoe UI", 10),
            command=lambda p=prompt: quick_prompt(p)
        ).pack(side="left", padx=5)


# ============================================================
# RIGHT PROMPTS PANEL
# ============================================================

ctk.CTkLabel(
    right,
    text="Prompts",
    font=("Segoe UI", 16, "bold"),
    text_color=C["text"]
).pack(anchor="w", padx=18, pady=(21, 2))

ctk.CTkLabel(
    right,
    text="Quick actions",
    font=("Segoe UI", 9),
    text_color=C["muted"]
).pack(anchor="w", padx=18, pady=(0, 12))


def prompt_button(title, subtitle, prompt, icon):
    card = ctk.CTkFrame(
        right,
        fg_color=C["card"],
        corner_radius=13,
        border_width=1,
        border_color=C["border"]
    )
    card.pack(fill="x", padx=12, pady=5)

    ctk.CTkButton(
        card,
        text=icon,
        width=38,
        height=38,
        corner_radius=10,
        fg_color=C["selected"],
        hover_color=C["hover"],
        text_color=C["accent2"],
        font=("Segoe UI", 15, "bold"),
        command=lambda p=prompt: quick_prompt(p)
    ).pack(side="left", padx=9, pady=9)

    text_frame = ctk.CTkFrame(card, fg_color="transparent")
    text_frame.pack(side="left", fill="x", expand=True, pady=8)

    ctk.CTkLabel(
        text_frame,
        text=title,
        font=("Segoe UI", 10, "bold"),
        text_color=C["text"],
        anchor="w"
    ).pack(fill="x")

    ctk.CTkLabel(
        text_frame,
        text=subtitle,
        font=("Segoe UI", 8),
        text_color=C["muted"],
        anchor="w"
    ).pack(fill="x")


PROMPTS = [
    ("Summarize this topic", "Get a short summary",
     "Summarize the topic I give you clearly.", "▤"),
    ("Explain in simple terms", "Easy to understand",
     "Explain the topic I give you in very simple terms with an example.", "▣"),
    ("Write an essay", "Well-structured essay",
     "Write a well-structured essay about the topic I give you.", "✎"),
    ("Correct this code", "Find and fix errors",
     "Help me debug and correct this code:", "</>"),
    ("Give me project ideas", "Creative suggestions",
     "Give me five creative project ideas.", "◇"),
    ("Improve my paragraph", "Enhance writing quality",
     "Improve this paragraph professionally:", "▤"),
    ("Make a presentation", "Presentation outline",
     "Create a presentation outline for this topic:", "▦"),
    ("Explain step by step", "Detailed guide",
     "Explain this step by step:", "↳"),
]

for p in PROMPTS:
    prompt_button(*p)


# ============================================================
# COMPOSER
# ============================================================

composer = ctk.CTkFrame(
    center,
    height=122,
    fg_color=C["input"],
    corner_radius=20,
    border_width=1,
    border_color=C["accent"]
)
composer.pack(fill="x", padx=20, pady=(8, 5))
composer.pack_propagate(False)

# Glass inner highlight
ctk.CTkFrame(
    composer,
    height=2,
    fg_color=C["accent2"],
    corner_radius=2
).place(relx=0.06, rely=0.02, relwidth=0.88)


composer_entry = ctk.CTkEntry(
    composer,
    height=48,
    border_width=0,
    fg_color=C["input"],
    text_color=C["text"],
    placeholder_text="Ask Nexora anything...",
    placeholder_text_color=C["muted"],
    font=("Segoe UI", 16)
)
composer_entry.pack(
    fill="x",
    padx=18,
    pady=(10, 0)
)


def send_message():
    global current_chat_id

    question = composer_entry.get().strip()

    if not question:
        return

    if current_chat_id is None:
        new_chat()

    if not chats[current_chat_id]["messages"]:
        chats[current_chat_id]["title"] = question[:30]

    timestamp = now_text()

    chats[current_chat_id]["messages"].append({
        "role": "user",
        "content": question,
        "time": timestamp
    })

    save_history()
    refresh_recent()

    # Always return to AI Chat when sending.
    show_chat_page()

    composer_entry.delete(0, "end")

    send_button.configure(
        state="disabled",
        text="..."
    )

    status_label.configure(
        text="● Thinking...",
        text_color=C["accent2"]
    )

    chat_id = current_chat_id

    threading.Thread(
        target=generate_response,
        args=(chat_id,),
        daemon=True
    ).start()


composer_entry.bind(
    "<Return>",
    lambda event: send_message()
)


# Composer tool bar
tools = ctk.CTkFrame(
    composer,
    fg_color="transparent"
)
tools.pack(side="left", padx=12, pady=5)


for label in ["＋", "⌕ Search", "◎ Reasoning", "▧ Create Image", "</> Code", "••• More"]:
    ctk.CTkButton(
        tools,
        text=label,
        height=32,
        width=58 if label == "＋" else 95,
        corner_radius=9,
        fg_color=C["card2"],
        hover_color=C["hover"],
        border_width=1,
        border_color=C["border"],
        text_color=C["muted"],
        font=("Segoe UI", 9),
        command=(
            focus_search if label == "⌕ Search"
            else lambda: None
        )
    ).pack(side="left", padx=3)


send_button = ctk.CTkButton(
    composer,
    text="➤",
    width=48,
    height=44,
    corner_radius=15,
    fg_color=C["accent"],
    hover_color=C["accent2"],
    text_color="#FFFFFF",
    font=("Segoe UI", 19, "bold"),
    command=send_message
)
send_button.pack(side="right", padx=14, pady=5)


ctk.CTkLabel(
    center,
    text="Nexora can make mistakes. Check important information.",
    font=("Segoe UI", 9),
    text_color=C["subtle"]
).pack(pady=(0, 7))


# ============================================================
# CHAT FUNCTIONS
# ============================================================

def open_chat(chat_id):
    global current_chat_id

    current_chat_id = chat_id
    current_page = "AI Chat"

    show_chat_page()
    refresh_recent()


def delete_chat(chat_id):
    global current_chat_id

    if not messagebox.askyesno(
        "Delete chat",
        "Delete this conversation permanently?"
    ):
        return

    chats.pop(chat_id, None)
    save_history()

    if current_chat_id == chat_id:
        current_chat_id = None

    refresh_recent()
    show_chat_page()


def clear_history():
    global chats, current_chat_id

    if not chats:
        return

    if not messagebox.askyesno(
        "Clear history",
        "Delete all saved conversations?"
    ):
        return

    chats = {}
    current_chat_id = None
    save_history()

    show_chat_page()
    refresh_recent()


def show_chat_page():
    global current_page

    current_page = "AI Chat"
    top_title.configure(text="AI Chat")
    set_nav_style()

    clear_widget(message_area)

    if current_chat_id is None or current_chat_id not in chats:
        show_welcome()
        status_label.configure(
            text="● Online",
            text_color=C["success"]
        )
        return

    messages = chats[current_chat_id].get("messages", [])

    if not messages:
        show_welcome()
        return

    for msg in messages:
        add_message(
            msg["role"],
            msg["content"],
            msg.get("time")
        )

    safe_after(100, scroll_bottom)


# ============================================================
# SEARCH
# ============================================================

def search_chats(event=None):
    query = search_entry.get().strip().lower()

    if not query:
        refresh_recent()
        return

    clear_widget(recent_area)

    found = []

    for cid, data in chats.items():
        title = data.get("title", "").lower()
        body = " ".join(
            m.get("content", "").lower()
            for m in data.get("messages", [])
        )

        if query in title or query in body:
            found.append((cid, data))

    for cid, data in reversed(found):
        title = data.get("title", "New Chat")

        ctk.CTkButton(
            recent_area,
            text="▱  " + title[:28],
            height=38,
            corner_radius=9,
            anchor="w",
            fg_color=C["selected"],
            hover_color=C["hover"],
            text_color=C["text"],
            font=("Segoe UI", 10),
            command=lambda x=cid: open_chat(x)
        ).pack(fill="x", pady=2)


search_entry.bind("<Return>", search_chats)


# ============================================================
# NAVIGATION PAGES
# ============================================================

def show_history_page():
    global current_page

    current_page = "History"
    top_title.configure(text="Chat History")
    set_nav_style()
    clear_widget(message_area)

    wrapper = ctk.CTkFrame(
        message_area,
        fg_color="transparent"
    )
    wrapper.pack(fill="both", expand=True, padx=30, pady=30)

    ctk.CTkLabel(
        wrapper,
        text="Chat History",
        font=("Segoe UI", 27, "bold"),
        text_color=C["text"]
    ).pack(anchor="w")

    ctk.CTkLabel(
        wrapper,
        text="All your saved Nexora conversations",
        font=("Segoe UI", 12),
        text_color=C["muted"]
    ).pack(anchor="w", pady=(5, 22))

    if not chats:
        ctk.CTkLabel(
            wrapper,
            text="No conversations yet.",
            font=("Segoe UI", 13),
            text_color=C["muted"]
        ).pack(pady=40)
        return

    for cid, data in reversed(list(chats.items())):
        card = glass_frame(wrapper)
        card.pack(fill="x", pady=5)

        ctk.CTkButton(
            card,
            text=data.get("title", "New Chat"),
            height=50,
            anchor="w",
            fg_color="transparent",
            hover_color=C["hover"],
            text_color=C["text"],
            font=("Segoe UI", 12),
            command=lambda x=cid: open_chat(x)
        ).pack(side="left", fill="x", expand=True, padx=5)

        ctk.CTkButton(
            card,
            text="Delete",
            width=70,
            height=32,
            corner_radius=9,
            fg_color=C["card2"],
            hover_color=C["danger"],
            text_color=C["danger"],
            command=lambda x=cid: delete_chat(x)
        ).pack(side="right", padx=10)


def show_settings_page():
    global current_page

    current_page = "Settings"
    top_title.configure(text="Settings")
    set_nav_style()
    clear_widget(message_area)

    wrapper = ctk.CTkFrame(
        message_area,
        fg_color="transparent"
    )
    wrapper.pack(fill="both", expand=True, padx=35, pady=35)

    ctk.CTkLabel(
        wrapper,
        text="Settings",
        font=("Segoe UI", 27, "bold"),
        text_color=C["text"]
    ).pack(anchor="w")

    ctk.CTkLabel(
        wrapper,
        text="Customize Nexora",
        font=("Segoe UI", 12),
        text_color=C["muted"]
    ).pack(anchor="w", pady=(5, 20))

    appearance = glass_frame(wrapper)
    appearance.pack(fill="x", pady=7)

    ctk.CTkLabel(
        appearance,
        text="Appearance",
        font=("Segoe UI", 13, "bold"),
        text_color=C["text"]
    ).pack(side="left", padx=18, pady=18)

    ctk.CTkButton(
        appearance,
        text="☀ Light" if dark_mode else "☾ Dark",
        width=110,
        height=36,
        corner_radius=10,
        fg_color=C["accent"],
        hover_color=C["accent2"],
        text_color="#FFFFFF",
        command=toggle_theme
    ).pack(side="right", padx=15)

    api = glass_frame(wrapper)
    api.pack(fill="x", pady=7)

    ctk.CTkLabel(
        api,
        text="Gemini API",
        font=("Segoe UI", 13, "bold"),
        text_color=C["text"]
    ).pack(side="left", padx=18, pady=18)

    ctk.CTkLabel(
        api,
        text=f"Model: {MODEL}",
        font=("Segoe UI", 10),
        text_color=C["success"]
    ).pack(side="right", padx=18)

    shortcuts = glass_frame(wrapper)
    shortcuts.pack(fill="x", pady=7)

    ctk.CTkLabel(
        shortcuts,
        text="Keyboard shortcuts",
        font=("Segoe UI", 13, "bold"),
        text_color=C["text"]
    ).pack(anchor="w", padx=18, pady=(15, 8))

    for text in [
        "Enter  →  Send message",
        "Ctrl + N  →  New chat",
        "Ctrl + K  →  Search",
        "Ctrl + L  →  Focus message box",
        "Ctrl + Shift + D  →  Toggle theme",
        "Esc  →  Focus message box",
    ]:
        ctk.CTkLabel(
            shortcuts,
            text="•  " + text,
            font=("Segoe UI", 10),
            text_color=C["muted"]
        ).pack(anchor="w", padx=20, pady=3)

    ctk.CTkButton(
        shortcuts,
        text="🗑  Clear All Chat History",
        height=38,
        corner_radius=10,
        fg_color=C["card2"],
        hover_color=C["danger"],
        text_color=C["danger"],
        command=clear_history
    ).pack(anchor="w", padx=18, pady=15)


def show_help_page():
    global current_page

    current_page = "Help & Support"
    top_title.configure(text="Help & Support")
    set_nav_style()
    clear_widget(message_area)

    wrapper = ctk.CTkFrame(
        message_area,
        fg_color="transparent"
    )
    wrapper.pack(fill="both", expand=True, padx=35, pady=35)

    ctk.CTkLabel(
        wrapper,
        text="Help & Support",
        font=("Segoe UI", 27, "bold"),
        text_color=C["text"]
    ).pack(anchor="w")

    for title, description in [
        ("How to chat", "Type your question in the composer and press Enter."),
        ("New conversation", "Click New Chat or press Ctrl + N."),
        ("Search", "Press Ctrl + K or click Search in the top bar."),
        ("Theme", "Click the moon/sun button to switch between Dark and Light."),
        ("History", "Your conversations are stored locally in chat_history.json."),
        ("Gemini API", "Your API key stays in your existing .env file."),
    ]:
        card = glass_frame(wrapper)
        card.pack(fill="x", pady=5)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 12, "bold"),
            text_color=C["text"]
        ).pack(anchor="w", padx=18, pady=(12, 3))

        ctk.CTkLabel(
            card,
            text=description,
            font=("Segoe UI", 10),
            text_color=C["muted"]
        ).pack(anchor="w", padx=18, pady=(0, 12))


def show_simple_page(name):
    global current_page

    current_page = name
    top_title.configure(text=name)
    set_nav_style()
    clear_widget(message_area)

    wrapper = ctk.CTkFrame(
        message_area,
        fg_color="transparent"
    )
    wrapper.pack(fill="both", expand=True, padx=35, pady=45)

    ctk.CTkLabel(
        wrapper,
        text="✦",
        font=("Segoe UI", 35, "bold"),
        text_color=C["accent2"]
    ).pack()

    ctk.CTkLabel(
        wrapper,
        text=name,
        font=("Segoe UI", 28, "bold"),
        text_color=C["text"]
    ).pack(pady=8)

    ctk.CTkLabel(
        wrapper,
        text=f"{name} workspace is ready.",
        font=("Segoe UI", 13),
        text_color=C["muted"]
    ).pack()

    ctk.CTkButton(
        wrapper,
        text="Ask Nexora",
        width=150,
        height=42,
        corner_radius=12,
        fg_color=C["accent"],
        hover_color=C["accent2"],
        command=lambda: show_page("AI Chat")
    ).pack(pady=25)


# ============================================================
# QUICK PROMPTS
# ============================================================

def quick_prompt(prompt):
    show_chat_page()
    composer_entry.delete(0, "end")
    composer_entry.insert(0, prompt)
    composer_entry.focus()


# ============================================================
# GEMINI
# ============================================================

def generate_response(chat_id):
    try:
        history = chats[chat_id]["messages"]

        conversation = []

        for msg in history:
            role = "User" if msg["role"] == "user" else "Assistant"
            conversation.append(
                f"{role}: {msg['content']}"
            )

        prompt = (
            "You are Nexora, a helpful desktop AI assistant. "
            "Give clear, accurate and friendly answers. "
            "Use headings and bullet points when useful.\n\n"
            + "\n".join(conversation)
        )

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        answer = response.text.strip()

        if not answer:
            answer = "I couldn't generate a response."

    except Exception as e:
        error = str(e)

        if "429" in error or "RESOURCE_EXHAUSTED" in error:
            answer = (
                "⚠ Gemini API rate limit/quota reached.\n\n"
                "Please wait a little and try again."
            )
        elif "404" in error or "NOT_FOUND" in error:
            answer = (
                "⚠ Gemini model was not found.\n\n"
                f"Current model: {MODEL}\n\n"
                "Set this in your existing .env file:\n"
                "GEMINI_MODEL=gemini-3.6-flash"
            )
        else:
            answer = "⚠ Nexora API error:\n\n" + error

    safe_after(
        0,
        lambda: receive_response(chat_id, answer)
    )


def receive_response(chat_id, answer):
    if chat_id not in chats:
        return

    chats[chat_id]["messages"].append({
        "role": "assistant",
        "content": answer,
        "time": now_text()
    })

    save_history()

    if chat_id == current_chat_id:
        add_message(
            "assistant",
            answer,
            now_text()
        )

        status_label.configure(
            text="● Online",
            text_color=C["success"]
        )

    send_button.configure(
        state="normal",
        text="➤"
    )

    refresh_recent()


# ============================================================
# THEME
# ============================================================

def apply_theme():
    """Apply the selected palette to ALL existing widgets.

    The previous version only recolored a few containers, which left
    old black buttons/cards behind after switching to Light mode.
    This version walks the complete widget tree and refreshes every
    CustomTkinter widget.
    """
    global C
    C = DARK if dark_mode else LIGHT

    app.configure(fg_color=C["bg"])

    def repaint(parent):
        for widget in parent.winfo_children():
            try:
                cls = widget.__class__.__name__

                if cls in ("CTkFrame", "CTkScrollableFrame"):
                    # Preserve the special composer accent; everything else
                    # gets the correct light/dark surface.
                    try:
                        current_border = widget.cget("border_color")
                    except Exception:
                        current_border = None

                    if widget is composer:
                        widget.configure(
                            fg_color=C["input"],
                            border_color=C["accent"]
                        )
                    elif widget in (sidebar, right):
                        widget.configure(
                            fg_color=C["sidebar"],
                            border_color=C["border"]
                        )
                    elif widget in (main, workspace, center, message_area, chat_header):
                        widget.configure(
                            fg_color=C["panel"],
                            border_color=C["border"]
                        )
                    elif current_border is not None:
                        widget.configure(
                            fg_color=C["surface"],
                            border_color=C["border"]
                        )

                elif cls == "CTkEntry":
                    widget.configure(
                        fg_color=C["input"],
                        text_color=C["text"],
                        placeholder_text_color=C["muted"],
                        border_color=C["border"]
                    )

                elif cls == "CTkButton":
                    text = str(widget.cget("text"))

                    if "New Chat" in text:
                        widget.configure(
                            fg_color=C["accent"],
                            hover_color=C["accent2"],
                            text_color="#FFFFFF",
                            border_color=C["accent"]
                        )
                    elif text == "➤" or text == "...":
                        widget.configure(
                            fg_color=C["accent"],
                            hover_color=C["accent2"],
                            text_color="#FFFFFF"
                        )
                    elif "Search" in text and "Ctrl K" in text:
                        widget.configure(
                            fg_color=C["surface"],
                            hover_color=C["hover"],
                            text_color=C["muted"],
                            border_color=C["border"]
                        )
                    elif text in ("☾", "☀"):
                        widget.configure(
                            fg_color=C["surface"],
                            hover_color=C["hover"],
                            text_color=C["text"],
                            border_color=C["border"]
                        )
                    elif text in ("□", "♡", "⌁", "↻", "⋮"):
                        widget.configure(
                            fg_color="transparent",
                            hover_color=C["hover"],
                            text_color=C["muted"]
                        )
                    else:
                        widget.configure(
                            hover_color=C["hover"],
                            text_color=C["text"]
                        )

                elif cls == "CTkLabel":
                    # Don't overwrite status green, accent icons or white
                    # text in user bubbles.
                    try:
                        old = str(widget.cget("text_color"))
                    except Exception:
                        old = ""

                    if old.lower() in ("#36d399", "#19a66b"):
                        widget.configure(text_color=C["success"])
                    elif old.lower() in ("#ffffff", "#e5e1ff", "#ddd9ff"):
                        # Keep intentionally white user-bubble labels.
                        pass
                    elif "✦" in str(widget.cget("text")):
                        widget.configure(text_color=C["accent2"])
                    else:
                        widget.configure(text_color=C["text"])

                repaint(widget)

            except Exception:
                # One widget failing should never break theme switching.
                try:
                    repaint(widget)
                except Exception:
                    pass

    # Main surfaces first.
    root.configure(fg_color=C["bg"])
    sidebar.configure(fg_color=C["sidebar"], border_color=C["border"])
    main.configure(fg_color=C["bg"])
    workspace.configure(fg_color=C["bg"])
    center.configure(fg_color=C["panel"])
    right.configure(fg_color=C["sidebar"], border_color=C["border"])
    topbar.configure(fg_color=C["top"], border_color=C["border"])
    chat_header.configure(fg_color=C["panel"], border_color=C["border"])
    message_area.configure(
        fg_color=C["panel"],
        scrollbar_button_color=C["border"],
        scrollbar_button_hover_color=C["border2"]
    )
    composer.configure(fg_color=C["input"], border_color=C["accent"])
    composer_entry.configure(
        fg_color=C["input"],
        text_color=C["text"],
        placeholder_text_color=C["muted"]
    )
    search_entry.configure(
        fg_color=C["surface"],
        border_color=C["border"],
        text_color=C["text"],
        placeholder_text_color=C["muted"]
    )

    # Repaint all nested widgets so Light mode cannot leave black controls.
    repaint(root)

    theme_button.configure(
        fg_color=C["surface"],
        hover_color=C["hover"],
        border_color=C["border"],
        text_color=C["text"],
        text="☾" if dark_mode else "☀"
    )

    top_title.configure(text_color=C["text"])
    status_label.configure(
        text_color=C["success"] if "Online" in status_label.cget("text") else C["accent2"]
    )

    nav_style()
    refresh_recent()
    build_prompts() if "build_prompts" in globals() else None

    # Rebuild the dynamic chat so message bubbles/cards use the new palette.
    if current_page == "AI Chat":
        show_chat_page()
    elif current_page == "History":
        show_history_page()
    elif current_page == "Settings":
        show_settings_page()
    elif current_page == "Help & Support":
        show_help_page()
    else:
        show_simple_page(current_page)


# ============================================================
# KEYBOARD SHORTCUTS
# ============================================================

app.bind(
    "<Control-n>",
    lambda e: (new_chat(), "break")[1]
)

app.bind(
    "<Control-k>",
    lambda e: (focus_search(), "break")[1]
)

app.bind(
    "<Control-l>",
    lambda e: (composer_entry.focus(), "break")[1]
)

app.bind(
    "<Control-Shift-D>",
    lambda e: (toggle_theme(), "break")[1]
)

app.bind(
    "<Escape>",
    lambda e: (composer_entry.focus(), "break")[1]
)


# ============================================================
# START
# ============================================================

load_history()

if chats:
    current_chat_id = list(chats.keys())[-1]

refresh_recent()
show_chat_page()
composer_entry.focus()

app.mainloop()
