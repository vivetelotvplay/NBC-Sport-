#!/usr/bin/env python3
"""
Ejemplo de uso del agente de chat NBC Sport
"""

import os
from chat_agent import ChatAgent


def demo_basic_usage():
    """Demuestra el uso básico del agente de chat."""
    print("=" * 60)
    print("DEMO: Uso Básico del Agente de Chat")
    print("=" * 60)
    
    # Crear instancia del agente
    agent = ChatAgent('config.json')
    
    # Ejemplos de conversación
    messages = [
        "hola",
        "¿qué deportes transmiten?",
        "horarios",
        "gracias"
    ]
    
    for msg in messages:
        print(f"\nUsuario: {msg}")
        response = agent.process_message(msg)
        print(f"Agente: {response}")


def demo_add_instructions():
    """Demuestra cómo agregar nuevas instrucciones."""
    print("\n\n" + "=" * 60)
    print("DEMO: Agregar Nuevas Instrucciones")
    print("=" * 60)
    
    agent = ChatAgent('config_demo.json')
    
    # Agregar nuevas instrucciones
    print("\n1. Agregando instrucciones personalizadas...")
    agent.add_instruction('tenis', 'NBC Sport transmite torneos de tenis como el US Open y más.')
    agent.add_instruction('golf', 'Disfruta del golf de clase mundial en NBC Sport.')
    agent.add_instruction('olimpiadas', 'NBC Sport es tu hogar oficial para las Olimpiadas.')
    
    # Probar las nuevas instrucciones
    print("\n2. Probando las nuevas instrucciones...")
    test_messages = ['tenis', 'golf', 'olimpiadas']
    
    for msg in test_messages:
        print(f"\nUsuario: {msg}")
        response = agent.process_message(msg)
        print(f"Agente: {response}")


def demo_conversation_history():
    """Demuestra el historial de conversación."""
    print("\n\n" + "=" * 60)
    print("DEMO: Historial de Conversación")
    print("=" * 60)
    
    agent = ChatAgent('config_demo.json')
    
    # Simular conversación
    conversation = [
        "hola",
        "deportes",
        "futbol",
        "horarios",
        "adios"
    ]
    
    print("\n1. Simulando conversación...")
    for msg in conversation:
        agent.process_message(msg)
        print(f"   - {msg}")
    
    # Mostrar historial
    print("\n2. Mostrando historial completo:")
    agent.show_conversation_history(10)


def demo_list_instructions():
    """Demuestra cómo listar todas las instrucciones."""
    print("\n\n" + "=" * 60)
    print("DEMO: Listar Instrucciones")
    print("=" * 60)
    
    agent = ChatAgent('config.json')
    agent.list_instructions()


def main():
    """Ejecuta todos los demos."""
    try:
        demo_basic_usage()
        demo_add_instructions()
        demo_conversation_history()
        demo_list_instructions()
        
        print("\n\n" + "=" * 60)
        print("✓ Todos los demos completados exitosamente")
        print("=" * 60)
        
        # Limpiar archivos de demo
        if os.path.exists('config_demo.json'):
            os.remove('config_demo.json')
            print("\n✓ Archivos de demo limpiados")
    
    except Exception as e:
        print(f"\n✗ Error en demo: {e}")


if __name__ == "__main__":
    main()
