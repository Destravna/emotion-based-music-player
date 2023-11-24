import { useState } from "react";
import { MoodContext } from "./components/context";
import { SongContext } from "./components/songContext";
import Profile from "./components/Profile";
import MusicPlayer from "./components/MusicPlayer";

const gridContainerStyle = {
  display: 'grid',
  gridTemplateColumns: '70% 30%',
  width: '100%',
  height: '100vh',
};

const leftColumnStyle = {
  backgroundColor: '#3498db',
  color: '#fff',
  padding: '20px',

}

const rightColumnStyle = {
  backgroundColor: '#3498db',
  color: '#fff',
  textAlign: 'center',
}

function App() {
  const [mood, setMood] = useState('neutral')
  const [song, setSong] = useState('http://localhost:8080/songs/happy/Coke Studio _ Season 14 _ Pasoori _ Ali Sethi x Shae Gill.mp3')
  let value = { mood, setMood }
  let songValue = { song, setSong }

  return (
    <MoodContext.Provider value={value}>
      <SongContext.Provider value={songValue}>
        <div className="grid-container" style={gridContainerStyle}>
          <div style={leftColumnStyle}>
            <MusicPlayer />
          </div>
          <div style={rightColumnStyle}>
            <Profile />
          </div>
        </div>
      </SongContext.Provider>

    </MoodContext.Provider>

  );
}

export default App;
