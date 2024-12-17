import re
import json


def parse_penal_code(file_path):
    # Initialize variables
    titulo_actual = ""
    titulo_completo = ""
    data = []
    
    # Regex patterns
    titulo_pattern = re.compile(r"TITULO\s+\w+", re.IGNORECASE)
    capitulo_pattern = re.compile(r"CAPITULO\s+[IVXLCDM]+", re.IGNORECASE)
    articulo_pattern = re.compile(r"ARTICULO\s+(\d+[A-Za-z]*)", re.IGNORECASE)
    
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    current_article = None
    current_text = []
    collecting_text = False

    for line in lines:
        line = line.strip()

        # Match TITULO
        if (titulo_match := titulo_pattern.match(line)):
            # Save the current article if any
            if current_article:
                data.append({
                    "titulo_completo": titulo_completo,
                    "delito_artículo": current_article,
                    "texto": " ".join(current_text).strip()
                })
                current_article = None
                current_text = []

            # Update current titulo
            titulo_actual = titulo_match.group().strip()
            titulo_completo = f"CPN - {titulo_actual}"
            continue

        # Match CAPITULO
        if (capitulo_match := capitulo_pattern.match(line)):
            # Save the current article if any
            if current_article:
                data.append({
                    "titulo_completo": titulo_completo,
                    "delito_artículo": current_article,
                    "texto": " ".join(current_text).strip()
                })
                current_article = None
                current_text = []

            # Update current capitulo
            titulo_completo = f"CPN - {titulo_actual} - {capitulo_match.group().strip()}"
            continue

        # Match ARTICULO
        if (articulo_match := articulo_pattern.match(line)):
            # Save the current article if any
            if current_article:
                data.append({
                    "titulo_completo": titulo_completo,
                    "delito_artículo": current_article,
                    "texto": " ".join(current_text).strip()
                })

            # Start a new article
            current_article = f"Art. {articulo_match.group(1)}"
            current_text = []
            collecting_text = True
            continue

        # Append text if in an article
        if collecting_text:
            current_text.append(line)
    
    # Add the last article
    if current_article:
        data.append({
            "titulo_completo": titulo_completo,
            "delito_artículo": current_article,
            "texto": " ".join(current_text).strip()
        })
    
    return data


def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Paths
input_file = "cp.txt"
output_file = "penal_code.json"

# Process and save
parsed_data = parse_penal_code(input_file)
save_to_json(parsed_data, output_file)

print(f"Penal code has been successfully parsed and saved to {output_file}.")
