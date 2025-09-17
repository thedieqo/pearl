# Joyería Perla — Arquitectura (Primera Entrega)

## Objetivo
Construir una solución distribuida para flujo de pedidos orquestado con **Saga**, usando mensajería, seguridad con **JWT**, observabilidad y despliegue en contenedores.

## Servicios (cada uno con su propia BD)
- **Pedidos** (orquestador de la Saga).
- **Inventario** (reserva/compensación).
- **Pagos** (simulado: aprueba/rechaza).
- **Catálogo** (consulta de productos; solo lectura).

## Casos de uso (resumen)
- Cliente: consultar catálogo, crear pedido, consultar estado.
- Admin: gestionar productos, revisar métricas/logs.
- Inventario: reservar stock, compensar (liberar stock).
- Pagos: procesar pago (aprobado/rechazado).

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
    U1((Consultar catálogo))
    U2((Crear pedido))
    U3((Consultar estado del pedido))
    U4((Gestionar productos inventario))
    U5((Revisar métricas / logs))
    U6((Reservar stock))
    U7((Compensar stock))
    U8((Procesar pago))
    U9((Confirmar pedido))
    U10((Cancelar pedido))
  end

  A --> U1
  A --> U2
  A --> U3
  B --> U4
  B --> U5
  C --> U6
  C --> U7
  D --> U8

  %% Flujo Saga
  U2 --> U6 --> U8
  U8 -->|aprobado| U9
  U8 -->|rechazado| U10 --> U7