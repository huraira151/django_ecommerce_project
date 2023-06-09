import { all, call, put, takeLatest } from "redux-saga/effects"

// utils
import XHR from "../../../../utils/XHR"

// types
import {
  POST_LOGIN_REQUEST,
} from "./type"

// actions
import {
  loginRequestSuccess,
  loginRequestFailure,
} from "./action"

// Toast
import toast from "react-hot-toast"
import { history } from "../../../../reduxStore/store"

async function postLoginAPI(data) {
  const URL = `${process.env.REACT_APP_BASE_URL}api/v1/login/`
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

function* postLoginInfo({ data }) {
  try {
    const response = yield call(postLoginAPI, data)
    yield put(loginRequestSuccess(response?.data?.user))
    localStorage.setItem("token", response.data.token)
    toast.success("Logged in successfully")
    history.push('/home')
    yield put(loginRequestFailure(false))
  } catch (e) {
    const { response } = e
    response?.data?.non_field_errors && toast.error(response?.data.non_field_errors)
    yield put(loginRequestFailure(response?.data))
  }
}

export default all([
  takeLatest(POST_LOGIN_REQUEST, postLoginInfo),
])
