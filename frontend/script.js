document.getElementById("predict-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const form = e.target;
  const data = {
    Time_spent_Alone: parseInt(form.Time_spent_Alone.value),
    Stage_fear: form.Stage_fear.value === "true",
    Social_event_attendance: parseInt(form.Social_event_attendance.value),
    Going_outside: parseInt(form.Going_outside.value),
    Drained_after_socializing: form.Drained_after_socializing.value === "true",
    Friends_circle_size: parseInt(form.Friends_circle_size.value),
    Post_frequency: parseInt(form.Post_frequency.value)
  };

  try {
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText = `Predicted Personality: ${result.personality}`;
    document.getElementById("confidence").innerText = `Confidence: ${result.confidence.toFixed(2)}%`;
  } catch (error) {
    document.getElementById("result").innerText = "Error: Could not connect to backend.";
    console.error(error);
  }
});
