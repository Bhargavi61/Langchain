// Event listener for the form submission
document.getElementById("question-form").addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent default form submission behavior
    const question = document.getElementById("question").value; // Get the user input

    // Send the question to the backend endpoint
    fetch("http://localhost:5000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json" // Content type for JSON
        },
        body: JSON.stringify({ question: question }) // Convert the question to JSON
    })
    .then((response) => response.json()) // Parse the JSON response
    .then((data) => {
        document.getElementById("answer").innerText = data.answer; // Update the answer area
    })
    .catch((error) => {
        console.error("Error:", error); // Log any errors
    });
});