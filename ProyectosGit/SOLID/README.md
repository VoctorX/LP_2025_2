# 💡 Principio Open/Closed (OCP) – Lenguajes de Programacion

---

## 🧠 Descripción
Este trabajo aplica el **principio Open/Closed (Abierto/Cerrado)**, uno de los principios SOLID.  
Este principio establece que las clases deben estar **abiertas a la extensión**, pero **cerradas a la modificación**.  
En otras palabras, el código debe permitir agregar nuevas funciones sin tener que cambiar lo que ya existe.

## 🧩 Explicación del Proyecto
En el ejemplo práctico se desarrolló un **sistema de pagos** en Python, donde el usuario puede elegir entre distintos métodos como **tarjeta**, **efectivo**, **PayPal** o **criptomonedas**.  
Cada método está implementado como una clase independiente que hereda de una clase base llamada `MetodoPago`.

Gracias a esta estructura, si en el futuro se desea agregar un nuevo método, como **Nequi** o **Wompi**, se puede hacer simplemente **creando una nueva clase**, sin modificar las ya existentes.  
Esto demuestra que el sistema está **abierto a la extensión** (pueden añadirse nuevos tipos de pago), pero **cerrado a la modificación** (no hay que alterar el código antiguo).

## 🎯 Justificación de la elección
Elegí el principio **Open/Closed** porque es muy útil en proyectos reales donde constantemente se agregan nuevas funciones o requisitos.  
Permite mantener el código estable y reduce el riesgo de errores al evitar modificar partes que ya funcionan correctamente.

## 📚 Aprendizaje obtenido
Al implementar este principio, comprendí la importancia de diseñar clases que sean **flexibles y escalables**.  
También aprendí que aplicar correctamente el Open/Closed hace que el mantenimiento del software sea más sencillo, organizado y profesional.

---

## ⚙️ Detalles técnicos
- **Lenguaje:** Python 3  
- **Entorno recomendado:** Visual Studio Code  
- **Principio aplicado:** OCP (Open/Closed)

## Construido con 🛠️

_Herramientas y lenguajes utilizados en los proyectos de este repositorio:_

* [Git](https://git-scm.com/) - Control de versiones ![GitHub](https://img.shields.io/badge/GitHub-actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
* [Visual Studio Code](https://code.visualstudio.com/) - Editor de código
* [Python](https://www.python.org/) - Lenguaje de programación ![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## Autor ✒️

* **Victor Cordoba** - *Creador y desarrollador principal* - [VoctorX](https://github.com/VoctorX)

## Licencia 📄

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Apoyame 🎁

* Comenta a otros sobre este proyecto 📢
* Da las gracias públicamente 🤓.
* Dona con cripto a esta dirección: `0x95d80d2e959099458EDCfd3E14391A44F532177a`
* Dona con Paypal: [![Donar con PayPal](https://img.shields.io/badge/Donar%20con-PayPal-00457C?logo=paypal&logoColor=white)](https://www.paypal.com/donate/?business=cordobavictorml@gmail.com&no_recurring=0&currency_code=USD) 
