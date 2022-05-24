from errors import ChoiceError

def write(file_names, option):
    if file_names == [] or option == 'Choose file':
        raise ChoiceError()
    for file in file_names:
        with open(file, 'r') as f:
            text = f.read()
        with open(file, 'w') as f:
            if option == 'Lower':
                text = text.lower()
            elif option == 'Upper':
                text = text.upper()
            elif option == 'Choose option':
                raise ChoiceError()
            f.write(text)