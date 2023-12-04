
import logo from "../assets/logo.png";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <>
    <nav className="">
    <div className="navbar bg-base-100 bg-whtie justify-between flex shadow-md">
    <div className="flex ">
            <div className="flex flex-row gap-0">
              <img className="w-[68px] h-[59]" src={logo} alt="" />
              <h1 className=" text-[#B52245] text-[30px] m-3">BIZ-NA</h1> 
            </div>
            <ul className="flex flex-column gap-10 ml-10">
              <li>
                <Link className="text-black text-[30px]" to="/">Market</Link>
              </li>
              <li>
                <Link className="text-black text-[30px]" to="/">News</Link>
              </li>
            </ul>
           
    </div>
    <div className="gap-10">
            <Link className="text-black text-[25px] " to="/login">Login</Link>
            <Link className="text-white text-[25px] bg-[#B52245] pl-4 pr-4 pt-2 pb-2 rounded-full" id="Register" to="/register">Sign up</Link>
    </div>
         
    </div>

    </nav>

   


    
</>
    
  
    
   

    
  );
}

export default Navbar;
