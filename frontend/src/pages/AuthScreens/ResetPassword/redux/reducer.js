import {
  POST_RESET_REQUEST,
  POST_RESET_SUCCESS,
  POST_RESET_FAILURE,
} from "./type"

const initialState = {
  resetInfo: false,
  error: false,
  requesting: false,
}

const resetReducer = (state = initialState, action) => {
  switch (action.type) {

    // POST Reset Password

    case POST_RESET_REQUEST:
      return {
        ...state,
        requesting: true
      }

    case POST_RESET_SUCCESS:
      return {
        ...state,
        requesting: false,
        resetInfo: action.data
      }

    case POST_RESET_FAILURE:
      return {
        ...state,
        requesting: false,
        error: action.data
      }

    default:
      return state
  }
}

export default resetReducer;
