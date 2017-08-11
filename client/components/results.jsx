import React, { Component } from 'react';
import request from 'superagent';

export default class Results extends Component {
  constructor() {
    super();
    this.state = {};
  }
  componentDidMount() {
    request.get('http://localhost:5000/tell-the-tale')
           .then((res, req) => {
            console.log(res.body)
           })
  }

  render() {
    return (
      <div className="results">
      </div>
    );
  }
};

