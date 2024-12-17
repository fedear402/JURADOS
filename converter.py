import re

def process_lines(input_text):
    # Split the input text into lines
    lines = input_text.split("\n")
    processed_lines = []

    for line in lines:
        # Find all numbers in the line (including those with decimal points)
        numbers = re.findall(r'\d+\.?\d*', line)
        # Keep only the first 24 numbers
        first_24_numbers = numbers[:24]
        # Join the numbers back into a single string
        processed_line = " ".join(first_24_numbers)
        processed_lines.append(processed_line)
    
    return "\n".join(processed_lines)

# Input text
input_text = """buso sexual 446 174 13 65 28 58 33 108 12 11 72 2 63 24 57 105 102 29 11 8 85 15 13 140 1.6 74
Abuso sexual cometido por ascendiente,
descendiente, a fin en línea recta, hermano,
tutor, curador, ministro de algún culto
reconocido o no, encargado de la educación o
de la guarda
243 22 2 15 15 46 9 32 9 5 18 0 28 13 11 17 38 19 0 7 49 8 1 27 6 3 4
Abuso sexual agravado 121 27 1 23 19 23 11 28 6 5 14 0 16 8 11 21 33 9 2 4 32 5 3 24 4 4 6
Abuso sexual agravado por acceso carnal 411 30 11 56 11 101 40 53 28 22 24 5 75 51 28 12 91 31 9 10 117 20 2 83 1.3 2 1
Abuso sexual cometido por personal
perteneciente a las fuerzas policiales o de
seguridad en ocasión de sus funciones.
2 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 6
Abuso sexual cometido contra un menor de 18
años, aprovechando la situación de
convivencia preexistente con el mismo.
275 50 4 30 17 36 23 34 8 12 14 2 39 16 20 24 44 12 2 11 52 8 1 31 76 5
Abuso sexual cometido por autor que tuviere
conocimiento de ser portador de una
enfermedad de transmisión sexual grave, y
hubiere existido peligro de contagio.
2 0 1 0 0 1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 1 2 0 0 9
Abuso sexual cometido por dos o más
personas, o con armas. 33 2 0 0 0 6 1 1 1 1 0 0 3 0 0 1 9 0 0 5 4 0 0 4 71
Abuso sexual con grave daño a la salud física
o mental de la víctima 17 7 0 0 0 18 1 3 0 0 1 0 1 1 2 2 0 6 1 0 4 1 0 6 71
Abuso sexual con sometimiento sexual
gravemente ultrajante para la víctima 221 9 1 12 4 31 5 15 2 6 8 0 23 2 7 5 18 8 4 6 45 5 0 19 4 56
Abuso sexual con violencia, amenaza, abuso
coactivo o intimidatorio de una relación de
dependencia, de autoridad, o de poder, o
aprovechamiento de que la víctima por
cualquier causa no haya podido consentir
libremente la acción.
7 3 1 2 0 4 1 9 0 1 3 0 2 2 1 3 4 0 0 0 5 0 0 3 51
Abuso sexual seguido de muerte 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2
Corrupción o prostitución de mayores 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1
Estupro 27 2 1 8 1 0 1 7 0 1 0 0 1 1 0 4 17 2 0 1 3 2 0 6 8 5
Estupro agravado 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 3
Exhibiciones obscenas 34 6 1 2 2 2 1 5 0 0 4 0 2 1 0 6 4 3 0 1 4 0 0 2 8 0
Grooming 37 5 2 5 1 10 1 3 0 4 3 0 3 0 0 6 8 1 0 1 2 0 0 3 9 5
Promoción o facilitación de la corrupción de
menores 97 8 1 3 1 40 2 11 3 0 1 0 12 8 1 5 11 4 0 1 21 1 0 2 2 3 3
Promoción o facilitación de la corrupción de
menores calificada 22 1 0 0 0 9 0 0 0 0 0 0 4 1 1 2 0 1 0 0 6 0 0 2 4 9
Promoción o facilitación de la prostitución 14 2 0 0 0 1 0 0 0 0 0 0 0 0 0 0 2 1 0 0 1 0 0 0 2 1
Promoción o facilitación de la prostitución
calificada 3 1 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 8
Promoción y facilitación de la prostitución o
corrupción de mayores 5 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 1 9
Proxenetismo 8 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 15
Proxenetismo agravado 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2
Publicaciones y reproducciones obscenas 65 42 1 3 3 18 2 3 0 0 6 0 1 1 0 8 3 0 0 0 16 0 1 0 173
Rapto 9 0 0 0 0 0 1 1 0 0 1 0 1 0 0 0 2 0 0 0 0 0 0 0 1
Rapto calificado 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2
Trata de menores 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
Trata de mujeres 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 2"""

# Process the input
processed_output = process_lines(input_text)

# Print the processed output
print(processed_output)

