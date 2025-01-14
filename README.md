# Envío de Emails con Python y Gmail

Este proyecto permite enviar emails utilizando Python y el servidor SMTP de Gmail. Es ideal para enviar recordatorios o notificaciones automáticas.

---

## 🚀 **Requisitos**

1. Python 3.x instalado en tu sistema.
2. Una cuenta de Gmail.

---

## 🛠️ **Instalación**

1. Clona este repositorio o descarga el archivo `enviar_email.py`.
2. Instala las librerías necesarias:
   ```bash
   pip install smtplib ssl


## ⚙️ **Configuración**
1. Habilitar verificación en dos pasos
Activa la verificación en dos pasos.
2. Generar una contraseña de aplicación
En la misma página, busca la sección "Contraseñas de aplicaciones".
Genera una nueva contraseña de aplicación y cópiala.
3. Configurar el script
Reemplaza las siguientes variables en el archivo enviar_email.py:
python
    TU_EMAIL = "tu_email@gmail.com"
    TU_PASSWORD = "contraseña_de_aplicación"

## 🧪 **Cómo usarlo**
Abre una terminal en la carpeta donde se encuentra el archivo.
Ejecuta el script:
    python enviar_email.py

## ✨ **Personalización**
Cambia el contenido del cuerpo del email para adaptarlo a tus necesidades.
Si deseas enviar emails con adjuntos, el script puede ser modificado fácilmente.
📬 Resultado esperado
Si todo está configurado correctamente, recibirás un email con el texto del recordatorio.

## 🛡️ **Seguridad**
No compartas tu contraseña de aplicación.
Borra las credenciales antes de subir el script a un repositorio público.