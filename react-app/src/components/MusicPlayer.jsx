import React, { useContext, useState } from 'react';
import { MoodContext } from './context';
import SongList from './SongList';
import AudioControl from './AudioControl';

const MusicPlayer = () => {
    const { mood, setMood } = useContext(MoodContext);
    const { audioSrc, setAudioSrc } = useState('http://localhost:8080/songs/happy/Coke Studio _ Season 14 _ Pasoori _ Ali Sethi x Shae Gill.mp3')


    const gridContainerStyle = {
        display: 'grid',
        gridTemplateRows: '80% 20%',
        height: '100vh', // Ensure the component takes up the entire viewport height
    };

    const rowStyle = {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        color: 'white',
        fontSize: '24px',
    };

    const row1Style = {
        ...rowStyle,
        borderRadius: '50px', // Set border radius to 50px.
        background: '#2a2828', // Set the background color.
        boxShadow: '20px 20px 60px #bebebe, -20px -20px 60px #383636', // Set the box shadow.

    };

    const row2Style = {
        ...rowStyle,
        marginTop : '-35px'

    };

    useState(() => {

    }, [audioSrc])

    return (
        <div>
            <div style={gridContainerStyle}>
                <div style={row1Style}>
                    <SongList />
                </div>
                <div style={row2Style}>
                    <AudioControl />
                </div>

            </div>
        </div>
    );
}

export default MusicPlayer;
