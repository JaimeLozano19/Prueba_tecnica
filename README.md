Detección de Lámparas utilizando OpenCV
Este proyecto realiza la detección de lámparas en imágenes mediante el uso de la biblioteca OpenCV. La detección se basa en un clasificador en cascada entrenado para reconocer patrones específicos asociados a lámparas. Este README proporciona información sobre el script de detección y las instrucciones para generar un archivo XML de entrenamiento utilizando la aplicación cascade-trainer-gui.

Contenido
Requisitos
Uso del Script
Generar un Archivo XML de Entrenamiento
Arquitectura del Modelo
Pasos de Entrenamiento y Evaluación
Mejoras y Ajustes
Requisitos
Asegúrate de tener instalada la biblioteca OpenCV en tu entorno de Python. Puedes instalarla utilizando el siguiente comando:


pip install opencv-python
Uso del Script
Configuración de la Ruta de la Imagen y el Archivo Cascade:

Especifica la ruta de la imagen de entrada en la variable input_image_path.
Proporciona la ruta del archivo cascade.xml en la variable cascade_path.
Cargar la Imagen y Convertirla a Escala de Grises:

La imagen se carga y se convierte a escala de grises para facilitar el procesamiento.
Redimensionar la Imagen:

La imagen se redimensiona para mejorar la eficiencia del proceso de detección. Ajusta la variable target_width según tus necesidades.
Detección de Lámparas:

Se utiliza un clasificador en cascada preentrenado para la detección de lámparas. Ajusta los parámetros de minNeighbors, minSize, y maxSize según sea necesario.
Dibujar Rectángulos alrededor de las Lámparas Detectadas:

Se dibujan rectángulos alrededor de las lámparas detectadas en la imagen redimensionada.
Guardar y Mostrar la Imagen Resultante:

La imagen resultante con los rectángulos se guarda en el archivo especificado por output_image_path.
Se muestra la imagen redimensionada con los rectángulos alrededor de las lámparas detectadas.
Generar un Archivo XML de Entrenamiento
Para generar un archivo XML de entrenamiento para la detección de lámparas, puedes utilizar la aplicación cascade-trainer-gui. Aquí tienes un paso a paso básico:

Instalar la Aplicación:

Descarga e instala la aplicación cascade-trainer-gui.
Preparar Conjunto de Datos:

Recopila un conjunto de imágenes positivas que contengan lámparas y un conjunto de imágenes negativas que no contengan lámparas.
Ejecutar la Aplicación:

Abre la aplicación y sigue las instrucciones para cargar las imágenes positivas y negativas.
Configurar Parámetros de Entrenamiento:

Establece parámetros como el número de etapas, tamaño de ventana, etc.
Iniciar el Entrenamiento:

Inicia el proceso de entrenamiento y espera a que se complete.
Generar el Archivo XML:

Después de completar el entrenamiento, la aplicación generará un archivo XML que puedes utilizar con el script de detección.
Nota: Este README proporciona instrucciones básicas. Consulta la documentación de cascade-trainer-gui para obtener detalles más específicos sobre la generación de archivos XML de entrenamiento.

Arquitectura del Modelo
La detección de lámparas se basa en un clasificador en cascada preentrenado, el cual es cargado mediante cv2.CascadeClassifier. Este clasificador ha sido entrenado para reconocer patrones visuales específicos asociados a lámparas.

Pasos de Entrenamiento y Evaluación
El entrenamiento del clasificador en cascada se realiza mediante la aplicación cascade-trainer-gui. A continuación, se describen los pasos generales:

Preparación de Datos:

Se recopilan imágenes positivas que contienen lámparas y negativas que no las contienen.
Entrenamiento:

Se utilizan estas imágenes para entrenar el clasificador en cascada mediante la aplicación cascade-trainer-gui.
Se establecen parámetros como el número de etapas, tamaño de ventana, etc.
La aplicación genera un archivo XML que contiene la información del clasificador entrenado.
Mejoras y Ajustes
El script proporciona la flexibilidad de ajustar parámetros como minNeighbors, minSize, y maxSize para mejorar la precisión de la detección. Experimenta con estos valores según tus necesidades específicas. Además, asegúrate de contar con un conjunto de datos de entrenamiento diverso para mejorar el rendimiento del clasificador.
