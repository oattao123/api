import React from 'react';
import { SiBinance } from 'react-icons/Si';
import { FaEthereum } from 'react-icons/fa';
import { BiLogoBitcoin } from 'react-icons/bi';

function RegisterCard() {
    
    return (
        <>
         <div className="table-flex">
          <table className="table-lg table-cus ">
            {/* head */}
            
            <tbody>
              {/* row 1 */}
              <tr >
                <th className=''><BiLogoBitcoin/></th> 
                <td className='text-[25px]'>BTC Bitcoin</td>
                <td className='text-[25px]'>$67500</td>
                <td className='text-[25px]'>-1.45%</td>
              </tr>
              {/* row 2 */}
           
              <tr>
                <th><FaEthereum/></th>
                <td className='text-[25px]'>ETH Ethereum</td>
                <td className='text-[25px]'>$10000</td>
                <td className='text-[25px]'>2.54%</td>
              </tr>
              {/* row 3 */}
              <tr>
                <th><SiBinance/></th>
                <td className='text-[25px]'>BNB Binancee</td>
                <td className='text-[25px]'>$500</td>
                <td className='text-[25px]'>1.23%</td>
              </tr>
            </tbody>
          </table>
</div>
      </>
       
    );
}


export default RegisterCard;
