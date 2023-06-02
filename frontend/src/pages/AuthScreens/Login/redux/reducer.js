import {
  POST_LOGIN_REQUEST,
  POST_LOGIN_SUCCESS,
  POST_LOGIN_FAILURE,
} from "./type"

const initialState = {
  loginInfo: false,
  error: false,
  requesting: false,
}

const loginReducer = (state = initialState, action) => {
  switch (action.type) {

    // POST LOGIN REQUEST

    case POST_LOGIN_REQUEST:
      return {
        ...state,
        requesting: true
      }

    case POST_LOGIN_SUCCESS:
      return {
        ...state,
        requesting: false,
        loginInfo: action.data
      }
    case POST_LOGIN_FAILURE:
      return {
        ...state,
        requesting: false,
        error: action.data
      }

    default:
      return state
  }
}

export default loginReducer;
