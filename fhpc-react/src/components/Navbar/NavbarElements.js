import styled from 'styled-components';
import {Link as LinkR} from 'react-router-dom';
import {Link as LinkS} from 'react-scroll'


export const Nav = styled.nav`
  background: #000;
  height: 80px;
  margin-top: -80px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1rem;
  position: sticky;
  top: 0;
  z-index:10;

  @media screen and (max-width: 960px) {
    transition: 0.8s all ease;
  }
`

export const NavbarContainer = styled.div`
display: flex;
justify-content: space-between;
height: 80px;
z-index: 1;
width: 100%;
padding: 0 24px;
max-width: 1100px;
`

export const NavLogo = styled(LinkR)`
color: #01bf71;
justify-self: flex-start;
cursor: pointer;
font-size: 1.5rem;
display: flex;
align-items: center;
font-weight: bold;
text-decoration: none;

&:hover {
  color: #fff;
}
`

export const MobileIcon = styled.div`
display: none;

@media screen and (max-width:768px) {
    display: flex;
    position: absolute;
    top: 6%;
    right: 0;
    align-items: center;
    transform: translate(-100%, 60%);
    font-size: 1.9rem;
    cursor: pointer;
    color: #01bf71;
    }
`

export const NavMenu = styled.ul`
display:flex;
align-items: center;
margin: auto;
list-style: none;
text-align: center;
maright-right: -22px;

@media screen and (max-width: 768px) {
    display: none;
}
`

export const NavItem = styled.li`
height:80px;
`

export const NavLinks = styled(LinkS)`
color: #01bf71;
display: flex;
align-items: center;
text-decoration: none;
padding: 0 1rem;
height: 100%;
cursor: pointer;

&:hover {
  color: #fff;
}
&.active {
    border-bottom: 3px solid #01bf71;
}
`

export const NavBtn = styled.nav`
display: flex;
aligh-items: center;

@media screen and (max-width: 768px) {
  display: none;
}
`

export const NavBtnLink = styled(LinkR)`
margin-right: 24px;
border-radius: 50px;
background: #01bf71;
white-space: nowrap;
padding: 10px 22px;
color: #010606;
font-size: 16px;
outline: none;
border: none;
cursor: pointer;
transition: all 0.2s ease-in-out;
text-decoration: none;

&:hover {
  transition: all 0.2s ease-in-out;
  background: #01bf71;
  color: #fff;
}
`