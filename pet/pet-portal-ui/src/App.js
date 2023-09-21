import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Park from './components/Park';
import Play from './components/Play';
import Movie from './components/Movie';

function App() {
  return (
    <Router>
      <div>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          {/* Navbar code here */}
        </nav>
        <div className="container mt-4">
          <Switch>
            <Route exact path="/park" component={Park} />
            <Route exact path="/play" component={Play} />
            <Route exact path="/movie" component={Movie} />
            {/* Add more routes as needed */}
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
