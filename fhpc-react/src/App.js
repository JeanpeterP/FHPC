import './App.css';
import Navbar from './components/Navbar';
import AccountForm from './AccountForm';
import LoginForm from "./Login"
import {BrowserRouter as Router} from 'react-router-dom'
import { useState } from 'react';
import Sidebar from './components/Sidebar';
import Home from './pages/index';

function App() {

  return (
    <Router>
      <Home />
    </Router>
  );
}

export default App;
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