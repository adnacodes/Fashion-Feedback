import React from 'react';
import localfont from 'next/font/local';
import { Michroma } from 'next/font/google';

export const michroma = Michroma({
  weight: ['400'],
  style: ['normal'],
  subsets: ['latin']
})

export default function Home() {
  return (
    <div className={`bg-[#2C1A36] flex flex-col h-screen items-center justify-center`}>
      <label className='text-5xl sm:text-5xl md:text-6xl lg:text-7xl text-center sm:text-center md:text-center'>
        <p className={`${michroma.className}`}>Fashion Feedback</p>
      </label>
      <div className='mt-4 w-9/12'>
        <div className="relative flex items-center w-full h-10 rounded-full focus-within:shadow-lg bg-white overflow-hidden">
          <div className="grid place-items-center h-full w-12 text-gray-300">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
          </div>
          <input
          className="peer h-full w-full outline-none text-gray-700 pr-2 text-xl"
          type="text"
          id="search"
          placeholder="What will you search today?" /> 
        </div>
      </div>
      <div className='flex w-9/12 mt-6 text-center'>
        <div className={`${michroma.className}`}>
        On this site, you can search for fashion items to see if they are trending based on their analytical data. Based on the data, we'll tell you if the item is trending or not based on the stability,  duration, and the quantity of searches for the item.
        </div>
      </div>
    </div>
  );
}