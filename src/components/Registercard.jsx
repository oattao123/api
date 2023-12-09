import React from 'react';
import PropTypes from 'prop-types';
import { Link } from "react-router-dom";
import { useState } from 'react';
import Swal from 'sweetalert2';
import { useNavigate } from 'react-router-dom';


export const Registercard = () => {

    const [inputs, setInputs] = useState({});
    const navigate = useNavigate();

    const handleChange = (event) => {
      const name = event.target.name;
      const value = event.target.value;
      setInputs(values => ({...values, [name]: value}))
    }
  
    const handleSubmit = (event) => {
      event.preventDefault();
     

        var myHeaders = new Headers();
            myHeaders.append("Content-Type", "application/json");

            var raw = JSON.stringify({
            "fisrt_name": inputs.fname,
            "last_name": inputs.lname,
            "username": inputs.username,
            "password": inputs.password,
            "email":    inputs.email,
            
            });

            var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
            };

            fetch("http://127.0.0.1:5000/sign_in", requestOptions)
            .then(response => response.json())
            .then(result => { if (result.status === 'ok') 
            {
              Swal.fire({
                title: "Good job!",
                text: "Register success!",
                icon: "success"
              }).then((value) => {
                localStorage.setItem('token',result.accessToken)
                navigate('/profile')});
            } 
            else 
            {
            console.log(result.message);
              Swal.fire({
                title: "Oops!",
                text: "Something went wrong!",
                icon: "error"
              });
            }}
            )
            .catch(error => console.log('error', error));
    }



    return (
      <>
       <form onSubmit={handleSubmit}>


<div className="flex border-2 w-[632px] h-[625px] flex-col mx-auto mt-[130px] bg-[#F5F4F4] rounded-md">
    <h1 className="text-center text-5xl p-[25px]">Sign up</h1>
    <div className="ml-auto mr-auto gap-10">
      <div className="form-control mb-3">
          <label className="label">
            <span className="label-text">Email</span>
          
          </label>
          <input value={inputs.email || ""} 
    onChange={handleChange} name="email" type="text" placeholder="Enter your email" className="input input-bordered h-[60px] w-[535px]" />
          
      </div>

      <div className="form-control mb-3 flex-row gap-[35px]">
         <div>
            <label className="label">
                <span className="label-text">Name</span>
            
            </label>
            <input value={inputs.fname || ""} 
    onChange={handleChange} name='fname' type="text" placeholder="First name" className="input input-bordered w-[250px]" />
          
          
         </div>
         <div>
            <label className="label">
                <span className="label-text">Surname</span>
            
            </label>
            <input value={inputs.lname || ""} 
    onChange={handleChange} type="text" name='lname' placeholder="Last name" className="input input-bordered w-[250px]" />
          
          
         </div>
      </div>

      <div className="form-control m-auto">
          <label className="label">
            <span className="label-text">username</span>
          
          </label>
          <input value={inputs.username || ""} 
    onChange={handleChange} type="text" name="username" placeholder="Username" className="input input-bordered h-[60px] w-[535px] " />
          
      </div>

      <div className="form-control mb-3">
          <label className="label">
            <span className="label-text">Password</span>
          
          </label>
          <input value={inputs.password || ""} 
    onChange={handleChange} type="password" name='password' placeholder="Enter your password" className="input input-bordered h-[60px] w-[535px] " />
          
      </div>
  
  
     
    </div>
   
    <div className="flex ml-auto mr-auto mt-5 mb-1">
       
        <input className=" text-[25px] w-[150px] h-[60px] bg-[#B52245] rounded-full text-white border-[#B52245]" type="submit" value="Sign up"/>
    </div>
    <div className="text-center">
        <Link className="text-center" to="/">Don't have an account? <span className="underline hover:decoration-2">Sign up</span></Link>
    </div>



    </div>


</form>
       


   
    
      </>
    )
  }
  
/* 



function RegisterCard() {
    
    return (
        <>
    <div className="flex border-2 w-[632px] h-[625px] flex-col mx-auto mt-[130px] bg-[#F5F4F4] rounded-md">
        <h1 className="text-center text-5xl p-[25px]">Sign up</h1>
        <div className="ml-auto mr-auto gap-10">
          <div className="form-control mb-3">
              <label className="label">
                <span className="label-text">Email</span>
              
              </label>
              <input type="text" placeholder="Enter your email" className="input input-bordered h-[60px] w-[535px] " />
              
          </div>

          <div className="form-control mb-3 flex-row gap-[35px]">
             <div>
                <label className="label">
                    <span className="label-text">Name</span>
                
                </label>
                <input type="text" placeholder="name" className="input input-bordered w-[250px]" />
              
              
             </div>
             <div>
                <label className="label">
                    <span className="label-text">Surname</span>
                
                </label>
                <input type="text" placeholder="surname" className="input input-bordered w-[250px]" />
              
              
             </div>
          </div>



          <div className="form-control mb-3">
              <label className="label">
                <span className="label-text">Password</span>
              
              </label>
              <input type="password" placeholder="Enter your password" className="input input-bordered h-[60px] w-[535px] " />
              
          </div>
          <div className="form-control m-auto">
              <label className="label">
                <span className="label-text">Confirm password</span>
              
              </label>
              <input type="password" placeholder="Confirm your password" className="input input-bordered h-[60px] w-[535px] " />
              
          </div>
        </div>
       
        <div className="flex ml-auto mr-auto mt-5 mb-1">
            <button className="text-[25px] w-[150px] h-[60px] bg-[#B52245] rounded-full text-white border-[#B52245]">Login</button>
        </div>
        <div className="text-center">
            <Link className="text-center" to="/">Don't have an account? <span className="underline hover:decoration-2">Sign up</span></Link>
        </div>



    </div>
        </>
       
    );
}



  <form onSubmit={handleSubmit}>
      <label>Enter your name:
      <input 
        type="text" 
        name="username" 
        value={inputs.username || ""} 
        onChange={handleChange}
      />
      </label>
      <label>Enter your age:
        <input 
          type="text" 
          name="email" 
          value={inputs.email || ""} 
          onChange={handleChange}
        />
        </label>

        <label>Enter your age:
        <input 
          type="text" 
          name="fname" 
          value={inputs.fname || ""} 
          onChange={handleChange}
        />
        </label>
        <label>Enter your lname:
        <input 
          type="text" 
          name="lname" 
          value={inputs.lname || ""} 
          onChange={handleChange}
        />
        </label>
        <label>Enter your password:
        <input 
          type="text" 
          name="password" 
          value={inputs.password || ""} 
          onChange={handleChange}
        />
        </label>
    
        <input type="submit" />
    </form>
*/


