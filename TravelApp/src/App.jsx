import React, { useState } from 'react';
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
// ---------------------------
// import React from 'react'
import Globe from 'react-globe.gl'
// import ReactGlobe from 'react-globe'
// import * as Location from 'expo-location'
import axios from 'axios';
// import { useHistory } from 'react-router-dom'; 
import { useNavigate } from "react-router-dom";
import { BrowserRouter as Router } from 'react-router-dom';

// import Carousel from 'react-bootstrap/Carousel'
// import ExampleCarouselImage from 'components/ExampleCarouselImage';

import Silder from "react-slick";

import {Link} from "react-router-dom"


// ---------------------------



function App() {

  /*
  const navigate = useNavigate()

  const goToNewPage = () => {
    navigate("/InfoPage")
  }
  */

  const [count, setCount] = useState(0);
  const [clickedCountry, setClickedCountry] = useState('');

  const navigate = useNavigate()

  const [cityData, setCityData] = useState(null);
  const [descripData, setDescripData] = useState(null);

  const [currentData, setCurrentData] = useState([])
  const [index, setIndex] = useState(0)

  const rand_countries = [  'Argentina',
  'Brazil',
  'Canada',
  'Denmark',
  'Egypt',
  'France',
  'Germany',
  'India',
  'Japan',
  'Kenya']

  const chooseRandCountry = () => {
    const countryName = rand_countries[Math.floor(Math.random() * rand_countries.length)]
    setClickedCountry(countryName)
  }

  const handleNext = () => {
    const temp = (index+1) % currentData.length
    setIndex(temp)
    setCityData(currentData[temp]['city'])
    setDescripData(currentData[temp]['description'])
  }

  const data = [
    {
      city: `Ann Arbor 1`,
      description: `sflkjsfskjdfhaskdjfsfdsf`
    },
    {
      city: `Ann Arbor 2`,
      description: `sflkjsfskjdfhaskdjfsfdsf`
    }
  ]

  var settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };

  const handleMarkerClick = ({ lat, lng }, eventvent) => {
    const countryName = event?.marker?.name || '';
    setClickedCountry(countryName);
    console.log("CLICKED")
    console.log(lat + ", " + lng)

    async function getCountry(){
      // https://api.opencagedata.com/geocode/v1/json?q=52.3877830%2C9.7334394&key=bbef5a91e2814fe1ab67b9a58b73fd74
      const link = `https://api.opencagedata.com/geocode/v1/json?q=${lat}%2C${lng}&key=bbef5a91e2814fe1ab67b9a58b73fd74`
      const response = await fetch(link)
      const val = await response.json();
      // console.log(val['results'][0]['components']['country'])
      console.log(typeof(val))
      setClickedCountry(val['results'][0]['components']['country'])

    }

    getCountry()
    


  };

  // const handleGoClick = () => {
  //   async function fetcher(){
  //     const fetchReq = await fetch(`/api/lucky?country=${clickedCountry}&travel_style=${"fly"}`)
  //     const response = await fetchReq.json()
  //     const resp = JSON.parse(response)
  //     // console.log(Object.keys(response).length)
  //     console.log(typeof(resp))
  //     console.log(resp)
  //     // navigate("/InfoPage")

  //     // const  = resp
  //     setCurrentData(resp)

  //     console.log(resp[0]['city'])
  //     setCityData(resp[0]['city']);
  //     setDescripData(resp[0]['description']);


  //     // navigate("/InfoPage")
  //     // console.log("Navigated to InfoPage");
  //   }

  //   fetcher()
  //   // goToNewPage()
    
  // }

  console.log(currentData)

  return (
    <>
      <div>
        <img src="/images/transparent.png" className="logo trek" alt=""/>
      </div>
      <h1>welcome, traveler!</h1>
      <SimpleGlobe onMarkerClick={handleMarkerClick} />
      <div className="card">
        
        <p>Pick the country you would like to travel to next.</p>
        <button onClick={chooseRandCountry}>
          Or...I'm Feeling Lucky? 🫣
          
        </button>
        <p>Want to plan a trip in... {clickedCountry}?</p>

        <Link to='/infoPage' state= {{clickedCountry: clickedCountry}}>
        {clickedCountry && (<button>
          Let's go!
        </button>)}
        </Link>

        <h1>{cityData}</h1>
        <h2>{descripData}</h2>   
        
        {currentData.length!==0 && (<button onClick={handleNext}> 
          Next
        </button>)}

      </div>
      

      
      <p className="read-the-docs">©TrekTician 2024</p>


    </>
  );
}

function SimpleGlobe({ onMarkerClick }) {
  const globeOptions = {
    globeImageUrl: '//unpkg.com/three-globe/example/img/earth-night.jpg',
    backgroundImageUrl: '//unpkg.com/three-globe/example/img/night-sky.png',
    onGlobeClick: onMarkerClick, // Pass the click handler to the globe component
  };

  return <Globe {...globeOptions} />;
}

export default App;