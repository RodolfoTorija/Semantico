import spacy

# Cargar el modelo de lenguaje español
nlp = spacy.load('es_core_news_sm')

# Texto de ejemplo
texto = 'El perro corre detras del gato'

# Analizar el texto utilizando Spacy
doc = nlp(texto)

# Variables para almacenar los sustantivos y verbos encontrados
sustantivos = []
verbos = []

# Iterar sobre las palabras en el texto
for palabra in doc:
    # Verificar si la palabra es un sustantivo
    if palabra.pos_ == 'NOUN':
        sustantivos.append(palabra.text)
    # Verificar si la palabra es un verbo
    elif palabra.pos_ == 'VERB':
        verbos.append(palabra.text)

for palabra in doc:
    print(palabra.text, palabra.dep_)

# Imprimir los sustantivos y verbos encontrados
print('Sustantivos encontrados:', sustantivos)
print('Verbos encontrados:', verbos)

# Definir función para buscar el sujeto
def buscar_sujeto(verbo):
    for palabra in verbo.lefts:
        if palabra.dep_ == 'nsubj':
            return palabra
    return None

# Definir función para buscar el objeto
def buscar_objeto(verbo):
    for palabra in verbo.rights:
        if palabra.dep_ == 'obj':
            return palabra
    return None

# Iterar sobre los verbos encontrados
for verbo in verbos:
    # Buscar el sujeto y el objeto para cada verbo
    for palabra in doc:
        if palabra.text == verbo:
            sujeto = buscar_sujeto(palabra)
            objeto = buscar_objeto(palabra)

            # Imprimir la relación semántica entre el sujeto y el objeto
            if sujeto and objeto:
                print('Relación semántica:', sujeto.text, verbo, objeto.text)
