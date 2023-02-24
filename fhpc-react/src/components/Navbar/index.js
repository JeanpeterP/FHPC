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
            <NavLogo to="/">Dollarrr</NavLogo>
            <MobileIcon onClick={toggle}>
              <FaBars />
            </MobileIcon>
            <NavMenu>
              <NavItem>
                <NavLinks to="about">About</NavLinks>
              </NavItem>
              <NavItem>
                <NavLinks to="services">Services</NavLinks>
              </NavItem>
              {isLoggedIn ? (
              <NavItem>
                <NavLinks to="signup">Appoitments</NavLinks>
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