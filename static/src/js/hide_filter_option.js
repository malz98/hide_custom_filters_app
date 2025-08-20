
// Esperamos a que el DOM esté completamente cargado para empezar a observar
odoo.loader.boot.then(() => {
    // El texto que queremos encontrar y ocultar. Puedes cambiarlo si tu Odoo está en otro idioma.
    const textToHide = "Agregar filtro personalizado";

    // Creamos un "observador" que vigile los cambios en la página web.
    // Esto es mucho más eficiente que comprobar constantemente.
    const observer = new MutationObserver((mutationsList, observer) => {
        // Cada vez que algo cambia en la página (se abre un menú, etc.), esto se ejecuta.
        for (const mutation of mutationsList) {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                // Buscamos dentro de toda la página un elemento de menú de Bootstrap (`.dropdown-item`)
                // que contenga exactamente el texto que queremos ocultar.
                const allMenuItems = document.querySelectorAll('.dropdown-item');
                allMenuItems.forEach(item => {
                    if (item.textContent.trim() === textToHide) {
                        // Si lo encontramos, lo ocultamos.
                        item.style.display = 'none';
                    }
                });
            }
        }
    });

    // Le decimos al observador que empiece a vigilar todo el cuerpo de la página
    // y que preste atención a cualquier nodo que se añada o elimine.
    observer.observe(document.body, { childList: true, subtree: true });
});