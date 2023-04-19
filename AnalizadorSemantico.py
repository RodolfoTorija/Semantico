import spacy

# Cargar el modelo de lenguaje español
nlp = spacy.load('es_core_news_sm')

# Texto de ejemplo
texto = 'El perro corre detrás del gato muy rapido'

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

# Imprimir los sustantivos y verbos encontrados
print('Sustantivos encontrados:', sustantivos)
print('Verbos encontrados:', verbos)
