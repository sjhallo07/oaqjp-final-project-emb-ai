# Emotion Detector

## Descripción
Emotion Detector es un proyecto desarrollado para la materia de Embebidos y AI. Permite la detección y análisis de emociones a partir de datos recibidos, proporcionando una solución escalable basada en Flask para aplicaciones web y sistemas embebidos.

## Estructura del Proyecto

```
final_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
└── (todas las capturas de pantalla requeridas)
```

- EmotionDetection/: Módulo principal de detección de emociones.
  - emotion_detection.py: Contiene la lógica y funciones para analizar emociones.
  - __init__.py: Permite importar el módulo.
- templates/: Archivos HTML para la interfaz web.
  - index.html: Interfaz principal (proporcionada).
- static/: Archivos estáticos (JavaScript, CSS, etc).
  - mywebscript.js: Script para la interacción en el frontend (proporcionado).
- server.py: Servidor principal Flask para atender las peticiones API y renderizar la interfaz web.
- test_emotion_detection.py: Pruebas unitarias para el módulo de detección de emociones.
- Capturas de pantalla: Evidencia visual de funcionamiento.

## Forma de Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/sjhallo07/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai/final_project
   ```

2. **Instalar dependencias:**  
   Instala las dependencias necesarias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
   *(Asegúrate de tener Flask, numpy, pandas, etc.)*

3. **Ejecutar el servidor Flask:**  
   ```bash
   python server.py
   ```
   o
   ```bash
   flask run
   ```

4. **Interacción con la API:**
   - GET: Consultar información, métricas o resultados de emociones.
   - POST: Enviar datos para el análisis y detección de emociones.

   Ejemplo de petición POST:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"texto": "Me siento feliz"}' http://localhost:5000/detect
   ```

   Ejemplo de petición GET:
   ```bash
   curl http://localhost:5000/emotions
   ```

5. **Interfaz Web:**  
   Accede a la aplicación en tu navegador:
   ```
   http://localhost:5000/
   ```
   La interfaz usa index.html y el script mywebscript.js para interactuar con el backend.

6. **Pruebas Unitarias:**  
   Ejecuta las pruebas con:
   ```bash
   python test_emotion_detection.py
   ```

## Casos de Uso

- Procesar texto o datos recibidos y detectar emociones mediante la API RESTful.
- Visualizar resultados y métricas en el dashboard web.
- Integrar el sistema en dispositivos embebidos o IoT.
- Ejecutar pruebas automáticas del módulo de emociones.

## Lenguajes y Dependencias

- Python (Flask, numpy, pandas)
- HTML/JS (Frontend)
- Todas las dependencias están especificadas en requirements.txt.

## Revisión de Código Estático

La calidad del código se verifica mediante **Pylint**.  
Para ejecutar Pylint y revisar el código estático:

```bash
pylint EmotionDetection/emotion_detection.py
```
o para todo el proyecto:
```bash
pylint .
```

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

## Modificación

Modificado por **Marcos Mora**.