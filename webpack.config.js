const path = require('path');
const webpack = require('webpack');

const config = {
  context: path.join(__dirname, 'client'),
  entry: [
            './index.jsx',
            'webpack/hot/dev-server',
            'webpack-dev-server/client?http://localhost:8080'
         ],
  output: {
    path: path.join(__dirname, 'dist', 'js'),
    filename: 'bundle.js',
    publicPath: '/'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        options: {
          presets: ['es2015', 'react'],
        }
      },
      {
        test: /\.scss$/,
        loader: ['style-loader', 'css-loader', 'sass-loader']
      },
      {
        test: /\.(jpe?g|png|gif|svg)$/i,
        loader: ['file-loader']
      }
    ],
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
  ]
}

module.exports = config;
