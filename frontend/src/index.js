import React from 'react';
import { unstable_HistoryRouter as HistoryRouter } from 'react-router-dom'
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import "../src/assets/scss/common.scss"
import { store, persistor } from "./reduxStore/store"
import { PersistGate } from "redux-persist/integration/react"
import { Provider } from "react-redux"
import { history } from "./reduxStore/store"

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    <PersistGate loading={null} persistor={persistor}>
      <HistoryRouter history={history}>
        <App />
      </HistoryRouter>
    </PersistGate>
  </Provider>
);
