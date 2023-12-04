import React from "react";
import { AiOutlineInstagram } from 'react-icons/ai';
import { BsFacebook,BsDiscord,BsYoutube } from 'react-icons/bs';
import { Link } from "react-router-dom";
import { FaXTwitter } from "react-icons/fa6";




export const Footer = () => {
  return (
    <>
    <footer className="footer footer-center p-10 bg-base-200 text-base-content rounded">
  <div className="flex-auto join gap-10">
    <Link className="link link-hover join-item">About us</Link> 
    <Link className="link link-hover join-item">Contact</Link> 
    <Link className="link link-hover join-item">Jobs</Link> 
    <Link className="link link-hover join-item">Press kit</Link>
  
  </div>
    
  
    <div className="flex-auto join gap-10">
    <h1><AiOutlineInstagram/></h1>
    <h1><BsFacebook/></h1>
    <h1><BsDiscord/></h1>
    <h1><BsYoutube/></h1>
    <h1><FaXTwitter/></h1>

    </div>
 
  <aside>
    <p>Copyright © 2023 - All right reserved by BIZ technology Ltd</p>
  </aside>
</footer>
    </>
  )
}
