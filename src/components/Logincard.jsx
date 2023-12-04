import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import Swal from 'sweetalert2'
import { useNavigate } from 'react-router-dom'







export const Logincard = () => {
  const [inputs,setInputs] = useState({});
  const navigate = useNavigate()
  
  
  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setInputs(values => ({...values, [name]:value}))

  }
  const handleSubmit = (e) => {
    e.preventDefault();
    
    console.log(inputs.username,inputs.password);

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
      "username": inputs.username,
      "password": inputs.password,
      "expiresIn": 1000000
    });

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };

    fetch("http://localhost:5000/sign_in", requestOptions)
    .then(response => response.json())
    .then(result => 
      {
      console.log(result);
  
      if (result.status === 'ok') 
      {
        Swal.fire({
          title: "Good job!",
          text: "You clicked the button!",
          icon: "success"
        }).then((value) => {
          localStorage.setItem('token',result.accessToken)
          navigate('/profile')});
      } 
      else 
      {
        Swal.fire({
          title: "Oops!",
          text: "Something went wrong!",
          icon: "error"
        });
      }
     })
    }
  
  return (
    <>


    <form onSubmit={handleSubmit}>
      <div className="flex border-2 w-[632px] h-[450px] flex-col mx-auto mt-[130px] bg-[#F5F4F4] rounded-md">
          <h1 className="text-center text-5xl p-[25px]">Login</h1>
          <div className="ml-auto mr-auto gap-10">
            <div className="form-control mb-3">
                <label className="label">
                  <span className="label-text">Email</span>
                
                </label>
                <input   name="username" 
        value={inputs.username || ""} 
        onChange={handleChange} type="text" placeholder="Email or username" className="input input-bordered h-[60px] w-[535px] " />
                
            </div>
            <div className="form-control m-auto">
                <label className="label">
                  <span className="label-text">Password</span>
                
                </label>
                <input name="password" 
          value={inputs.password || ""} 
          onChange={handleChange} type="password" placeholder="Enter your password" className="input input-bordered h-[60px] w-[535px] " />
                
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
/*return (
    <>
    <div className="flex border-2 w-[632px] h-[450px] flex-col mx-auto mt-[130px] bg-[#F5F4F4] rounded-md">
        <h1 className="text-center text-5xl p-[25px]">Login</h1>
        <div className="ml-auto mr-auto gap-10">
          <div className="form-control mb-3">
              <label className="label">
                <span className="label-text">Email</span>
              
              </label>
              <input type="text" placeholder="Email or username" className="input input-bordered h-[60px] w-[535px] " />
              
          </div>
          <div className="form-control m-auto">
              <label className="label">
                <span className="label-text">Password</span>
              
              </label>
              <input type="password" placeholder="Enter your password" className="input input-bordered h-[60px] w-[535px] " />
              
          </div>
        </div>
       
        <div className="flex ml-auto mr-auto mt-5">
        <button className="text-[25px] w-[150px] h-[60px] bg-[#B52245] rounded-full text-white border-[#B52245]" >Login</button>
          </div>
        <div className="text-center">
            <Link className="text-center" to="/">Don't have an account? <span className="underline hover:decoration-2">Sign up</span></Link>
        </div>



    </div>
    </>
    
  ) 

  
}
*/