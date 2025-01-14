import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP de Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Credenciales
TU_EMAIL = "tu_email@gmail.com"
TU_PASSWORD = "abcd efgh ijkl mnop"  # Contraseña de aplicación generada en Google

# Función para enviar email
def enviar_email(destinatario, asunto, cuerpo):
    try:
        # Crear el mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = TU_EMAIL
        mensaje["To"] = destinatario
        mensaje["Subject"] = asunto

        # Agregar el cuerpo del email
        mensaje.attach(MIMEText(cuerpo, "html"))

        # Conectar con el servidor y enviar el email
        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=contexto) as server:
            server.login(TU_EMAIL, TU_PASSWORD)
            server.sendmail(TU_EMAIL, destinatario, mensaje.as_string())

        print("✅ Email enviado exitosamente.")

    except Exception as e:
        print(f"❌ Error al enviar el email: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    destinatario = "destinatario@gmail.com"
    asunto = "🚀 Recordatorio de Tareas Pendientes"
    cuerpo = """
    ✨ ¡Hola Maxi! Aquí tienes tu recordatorio de tareas pendientes ✨

    📋 **Lista de cosas para hacer:**

    🚗 **Retirar autitos**  
    🎮 **Buscar Play (¡no te olvides de los juegos también!)**  
    🚙 **Alquilar auto en Brasil (revisar seguros y precios)**  
    💉 **Vacunarte para la gripe amarilla (consulta con tu médico)**  
    🔨 **Poner techo para el ventilete (revisar materiales necesarios)**  
    🎙️ **Armar esquema para la presentación en stream:**  
       📌 Haz una presentación de 1 hora introduciéndote  
       🎯 Habla de tus proyectos y objetivos  

    ⚡ **Recuerda:** Organiza tu tiempo y ¡dale con todo! 💪  
    🎉 ¡Éxitos con todo lo que emprendas!

    💻 **Generado por tu asistente favorito: ChatGPT** 😎
    """
    enviar_email(destinatario, asunto, cuerpo)
