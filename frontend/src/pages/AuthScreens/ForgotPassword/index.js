import React, { useState } from "react";
import "./style.scss";
import Button from "../../../components/Button/index";
import UInput from "../../../components/UInput/index";
import useForm from "../../../utils/useForm";
import { forgotpassRequest, forgotpassRequestFailure } from "./redux/action";
import { connect } from "react-redux";

const ForgotPassScreen = (props) => {
  const [emailError, setEmailError] = useState("");

  const {
    forgotpassInfo,
    error,
    requesting,
    forgotpassRequestFailure,
    forgotpassRequest,
  } = props;

  const stateSchema = {
    email: {
      value: "",
      error: "",
    },
  };

  const validationStateSchema = {
    email: {
      required: true,
    },
  };

  const { state, handleOnChange, setState } = useForm(
    stateSchema,
    validationStateSchema
  );

  const onSubmit = () => {
    const data = {
      email: state.email.value.trim(),
    };
    forgotpassRequest(data);
  };

  return (
    <div className="forgot-section-wrapper">
      <div className="forgot-form-container">
        <div className="forgot-form-section">
          <h1>Forgot Password</h1>
          <UInput
            placeholder="Email"
            type="email"
            required={true}
            value={state.email.value}
            onChange={(val) => {
              const emailInputValue = val.target.value.trim();
              const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

              if (!pattern.test(emailInputValue)) {
                setEmailError("The email you entered is not valid");
              } else {
                setEmailError("");
              }
              handleOnChange("email", emailInputValue);
            }}
            onFocus={() => {
              forgotpassRequestFailure(false);
            }}
            inputError={emailError?.length > 0 ? emailError : error?.email}
            errorText={
              emailError?.length > 0
                ? emailError
                : error?.email || state.email.error
            }
            errorClass={
              error?.email || state.email.error || emailError?.length > 0
                ? "opacity-1"
                : ""
            }
          />
          <Button
            title={requesting ? "" : "Forgot Password"}
            className="forgot-btn"
            showSpinner={requesting}
            onClick={() => onSubmit()}
            disabled={emailError?.length > 0 ? true : false}
          />
        </div>
      </div>
    </div>
  );
};

const mapStateToProps = (state) => ({
  forgotpassInfo: state.forgotPass.forgotpassInfo,
  error: state.forgotPass.error,
  requesting: state.forgotPass.requesting,
});

const mapDispatchToProps = (dispatch) => ({
  forgotpassRequest: (data) => dispatch(forgotpassRequest(data)),
  forgotpassRequestFailure: (data) => dispatch(forgotpassRequestFailure(data)),
});

export default connect(mapStateToProps, mapDispatchToProps)(ForgotPassScreen);
