import React from 'react';
import { render } from 'react-dom';

import '../dist/stylesheets/main.scss';
import Routes from './routes/routes.jsx';

render(<Routes />, document.querySelector("#root"));

if (module.hot) {
  module.hot.accept();
}
