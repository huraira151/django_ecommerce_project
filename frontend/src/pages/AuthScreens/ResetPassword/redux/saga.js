import { all, call, put, takeLatest } from "redux-saga/effects"

// utils
import XHR from "../../../../utils/XHR"

// types
import {
  POST_RESET_REQUEST,
} from "./type"

// actions
import {
  resetRequestSuccess,
  resetRequestFailure,
} from "./action"

import { loginRequestSuccess } from '../../Login/redux/action'

// Toast
import toast from "react-hot-toast"
import { history } from "../../../../reduxStore/store"

async function resetPassAPI(data) {
  const URL = `${process.env.REACT_APP_BASE_URL}api/v1/reset-password-confirm/`
  const options = {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    method: "POST",
    data
  }
  return XHR(URL, options)
}

function* resetPass({ data }) {
  try {
    const response = yield call(resetPassAPI, data)
    yield put(resetRequestSuccess(response?.data))
    toast.success("Password Reset Successfully")
    loginRequestSuccess(false)
    history.push('/login')
  } catch (e) {
    const { response } = e
    // response?.data?.non_field_errors && toast.error(response?.data.non_field_errors)
    yield put(resetRequestFailure(response?.data))
  }
}

export default all([
  takeLatest(POST_RESET_REQUEST, resetPass),
])
