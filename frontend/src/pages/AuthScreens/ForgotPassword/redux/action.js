import {
  POST_FORGOTPASS_REQUEST,
  POST_FORGOTPASS_SUCCESS,
  POST_FORGOTPASS_FAILURE,
} from "./type"

// POST Forgot Password
export const forgotpassRequest = data => ({
  type: POST_FORGOTPASS_REQUEST,
  data
})

export const forgotpassRequestSuccess = data => ({
  type: POST_FORGOTPASS_SUCCESS,
  data
})

export const forgotpassRequestFailure = data => ({
  type: POST_FORGOTPASS_FAILURE,
  data
})
