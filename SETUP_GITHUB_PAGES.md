# Guía de Configuración de GitHub Pages

Esta guía te ayudará a activar GitHub Pages para que tu sitio web esté disponible públicamente.

## 📝 Pasos para Activar GitHub Pages

### 1. Acceder a la Configuración del Repositorio

1. Ve a tu repositorio en GitHub: https://github.com/vivetelotvplay/NBC-Sport-
2. Haz clic en **"Settings"** (Configuración) en la barra de navegación superior

### 2. Configurar GitHub Pages

1. En el menú lateral izquierdo, busca y haz clic en **"Pages"**
2. En la sección **"Source"** (Fuente):
   - Selecciona la rama que quieres publicar (recomendado: `main` o `copilot/setup-github-pages`)
   - Deja la carpeta como **"/ (root)"**
3. Haz clic en **"Save"** (Guardar)

### 3. Esperar el Despliegue

- GitHub comenzará a construir tu sitio automáticamente
- Este proceso puede tomar de 1 a 5 minutos
- Verás un mensaje indicando que tu sitio se está construyendo

### 4. Acceder a tu Sitio

Una vez completado el despliegue, tu sitio estará disponible en:

**https://vivetelotvplay.github.io/NBC-Sport-/**

## ✅ Verificación

Para verificar que todo funciona correctamente:

1. Visita la URL de tu sitio
2. Deberías ver la interfaz del chat agent de NBC Sport
3. Prueba enviando mensajes como "hola", "deportes", etc.
4. Prueba comandos como `/listar`, `/ayuda`, `/historial`

## 🔄 Actualizaciones

Cada vez que hagas cambios en los archivos HTML, CSS o JavaScript y los subas a la rama configurada:

1. GitHub Pages reconstruirá automáticamente tu sitio
2. Los cambios estarán visibles en unos minutos

## 🛠️ Solución de Problemas

### El sitio no se muestra

- Verifica que hayas seleccionado la rama correcta en la configuración de Pages
- Asegúrate de que el archivo `index.html` esté en la raíz del repositorio
- Espera unos minutos más, el despliegue puede tardar

### Los cambios no se reflejan

- El cache del navegador puede estar mostrando una versión antigua
- Intenta refrescar con Ctrl+F5 (Windows/Linux) o Cmd+Shift+R (Mac)
- Limpia el cache de tu navegador

### Error 404

- Verifica que la configuración de Pages esté activa
- Asegúrate de usar la URL correcta: `https://TU-USUARIO.github.io/NOMBRE-REPO/`

## 📚 Recursos Adicionales

- [Documentación oficial de GitHub Pages](https://docs.github.com/en/pages)
- [Documentación de Jekyll (usado por GitHub Pages)](https://jekyllrb.com/docs/)

## 🎉 ¡Listo!

Tu agente de chat NBC Sport ahora está disponible públicamente en Internet. Puedes compartir la URL con cualquier persona para que pruebe el chat agent.
