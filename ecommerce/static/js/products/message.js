document.addEventListener('DOMContentLoaded', function() {
    const alert = document.getElementById('alert');
    
    if (alert){
        alert.classList.remove('hidden');
        setTimeout(function() {
            alert.classList.add('hidden');
        }, 1500);
    }
});