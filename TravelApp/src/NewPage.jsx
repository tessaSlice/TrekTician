import React, { useEffect, useState } from 'react';
import {useLocation} from 'react-router-dom'

function NewPage() {


   // const{state} = props.location
    // const {curentData} = state

    const location = useLocation()
    const dat = location.state
    console.log(location)
    console.log(dat)

    const clickedCountry = dat.clickedCountry;


    const [cityData, setCityData] = useState(null);
  const [descripData, setDescripData] = useState(null);
  const [imgData, setImgpData] = useState(null);

  const [currentData, setCurrentData] = useState([])
  const [index, setIndex] = useState(0)

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetcher(){
        setLoading(true)
        const fetchReq = await fetch(`/api/lucky?country=${clickedCountry}&travel_style=${"fly"}`)
        const response = await fetchReq.json()
        const resp = JSON.parse(response)
        // console.log(Object.keys(response).length)
        console.log(typeof(resp))
        console.log(resp)
        // navigate("/InfoPage")
  
        // const  = resp
        setCurrentData(resp)
  
        console.log(resp[0]['city'])
        setCityData(resp[0]['city']);
        setDescripData(resp[0]['description']);
        setImgpData(resp[0]['image_url'])
        setLoading(false)
  
  
        // navigate("/InfoPage")
        // console.log("Navigated to InfoPage");
      }
  
      fetcher()
  }, [])



  const handleNext = () => {
    const temp = (index+1) % currentData.length
    setIndex(temp)
    setCityData(currentData[temp]['city'])
    setDescripData(currentData[temp]['description'])
    setImgpData(currentData[temp]['image_url'])
  }

  if (loading) {
    return <h1>Finding your perfect cities...</h1>
  }

  return (
    <div>
      <h1>{cityData}</h1>
        <h2>{descripData}</h2>   
        <img src={imgData}/>
        <br/>
        {currentData.length!==0 && (<button onClick={handleNext}> 
          Next
        </button>)}
    </div>
  );
}

export default NewPage;
