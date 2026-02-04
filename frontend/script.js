function analyze() {
  fetch("http://127.0.0.1:8000/honeypot", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": "nandhini-honeypot-key"
    },
    body: JSON.stringify({
      sessionId: "frontend-dashboard",
      message: {
        sender: "scammer",
        text: document.getElementById("msg").value,
        timestamp: new Date().toISOString()
      }
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("reply").innerText = data.reply;
    document.getElementById("type").innerText = data.scamType;
    document.getElementById("keywords").innerText = data.keywords.join(", ");
    document.getElementById("confidence").innerText = data.confidence;
  });
}
