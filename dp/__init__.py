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