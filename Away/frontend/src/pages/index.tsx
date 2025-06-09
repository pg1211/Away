import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from '../components/Navbar';
import LandingPage from './LandingPage';
import Dashboard from './Dashboard';
import TripPlanner from './TripPlanner';

const App: React.FC = () => {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/trip-planner" element={<TripPlanner />} />
            </Routes>
        </Router>
    );
};

export default App;