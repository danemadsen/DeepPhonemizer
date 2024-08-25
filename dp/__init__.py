from dp.phonemizer import Phonemizer
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
default_checkpoint = os.path.join(current_dir, 'checkpoints', 'latin_ipa_forward.pt')

def text_to_sequence(text):
    phonemizer = Phonemizer.from_checkpoint(default_checkpoint)

    # Split text by ' '
    split_text = text.split(' ')

    result = phonemizer.phonemise_list(split_text, lang='en_us')

    tokens = []
    for pred in result.predictions:
        tokens += pred.phoneme_tokens
        tokens.append(0)
    
    return tokens

def sequence_to_text(sequence):
    phonemizer = Phonemizer.from_checkpoint(default_checkpoint)
    inx_to_token = phonemizer.predictor.phoneme_tokenizer.idx_to_token
    punctuation = ['.', ',', ':', ';', '?', '!', '\"', '(', ')', '-']

    result = ''
    for token in sequence:
        if token >= len(inx_to_token):
            result += punctuation[token - len(inx_to_token)]
        else:
            result += inx_to_token[token]

    return result.replace('_', ' ')