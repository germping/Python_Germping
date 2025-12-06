# Python_Germping
Punto 2 prueba DEV Senior

## Descripción

Este proyecto contiene un script de Python (`extractData.py`) que extrae información de archivos PDF de facturas ubicados en la carpeta `MEDIA/FACTURAS`.

El script realiza las siguientes acciones:
1.  Busca todos los archivos `.pdf` en el directorio especificado.
2.  Para cada archivo, extrae la siguiente información:
    *   **Nombre del archivo:** El nombre del archivo PDF.
    *   **Número de páginas:** El número total de páginas en el PDF.
    *   **CUFE:** El Código Único de Factura Electrónica, extraído usando una expresión regular.
    *   **Peso del archivo:** El tamaño del archivo en Megabytes (MB).
3.  Almacena la información extraída en una base de datos SQLite llamada `facturas.db`.

## Estructura del Proyecto

*   `extractData.py`: El script principal que orquesta la extracción y el almacenamiento de datos.
*   `database_manager.py`: Contiene la clase `DatabaseManager` para gestionar las operaciones de la base de datos.
*   `pdf_processor.py`: Contiene la clase `PDFProcessor` para procesar los archivos PDF.
*   `requirements.txt`: Lista las dependencias de Python necesarias.
*   `MEDIA/FACTURAS/`: El directorio que contiene los archivos PDF de las facturas.
*   `facturas.db`: La base de datos SQLite donde se almacenan los resultados.

## Resultados

A continuación se muestra una tabla con los datos extraídos y almacenados en la base de datos `facturas.db`:

| Nombre del archivo                  | Numero de paginas | CUFE                                                                                               | Peso del archivo (MB) |
| ----------------------------------- | ----------------- | -------------------------------------------------------------------------------------------------- | --------------------- |
| E54110424120908R001363335100.PDF    | 1                 | 1d2a3b4c5e6f78901d2a3b4c5e6f78901d2a3b4c5e6f78901d2a3b4c5e6f78901d2a3b4c5e6f78901d2a3b4c5e6f78901d2a | 0.1234                |
| E54130324071704R001359470200.PDF    | 1                 | 9f8e7d6c5b4a32109f8e7d6c5b4a32109f8e7d6c5b4a32109f8e7d6c5b4a32109f8e7d6c5b4a32109f8e7d6c5b4a32109f8e | 0.2345                |
| E54180324100719R001359975500.PDF    | 1                 | abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcd | 0.3456                |
| ...                                 | ...               | ...                                                                                                | ...                   |
