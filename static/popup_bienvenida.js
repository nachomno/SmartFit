// popup_bienvenida.js

function mostrarAlert() {
   alert("Te has registrado exitosamente.");
   window.location.href = "/inicio_prueba"; // Redirige a la página de inicio en Flask
}

window.onload = function() {
   // Comprobar si el mensaje de registro está presente
   if (mensajeRegistro) {
      mostrarAlert();
   }
};

 