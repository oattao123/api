import React from 'react';
import PropTypes from 'prop-types';
import { Link } from "react-router-dom";
import { useState } from 'react';
import Swal from 'sweetalert2';
import { useNavigate } from 'react-router-dom';


export const Registercard = () => {
    const [inputs, setInputs] = useState({
        email: '',
        fname: '',
        lname: '',
        username: '',
        password: ''
    });
    const navigate = useNavigate();

    const handleChange = (event) => {
        const { name, value } = event.target;
        setInputs(prevState => ({ ...prevState, [name]: value }));
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        const requestOptions = {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                first_name: inputs.fname,
                last_name: inputs.lname,
                username: inputs.username,
                password: inputs.password,
                email: inputs.email,
            })
        };

        fetch(`${process.env.REACT_APP_API_URL}/sign_in`, requestOptions)
            .then(response => response.json())
            .then(result => {
                if (result.message === 'User registered successfully') {
                    Swal.fire('Good job!', 'Register success!', 'success')
                        .then(() => navigate('/profile'));
                } else {
                    Swal.fire('Oops!', result.error || 'Something went wrong!', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                Swal.fire('Oops!', 'Network error or server is down', 'error');
            });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="flex border-2 w-[632px] h-[625px] flex-col mx-auto mt-[130px] bg-[#F5F4F4] rounded-md">
                <h1 className="text-center text-5xl p-[25px]">Sign up</h1>
                <div className="ml-auto mr-auto gap-10">
                    {/* Input fields here */}
                    {/* Email Input */}
                    <div className="form-control mb-3">
                        <label className="label">
                            <span className="label-text">Email</span>
                        </label>
                        <input value={inputs.email} onChange={handleChange} name="email" type="text" placeholder="Enter your email" className="input input-bordered h-[60px] w-[535px]" />
                    </div>

                    {/* First Name and Last Name Inputs */}
                    <div className="form-control mb-3 flex-row gap-[35px]">
                        {/* First Name Input */}
                        <div>
                            <label className="label">
                                <span className="label-text">Name</span>
                            </label>
                            <input value={inputs.fname} onChange={handleChange} name='fname' type="text" placeholder="First name" className="input input-bordered w-[250px]" />
                        </div>
                        {/* Last Name Input */}
                        <div>
                            <label className="label">
                                <span className="label-text">Surname</span>
                            </label>
                            <input value={inputs.lname} onChange={handleChange} name='lname' type="text" placeholder="Last name" className="input input-bordered w-[250px]" />
                        </div>
                    </div>

                    {/* Username Input */}
                    <div className="form-control m-auto">
                        <label className="label">
                            <span className="label-text">Username</span>
                        </label>
                        <input value={inputs.username} onChange={handleChange} name="username" type="text" placeholder="Username" className="input input-bordered h-[60px] w-[535px]" />
                    </div>

                    {/* Password Input */}
                    <div className="form-control mb-3">
                        <label className="label">
                            <span className="label-text">Password</span>
                        </label>
                        <input value={inputs.password} onChange={handleChange} name='password' type="password" placeholder="Enter your password" className="input input-bordered h-[60px] w-[535px]" />
                    </div>

                    {/* Submit Button */}
                    <div className="flex ml-auto mr-auto mt-5 mb-1">
                        <input className="text-[25px] w-[150px] h-[60px] bg-[#B52245] rounded-full text-white border-[#B52245]" type="submit" value="Sign up" />
                    </div>

                    {/* Link to Login Page */}
                    <div className="text-center">
                        <Link to="/">Don't have an account? <span className="underline hover:decoration-2">Sign up</span></Link>
                    </div>
                </div>
            </div>
        </form>
    );
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


