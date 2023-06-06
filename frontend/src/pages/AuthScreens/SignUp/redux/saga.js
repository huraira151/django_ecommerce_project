import { all, call, put, takeLatest } from "redux-saga/effects"

// utils
import XHR from "../../../../utils/XHR"

// types
import {
  POST_SIGNUP_REQUEST,
} from "./type"

// actions
import {
  signupRequestSuccess,
  signupRequestFailure,
} from "./action"

// Toast
import toast from "react-hot-toast"
import { history } from "../../../../reduxStore/store"

async function postSignupAPI(data) {
  const URL = `${process.env.REACT_APP_BASE_URL}api/v1/signup/`
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

function* postSignupInfo({ data }) {
  try {
    const response = yield call(postSignupAPI, data)
    yield put(signupRequestSuccess(response?.data?.user))
    toast.success("SignUp Successfull")
    history.push('/login')
  } catch (e) {
    const { response } = e
    yield put(signupRequestFailure(response?.data))
  }
}

export default all([
  takeLatest(POST_SIGNUP_REQUEST, postSignupInfo),
])
