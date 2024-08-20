from dp import text_to_sequence

if __name__ == '__main__':
    tokens = text_to_sequence('hello world. This is a tokeniser test.')
    print(tokens)