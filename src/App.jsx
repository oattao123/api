import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

import { LoginPages } from './pages/LoginPages'
import { Route, Routes } from 'react-router-dom'
import { RegisterPages } from './pages/RegisterPages'
import { MarketPages } from './pages/MarketPages'
import { NewsPages} from './pages/NewsPages'
import { SinglePages } from './pages/singlepages/SinglePages'
import { SecondPages } from './pages/secondpages/SecondPages'
import { ProfilePages } from './pages/ProfilePages'

import { Crypto } from './pages/Crypto/Crypto'
import { SavePage } from './pages/Crypto/SavePage'
import { Trending } from './pages/Crypto/Trending'
import { Profile } from './pages/Addcoin/Profile'
import { Addcoin } from './pages/Addcoin/Addcoin'


function App() {
  
  return (
    <>
   <Routes>
      <Route path="/" element={<LoginPages />} />
      <Route path="/login" element={<LoginPages />} />
      <Route path="/register" element={<RegisterPages />} />
      <Route path="/market" element={<MarketPages />} />
      <Route path="/news" element={<NewsPages />} />
      <Route path='/singlepage/:id' element={ <SinglePages/>} />
      <Route path='/secondpage/:id' element={ <SecondPages/>} />
      <Route path='/profile' element={ <ProfilePages/>} />
    

    
      <Route path='/home' element={ <Crypto/>} />
      <Route path='/saved' element={ <SavePage/>} />
      <Route path='/trending' element={ <Trending/>} />
      <Route path='/user' element={ <Profile/>} />
      <Route path='/addcoin' element={ <Addcoin/>} />

   </Routes>
    </>
  )
}

export default App
