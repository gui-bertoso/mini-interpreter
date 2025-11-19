import tokens

def preprocess(tokens_list):
    new_tokens_list = []
    tokens_list_size = len(tokens_list)
    for i in range(0, tokens_list_size):
        if tokens_list[i] == tokens.INIT_COL and i+1 <= tokens_list_size and tokens_list[i+1] == tokens.PRINT:
            pass
        elif tokens_list[i] == tokens.ELSE and i+1 <= tokens_list_size:
            new_tokens_list.append(tokens_list[i])
            new_tokens_list.append(tokens.TAB)
        else:
            new_tokens_list.append(tokens_list[i])

    return new_tokens_list