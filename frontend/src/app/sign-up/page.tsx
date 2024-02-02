import React from 'react';
import Image from 'next/image';
import picture from './../fashion.png';

export default function SignUp() {
  return (
    <div className='flex flex-row h-screen overflow-hidden'>
      <div className='flex w-1/2 text-pink-500 items-center justify-center'>
        {/* Content on the left side */}
        Left Content
      </div>
      <div className='fixed right-0'>
        <div className=''>
            <Image src={picture} alt='sign-up-pic' width={700} />
        </div>
      </div>
    </div>
  );
}
