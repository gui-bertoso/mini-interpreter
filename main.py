from lexer import lex
from interpleter import preprocess
from compiler import compile_tokens
from utils import read_file, write_file

INPUT = "examples/input_file.mny"
OUTPUT = "examples/output_file.py"

if __name__ == "__main__":
    text = read_file(INPUT)
    tokens = lex(text)
    preprocessed_text = preprocess(tokens)
    py_code = compile_tokens(preprocessed_text)

    print("TOKENS: ", tokens)
    print("-" * 40)
    print(py_code)
    print("-" * 40)

    write_file(OUTPUT, py_code)