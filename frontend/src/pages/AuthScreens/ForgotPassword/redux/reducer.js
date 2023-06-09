import {
  POST_FORGOTPASS_REQUEST,
  POST_FORGOTPASS_SUCCESS,
  POST_FORGOTPASS_FAILURE,
} from "./type"

const initialState = {
  forgotpassInfo: false,
  error: false,
  requesting: false,
}

const forgotpassReducer = (state = initialState, action) => {
  switch (action.type) {

    // POST Forgot Password

    case POST_FORGOTPASS_REQUEST:
      return {
        ...state,
        requesting: true
      }

    case POST_FORGOTPASS_SUCCESS:
      return {
        ...state,
        requesting: false,
        forgotpassInfo: action.data
      }
    case POST_FORGOTPASS_FAILURE:
      return {
        ...state,
        requesting: false,
        error: action.data
      }

    default:
      return state
  }
}

export default forgotpassReducer;
