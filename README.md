# Entorno-Python de Automatizacion de tareas para QA
Todos los archivos necesarios para montar un entorno de desarrollo que incluye:
- Dockerfile
- Docker-Compose : Ejecuta dockerfile y configura el entorno. 
- requirements.txt : Librerias que se instalaran en el contenedor luego de que este levante.
- Carpeta APP: Contiene los scripts base que serviran como ejemplo. Esta carpeta esta configurada como BIND, con lo cual los cambios realizados en el host seran visibles automaticamente en el contenedor y viceversa.
- Archivos de ejemplo de como montar una solucion OOP para la automatizacion de tareas de QA