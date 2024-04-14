import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { BrowserRouter, RouterProvider, createBrowserRouter, createRoutesFromElements, Route } from 'react-router-dom'
import NewPage from './NewPage.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  // <React.StrictMode>

    <Main />
  // </React.StrictMode>,
)


function Main(){
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path = "/">
        <Route index element={<App/>} />
        <Route path ="/infoPage" element={<NewPage/>} />
  
      </Route>,
    )
  )

  return (
    <>
    <RouterProvider router={router}/>
    </>
  )
}

