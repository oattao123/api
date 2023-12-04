import React from 'react'



export const Addcoin = () => {

 
    return (
        <form className='container flex flex-col   mr-auto ml-auto '>
            <div className='text-center'>
            <div>
                <label htmlFor="fname">firstname</label>
                <input
                    type="text"
                    id="fname"
                    className='border'
                />
            </div>
            <div>
                <label htmlFor="lname">lastname</label>
                <input
                    type="text"
                    id="lname"
                    className='border'
                />
            </div>
            <div>
                <label htmlFor="username">username</label>
                <input
                    type="text"
                    id="username"
                    className='border'
                />
            </div>
            <div>
                <label htmlFor="email">email</label>
                <input
                    type="text"
                    id="email"
                    className='border'
                />
            </div>
            <div>
                <label htmlFor="avartar">avatar</label>
                <input
                    type="text"
                    id="avartar"
                    className='border'
                />
            </div>
            <button type="submit">Add Coin</button>
            </div>
        </form>
    );
};
