const textarea = document.getElementById("text");

textarea.addEventListener('focus', (event) => {
    alert("asidhiasuhh")
  event.target.style.transform = "scale(1.2)";
});

textarea.addEventListener('blur', (event) => {
    alert("asidhiasuhh")
    event.target.style.transform = "scale(1)";
});