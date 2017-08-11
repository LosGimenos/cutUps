import React, { Component } from 'react';
import Hero from './hero.jsx';
import About from './about.jsx';

export default class App extends Component {
  render() {
    return (
      <div className="main-wrapper">
        <Hero />
        <About />
      </div>
    );
  }
}
