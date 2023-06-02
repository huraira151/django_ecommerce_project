import {
  POST_LOGIN_REQUEST,
  POST_LOGIN_SUCCESS,
  POST_LOGIN_FAILURE,
} from "./type"

// POST LOGIN
export const loginRequest = data => ({
  type: POST_LOGIN_REQUEST,
  data
})

export const loginRequestSuccess = data => ({
  type: POST_LOGIN_SUCCESS,
  data
})

export const loginRequestFailure = data => ({
  type: POST_LOGIN_FAILURE,
  data
})
