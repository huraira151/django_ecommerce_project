import {all} from 'redux-saga/effects';
import login from '../pages/AuthScreens/Login/redux/saga';
import signup from '../pages/AuthScreens/SignUp/redux/saga'

export function* rootSaga() {
  yield all([
    login,
    signup,
  ]);
}
