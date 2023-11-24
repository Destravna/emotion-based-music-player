import React, { useContext, useEffect } from 'react'
import { SongContext } from './songContext'

const AudioControl = () => {
    const { song, setSong } = useContext(SongContext);
    useEffect(()=>{

    }, [song])
    console.log("song from context " + song);
    return (
        <audio controls src={song} autoPlay type="audio/mp3">
            your browser has no audio tag
        </audio>
    )
}

export default AudioControl