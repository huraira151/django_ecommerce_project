import {all} from 'redux-saga/effects';
import login from '../pages/AuthScreens/Login/redux/saga';
import signup from '../pages/AuthScreens/SignUp/redux/saga';
import forgotPass from '../pages/AuthScreens/ForgotPassword/redux/saga';
import resetPass from '../pages/AuthScreens/ResetPassword/redux/saga';

export function* rootSaga() {
  yield all([
    login,
    signup,
    forgotPass,
    resetPass,
  ]);
}
