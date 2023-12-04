import React from 'react'
import TableOV from '../components/tableov'




export const Cardov = () => {
  return (
   <>
    <div className="container">
      <h1>Market overview</h1>
      <div className='box-container'>
          <div className='box-1'>
            <h1 >Crytocurrency</h1>
            <TableOV></TableOV>
          </div>
          <div className='box-1'>
            <h1>Stock</h1>
            <TableOV></TableOV>
          </div>
      </div>
  </div>
   
   </>
    
  )
}
