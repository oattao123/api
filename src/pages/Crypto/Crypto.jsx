import React from 'react'
import { NavCrypto } from './CryptoComponent/NavCrypto'
import Nav2 from '/src/components/Nav2'
import { TableComponent } from './CryptoComponent/TableComponent'
import { CryptoProvider } from './context/CryptoContext'
import { Filters } from './CryptoComponent/Filters'
import { StorageProvider } from './context/StorageContext'

export const Crypto = () => {
  return (
    <>
    <CryptoProvider>
    <StorageProvider>
        <Nav2/>
        <NavCrypto/>
        <Filters/>
        <TableComponent/>
    </StorageProvider>
    </CryptoProvider>
   
    </>
  )
}