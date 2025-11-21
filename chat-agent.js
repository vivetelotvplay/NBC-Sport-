// Agente de Chat NBC Sport - Versión JavaScript
class ChatAgent {
    constructor() {
        this.responses = {
            "hola": "¡Hola! Soy el agente de chat de NBC Sport. ¿En qué puedo ayudarte?",
            "ayuda": "Puedo responder preguntas sobre deportes, eventos y horarios. También puedes usar comandos como /listar, /historial y /limpiar.",
            "deportes": "NBC Sport transmite una amplia variedad de deportes incluyendo fútbol, básquetbol, béisbol, hockey y más.",
            "horarios": "Los horarios de transmisión varían según el evento. Por favor, visita nuestro sitio web para información actualizada.",
            "contacto": "Puedes contactarnos a través de nuestro sitio web o redes sociales oficiales.",
            "adios": "¡Hasta luego! Que tengas un excelente día.",
            "gracias": "¡De nada! Estoy aquí para ayudarte.",
            "futbol": "NBC Sport transmite los mejores partidos de fútbol. Consulta nuestra programación para horarios específicos.",
            "basquetbol": "Disfruta de la mejor acción del básquetbol en NBC Sport, incluyendo la NBA y más.",
            "beisbol": "NBC Sport te trae toda la emoción del béisbol, incluyendo la MLB.",
            "noticias": "Visita nuestro sitio web para las últimas noticias deportivas y actualizaciones en tiempo real.",
            "streaming": "NBC Sport está disponible en múltiples plataformas de streaming. Consulta nuestro sitio web para más información.",
            "suscripcion": "Para información sobre suscripciones y paquetes, visita nuestra página web oficial o contacta a servicio al cliente."
        };
        
        this.conversationHistory = [];
        this.loadHistory();
    }

    // Cargar historial desde localStorage
    loadHistory() {
        const saved = localStorage.getItem('chatHistory');
        if (saved) {
            try {
                this.conversationHistory = JSON.parse(saved);
            } catch (e) {
                this.conversationHistory = [];
            }
        }
    }

    // Guardar historial en localStorage
    saveHistory() {
        try {
            localStorage.setItem('chatHistory', JSON.stringify(this.conversationHistory));
        } catch (e) {
            console.error('Error guardando historial:', e);
        }
    }

    // Buscar respuesta para un mensaje
    findResponse(message) {
        const lowerMessage = message.toLowerCase().trim();
        
        // Buscar coincidencia exacta
        if (this.responses[lowerMessage]) {
            return this.responses[lowerMessage];
        }
        
        // Buscar coincidencia parcial
        for (const [keyword, response] of Object.entries(this.responses)) {
            if (lowerMessage.includes(keyword)) {
                return response;
            }
        }
        
        return null;
    }

    // Procesar mensaje del usuario
    processMessage(message) {
        const timestamp = new Date().toISOString();
        
        // Agregar mensaje del usuario al historial
        this.conversationHistory.push({
            type: 'user',
            message: message,
            timestamp: timestamp
        });

        let response;

        // Procesar comandos especiales
        if (message.startsWith('/')) {
            response = this.handleCommand(message);
        } else {
            // Buscar respuesta
            response = this.findResponse(message);
            
            if (!response) {
                response = "Lo siento, no tengo información sobre eso. Intenta preguntar sobre deportes, horarios, streaming o usa /ayuda para ver los comandos disponibles.";
            }
        }

        // Agregar respuesta del agente al historial
        this.conversationHistory.push({
            type: 'agent',
            message: response,
            timestamp: new Date().toISOString()
        });

        this.saveHistory();
        return response;
    }

    // Manejar comandos especiales
    handleCommand(command) {
        const cmd = command.toLowerCase().trim();

        switch (cmd) {
            case '/ayuda':
                return `Comandos disponibles:\n\n` +
                       `• /ayuda - Muestra esta información\n` +
                       `• /listar - Lista todas las palabras clave disponibles\n` +
                       `• /historial - Muestra el historial de conversación\n` +
                       `• /limpiar - Limpia el historial de conversación\n\n` +
                       `También puedes preguntar sobre deportes, horarios, streaming y más.`;

            case '/listar':
                const keywords = Object.keys(this.responses);
                let list = '=== Instrucciones Disponibles ===\n\n';
                keywords.forEach((keyword, index) => {
                    const response = this.responses[keyword];
                    const preview = response.length > 50 ? response.substring(0, 50) + '...' : response;
                    list += `${index + 1}. '${keyword}' → ${preview}\n`;
                });
                return list;

            case '/historial':
                if (this.conversationHistory.length === 0) {
                    return 'No hay historial de conversación.';
                }
                
                let history = '=== Historial de Conversación ===\n\n';
                this.conversationHistory.forEach(entry => {
                    const date = new Date(entry.timestamp).toLocaleString('es-ES');
                    const prefix = entry.type === 'user' ? 'Usuario' : 'Agente';
                    history += `[${date}]\n${prefix}: ${entry.message}\n\n`;
                });
                return history;

            case '/limpiar':
                this.conversationHistory = [];
                this.saveHistory();
                return 'Historial de conversación limpiado.';

            default:
                return `Comando no reconocido: ${command}\nUsa /ayuda para ver los comandos disponibles.`;
        }
    }

    // Limpiar historial
    clearHistory() {
        this.conversationHistory = [];
        this.saveHistory();
    }
}

// Inicializar la aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    const chatAgent = new ChatAgent();
    const chatWindow = document.getElementById('chatWindow');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');

    // Función para agregar mensaje a la ventana de chat
    function addMessage(text, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'agent-message'}`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const prefix = isUser ? '<strong>Tú:</strong> ' : '<strong>Agente:</strong> ';
        
        // Convertir saltos de línea y formato
        let formattedText = text.replace(/\n/g, '<br>');
        
        contentDiv.innerHTML = prefix + formattedText;
        messageDiv.appendChild(contentDiv);
        chatWindow.appendChild(messageDiv);
        
        // Scroll al final
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Función para enviar mensaje
    function sendMessage() {
        const message = userInput.value.trim();
        
        if (message === '') {
            return;
        }

        // Mostrar mensaje del usuario
        addMessage(message, true);

        // Limpiar input
        userInput.value = '';

        // Procesar mensaje y obtener respuesta
        const response = chatAgent.processMessage(message);

        // Mostrar respuesta del agente con un pequeño delay
        setTimeout(() => {
            addMessage(response, false);
        }, 300);
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Foco en el input al cargar
    userInput.focus();

    // Cargar historial previo si existe
    if (chatAgent.conversationHistory.length > 0) {
        const loadPrevious = confirm('¿Deseas cargar el historial de conversación anterior?');
        if (loadPrevious) {
            chatAgent.conversationHistory.forEach(entry => {
                addMessage(entry.message, entry.type === 'user');
            });
        } else {
            chatAgent.clearHistory();
        }
    }
});
