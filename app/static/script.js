// Slideshow Logic
let currentIndex = 0;
const images = document.querySelectorAll('.slides img');

function showNextImage() {
    images[currentIndex].style.display = 'none';
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].style.display = 'block';
}

setInterval(showNextImage, 3000);

// Alarm Toggle
document.getElementById('alarm-toggle').addEventListener('click', () => {
    const alarmIndicator = document.getElementById('alarm-indicator');
    alarmIndicator.classList.toggle('alarm-on');
});
