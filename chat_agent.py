#!/usr/bin/env python3
"""
Chat Agent - Agente de chat con respuestas preprogramadas y capacidad para agregar instrucciones
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime


class ChatAgent:
    """
    Agente de chat que puede responder mensajes preprogramados y aceptar nuevas instrucciones.
    """
    
    def __init__(self, config_file: str = "config.json"):
        """
        Inicializa el agente de chat.
        
        Args:
            config_file: Ruta al archivo de configuración con respuestas preprogramadas
        """
        self.config_file = config_file
        self.responses = {}
        self.custom_instructions = []
        self.conversation_history = []
        self.load_config()
    
    def load_config(self):
        """Carga las respuestas preprogramadas desde el archivo de configuración."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.responses = data.get('responses', {})
                    self.custom_instructions = data.get('custom_instructions', [])
                    print(f"✓ Configuración cargada desde {self.config_file}")
            except Exception as e:
                print(f"✗ Error al cargar la configuración: {e}")
                self.initialize_default_config()
        else:
            print(f"⚠ Archivo de configuración no encontrado. Creando configuración por defecto...")
            self.initialize_default_config()
    
    def initialize_default_config(self):
        """Inicializa las respuestas preprogramadas por defecto."""
        self.responses = {
            "hola": "¡Hola! Soy el agente de chat de NBC Sport. ¿En qué puedo ayudarte?",
            "ayuda": "Puedo responder preguntas sobre deportes, eventos y horarios. También puedes agregar nuevas instrucciones usando el comando 'agregar instrucción'.",
            "deportes": "NBC Sport transmite una amplia variedad de deportes incluyendo fútbol, básquetbol, béisbol, hockey y más.",
            "horarios": "Los horarios de transmisión varían según el evento. Por favor, visita nuestro sitio web para información actualizada.",
            "contacto": "Puedes contactarnos a través de nuestro sitio web o redes sociales oficiales.",
            "adios": "¡Hasta luego! Que tengas un excelente día.",
            "gracias": "¡De nada! Estoy aquí para ayudarte.",
        }
        self.custom_instructions = []
        self.save_config()
    
    def save_config(self):
        """Guarda la configuración actual en el archivo."""
        try:
            data = {
                'responses': self.responses,
                'custom_instructions': self.custom_instructions,
                'last_updated': datetime.now().isoformat()
            }
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✓ Configuración guardada en {self.config_file}")
        except Exception as e:
            print(f"✗ Error al guardar la configuración: {e}")
    
    def add_instruction(self, keyword: str, response: str):
        """
        Agrega una nueva instrucción/respuesta al agente.
        
        Args:
            keyword: Palabra clave que activará la respuesta
            response: Respuesta a dar cuando se detecte la palabra clave
        """
        keyword = keyword.lower().strip()
        self.responses[keyword] = response
        
        instruction_record = {
            'keyword': keyword,
            'response': response,
            'added_at': datetime.now().isoformat()
        }
        self.custom_instructions.append(instruction_record)
        
        self.save_config()
        print(f"✓ Nueva instrucción agregada: '{keyword}'")
    
    def find_response(self, message: str) -> Optional[str]:
        """
        Busca una respuesta apropiada para el mensaje dado.
        
        Args:
            message: Mensaje del usuario
            
        Returns:
            Respuesta encontrada o None si no hay coincidencia
        """
        message_lower = message.lower().strip()
        
        # Buscar coincidencia exacta
        if message_lower in self.responses:
            return self.responses[message_lower]
        
        # Buscar coincidencia parcial (priorizar palabras clave más largas)
        matches = []
        for keyword, response in self.responses.items():
            if keyword in message_lower:
                matches.append((len(keyword), keyword, response))
        
        # Retornar la coincidencia con la palabra clave más larga
        if matches:
            matches.sort(reverse=True)  # Ordenar por longitud descendente
            return matches[0][2]  # Retornar la respuesta
        
        return None
    
    def process_message(self, message: str) -> str:
        """
        Procesa un mensaje y genera una respuesta.
        
        Args:
            message: Mensaje del usuario
            
        Returns:
            Respuesta del agente
        """
        # Agregar mensaje al historial
        self.conversation_history.append({
            'timestamp': datetime.now().isoformat(),
            'user': message,
            'agent': None
        })
        
        # Buscar respuesta
        response = self.find_response(message)
        
        if response is None:
            response = "No tengo una respuesta preprogramada para eso. Puedes agregar una nueva instrucción o reformular tu pregunta."
        
        # Actualizar historial con la respuesta
        self.conversation_history[-1]['agent'] = response
        
        return response
    
    def list_instructions(self):
        """Lista todas las instrucciones/respuestas disponibles."""
        print("\n=== Instrucciones Preprogramadas ===")
        for i, (keyword, response) in enumerate(self.responses.items(), 1):
            print(f"{i}. '{keyword}' -> {response[:50]}{'...' if len(response) > 50 else ''}")
        
        if self.custom_instructions:
            print("\n=== Instrucciones Personalizadas ===")
            for i, instruction in enumerate(self.custom_instructions, 1):
                print(f"{i}. '{instruction['keyword']}' (Agregada: {instruction['added_at']})")
    
    def show_conversation_history(self, limit: int = 10):
        """
        Muestra el historial de conversación.
        
        Args:
            limit: Número máximo de mensajes a mostrar
        """
        print("\n=== Historial de Conversación ===")
        recent_history = self.conversation_history[-limit:]
        for entry in recent_history:
            print(f"\n[{entry['timestamp']}]")
            print(f"Usuario: {entry['user']}")
            print(f"Agente: {entry['agent']}")
    
    def clear_history(self):
        """Limpia el historial de conversación."""
        self.conversation_history = []
        print("✓ Historial de conversación limpiado")


def main():
    """Función principal para ejecutar el agente de chat."""
    print("=" * 60)
    print("        AGENTE DE CHAT - NBC SPORT")
    print("=" * 60)
    print("\nComandos especiales:")
    print("  /ayuda              - Muestra información de ayuda")
    print("  /listar             - Lista todas las instrucciones")
    print("  /agregar            - Agrega una nueva instrucción")
    print("  /historial          - Muestra el historial de conversación")
    print("  /limpiar            - Limpia el historial")
    print("  /salir              - Sale del programa")
    print("=" * 60)
    
    agent = ChatAgent()
    
    while True:
        try:
            print("\n")
            user_input = input("Tú: ").strip()
            
            if not user_input:
                continue
            
            # Comandos especiales
            if user_input.lower() == '/salir':
                print("\nAgente: ¡Hasta luego!")
                break
            
            elif user_input.lower() == '/ayuda':
                response = agent.find_response("ayuda")
                if response:
                    print(f"\nAgente: {response}")
                else:
                    print("\nAgente: Comando de ayuda disponible. Usa palabras clave como 'hola', 'deportes', 'horarios' o usa /listar para ver todas las opciones.")
            
            elif user_input.lower() == '/listar':
                agent.list_instructions()
            
            elif user_input.lower() == '/agregar':
                print("\n--- Agregar Nueva Instrucción ---")
                keyword = input("Palabra clave: ").strip()
                if not keyword:
                    print("✗ Palabra clave no puede estar vacía")
                    continue
                response_text = input("Respuesta: ").strip()
                if not response_text:
                    print("✗ Respuesta no puede estar vacía")
                    continue
                agent.add_instruction(keyword, response_text)
            
            elif user_input.lower() == '/historial':
                agent.show_conversation_history()
            
            elif user_input.lower() == '/limpiar':
                agent.clear_history()
            
            else:
                # Procesar mensaje normal
                response = agent.process_message(user_input)
                print(f"\nAgente: {response}")
        
        except KeyboardInterrupt:
            print("\n\nAgente: ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n✗ Error: {e}")


if __name__ == "__main__":
    main()
