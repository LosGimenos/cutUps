import React from 'react';
import { render } from 'react-dom';

import '../dist/stylesheets/main.scss';
import App from './components/app.jsx';

render(<App />, document.querySelector("#root"));

if (module.hot) {
  module.hot.accept();
}
