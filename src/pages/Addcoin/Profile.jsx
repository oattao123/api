import React from 'react'
import { useState,useEffect } from 'react'

export const Profile = () => {
  const [items, setItems] = useState([]);

 
  useEffect(() => {
    fetch('https://www.melivecode.com/api/users')
      .then((res) => res.json())
      .then((data) => {
        setItems(data);
      });
  }, [])


  return (
    <>
     <div className="container border flex flex-col mr-auto ml-auto">
      <table className=''>
        <thead className=''>
          <tr>
              <th>Coin logo</th>
              <th className='py-1 '>Coin</th>
              <th className='py-1'>Amount</th>
              <th className='py-1'>Price</th>       
               
              <th className='py-1'>add</th>  
              <th className='py-1'>edit</th>  
          </tr>
        </thead>
        <tbody>
          {items.map((row) => (
            <tr >
             <td className='py-1 '>{row.id}</td>
              <td className='py-1'><img src={row.avatar} alt="" className='w-[50px]'/></td>
              <td className='py-1'>{row.fname}</td>
              <td className='py-1'>{row.lname}</td>
              <td className='py-1'>{row.username}</td>
              <td className='py-1'>{row.email}</td>
              
              <td className='py-1'>test</td>
         
            </tr>
          ))
          }
        </tbody>
      </table>
     </div>
    
    </>

    )
}
