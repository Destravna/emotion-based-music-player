import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useContext } from 'react';
import { MoodContext } from './context';
import ListGroup from 'react-bootstrap/ListGroup';
import SongListItem from './SongListItem';

const getSongs = async (mood, setSongs) => {
    const response = await axios({
        method: 'GET',
        url: 'http://localhost:8080/getSongList/' + mood
    });
    console.log(response.data);
    setSongs(response.data.songs)

}

const h3Style = {
    color : 'white',
    margin : 'auto',
    textAlign : 'center'
}

const SongList = () => {
    const { mood, setMood } = useContext(MoodContext);
    const [songs, setSongs] = useState([]);

    useEffect(() => {
        getSongs(mood, setSongs);
    }, [mood])

    console.log('mood from song list' + mood);
    return (

        <div>
            <h5 style={h3Style}> you look {mood} </h5>
            <h5 style={h3Style}>Here are some {mood} songs </h5>
            <ListGroup>
                {songs.map(song => {
                    return <SongListItem name={song.name} url={song.url} />
                })}
            </ListGroup>
           
        </div>
    )
}

export default SongList;