const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');
const webpack = require('webpack'); // to access built-in plugins
const Dotenv = require('dotenv-webpack'); // for loading environment variables

module.exports = {
  mode: 'development',
  devtool: 'eval-source-map',
  entry: {
    index: './src/index.js',
    home: './src/home.js',
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js', // [name] is replaced by the key in the entry object
  },
  watch: true,
  resolve: {
    fallback: {
      path: require.resolve('path-browserify'),
      crypto: require.resolve('crypto-browserify'),
      buffer: require.resolve('buffer/'),
      stream: require.resolve('stream-browserify'),
      os: require.resolve('os-browserify/browser'),
      vm: require.resolve('vm-browserify'),
      process: require.resolve('process/browser'),
    },
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(png|jpg|jpeg|gif|svg)$/i,
        type: 'asset/resource',
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      chunks: ['index'], // associate this html file with the index bundle
      filename: 'index.html',
    }),
    new HtmlWebpackPlugin({
      template: './src/login_signup.html',
      chunks: ['index'], // associate this html file with the index bundle
      filename: 'login_signup.html',
    }),
    new HtmlWebpackPlugin({
      template: './src/home.html',
      chunks: ['home'], //  associate this html file with the home bundle
      filename: 'home.html',
    }),
    new Dotenv({ systemvars: true }), // for loading environment variables
    new webpack.ProvidePlugin({
      process: 'process/browser',
    }),
  ],
};
