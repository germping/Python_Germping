import os
from pdf_processor import PDFProcessor
from database_manager import DatabaseManager

def main():
    #Las facturas se sacan de MEDIA/FACTURAS
    pdf_directory = os.path.join('MEDIA', 'FACTURAS')
    db_name = 'facturas.db'#DB Sqlite

    if not os.path.exists(pdf_directory):
        print(f"El directorio {pdf_directory} no existe.")
        return

    with DatabaseManager(db_name) as db:
        db.create_table()

        for filename in os.listdir(pdf_directory):
            if filename.lower().endswith('.pdf'):
                file_path = os.path.join(pdf_directory, filename)
                
                try:
                    pdf_processor = PDFProcessor(file_path)
                    
                    nombre_archivo = filename
                    numero_paginas = pdf_processor.get_numero_paginas()
                    cufe = pdf_processor.extract_cufe()
                    peso_archivo = pdf_processor.get_peso_archivo()

                    db.insert_factura(nombre_archivo, numero_paginas, cufe, peso_archivo)
                    print(f"Procesado y guardado en la DB: {nombre_archivo}")

                except FileNotFoundError as e:
                    print(e)
                except Exception as e:
                    print(f"Ocurrió un error al procesar el archivo {filename}: {e}")

    print("\nProceso completado. Los datos han sido extraídos y almacenados en la base de datos.")

if __name__ == '__main__':
    main()
