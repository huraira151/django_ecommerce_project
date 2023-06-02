import {combineReducers} from 'redux';

import login from '../pages/AuthScreens/Login/redux/reducer';

import {persistReducer} from 'redux-persist';
import storage from 'redux-persist/lib/storage';
const presistConfig = {
  key: 'login',
  storage,
};

export const combinedReducers = combineReducers({
  login: persistReducer(presistConfig, login),
});
