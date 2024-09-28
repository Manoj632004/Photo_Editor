window.onload = function() {
    const brightnessToggle = document.getElementById("brightness-toggle") as HTMLInputElement;
    const brightnessSlider = document.getElementById("brightness-slider") as HTMLInputElement;
    const rotateToggle = document.getElementById("rotate-toggle") as HTMLInputElement;
    const rotateSelect = document.getElementById("rotate-select") as HTMLSelectElement;

    brightnessToggle.addEventListener("change", function() {
        brightnessSlider.style.display = brightnessToggle.checked ? "block" : "none";
    });

    rotateToggle.addEventListener("change", function() {
        rotateSelect.style.display = rotateToggle.checked ? "block" : "none";
    });
};
