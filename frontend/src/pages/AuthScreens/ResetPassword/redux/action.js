import {
  POST_RESET_REQUEST,
  POST_RESET_SUCCESS,
  POST_RESET_FAILURE,
} from "./type"

// POST Reset Password
export const resetRequest = data => ({
  type: POST_RESET_REQUEST,
  data
})

export const resetRequestSuccess = data => ({
  type: POST_RESET_SUCCESS,
  data
})

export const resetRequestFailure = data => ({
  type: POST_RESET_FAILURE,
  data
})
