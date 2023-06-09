import {combineReducers} from 'redux';

import login from '../pages/AuthScreens/Login/redux/reducer';
import signup from '../pages/AuthScreens/SignUp/redux/reducer';
import forgotPass from '../pages/AuthScreens/ForgotPassword/redux/reducer';
import resetPass from '../pages/AuthScreens/ResetPassword/redux/reducer';

import {persistReducer} from 'redux-persist';
import storage from 'redux-persist/lib/storage';
const presistConfig = {
  key: 'login',
  storage,
};

export const combinedReducers = combineReducers({
  login: persistReducer(presistConfig, login),
  signup,
  forgotPass,
  resetPass,
});
