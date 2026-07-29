import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [story, setStory] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const generateStory = async () => {
    if (!prompt.trim()) {
      setError("Please enter a story prompt.");
      return;
    }

    setLoading(true);
    setStory("");
    setError("");

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/story/generate",
        {
          prompt: prompt,
        }
      );

      setStory(response.data.story);
    } catch (err) {
      console.error(err);
      setError("Unable to generate the story. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const copyStory = async () => {
  try {
    await navigator.clipboard.writeText(story);
    alert("Story copied to clipboard!");
  } catch (err) {
    console.error(err);
    alert("Failed to copy story.");
  }
};

const downloadStory = () => {
  const element = document.createElement("a");

  const file = new Blob([story], {
    type: "text/plain",
  });

  element.href = URL.createObjectURL(file);
  element.download = "storyforge_story.txt";

  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);

  URL.revokeObjectURL(element.href);
};

  return (
    <div className="container">
      <h1>🎬 StoryForge AI</h1>
      <p>AI Story Generator & Creative Director</p>

      <textarea
        rows="8"
        maxLength={500}
        placeholder="Enter your story prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <p className="counter">
        {prompt.length}/500 characters
      </p>

      <button
        onClick={generateStory}
        disabled={loading}
      >
        {loading ? "Generating Story..." : "Generate Story"}
      </button>

      {error && <p className="error">{error}</p>}

      {story && (
        <>
          <h2>Generated Story</h2>

          <div className="story-box">
            {story}
          </div>

          <button
  className="copy-btn"
  onClick={copyStory}
>
  📋 Copy Story
</button>
<button
  className="download-btn"
  onClick={downloadStory}
>
  📥 Download Story
</button>
        </>
      )}
    </div>
  );
}

export default App;