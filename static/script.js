document.getElementById("actionForm").onsubmit = function(event) {
    event.preventDefault();
    var submitBtn = document.getElementById("submitBtn");
    submitBtn.disabled = true;

    var loadingDiv = document.getElementById("loading");
    var resultDiv = document.getElementById("result");

    // Show loading animation and hide the result
    loadingDiv.style.display = "flex";
    resultDiv.style.display = "none"; 

    var formData = new FormData(document.getElementById("actionForm"));
    fetch('/submit-form', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Populate and show result, hide loading animation
        resultDiv.innerHTML = data;
        resultDiv.style.display = "block"; // or "flex", if using flexbox for result
        loadingDiv.style.display = "none";

        submitBtn.disabled = false;
    });
};

function copyToClipboard(elementId) {
    var text = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(text);
}
