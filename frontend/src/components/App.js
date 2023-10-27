import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Projects from './Projects';
import Services from './Services';
import Contacts from './Contacts';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/projects" component={Projects} />
        <Route path="/services" component={Services} />
        <Route path="/contacts" component={Contacts} />
      </Switch>
    </Router>
  );
}

export default App;
