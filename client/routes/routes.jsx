import React from 'react';
import { HashRouter as Router, Route, Switch } from 'react-router-dom';
import App from '../components/app.jsx';
import Header from '../components/header.jsx';
import Results from '../components/results.jsx';

const Routes = () => (
  <Router>
    <div>
      <Header />
      <Switch>
        <Route exact path="/" component={App} />
        <Route path="/results" component={Results} />
      </Switch>
    </div>
  </Router>
);

export default Routes;
