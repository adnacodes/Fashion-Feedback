"use client"
import React, { useEffect, useState } from 'react';
import Link from 'next/link'
import { FiMenu } from "react-icons/fi"
import { BsX } from "react-icons/bs"

function Navbar() {
    const [menuOpen, setMenuOpen] = useState(false);
  
    useEffect(() => {
      // Handle body styles when the menu is open
      if (menuOpen) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = 'visible';
      }
    }, [menuOpen]);
  
    const toggleMenu = () => setMenuOpen(!menuOpen);
    return(
        <header>
            <nav className='fixed z-10 w-full h-16 bg-[#D9D9D9]'>
                <div className="flex items-center justify-between px-4 h-full w-full">
                    <div className='pl-12'>
                        <FiMenu onClick={toggleMenu} className='cursor-pointer h-6 w-6 text-black'></FiMenu>
                    </div>
                </div>
            </nav>
            <div className={
                menuOpen 
                ? 'fixed top-0 left-0 w-2/3 lg:w-1/3 md:w-1/3 h-screen p-5 lg:p-10 md:p-10 ease-in-out duration-500 bg-[#ECF0F3] z-40' 
                : 'fixed left-[-100%] top-0 p-10'
                }>
                <div className='flex w-full items-center justify-end'>
                    <div>
                        <BsX onClick={toggleMenu} className='cursor-pointer h-6 w-6 text-black'></BsX>
                    </div>
                </div>
                <div className='flex-col py-8 px-10 lg:py-4 lg:px-16 text-xl  whitespace-nowrap'>
                    <ul>
                        <li onClick={() => setMenuOpen(false)} className='py-4 text-black hover:underline'>
                            <Link href="/search">Search</Link>
                        </li>
                        <li onClick={() => setMenuOpen(false)} className='py-4 text-black hover:underline'>
                            <Link href="/trending-items">Trending Items</Link>
                        </li>
                        <li onClick={() => setMenuOpen(false)} className='py-4 text-black hover:underline'>
                            <Link href="/recent-searches">Recent Searches</Link>
                        </li>
                        <li onClick={() => setMenuOpen(false)} className='py-4 text-black hover:underline'>
                            <Link href="/how-it-works">How it works</Link>
                        </li>
                        <li onClick={() => setMenuOpen(false)} className='flex items-center py-4'>
                            <button className='border bg-slate-300  py-3 px-8 whitespace-nowrap items-center justify-center rounded-full hover:bg-yellow-600 text-black'>
                                <Link href="/sign-in">Sign In</Link>
                            </button>
                        </li>
                        <li onClick={() => setMenuOpen(false)} className='flex items-center py-4'>
                            <button className='border bg-slate-300 py-3 px-8 whitespace-nowrap rounded-full hover:bg-yellow-600 text-black'>
                                <Link href="/sign-up">Sign Up</Link>
                            </button>
                        </li>
                    </ul>
                </div>
                <div>
                    <p className='text-black flex flex-row justify-center whitespace-nowrap items-center pt-10 text-2xl lg:text-3xl font-extralight'>
                        <Link href='/' onClick={() => setMenuOpen(false)}>Fashion Feedback</Link>
                    </p>
                </div>
            </div>
        </header>
    )
}
export default Navbar;
