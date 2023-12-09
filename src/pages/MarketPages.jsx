import React from 'react'
import Nav2 from '../components/Nav2'
import { Footer } from '/src/components/Footer'

import TableOV from '../components/tableov'
import Market from '../components/market/market'

export const MarketPages = () => {
  return (
   <>
   <Nav2></Nav2>
   <div className='flex justify-center mt-[80px]'>
        <div className="">
            <h1 className='text-[30px]'>Market overview</h1>
            
            <div className='flex flex-row  gap-5'>
                <div className='outline outline-offset-0 p-3 rounded-md w-[640px] h-[260px]'>
                  <h1 className='text-[30px]'>Crytocurrency</h1>
                  <TableOV></TableOV>
                </div>
                <div className='outline outline-offset-0 p-3 rounded-md w-[640px] h-[260px]'>
                  <h1 className='text-[30px]'>Stock</h1>
                  <TableOV></TableOV>
                </div>
              
            </div>
        </div>
   </div>



  <div className='flex justify-center w-full'>
    <Market></Market>
  </div>
  
   <Footer></Footer>
   
   </>
    
  )
}

