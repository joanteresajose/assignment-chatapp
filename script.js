// JavaScript to dynamically adjust width based on screen size
document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggle-menu');
    const leftMenu = document.querySelector('.left-menu');

    toggleButton.addEventListener('click', () => {
        // Toggle the 'collapsed' class on the left menu
        leftMenu.classList.toggle('collapsed');

        // Change the button text based on the menu state
        if (leftMenu.classList.contains('collapsed')) {
            toggleButton.textContent = 'Expand';
        } else {
            toggleButton.textContent = 'Collapse';
        }
    });
});
