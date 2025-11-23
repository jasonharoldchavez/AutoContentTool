async function generate() {
    const text = document.getElementById("userInput").value;

    const response = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: text })
    });

    const data = await response.json();
    document.getElementById("output").innerText = data.result || "No response.";
}
