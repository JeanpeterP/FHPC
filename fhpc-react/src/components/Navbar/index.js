import React from 'react'
import {FaBars} from 'react-icons/fa'
import {
    Nav,
    NavbarContainer,
    NavLogo,
    MobileIcon,
    NavMenu,
    NavItem,
    NavLinks,
    NavBtn,
    NavBtnLink
} from './NavbarElements';
const Navbar = ({ isLoggedIn, handleLogout, toggle }) => {
    return (
      <>
        <Nav>
          <NavbarContainer>
            <NavLogo to="/">FHPC</NavLogo>
            <MobileIcon onClick={toggle}>
              <FaBars />
            </MobileIcon>
            <NavMenu>
              <NavItem>
                <NavLinks to="about">About</NavLinks>
              </NavItem>
              <NavItem>
                <NavLinks to="Discover">Discover</NavLinks>
              </NavItem>
              <NavItem>
                <NavLinks to="Services">Services</NavLinks>
              </NavItem>  
              {isLoggedIn ? (
              <NavItem>
                <NavLinks to="Services">My Profile</NavLinks>
              </NavItem>              
              ) : (
              <NavItem>
                <NavLinks to="signup">Sign Up</NavLinks>
              </NavItem>                   
              )}
            </NavMenu>
          </NavbarContainer>
          {isLoggedIn ? (
          <NavBtn>
            <NavBtnLink to="/signin" onClick={handleLogout}>Logout</NavBtnLink>
            </NavBtn>
          ) : (
          <NavBtn>
            <NavBtnLink to="/signin">Sign In</NavBtnLink>
          </NavBtn>
          )}
        </Nav>
      </>
    );
  };

export default Navbar