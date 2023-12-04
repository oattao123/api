import React from "react";
import '/src/components/hero/hero.css';
import {Link} from 'react-router-dom';
export const Card = ({ items:{id,cover,catgeory,title,authorName,authorImg,time} }) => {
    return (
        <>
        
            
        <div className='box'>
            <div className='img'>
                <img src={cover} alt='' />
            </div>

            <div className='text'>
                <span className='category p-1'>{catgeory}</span>
            {/*<h1 className='titleBg'>{title}</h1>*/}
            <Link to={`/SinglePage/${id}`}>
                <h1 className='titleBg'>{title}</h1>
            </Link>
            <div className='author flex'>
                <span>by {authorName}</span>
                <span>{time}</span>
            </div>
            </div>
        </div>
          
        </>




    )
        


}