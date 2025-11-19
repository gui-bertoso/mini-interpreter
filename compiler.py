import tokens

def compile_tokens(tokens_list):
    output = ""
    for token in tokens_list:
        match token:
            case tokens.PRINT: output += "print"
            case tokens.IF: output += "if "
            case tokens.INIT_PAREN: output += "(f'"
            case tokens.END_PAREN: output += "')"
            case tokens.INIT_COL: output += ":"
            case tokens.ELSE: output += "\nelse:\n"
            case tokens.SET_TYPE: output += ":"
            case tokens.SET_VAR: output += " = "
            case tokens.NEW_VAR: output += ""
            case tokens.END_COL: output += ""
            case tokens.INIT_INSERT: output += "{"
            case tokens.END_INSERT: output += "}"
            case tokens.LESS: output += " < "
            case tokens.GREATER: output += " > "
            case tokens.EQUAL: output += " == "
            case tokens.NEWLINE: output += "\n"
            case tokens.TAB: output += "\t"
            case tokens.TYPE_INT: output += "int"
            case _: output += token
    return output