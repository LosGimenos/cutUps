import React, { Component } from 'react';
import Header from './header.jsx';
import Hero from './hero.jsx';
import About from './about.jsx';

export default class App extends Component {
  render() {
    return (
      <div className="main-wrapper">
        <Header />
        <Hero />
        <About />
      </div>
    );
  }
}
