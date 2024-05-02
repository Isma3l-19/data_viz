document.addEventListener('DOMContentLoaded', function() {
    var viewDataBtn = document.getElementById('viewDataBtn');

    viewDataBtn.addEventListener('click', function() {
        window.location.href = '/view_data/<filename>';  // Navigate to the view data route
    });
});
