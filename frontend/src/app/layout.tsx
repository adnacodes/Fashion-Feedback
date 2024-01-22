import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import React from 'react'
import Navbar from '@/components/Navbar'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Fashion Feedback',
  description: 'Website to see fashion trends',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <main>
          <Navbar/>
          {children}
        </main>
      </body>
    </html>
  )
}
