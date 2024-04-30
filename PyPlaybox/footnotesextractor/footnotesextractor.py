import re
from docx2python import docx2python
from docx2python.iterators import iter_paragraphs

def extract_footnotes(input_string):
    pattern = r"footnote(\d+)\)\\t', '(.+?)'"

    footnote_dict = {}

    matches = re.findall(pattern, input_string)

    for match in matches:
        key = match[0]
        value = match[1]

        if "Ivi" in value or "Ibidem" in value:
            continue

        footnote_dict[key] = value

    return footnote_dict


def flatten_nested_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_nested_list(item))
        else:
            flattened_list.append(item)

    return flattened_list


with docx2python("Salvatore Di Fazio.docx") as output:
    footnotes = output.footnotes
    individual_footnote_strings = list(iter_paragraphs(footnotes))

    footnotes_string = "".join(flatten_nested_list(footnotes))
    print(individual_footnote_strings)

#    lines = footnotes_string.splitlines()
#    i = 1
#    for line in lines:
#        print(i)
#        print(line + "\\n")
#        i = i + 1

    # for key, value in risultato.items():
    #     print(f"Chiave: {key}\nValore: {value}\n")


