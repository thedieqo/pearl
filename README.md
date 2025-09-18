# 🪙 Joyería Perla – Arquitectura y Proyecto (Primera Entrega)

## 🎯 Objetivo
Construir una solución distribuida para flujo de pedidos orquestado con **Saga**, usando mensajería, seguridad con **JWT**, observabilidad y despliegue en contenedores.

---

## 🛠️ Servicios (cada uno con su propia BD)
- **Pedidos**: orquestador de la Saga.  
- **Inventario**: reserva/compensación.  
- **Pagos**: simulado (aprueba/rechaza).  
- **Catálogo**: consulta de productos (sólo lectura).  

---

## 👥 Casos de uso (resumen)
- **Cliente**: consultar catálogo, crear pedido, consultar estado.  
- **Administrador**: gestionar productos, revisar métricas/logs.  
- **Inventario**: reservar stock, compensar (liberar stock).  
- **Pagos**: procesar pago (aprobado/rechazado).  

---

## 📊 Diagramas

### Diagrama de casos de uso (Mermaid)
> GitHub renderiza Mermaid automáticamente.

```mermaid
flowchart LR
subgraph Actores
A[Cliente]
B[Administrador]
C[Sistema de Inventario]
D[Sistema de Pagos]
end

subgraph Sistema de Pedidos (Saga)
U1[(Consultar catálogo)]
U2[(Crear pedido)]
U3[(Consultar estado del pedido)]
U4[(Gestionar productos inventario)]
U5[(Revisar métricas / logs)]
U6[(Reservar stock)]
U7[(Compensar stock)]
U8[(Procesar pago)]
U9[(Confirmar pedido)]
U10[(Cancelar pedido)]
end

A --> U1
A --> U2
A --> U3
B --> U4
B --> U5
C --> U6
C --> U7
D --> U8
U2 --> U6 --> U8 --> U9
U8 --> U10

 Instalación y ejecución local

1. Clonar el repositorio
git clone https://github.com/tuusuario/joyeria_perla.git
cd joyeria_perla

2. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Instalar dependencias
pip install -r requirements.txt

4. Configurar la base de datos
En joyeria/settings.py, ajusta según tu entorno. Por ahora se usa SQLite por simplicidad:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

5. Migraciones y superusuario
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

6. Levantar el servidor
python manage.py runserver

La app estará disponible en: http://127.0.0.1:8000

📡 Endpoints principales (API REST)
	•	Productos (Inventario/Catálogo):
	•	GET /api/productos/ → listar productos
	•	POST /api/productos/ → crear producto
	•	Clientes:
	•	GET /api/clientes/ → listar clientes
	•	POST /api/clientes/ → crear cliente
	•	Ventas/Pedidos:
	•	GET /api/ventas/ → listar ventas
	•	POST /api/ventas/ → crear venta

⸻

🔐 Seguridad
	•	Autenticación con JWT (próxima iteración).
	•	Roles básicos: cliente y admin.

⸻

📊 Observabilidad
	•	Logs centralizados.
	•	Métricas por servicio.
	•	Tracing del flujo Saga (en diseño).

⸻

🐳 Despliegue con Docker

En la siguiente entrega se usará docker-compose.yml para levantar:
	•	django (servicios)
	•	mysql/postgres (según BD final)
	•	rabbitmq o kafka (mensajería).