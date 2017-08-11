import React from 'react';
import { Link } from 'react-router-dom';

const About = () => (
  <div className="about">
    <h2>Pluck the Word</h2>
    <ol>
      <li>
        <span><p>Take some headlines</p></span>
      </li>
      <li>
        <span><p>Slice em up</p></span>
      </li>
      <li>
        <span><p>Churn em right back out</p></span>
      </li>
      <li>
        <span><p>Check out the current state of the world</p></span>
      </li>
    </ol>
    <Link to="results">
      <button>
        Get Going
      </button>
    </Link>
  </div>
);

export default About;
