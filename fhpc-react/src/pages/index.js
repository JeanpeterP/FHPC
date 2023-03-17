import React, {useEffect, useState} from 'react'
import Sidebar from '../components/Sidebar'
import Navbar from '../components/Navbar'
import LoginForm from '../Login'
import AccountForm from '../AccountForm'
import HeroSection from '../components/HeroSection'
import InfoSection from '../components/InfoSection'
import { HomeObjOne, HomeObjThree, HomeObjTwo } from '../components/InfoSection/Data'
import Cookies from 'js-cookie';
import Services from '../components/Services'
import Footer from '../components/Footer'

const Home = () => {
  const [isOpen, setIsOpen] = useState(false)
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const isLoggedInCookie = Cookies.get('isLoggedIn');
    if (isLoggedInCookie === 'true') {
      setIsLoggedIn(true);
    } else {
      setIsLoggedIn(false);
    }
  }, []);

  const handleLogout = () => {
    setIsLoggedIn(false);
    Cookies.set('isLoggedIn', false);
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
        <InfoSection {...HomeObjTwo}/>
        <Services/>
        <InfoSection {...HomeObjThree}/>
        <AccountForm />
        <LoginForm setIsLoggedIn={setIsLoggedIn}/>
        <Footer/>
    </>
  )
}

export default Home