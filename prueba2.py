import cv2

# Ruta de la imagen de entrada
input_image_path = '1.png'

# Ruta del archivo cascaded.xml para la detección de lámparas
cascade_path = 'cascade.xml'

# Cargar la imagen de entrada
image = cv2.imread(input_image_path)
if image is None:
    print(f"Error: No se pudo cargar la imagen de entrada en la ruta '{input_image_path}'.")
    exit()

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Redimensionar la imagen a un tamaño más manejable
target_width = 3000  # Puedes ajustar este valor según tus necesidades
height, width, _ = image.shape
aspect_ratio = width / height
target_height = int(target_width / aspect_ratio)
resized_image = cv2.resize(image, (target_width, target_height))

# Cargar el clasificador en cascada para la detección de lámparas
lamp_cascade = cv2.CascadeClassifier(cascade_path)

# Realizar la detección de lámparas en la imagen con ajuste automático
lamp_rectangles = lamp_cascade.detectMultiScale(
    gray_image,
    scaleFactor=1.05,
    minNeighbors=90,  # Ajustar este valor para cambiar la precisión
    minSize=(25, 10),  # Ajustar este valor para permitir detección de detalles pequeños
    maxSize=(65, 80),  # Establecer el tamaño máximo de los rectángulos
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Dibujar rectángulos alrededor de las lámparas detectadas
for (x, y, w, h) in lamp_rectangles:
    # Ajustar el tamaño mínimo y máximo de los rectángulos
    w = min(max(w, 50), 55)
    h = min(max(h, 50), 55)
    cv2.rectangle(resized_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Guardar la imagen con los rectángulos alrededor de las lámparas detectadas
output_image_path = 'resultado_deteccion.png'
cv2.imwrite(output_image_path, resized_image)

# Mostrar la imagen redimensionada con los rectángulos alrededor de las lámparas detectadas
cv2.imshow('Detección de lámparas', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
