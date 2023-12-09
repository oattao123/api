
import logo from "../assets/logo.png";
import { Link } from "react-router-dom";
import {FaRegUserCircle} from "react-icons/fa";

function Nav2() {
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
                <Link className="text-black text-[30px]" to="/news">News</Link>
              </li>
              <li>
                <Link className="text-black text-[30px]" to="/home">Dashboard</Link>
              </li>
            </ul>
           
    </div>
    <div className="gap-10">
         <FaRegUserCircle className="text-black text-[40px] mr-[10px]"/>
    </div>
         
    </div>

    </nav>

   


    
</>
    
  
    
   

    
  );
}

export default Nav2;
