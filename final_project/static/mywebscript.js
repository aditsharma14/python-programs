let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const responseContainer = document.getElementById("system_response");

    responseContainer.textContent = "Analyzing...";

    fetch("/emotionDetector", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: textToAnalyze })
    })
        .then((response) => response.json().then((data) => ({ status: response.status, data })))
        .then(({ status, data }) => {
            if (status !== 200) {
                responseContainer.textContent = `Error: ${data.error || 'Unable to analyze text.'}`;
                return;
            }
            responseContainer.textContent = JSON.stringify(data, null, 2);
        })
        .catch((error) => {
            responseContainer.textContent = `Network error: ${error.message}`;
        });
};
