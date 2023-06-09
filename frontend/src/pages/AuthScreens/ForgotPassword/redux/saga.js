import { all, call, put, takeLatest } from "redux-saga/effects"

// utils
import XHR from "../../../../utils/XHR"

// types
import {
  POST_FORGOTPASS_REQUEST,
} from "./type"

// actions
import {
  forgotpassRequestSuccess,
  forgotpassRequestFailure,
} from "./action"

// Toast
import toast from "react-hot-toast"
import { history } from "../../../../reduxStore/store"

async function postForgotPassAPI(data) {
  const URL = `${process.env.REACT_APP_BASE_URL}api/v1/forgot-password/`
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

function* postForgotPass({ data }) {
  try {
    const response = yield call(postForgotPassAPI, data)
    yield put(forgotpassRequestSuccess(response?.data))
    toast.success("Email Sent Successfully")
    history.push('/reset-pass')
  } catch (e) {
    const { response } = e
    yield put(forgotpassRequestFailure(response?.data))
  }
}

export default all([
  takeLatest(POST_FORGOTPASS_REQUEST, postForgotPass),
])
