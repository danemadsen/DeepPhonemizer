from dp.phonemizer import Phonemizer

def text_to_sequence(text):
    phonemizer = Phonemizer.from_checkpoint('checkpoints/latin_ipa_forward.pt')

    # Split text by ' '
    split_text = text.split(' ')

    result = phonemizer.phonemise_list(split_text, lang='en_us')

    tokens = []
    for pred in result.predictions:
        tokens.append(pred.phoneme_tokens)
        tokens.append(0)  # Add a space between words