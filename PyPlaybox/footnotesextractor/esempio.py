import re


def extract_footnotes(input_string):
    # Definiamo un pattern regex per estrarre le chiavi e i valori delle footnote
    pattern = r"footnote(\d+)\)\\t', '(.+?)'"

    # Inizializziamo un dizionario vuoto per memorizzare le coppie chiave-valore
    footnote_dict = {}

    # Troviamo tutte le corrispondenze nel testo
    matches = re.findall(pattern, input_string)

    # Popoliamo il dizionario con le chiavi e i valori estratti
    for match in matches:
        key = match[0]
        value = match[1]
        footnote_dict[key] = value

    return footnote_dict


# La tua stringa di input
stringa_footnote = "[['footnote1)\\t', ' Cf. Benedetto XVI, Discorso all’Assemblea Generale della Conferenza Episcopale Italiana, 27 maggio 2010.']], [['footnote2)\\t', ' Cf. Francesco, Messaggio per la LVII giornata mondiale della pace: Intelligenza artificiale e pace, 1° maggio 2024.']], [['footnote4)\\t', 'altro testo']], [['footnote5)\\t', 'ancora altro testo']]"

# Estraiamo le chiavi e i valori
risultato = extract_footnotes(stringa_footnote)

# Stampa il risultato
for key, value in risultato.items():
    print(f"Chiave: {key}\nValore: {value}\n")
