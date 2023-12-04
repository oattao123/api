import React from 'react'
import { useState,useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Nav2 from '../components/Nav2'
export const ProfilePages = () => {
    const navigate = useNavigate()
    const [isLoaded, setIsLoaded] = useState(true);
    const [user, setUser] = useState([]);

    useEffect(() => {
      
        const token = localStorage.getItem('token')
        var myHeaders = new Headers();
        myHeaders.append("Authorization", "Bearer "+ token);
        
        var requestOptions = {
          method: 'GET',
          headers: myHeaders,
          redirect: 'follow'
        };
        
        fetch("https://www.melivecode.com/api/auth/user", requestOptions)
          .then(response => response.json())
          .then(result => {
            if (result.status === 'ok') {
              setUser(result.user)
              setIsLoaded(false)

            }
            else if (result.status === 'forbidden') {
              navigate('/login')
              localStorage.removeItem('token')
              setIsLoaded(true)
            }
            console.log(result)})
          .catch(error => console.log('error', error));
      }, [])
      const Logout = () => {
        localStorage.removeItem('token')
        navigate('/login')
      }



      if (isLoaded) return <div>Loading...</div>
      else {
        return (

<>

<Nav2/>
          <div>
            <h1>Profile</h1>
            <h2>Username: {user.username}</h2>
            <h2>Email: {user.email}</h2>
            <h2>Role: {user.role}</h2>
            <img src={user.avatar} alt="" width={100}/>
            <div>
              <button onClick={Logout}>Logout</button>
            </div>

          </div>
</>

        )
      }


}
