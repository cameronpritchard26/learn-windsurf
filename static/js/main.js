// Main JavaScript for Windsurf Learning App

document.addEventListener('DOMContentLoaded', function() {
    // Get Time Button Handler
    const timeBtn = document.getElementById('time-btn');
    const timeDisplay = document.getElementById('time-display');
    
    if (timeBtn && timeDisplay) {
        timeBtn.addEventListener('click', async function() {
            try {
                const response = await fetch('/api/time');
                const data = await response.json();
                timeDisplay.textContent = `Server Time: ${data.time}`;
                timeDisplay.style.display = 'block';
            } catch (error) {
                timeDisplay.textContent = 'Error fetching time';
                console.error('Error:', error);
            }
        });
    }
    
    // Log page load
    console.log('Windsurf Learning App loaded successfully! 🏄');
});
