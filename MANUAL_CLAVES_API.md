# Manual: claves de API gratuitas (Google AI Studio y Pexels)

Las dos son **gratis y sin tarjeta**. Las claves son como contraseñas: **nunca las pegues en el chat de Claude, ni en la Sala, ni en ningún otro sitio** que no sea `config/claves.txt` del Mac. Esa carpeta no se sube nunca a GitHub.

---

## 1. Google AI Studio (voz de Gemini) — PENDIENTE

Sirve para que Claude genere la voz nueva (Gemini TTS), con emoción y mucho más natural que la actual.

1. En el Mac, abre Chrome y entra en **https://aistudio.google.com**.
2. Pulsa **«Sign in» / «Iniciar sesión»** y entra con tu cuenta de Google (la misma de Gemini).
3. La primera vez te pedirá aceptar las condiciones: marca la casilla de las condiciones de uso y pulsa **«Continuar»**. Las casillas de recibir correos son opcionales.
4. En el menú de la izquierda (abajo) o arriba a la derecha, pulsa **«Get API key» / «Obtener clave de API»**.
5. Pulsa **«Create API key» / «Crear clave de API»**. Si te pregunta por un proyecto, elige **«Create API key in new project» / «Crear clave de API en un proyecto nuevo»**.
6. Aparecerá una clave larga que empieza por **AIza…**. Pulsa el icono de **copiar** que tiene al lado.
7. **No actives la facturación.** Si en algún momento te sale «Set up billing» / «Configurar facturación» o te pide una tarjeta, ciérralo: no hace falta, el plan gratuito funciona sin ella.
8. Ahora guarda la clave en el Mac:
   - Abre el **Finder** → **Descargas** → **faceless** → **config**.
   - Haz clic derecho en **claves.txt** → **Abrir con** → **TextEdit**.
   - Ve al final del archivo y escribe una línea nueva exactamente así (con los dos puntos y un espacio): `GEMINI_CLAVE: ` y justo después pega la clave (Cmd + V).
   - Guarda con **Cmd + S** y cierra TextEdit.
9. Dile a Claude: **«ya está la clave de Gemini»**. Claude comprueba que funciona sin enseñarla.

Si algo no coincide (botones con otro nombre, menús en inglés), haz una captura de pantalla de la página **sin la clave visible** y pásasela a Claude.

---

## 2. Pexels (vídeos reales gratis) — YA HECHO EN ESTE MAC

En este Mac la clave de Pexels **ya está guardada y funciona** (comprobado el 29/10/2026). Solo hace falta repetirlo si trabajas en otro ordenador:

1. Entra en **https://www.pexels.com/api/** y pulsa **«Get Started» / «Empezar»**.
2. Crea la cuenta (o entra con Google) y rellena el formulario corto: nombre del proyecto «Ticket Medio», uso «vídeos para YouTube».
3. En **https://www.pexels.com/api/new/** (o en tu perfil → «Image & Video API») verás **«Your API Key»**. Cópiala.
4. Guárdala en `config/claves.txt` igual que la de Google, en una línea: `PEXELS_CLAVE: ` + la clave.
5. Dile a Claude: **«ya está la clave de Pexels»**.

Pexels pide citar al autor cuando se pueda: Claude lo pone en la descripción de cada vídeo.
