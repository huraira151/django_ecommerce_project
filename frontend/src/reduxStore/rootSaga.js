import {all} from 'redux-saga/effects';
import login from '../pages/AuthScreens/Login/redux/saga';

export function* rootSaga() {
  yield all([
    login,
  ]);
}