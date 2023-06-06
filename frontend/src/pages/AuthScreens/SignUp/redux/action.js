import {
  POST_SIGNUP_REQUEST,
  POST_SIGNUP_SUCCESS,
  POST_SIGNUP_FAILURE,
} from "./type"

// POST LOGIN
export const signupRequest = data => ({
  type: POST_SIGNUP_REQUEST,
  data
})

export const signupRequestSuccess = data => ({
  type: POST_SIGNUP_SUCCESS,
  data
})

export const signupRequestFailure = data => ({
  type: POST_SIGNUP_FAILURE,
  data
})
