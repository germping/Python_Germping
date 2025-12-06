import os
import re
import PyPDF2
#Clase que contiene las funciones para extraer los datos solicitados
class PDFProcessor:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo no fue encontrado en: {file_path}")
        self.file_path = file_path
        self.cufe_regex = re.compile(r'\b([0-9a-fA-F]\n*){95,100}\b')

    def get_numero_paginas(self):
        try:
            with open(self.file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                return len(reader.pages)
        except Exception as e:
            print(f"Error al leer el número de páginas de {self.file_path}: {e}")
            return 0

    def extract_cufe(self):
        try:
            with open(self.file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                
                # Se lee el contenido para proceder con la REGEX
                cleaned_text = ''.join(filter(str.isalnum, text))                
                match = self.cufe_regex.search(cleaned_text)
                if match:
                    return match.group(0)
                else:
                    return "CUFE no encontrado"
        except Exception as e:
            print(f"Error al extraer CUFE de {self.file_path}: {e}")
            return "Error al extraer CUFE"

    def get_peso_archivo(self):
        try:
            return os.path.getsize(self.file_path) / (1024 * 1024)  # PESO en MB
        except Exception as e:
            print(f"Error al obtener el peso del archivo {self.file_path}: {e}")
            return 0
