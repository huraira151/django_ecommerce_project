import React, { useState } from 'react'
import './style.scss'
import Button from '../../../components/Button/index'
import UInput from '../../../components/UInput/index'
import useForm from '../../../utils/useForm'
import { resetRequest, resetRequestFailure } from './redux/action'
import { connect } from 'react-redux';

const ResetPassScreen = (props) => {
    const [PassError, setPassError] = useState("");
    const [confirmPassError, setconfirmPassError] = useState("");

    const {
        resetRequest,
        error,
        requesting,
        resetRequestFailure,
    } = props

    const stateSchema = {
        password: {
            value: "",
            error: ""
        },
        confirm_password: {
            value: "",
            error: ""
        },
        token: {
            value: "",
            error: ""
        }
    }

    const validationStateSchema = {
        password: {
            required: true,
        },
        confirm_password: {
            required: true,
        },
        token: {
            required: true,
        }
    }

    const { state, handleOnChange, setState } = useForm(
        stateSchema,
        validationStateSchema,
    );

    const onSubmit = () => {
        const data = {
            password: state.password.value,
            confirm_password: state.confirm_password.value,
            token: state.token.value,
        };
        resetRequest(data);
    };

    return (
        <div className='reset-section-wrapper'>
            <div className='reset-form-container'>
                <div className='reset-form-section'>
                    <h1>Reset Password</h1>
                    <UInput
                        placeholder='Password'
                        type='password'
                        required={true}
                        value={state.password.value}
                        onChange={(val) => {
                            const inputValue = val.target.value
                            if (inputValue?.length < 8) {
                                setPassError("Password should be 8 characters long")
                            } else {
                                setPassError("")
                            }
                            handleOnChange('password', inputValue)
                        }
                        }
                        onFocus={() => resetRequestFailure(false)}
                        inputError={PassError?.length > 0 ? PassError : error?.password || error?.non_field_errors}
                        errorText={PassError?.length > 0 ? PassError : error?.non_field_errors || error?.password || state.password.error}
                        errorClass={
                            error?.non_field_errors || error?.password || state.password.error || PassError?.length > 0 ? 'opacity-1' : ''
                        }
                    />
                    <UInput
                        placeholder='Confirm Password'
                        type='password'
                        required={true}
                        value={state.confirm_password.value}
                        onChange={(val) => {
                            const inputValue = val.target.value
                            if (inputValue?.length < 8) {
                                setconfirmPassError("Password should be 8 characters long")
                            } else {
                                setconfirmPassError("")
                            }
                            handleOnChange('confirm_password', inputValue)
                        }}
                        onFocus={() => resetRequestFailure(false)}
                        inputError={confirmPassError?.length > 0 ? confirmPassError : error?.confirm_password}
                        errorText={confirmPassError?.length > 0 ? confirmPassError : error?.confirm_password || state.confirm_password.error}
                        errorClass={
                            error?.confirm_password || state.confirm_password.error || confirmPassError?.length > 0 ? 'opacity-1' : ''
                        }
                    />
                    <UInput
                        placeholder='Token'
                        type='number'
                        required={true}
                        value={state.token.value}
                        onChange={(val) => {handleOnChange('token', val.target.value)}}
                        onFocus={() => resetRequestFailure(false)}
                        inputError={error?.status || error?.token}
                        errorText={error?.status || state.token.error || error?.token}
                        errorClass={
                            error?.token || error?.status || state.token.error ? 'opacity-1' : ''
                        }
                    />
                    <Button
                        title={requesting ? '' : 'Reset Password'}
                        className='reset-btn'
                        showSpinner={requesting}
                        onClick={() => onSubmit()}
                        disabled={
                            PassError?.length > 0 ? true : false}
                    />
                </div>
            </div>
        </div>
    )
}

const mapStateToProps = (state) => ({
    console: console.log(state),
    resetInfo: state.resetPass.loginInfo,
    error: state.resetPass.error,
    requesting: state.resetPass.requesting,
});

const mapDispatchToProps = (dispatch) => ({
    resetRequest: (data) => dispatch(resetRequest(data)),
    resetRequestFailure: (data) => dispatch(resetRequestFailure(data)),
});

export default connect(mapStateToProps, mapDispatchToProps)(ResetPassScreen);
