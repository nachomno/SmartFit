document.getElementById("principiante-btn").addEventListener("click", function() {
    document.getElementById("principiante").style.display = "flex";
    document.getElementById("intermedio").style.display = "none";
    document.getElementById("avanzado").style.display = "none";
    
    // Cambiar el fondo de los botones
    document.getElementById("principiante-btn").classList.add("activo");
    document.getElementById("intermedio-btn").classList.remove("activo");
    document.getElementById("avanzado-btn").classList.remove("activo");
    //desplazar hacia abajo
    if (window.scrollY === 0) {
        window.scrollBy(0, 300);
    }
});

document.getElementById("intermedio-btn").addEventListener("click", function() {
    document.getElementById("principiante").style.display = "none";
    document.getElementById("intermedio").style.display = "flex";
    document.getElementById("avanzado").style.display = "none";
    
    // Cambiar el fondo de los botones
    document.getElementById("principiante-btn").classList.remove("activo");
    document.getElementById("intermedio-btn").classList.add("activo");
    document.getElementById("avanzado-btn").classList.remove("activo");
    //desplazar hacia abajo
    if (window.scrollY === 0) {
        window.scrollBy(0, 300);
    }
});

document.getElementById("avanzado-btn").addEventListener("click", function() {
    document.getElementById("principiante").style.display = "none";
    document.getElementById("intermedio").style.display = "none";
    document.getElementById("avanzado").style.display = "flex";
    
    // Cambiar el fondo de los botones
    document.getElementById("principiante-btn").classList.remove("activo");
    document.getElementById("intermedio-btn").classList.remove("activo");
    document.getElementById("avanzado-btn").classList.add("activo");
    //desplazar hacia abajo
    if (window.scrollY === 0) {
        window.scrollBy(0, 300);
    }
});

                                // codigo para calcular el IMC

document.getElementById('calcularBtn').addEventListener('click', function () {
    const nombre = document.getElementById('nombre').value;
    const altura = parseFloat(document.getElementById('altura').value) / 100; // Convertimos de cm a metros
    const peso = parseFloat(document.getElementById('peso').value);

    if (isNaN(altura) || isNaN(peso) || !nombre) {
        alert("Por favor, ingresa todos los campos.");
        return;
    }

    const imc = peso / (altura * altura);
    let estadoPeso = '';
    let caloriasQuemar = 0;

    if (imc < 18.5) {
        estadoPeso = 'Bajo peso';
        caloriasQuemar = 1500; // Ejemplo
    } else if (imc >= 18.5 && imc <= 24.9) {
        estadoPeso = 'Saludable';
        caloriasQuemar = 2000; // Ejemplo
    } else if (imc >= 25 && imc <= 29.9) {
        estadoPeso = 'Exceso de peso';
        caloriasQuemar = 2500; // Ejemplo
    } else {
        estadoPeso = 'Obeso';
        caloriasQuemar = 3000; // Ejemplo
    }

    document.getElementById('resultadoIMC').innerHTML = `
        <p>Hola ${nombre}, tu IMC es de ${imc.toFixed(2)} y tu estado de peso es ${estadoPeso}. 
        Necesitarías quemar aproximadamente ${caloriasQuemar} calorías al día.</p>`;
});
