# Agente de Chat NBC Sport

Un agente de chat inteligente con respuestas preprogramadas y la capacidad de agregar nuevas instrucciones de forma dinámica.

## 🌟 Características

- **Respuestas Preprogramadas**: El agente viene con un conjunto de respuestas predefinidas para preguntas comunes sobre NBC Sport.
- **Instrucciones Personalizables**: Puedes agregar nuevas instrucciones y respuestas en tiempo real.
- **Historial de Conversación**: Mantiene un registro de todas las interacciones.
- **Persistencia de Datos**: Las nuevas instrucciones se guardan automáticamente en un archivo de configuración.
- **Búsqueda Inteligente**: Busca coincidencias exactas y parciales en las palabras clave.

## 📋 Requisitos

- Python 3.6 o superior
- No requiere bibliotecas externas (solo módulos estándar de Python)

## 🚀 Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/vivetelotvplay/NBC-Sport-.git
cd NBC-Sport-
```

2. El agente está listo para usar, no requiere instalación adicional.

## 💻 Uso

### Ejecución Básica

Para iniciar el agente de chat, ejecuta:

```bash
python3 chat_agent.py
```

### Comandos Disponibles

El agente de chat reconoce los siguientes comandos especiales:

| Comando | Descripción |
|---------|-------------|
| `/ayuda` | Muestra información de ayuda |
| `/listar` | Lista todas las instrucciones disponibles |
| `/agregar` | Agrega una nueva instrucción/respuesta |
| `/historial` | Muestra el historial de conversación |
| `/limpiar` | Limpia el historial de conversación |
| `/salir` | Sale del programa |

### Ejemplos de Uso

#### 1. Conversación Normal

```
Tú: hola
Agente: ¡Hola! Soy el agente de chat de NBC Sport. ¿En qué puedo ayudarte?

Tú: deportes
Agente: NBC Sport transmite una amplia variedad de deportes incluyendo fútbol, básquetbol, béisbol, hockey y más.
```

#### 2. Agregar una Nueva Instrucción

```
Tú: /agregar

--- Agregar Nueva Instrucción ---
Palabra clave: hockey
Respuesta: NBC Sport transmite los mejores juegos de hockey sobre hielo, incluyendo la NHL.
✓ Nueva instrucción agregada: 'hockey'
```

#### 3. Listar Instrucciones

```
Tú: /listar

=== Instrucciones Preprogramadas ===
1. 'hola' -> ¡Hola! Soy el agente de chat de NBC Sport. ¿En...
2. 'ayuda' -> Puedo responder preguntas sobre deportes, event...
3. 'deportes' -> NBC Sport transmite una amplia variedad de de...
...
```

#### 4. Ver Historial

```
Tú: /historial

=== Historial de Conversación ===

[2025-11-21T16:46:00.123456]
Usuario: hola
Agente: ¡Hola! Soy el agente de chat de NBC Sport. ¿En qué puedo ayudarte?

[2025-11-21T16:46:15.789012]
Usuario: deportes
Agente: NBC Sport transmite una amplia variedad de deportes...
```

## 📁 Estructura del Proyecto

```
NBC-Sport-/
├── chat_agent.py          # Código principal del agente de chat
├── config.json            # Archivo de configuración con respuestas preprogramadas
└── README.md              # Este archivo
```

## ⚙️ Configuración

El archivo `config.json` contiene las respuestas preprogramadas y las instrucciones personalizadas. Tiene la siguiente estructura:

```json
{
  "responses": {
    "palabra_clave": "respuesta correspondiente",
    ...
  },
  "custom_instructions": [
    {
      "keyword": "palabra_clave",
      "response": "respuesta",
      "added_at": "2025-11-21T16:46:00.000Z"
    }
  ],
  "last_updated": "2025-11-21T16:46:00.000Z"
}
```

### Respuestas Preprogramadas Incluidas

El agente viene con respuestas preprogramadas para:

- Saludos (hola)
- Ayuda (ayuda)
- Información de deportes (deportes, futbol, basquetbol, beisbol)
- Horarios (horarios)
- Contacto (contacto)
- Despedidas (adios)
- Agradecimientos (gracias)
- Noticias (noticias)
- Streaming (streaming)
- Suscripción (suscripcion)

## 🔧 Personalización

### Agregar Respuestas Manualmente

Puedes editar el archivo `config.json` directamente para agregar nuevas respuestas:

```json
{
  "responses": {
    "nueva_palabra": "Nueva respuesta personalizada"
  }
}
```

### Agregar Respuestas en Tiempo de Ejecución

Usa el comando `/agregar` dentro del chat para agregar nuevas instrucciones sin editar archivos.

## 🧪 Características Técnicas

### Clase `ChatAgent`

La clase principal que maneja toda la lógica del agente:

- **`load_config()`**: Carga la configuración desde el archivo JSON
- **`save_config()`**: Guarda la configuración actual
- **`add_instruction(keyword, response)`**: Agrega una nueva instrucción
- **`find_response(message)`**: Busca una respuesta apropiada
- **`process_message(message)`**: Procesa un mensaje y genera una respuesta
- **`list_instructions()`**: Lista todas las instrucciones disponibles
- **`show_conversation_history(limit)`**: Muestra el historial de conversación
- **`clear_history()`**: Limpia el historial

### Búsqueda de Respuestas

El agente utiliza dos métodos de búsqueda:

1. **Coincidencia Exacta**: Busca primero una coincidencia exacta con la palabra clave
2. **Coincidencia Parcial**: Si no hay coincidencia exacta, busca palabras clave contenidas en el mensaje

## 📝 Ejemplo de Uso Programático

También puedes usar el agente en tu propio código:

```python
from chat_agent import ChatAgent

# Crear una instancia del agente
agent = ChatAgent(config_file='config.json')

# Procesar un mensaje
response = agent.process_message("hola")
print(response)

# Agregar una nueva instrucción
agent.add_instruction("nuevo_tema", "Esta es una respuesta sobre un nuevo tema")

# Listar todas las instrucciones
agent.list_instructions()
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Agrega nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## 📞 Contacto

Para preguntas o soporte, por favor contacta a través del repositorio de GitHub.

## 🔄 Actualizaciones Futuras

Próximas características planificadas:

- [ ] Integración con base de datos
- [ ] API REST para acceso remoto
- [ ] Interfaz web
- [ ] Procesamiento de lenguaje natural (NLP) para respuestas más inteligentes
- [ ] Soporte multiidioma
- [ ] Análisis de sentimientos
- [ ] Exportación de historial de conversaciones

---

Desarrollado con ❤️ para NBC Sport
