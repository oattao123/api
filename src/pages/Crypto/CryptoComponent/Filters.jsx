import React,{useContext,useRef} from 'react'
import submitIcon from '/src/assets/submit-icon.svg'
import selectIcon from '/src/assets/select-icon.svg'
import { Search } from './Search'
import { CryptoContext } from '../context/CryptoContext'
export const Filters = () => {

    let {setCurrency,setSortBy} = useContext(CryptoContext);
    const currencyRef = useRef(null);

    const handleCurrencySubmit = (e) => {
        e.preventDefault();
        let val = currencyRef.current.value;
        setCurrency(val);
        currencyRef.current.value = "";
    }
    const handleSortBy = (e) => {
        e.preventDefault();
        let val = e.target.value;
        setSortBy(val);
    }

  return (
    <div className="w-full h-12 border-2 border-gray-100 rounded-lg 
    flex items-enter justify-between relative">
        <Search/>
        <div className='flex mr-7 '>
            <form action="" className='relative flex items-center
            font-nunito mr-12 '
            onSubmit={handleCurrencySubmit}>
                <label htmlFor='currency' className='relative flex
                justify-center items-centermr-2 font-bold'>currency</label>
                <input className='w-16 rounded bg-gray-200 placeholder:text-gray-100 pl-2 required outline-0 border-transparent 
                focus:border-[#00FFFF] leading-4'
                 placeholder='usd' type="text" name='currency'
                 ref={currencyRef}/>
                <button type='submit' className='ml-1'>
                    <img src={submitIcon} alt="submit" className='w-full h-auto'/>
                </button>
            </form>
            <label className='relative flex justify-center items-center'>
            <span className='font-bold mr-2 '>sort by:</span>
                <select className="rounded bg-gray-200 text-base pl-2 pr-10 py-0.5 leading-4 capitalize focus:outline-0 " name="sortby" id="" onClick={handleSortBy}>
               
                    <option value="market_cap_asc">market cap asc</option>
                    <option value="market_cap_desc">market cap desc</option>
                    <option value="volume_asc">volume asc</option>
                    <option value="volume_desc">volume desc</option>
                    <option value="id_asc">id asc</option>
                    <option value="id_desc">id desc</option>
                </select>
                <img src={selectIcon} alt="submit" className='w-[1rem] h-auto absolute right-[-1px] top-[15px] pointer-events-none'/>


        </label>
        </div>
      
    </div>
  )
}
