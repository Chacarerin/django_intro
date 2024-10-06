document.addEventListener('DOMContentLoaded', function () {
    const themeToggleBtn = document.getElementById('theme-toggle');  // Botón de alternancia
    const themeIcon = document.getElementById('theme-icon');  // Icono del sol/luna
    const navbar = document.querySelector('.navbar');  // Seleccionar el navbar
    const currentTheme = localStorage.getItem('theme') || 'light';  // Tema guardado o predeterminado

    // Establecer el tema inicial basado en la preferencia guardada
    setTheme(currentTheme);

    // Alternar entre temas cuando el usuario hace clic en el botón
    themeToggleBtn.addEventListener('click', function () {
        const newTheme = document.body.classList.contains('dark-theme') ? 'light' : 'dark';
        setTheme(newTheme);
    });

    // Función para establecer el tema
    function setTheme(theme) {
        if (theme === 'dark') {
            document.body.classList.add('dark-theme');  // Añadir la clase para tema oscuro
            navbar.classList.add('dark-theme');  // Añadir la clase al navbar
            themeIcon.classList.remove('fa-sun');  // Cambiar el icono de sol a luna
            themeIcon.classList.add('fa-moon');
        } else {
            document.body.classList.remove('dark-theme');  // Quitar la clase para volver al tema claro
            navbar.classList.remove('dark-theme');  // Quitar la clase del navbar
            themeIcon.classList.remove('fa-moon');  // Cambiar el icono de luna a sol
            themeIcon.classList.add('fa-sun');
        }
        localStorage.setItem('theme', theme);  // Guardar la preferencia del usuario
    }
});

// Exportar a Excel:

document.getElementById('export-btn').addEventListener('click', function() {
    var table = document.getElementById("vehiculo-table");
    var workbook = XLSX.utils.table_to_book(table, {sheet: "Vehiculos"});
    XLSX.writeFile(workbook, "Listado_Vehiculos.xlsx");
});