import React from "react";
import Navbar from "./Navbar";
import Footer from "./Footer";

export default function Layout({ children }: {children: React.ReactNode}) {
  return (
    <div className="w-full">
        <Navbar />
      {children}
      <Footer />
    </div>
  )
}