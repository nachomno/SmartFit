// Obtener elementos del DOM
const finalizarBtn = document.getElementById('finalizar-btn');
const modal = document.getElementById('modal');
const closeModal = document.getElementsByClassName('close')[0];
const totalCaloriasSpan = document.getElementById('total-calorias');
const caloriasCheckboxes = document.querySelectorAll('.calorias-checkbox');
const guardarCaloriasBtn = document.getElementById('guardar-calorias');
const idEntrenamiento = document.getElementById('id_entrenamiento').value;

// Función para calcular las calorías
const calcularCalorias = () => {
    let totalCalorias = 0;
    caloriasCheckboxes.forEach(checkbox => {
        if (checkbox.checked) {
            totalCalorias += parseInt(checkbox.getAttribute('data-calorias'));
        }
    });
    return totalCalorias;
};

// Evento para mostrar el modal
finalizarBtn.addEventListener('click', () => {
    const totalCalorias = calcularCalorias();
    totalCaloriasSpan.textContent = totalCalorias;
    modal.style.display = 'flex'; // Mostrar el modal
});

// Evento para cerrar el modal
closeModal.onclick = function() {
    modal.style.display = 'none'; // Ocultar el modal
};

// Cerrar el modal al hacer clic fuera de él
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = 'none'; // Ocultar el modal
    }
};

// Evento para guardar las calorías y redirigir al perfil
guardarCaloriasBtn.onclick = function() {
    const totalCalorias = calcularCalorias();
    
    // Realizar la petición POST para enviar calorías y el título del entrenamiento al servidor
    fetch('/actualizar_calorias_y_entrenamiento', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ calorias: totalCalorias, entrenamiento_id: idEntrenamiento })
    })
    .then(response => {
        if (response.ok) {
            console.log("Calorías y entrenamiento enviados correctamente al servidor.");
            modal.style.display = 'none'; // Ocultar el modal
            window.location.href = '/perfil'; // Redirigir al perfil
        } else {
            console.error('Error al actualizar las calorías y el título del entrenamiento');
        }
    })
    .catch(error => console.error('Error en la solicitud:', error));
};