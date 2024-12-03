document.getElementById('emotionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const text = document.getElementById('text').value;

    // Call Flask API
    const response = await fetch('/detect-emotion', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });

    const data = await response.json();
    if (data.error) {
        alert(data.error);
    } else {
        document.getElementById('emotion').innerText = data.emotion;
        document.getElementById('emoji').innerText = data.emoji;
        document.getElementById('confidence').innerText = `${(data.confidence * 100).toFixed(2)}%`;
    }
});
