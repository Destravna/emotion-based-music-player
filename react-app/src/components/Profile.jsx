import React, { useContext, useEffect, useState } from 'react'
import Webcam from 'react-webcam'
import axios from 'axios'
import { MoodContext } from './context'
import Button from '@mui/material/Button';

const WebcamComponent = () => <Webcam />


const videoConstraints = {
  width: 400,
  height: 400,
}

const divStyle = {
  borderRadius: '25px', // Set border radius to 50px.
  background: '#2a2828', // Set the background color.
  boxShadow: '20px 20px 60px #bebebe, -20px -20px 60px #383636', // Set the box shadow.
  height: '90vh'
}


function dataURItoBlob(dataURI) {
  // Split the data URI to get the actual data part (after "base64,")
  const byteString = atob(dataURI.split(',')[1]);
  const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

  // Create an ArrayBuffer to hold the binary data
  const ab = new ArrayBuffer(byteString.length);
  const ia = new Uint8Array(ab);

  // Fill the ArrayBuffer with the binary data
  for (let i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }

  // Create a Blob from the ArrayBuffer and set the MIME type
  return new Blob([ab], { type: mimeString });
}




const Profile = () => {
  const { mood, setMood } = useContext(MoodContext);
  const [picture, setPicture] = useState('')
  const webcamRef = React.useRef(null)

  const savePicture = async () => {
    if (picture.length > 0) {
      console.log('save picture was called!!')
      alert('save called')
      console.log(picture);
      const blob = dataURItoBlob(picture);
      console.log(blob);
      const file = new File([blob], 'image.jpeg', { type: 'image/jpeg' })
      const formData = new FormData();
      formData.append('image', file);
      console.log('wtf is happening');
      const response = await axios.post('http://localhost:8080/detect', formData);
      console.log("data from review" + response.data.emotion)
      setMood(response.data.emotion)
      alert('YOU LOOK ' + response.data.emotion)
    }

  }


  const capture = React.useCallback(() => {
    const pictureSrc = webcamRef.current.getScreenshot()
    setPicture(pictureSrc)
  })

  useEffect(() => {
    console.log(picture);
    savePicture();
  }, [picture]);

  // useEffect(()=>{
  //   savePicture()
  // }, [picture]);


  // useEffect(() => {
  //   savePicture(captured)
  // })

  return (
    <div style={divStyle}>
      <h5 className="mb-5 text-center">
        👋 capture your photo to play songs based on mood
      </h5>
      <div>
        {picture == '' ? (
          <Webcam
            audio={false}
            height={450}
            ref={webcamRef}
            width={300}
            marginLeft='-10px'
            screenshotFormat="image/jpeg"
            videoConstraints={videoConstraints}
          />
        ) : (
          <img src={picture} />
        )}
      </div>
      <div>
        {picture != '' ? (
          <button
            onClick={(e) => {
            window.location.reload();

            }}
            className="btn btn-primary"
          >
            Retake
          </button>
        ) : (
          // <Button variant="contained">Contained</Button>

          <Button
            variant='contained'
            onClick={async (e) => {
              e.preventDefault()
              capture()


            }}
          >
            Capture
          </Button>
        )}
      </div>
    </div>
  )
}
export default Profile

