import './App.css';
import Navbar from './components/Navbar';
import AccountForm from './AccountForm';
import LoginForm from "./Login"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from 'react';
import Sidebar from './components/Sidebar';
import Home from './pages/index';
import SigninPage from './pages/signin'

function App() {

  return (
    <Router>
      <Routes>
            <Route path="/" element={<Home/>} exact />
            <Route path="/signin" element={<SigninPage/>} exact />
      </Routes>
    </Router>
  );
}

export default App;