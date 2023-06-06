import {
  POST_SIGNUP_REQUEST,
  POST_SIGNUP_SUCCESS,
  POST_SIGNUP_FAILURE,
} from "./type"

const initialState = {
  signupInfo: false,
  error: false,
  requesting: false,
}

const signupReducer = (state = initialState, action) => {
  switch (action.type) {

    // POST SIGNUP REQUEST

    case POST_SIGNUP_REQUEST:
      return {
        ...state,
        requesting: true,
      }

    case POST_SIGNUP_SUCCESS:
      return {
        ...state,
        requesting: false,
        signupInfo: action.data
      }
    case POST_SIGNUP_FAILURE:
      return {
        ...state,
        requesting: false,
        error: action.data
      }

    default:
      return state
  }
}

export default signupReducer;
