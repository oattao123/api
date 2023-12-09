import React from 'react'
import { useState,useContext } from 'react'
import searchIcon from '/src/assets/search-icon.svg'
import { CryptoContext } from '../context/CryptoContext'
import { debounce, get } from 'lodash'

const SearchInput = ({handleSearch}) => {

    const [searchText, setSearchText] = useState("");

    let { searchData, setCoinSearch,setSearchData } = useContext(CryptoContext);

    let handleInput = (e) => {
        e.preventDefault();
        let query = e.target.value;
        setSearchText(query);
        handleSearch(query);  
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setCoinSearch(searchText);
       
    };

    const selectCoin = (coin) => {
        setSearchText("");
        setCoinSearch(coin);
        setSearchData();
    }

    return (
            <>
             <form className='w-96 relative flex items-center ml-7 font-nunito'>
    <input onChange={handleInput}
     value={searchText} 
     onSubmit={handleSubmit}
     type="text" name='search' className='w-full rounded bg-gray-600 
    placeholder:text-gray-500 pl-2 required outline-0 border border-transparent 
    focus:border-[#00FFFF]' placeholder='search here...'/>
    <button type='submit'>
        <img src={searchIcon} alt="search" 
        className='absolute right-1 top-[0.7rem] cursor-pointer'/>
    </button>
</form>
{
    searchText.length > 0 ?

    <ul className='absolute top-11 left-0 w-96 h-96 rounded 
    overflow-x-hidden py-2 bg-gray-200 bg-opacity-60 
    backdrop-blur-md'>
        {
            searchData ? 
            
            searchData.map(coin => {return <li 
            className='flex items-center ml-4 my-2 cursor-pointer'
            key={coin.id}
            onClick={() => selectCoin(coin.id)}>
                 <img className="w-[1.2rem] h-[1.2rem] mx-1.5" src={coin.thumb} alt={coin.name} /> 
                    <span className=''>{coin.name}</span>
               </li>})
            
            : <div className='w-full h-full flex justify-center items-center'>
                <div className='w-8 h-8 border-4 border-cyan-300 rounded-full border-b-gray-200 animate-spin "role="status'
                />
                <span className='ml-2'>Searching...</span>
            </div>
        }
    </ul> 
    
    : null}

         </>
    );
};

export const Search = () => {
  let { getSearchResult } = useContext(CryptoContext);

  const debounceFunc = debounce(function(val){
    getSearchResult(val);
  }, 2000);

  return (
    <div className="relative">
      <SearchInput handleSearch={debounceFunc}/>
    </div>
  );
};

