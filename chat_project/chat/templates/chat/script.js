// Script to toggle the left menu visibility
document.getElementById('toggleMenu').addEventListener('click', function() {
    var leftMenu = document.getElementById('leftMenu');
    leftMenu.classList.toggle('collapsed');
    this.textContent = leftMenu.classList.contains('collapsed') ? 'Expand' : 'Collapse';
});

