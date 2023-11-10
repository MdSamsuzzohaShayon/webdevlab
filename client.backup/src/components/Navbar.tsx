import React from 'react';
import { Link } from 'gatsby';

function Navbar() {
  return (
    <header className="flex items-center justify-between py-2 border-b">
      <Link to="/" className="px-2 lg:px-0 uppercase font-bold text-purple-800">
        Web Dev Lab
      </Link>
      <ul className="inline-flex items-center">
        <li className="px-2 md:px-4">
          <Link to="/" className="text-purple-600 font-semibold hover:text-purple-500"> Home </Link>
        </li>
        <li className="px-2 md:px-4">
          <Link to="/about" className="text-gray-500 font-semibold hover:text-purple-500"> About </Link>
        </li>
        <li className="px-2 md:px-4">
          <Link to="/" className="text-gray-500 font-semibold hover:text-purple-500"> Press </Link>
        </li>
        <li className="px-2 md:px-4">
          <Link to="/" className="text-gray-500 font-semibold hover:text-purple-500"> Contact </Link>
        </li>
        <li className="px-2 md:px-4 hidden md:block">
          <Link to="/" className="text-gray-500 font-semibold hover:text-purple-500"> Login </Link>
        </li>
        <li className="px-2 md:px-4 hidden md:block">
          <Link to="/" className="text-gray-500 font-semibold hover:text-purple-500"> Register </Link>
        </li>
      </ul>

    </header>
  )
}

export default Navbar;