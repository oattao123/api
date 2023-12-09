import React from 'react'
import { NavCrypto } from './CryptoComponent/NavCrypto'
import Nav2 from '/src/components/Nav2'
import { StorageProvider } from './context/StorageContext'
import { Saved } from './Saved'
import { CryptoProvider } from './context/CryptoContext'
export const SavePage = () => {
  return (
    <>
    <CryptoProvider>
    <StorageProvider>
    <Nav2/>
    <NavCrypto/>
        <Saved/>

   </StorageProvider>

    </CryptoProvider>
 

    </>
  )
}
