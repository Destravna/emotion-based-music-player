import React, { useContext } from 'react';
import { SongContext } from './songContext';
import { ListGroup } from 'react-bootstrap';
import { AiFillPlayCircle } from 'react-icons/ai';

const ItemStyle = {
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  padding: '8px 16px',
  border: '1px solid transparent', // Transparent border to create smooth borders without gaps.
  borderRadius: '5px',
  fontSize: '15px',
  width: '700px',
};

const SongListItem = ({ name, url }) => {
  const { song, setSong } = useContext(SongContext);
  return (
    <ListGroup.Item style={ItemStyle}>
      <span style={{ flex: 1 }}>{name}</span>
      <AiFillPlayCircle onClick={() => setSong(url)} />
    </ListGroup.Item>
  );
};

export default SongListItem;
