import React, {useState} from 'react'
import Sidebar from '../components/Sidebar'
import Navbar from '../components/Navbar'
import LoginForm from '../Login'
import AccountForm from '../AccountForm'
import HeroSection from '../components/HeroSection'
import InfoSection from '../components/InfoSection'
import { HomeObjOne } from '../components/InfoSection/Data'

const Home = () => {
  const [isOpen, setIsOpen] = useState(false)
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  const toggle = () => {
    setIsOpen(!isOpen)
  }

  return (
    <>
        <Sidebar isOpen={isOpen} toggle={toggle} />
        <Navbar isLoggedIn={isLoggedIn} handleLogout={handleLogout} toggle={toggle}/>
        <HeroSection />
        <InfoSection {...HomeObjOne}/>
        <AccountForm />
        <LoginForm setIsLoggedIn={setIsLoggedIn}/>
    </>
  )
}

export default Home