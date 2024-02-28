# Descripción general del proyecto

## Descripción

Promptior chatbot es un chatbot que permite a los usuarios obtener información de Promptior, una empresa que se especializa en implementar soluciones generativas de vanguardia, especializándose en la implementación de la arquitectura RAG (Retrieval Augmented Generation) para satisfacer las diversas necesidades de sus clientes.

## Objetivo del proyecto

Desarrollar y desplegar un asistente chatbot que utilice la arquitectura RAG para responder preguntas
sobre el contenido del sitio web de Promptior, basándose en la librería LangChain.

## Funcionalidades

- Responder preguntas sobre Promptior.
- Interfaz amigable para el usuario.
- Despliegue en la web.

## Tecnologías

LangChain, Python, FastAPI, Docker, HTML, CSS, JavaScript, RAG

## Principales desafíos

Aprender a utilizar la arquitectura RAG, fueron horas  horas de ver tutoriales, leer documentación y hacer pruebas para entender cómo funciona y cómo implementarla en el chatbot. Hay muchas opiniones diversas y diferentes formas de implementarla, por lo que fue un desafío encontrar la mejor forma de hacerlo.

Por ejemplo, el texto de entrada para el modelo RAG debe ser una concatenación de la pregunta y el contexto, por lo que fue un desafío encontrar la mejor forma de obtener el contexto de la pregunta y cómo concatenarlos.

Otro tema que estuve investigando era la forma de estructurar el proyecto. No quería que el código del modelo RAG estuviera en el mismo archivo que el código del chatbot, por lo que tuve que buscar una forma de separarlos. Después de buscar numerosas fuentes me decidi con la estructura actual, que me pareció la más limpia y ordenada.

Otro problema fue la obtención de la información para el contexto. Lamentablemente no se puede hacer scraping a la página web de Promptior, por lo que tuve que buscar otra forma de obtener la información. Lo que hice simplemente fue cargar la información en un archivo txt y leerlo desde el chatbot. No estoy muy conforme con esta solución, pero fue la única que se me ocurrió. Igualemente me gustaría buscar una solución más elegante en el futuro.

## Posibles Mejoras

- Mejorar la obtención de la información para el contexto.
- Implementar un sistema de autenticación para que solo los usuarios autorizados puedan acceder al chatbot.
- Implementar un sistema de almacenamiento de conversaciones.
- Implementar el paso de información del historial de conversaciones al modelo RAG para que pueda responder preguntas sobre conversaciones pasadas.
- Implementar el uso de otros modelos, no solo de OpenAI, sino también de otros proveedores como Google, Microsoft, etc.


