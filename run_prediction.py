from dp.phonemizer import Phonemizer

if __name__ == '__main__':

    checkpoint_path = 'checkpoints/latin_ipa_forward.pt'
    phonemizer = Phonemizer.from_checkpoint(checkpoint_path)

    text = ['hello', 'world.', 'this', 'is', 'a', 'test.']

    result = phonemizer.phonemise_list(text, lang='en_us')

    print(result.phonemes)
    print(result.predictions)
    for pred in result.predictions:
        print(pred.phoneme_tokens)

