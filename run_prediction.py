from dp import text_to_sequence, sequence_to_text

if __name__ == '__main__':
    tokens = text_to_sequence('hello world. This is a tokeniser test.')
    print(tokens)
    text = sequence_to_text(tokens)
    print(text)