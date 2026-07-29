import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [story, setStory] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [analysis, setAnalysis] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [images, setImages] = useState({});
const [generatingImage, setGeneratingImage] = useState(null);

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
  const analyzeStory = async () => {
  if (!story) return;

  setAnalyzing(true);

  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/analyze/",
      {
        story: story,
      }
    );

    setAnalysis(response.data);
  } catch (error) {
    console.error(error);
    alert("Failed to analyze story.");
  }

  setAnalyzing(false);
};

const generateImage = async (sceneNumber, prompt) => {
  setGeneratingImage(sceneNumber);

  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/image/generate",
      {
        prompt: prompt,
      }
    );

    if (response.data.success) {
      setImages((prev) => ({
        ...prev,
        [sceneNumber]: response.data.image,
      }));
    } else {
      alert(
  `${response.data.provider}: ${response.data.message}`
);
    }
  } catch (error) {
    console.error(error);
    alert("Image generation failed.");
  }

  setGeneratingImage(null);
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
      <br />

<button
  onClick={analyzeStory}
  disabled={!story || analyzing}
>
  {analyzing ? "Analyzing..." : "Analyze Story"}
</button>

      {error && <p className="error">{error}</p>}

      {story && (
        <>
          <h2>Generated Story</h2>

          <div className="story-box">
            {story}
          </div>
          {analysis && (
  <>
    <h2>Story Summary</h2>
    <div className="story-box">
      {analysis.summary}
    </div>
  </>
)}
{analysis && (
  <>
    <h2>Characters</h2>

    <div className="characters-list">
  <ul>
    {analysis.characters.map((character, index) => (
      <li key={index}>{character}</li>
    ))}
  </ul>
</div>
  </>
)}

{analysis && (
  <>
    <h2>Storyboard</h2>

    {analysis.scenes.map((scene) => (
      <div
        key={scene.scene}
        className="story-box"
        style={{ marginBottom: "20px" }}
      >
        <h3>Scene {scene.scene}</h3>

        <p>
          <strong>Description:</strong>
        </p>

        <p>{scene.description}</p>

        <p>
          <strong>Visual Prompt:</strong>
        </p>

        <p>{scene.visual_prompt}</p>
        <button
  onClick={() => navigator.clipboard.writeText(scene.visual_prompt)}
>
  📋 Copy Prompt
</button>
<button
  onClick={() =>
    generateImage(scene.scene, scene.visual_prompt)
  }
>
  {generatingImage === scene.scene
    ? "Generating..."
    : "🖼 Generate Image"}
</button>
{images[scene.scene] && (
  <img
    src={images[scene.scene]}
    alt={`Scene ${scene.scene}`}
    style={{
      width: "100%",
      marginTop: "20px",
      borderRadius: "10px",
    }}
  />
)}
      </div>
    ))}
  </>
)}

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