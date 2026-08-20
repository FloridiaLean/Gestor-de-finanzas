# 📊 Gestor de Finanzas Personales

Aplicación personal desarrollada en Python para registrar ingresos, gastos, transferencias y conversiones entre pesos argentinos y dólares en difentes tipos de cuentas ya sean orientadas a ahorros o gastos regulares.

Este proyecto nace de una necesidad real: reemplazar un sistema de seguimiento financiero realizado inicialmente en Excel para migrar a una aplicación más escalable, organizada y adaptable a las necesidades del usuario.

---

## 📚 Pilares de Aprendizaje y Buenas Prácticas

El foco del proyecto no es únicamente el resultado final, sino también el aprendizaje continuo de conceptos técnicos como:

- Programación Orientada a Funciones y Objetos: Modelado limpio del dominio financiero.
- Modularización y Arquitectura Escalable: Diseño pensado desde el día uno para migrar de consola a Flask sin romper el núcleo del negocio.
- Separación de Responsabilidades (SoC): Desacoplamiento total entre la lógica financiera, el almacenamiento de datos (SQL) y la interfaz de usuario.
- Persistencia y Modelado de Datos: Transición de estructuras en memoria hacia una base de datos relacional robusta.
- Control de Versiones Profesional: Uso estratégico de Git con flujo de trabajo basado en ramas (Feature Branch Workflow).

---

## 🎯 Objetivo

Desarrollar una plataforma web para la gestión de gastos personales y poder generar información útil a partir de ellas.

El proyecto tiene como objetivo principal no solo construir la herramienta, sino aplicar de punta a punta las mejores prácticas de ingeniería de software, dominando la separación de responsabilidades, la persistencia relacional y la transición de lógica de consola a un entorno web real.

La aplicación busca ofrecer una visión completa sobre gastos regulares mediante indicadores, resumenes regulares, permitiendo registrar ingresos, gastos transferencias de dinero entre diferentes cuentas desde una interfaz web intuitiva.

El sistema permitirá diferenciar entre el dinero disponible para utilizar y el dinero destinado al ahorro.

### Dinero disponible

Ejemplos de cuentas:
- Mercado Pago
- Efectivo
- Otras cuentas en pesos

Estas cuentas podrán utilizarse para registrar gastos, ingresos y transferencias.

### Ahorro

Inicialmente, el ahorro estará representado por dólares estadounidenses.

El sistema permitirá:
- Comprar dólares utilizando dinero disponible en pesos.
- Vender dólares para obtener dinero disponible en pesos.
- Registrar el precio de compra o venta.
- Calcular el valor estimado del ahorro en pesos argentinos.

Las conversiones entre pesos y dólares no serán consideradas ingresos ni gastos, ya que representan una transformación entre activos propios.

---

## 🧠 Funcionalidades Planificadas

- Gestión de cuentas.
- Registro de ingresos.
- Registro de gastos.
- Transferencias entre cuentas.
- Compra de dólares.
- Venta de dólares.
- Validación de saldo disponible.
- Gestión de categorías.
- Historial de operaciones.
- Filtros por período, categoría y tipo de operación.
- Dashboard financiero.
- Estadísticas mensuales y anuales.
- Visualización de gastos por categoría.

### Tipos de Operaciones

El sistema deberá soportar inicialmente los siguientes tipos de operaciones:

| Operación         | Origen        | Destino       | ¿Representa un gasto? |
| ----------------- | ------------- | ------------- | --------------------- |
| Ingreso           | Externo       | Cuenta        | No                    |
| Gasto             | Cuenta        | Externo       | Sí                    |
| Transferencia     | Cuenta        | Cuenta        | No                    |
| Compra de dólares | Cuenta en ARS | Ahorro en USD | No                    |
| Venta de dólares  | Ahorro en USD | Cuenta en ARS | No                    |


### Ejemplo de cuentas

| Nombre       | Moneda | Propósito  |
| ------------ | ------ | ---------- |
| Mercado Pago | ARS    | Disponible |
| Efectivo     | ARS    | Disponible |
| Ahorro       | USD    | Ahorro     |

---

## 🏗️ Arquitectura Inicial

El proyecto comenzará desarrollando la lógica principal en Python.

Posteriormente se incorporará una base de datos SQLite utilizando SQL para persistir la información.

Finalmente, se desarrollará una interfaz web utilizando Flask, HTML y CSS.

La evolución prevista será:

Lógica en Python
       ↓
Base de datos SQLite + SQL
       ↓
Persistencia de datos
       ↓
Aplicación Flask
       ↓
Interfaz web
       ↓
Dashboard y estadísticas

---

## 🚀 Tecnologías 

Actualmente se planea utilizar:

- Python
- SQLite
- SQL
- Flask
- Jinja2
- HTML
- JavaScript
- JSON
- CSS

Las tecnologías y herramientas podrán evolucionar a medida que avance el proyecto.

---

## 🗺️  Roadmap y Planificación (Sprints)

El proyecto se divide en fases incrementales para asegurar un desarrollo ordenado y medible:

### 🔹 Sprint 0 — Configuración inicial
- ✅ Crear repositorio local.
- ✅ Inicializar Git.
- ✅ Configurar la rama principal main.
- ✅ Crear estructura inicial del proyecto.
- ✅ Crear .gitignore.
- ✅ Crear README inicial.
- ✅ Crear repositorio remoto en GitHub.
- ✅ Realizar el primer commit.
- ✅ Subir el proyecto a GitHub.

### 🔹 Sprint 1 — Núcleo financiero en Python
- ✅ Definir monedas disponibles.
- ✅ Definir propósitos de cuenta.
- ✅ Modelar cuentas.
- ✅ Gestionar saldos.
- [ ] Registrar ingresos.
- [ ] Registrar gastos.
- [ ] Validar saldo disponible.
- [ ] Implementar transferencias entre cuentas.
- [ ] Implementar compra de dólares.
- [ ] Implementar venta de dólares.

### 🔹 Sprint 2 — Base de datos
- [ ] Diseñar el modelo de datos.
- [ ] Crear la base de datos SQLite.
- [ ] Crear tablas.
- [ ] Conectar Python con SQLite.
- [ ] Persistir cuentas.
- [ ] Persistir operaciones.

### 🔹 Sprint 3 — Gestión de categorías
- [ ] Crear categorías.
- [ ] Editar categorías.
- [ ] Eliminar o desactivar categorías.
- [ ] Asociar categorías a operaciones.

### 🔹 Sprint 4 — Historial y consultas
- [ ] Visualizar operaciones.
- [ ] Filtrar por período.
- [ ] Filtrar por categoría.
- [ ] Filtrar por tipo.
- [ ] Consultar saldos.

### 🔹 Sprint 5 — Aplicación web
- [ ] Incorporar Flask.
- [ ] Crear rutas.
- [ ] Crear templates.
- [ ] Integrar la lógica financiera con la aplicación web.

### 🔹 Sprint 6 — Interfaz
- [ ] Crear dashboard general.
- [ ] Registrar operaciones desde formularios.
- [ ] Gestionar cuentas.
- [ ] Gestionar categorías.
- [ ] Crear historial visual.

### 🔹 Sprint 7 — Estadísticas
- [ ] Dashboard mensual.
- [ ] Selector de período.
- [ ] Gastos por categoría.
- [ ] Estadísticas mensuales.
- [ ] Estadísticas anuales.
- [ ] Gráficos.

---

## 🧩 Convención de Commits

El proyecto utilizará los siguientes tipos de commits:

feat: nueva funcionalidad o mejora visible.
fix: corrección de un error.
refactor: reorganización del código sin modificar su comportamiento.
docs: documentación.
test: incorporación o modificación de pruebas.
chore: tareas de mantenimiento, configuración o estructura del proyecto.

---

## 🚀 Estado del Proyecto

🚧 En desarrollo

Actualmente se encuentra en la etapa de configuración inicial y planificación de la arquitectura.


---

## 👨‍💻 Autor

Leandro Floridia

Proyecto personal desarrollado como parte de mi proceso de aprendizaje en:

- Programación en Python
- Arquitectura de Software
- Desarrollo web
- Ciencia de datos aplicada a finanzas
- Git y GitHub

El objetivo del proyecto es evolucionar progresivamente desde una aplicación de consola hasta una aplicación web completa, aplicando buenas prácticas de programación y diseño de software durante todo el proceso.

---
