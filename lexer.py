from tokens import *

REPLACEMENTS = [
    ("\n", ";"),
    ("    ", TAB),
    (" ", NULL),
    ("WriteText", PRINT),
    ("Variable", NEW_VAR),
    ("Cdt", IF),
    ("Ccdt", ELSE),
    ("<<", LESS),
    (">>", GREATER),
    ("->", SET_TYPE),
    ("==", EQUAL),
    ("=", SET_VAR),
    ("(", INIT_PAREN),
    (")", END_PAREN),
    ("{", INIT_COL),
    ("}", END_COL),
    ("<[", INIT_INSERT),
    ("]>", END_INSERT),
    (";", NEWLINE),
    ("Integer", TYPE_INT),
]

def lex(text):
    for old, new in REPLACEMENTS:
        text = text.replace(old, f"-{new}-")

    tokens = [t for t in text.split("-") if t.strip() != ""]
    return tokens