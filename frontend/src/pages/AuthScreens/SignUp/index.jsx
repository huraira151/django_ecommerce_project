import React, { useState } from 'react'
import './style.scss'
import Button from '../../../components/Button/index'
import UInput from '../../../components/UInput/index'
import { Divider } from '@mui/material'
import GoogleIcon from '@mui/icons-material/Google';
import FacebookIcon from '@mui/icons-material/Facebook';
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import { history } from '../../../reduxStore/store'
import { signupRequest, signupRequestFailure } from './redux/action'
import useForm from '../../../utils/useForm'
import { connect } from 'react-redux';

const SignUpScreen = (props) => {
    const [PassError, setPassError] = useState("")
    const [emailError, setEmailError] = useState("")

    const {
        signupRequest,
        signupInfo,
        error,
        requesting,
        signupRequestFailure,
    } = props

    const stateSchema = {
        name: {
            value: "",
            error: ""
        },
        email: {
            value: "",
            error: ""
        },
        phone_number: {
            value: "",
            error: ""
        },
        address: {
            value: "",
            error: ""
        },
        password: {
            value: "",
            error: ""
        },
        confirm_password: {
            value: "",
            error: ""
        }
    }

    const validationStateSchema = {
        name: {
            required: true,
        },
        email: {
            required: true,
        },
        phone_number: {
            required: true,
        },
        address: {
            required: true,
        },
        password: {
            required: true,
        },
        confirm_password: {
            required: true
        }
    }

    const { state, handleOnChange, setState } = useForm(
        stateSchema,
        validationStateSchema,
    );

    const onSubmit = () => {
        const data = {
            name: state.name.value,
            email: state.email.value.trim(),
            phone_number: state.phone_number.value,
            address: state.address.value,
            password: state.password.value,
            confirm_password: state.confirm_password.value,
            role: "customer"
        };
        console.log("data", data)
        signupRequest(data);
    };

    return (
        <div className='signup-section-wrapper'>
            <div className='signup-form-container'>
                <div className='signup-form-section'>
                    <h1>Sign Up</h1>
                    <UInput
                        placeholder='Name'
                        type='text'
                        value={state.name.value}
                        onChange={(val) => { handleOnChange('name', val.target.value) }}
                        onFocus={() => {
                            signupRequestFailure(false);
                        }}
                        inputError={error?.name}
                        errorText={error?.name || state.name.error}
                        errorClass={
                            error?.name || state.name.error ? 'opacity-1' : ''
                        }
                    />
                    <UInput
                        placeholder='Email'
                        type='email'
                        required={true}
                        value={state.email.value}
                        onChange={(val) => {
                            const emailInputValue = val.target.value.trim()
                            const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

                            if (!pattern.test(emailInputValue)) {
                                setEmailError('The email you entered is not valid');
                            } else {
                                setEmailError('');
                            }
                            handleOnChange('email', emailInputValue)
                        }
                        }
                        onFocus={() => {
                            signupRequestFailure(false);
                            setEmailError("")
                        }}
                        inputError={emailError?.length > 0 ? emailError : error?.email}
                        errorText={emailError?.length > 0 ? emailError : error?.email || state.email.error}
                        errorClass={
                            error?.email || state.email.error || emailError?.length > 0 ? 'opacity-1' : ''
                        }
                    />
                    <UInput
                        placeholder='Phone Number'
                        type='tel'
                        value={state.phone_number.value}
                        onChange={(val) => { handleOnChange('phone_number', val.target.value) }}
                        onFocus={() => {
                            signupRequestFailure(false);
                        }}
                        inputError={error?.phone_number}
                        errorText={error?.phone_number || state.phone_number.error}
                        errorClass={
                            error?.phone_number || state.phone_number.error ? 'opacity-1' : ''
                        }
                    />
                    <UInput
                        placeholder='Address'
                        type='text'
                        value={state.address.value}
                        onChange={(val) => { handleOnChange('address', val.target.value) }}
                        onFocus={() => {
                            signupRequestFailure(false);
                        }}
                        inputError={error?.address}
                        errorText={error?.address || state.address.error}
                        errorClass={
                            error?.address || state.address.error ? 'opacity-1' : ''
                        }
                    />
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
                        }}
                        onFocus={() => {
                            signupRequestFailure(false);
                            setPassError('');
                        }}
                        inputError={PassError?.length > 0 ? PassError : error?.password}
                        errorText={PassError?.length > 0 ? PassError : error?.password || state.password.error || error?.error}
                        errorClass={
                            error?.password || state.email.error || PassError?.length > 0 ? 'opacity-1' : ''
                        }
                    />
                    <UInput
                        placeholder='Confirm Password'
                        type='password'
                        required={true}
                        value={state.confirm_password.value}
                        onChange={(val) => { handleOnChange('confirm_password', val.target.value) }}
                        onFocus={() => {
                            signupRequestFailure(false)
                        }}
                        inputError={error?.confirm_password}
                        errorText={error?.confirm_password || state.confirm_password.error}
                        errorClass={
                            error?.confirm_password || state.confirm_password.error ? 'opacity-1' : ''
                        }
                    />
                    <Button
                        title={requesting ? '' : 'Sign Up'}
                        className='signup-btn'
                        showSpinner={requesting}
                        onClick={() => onSubmit()}
                        disabled={PassError?.length > 0 || emailError?.length > 0 ? true : false}
                    />
                    <div className='signup-account-wrapper'>
                        <span className='already-account'>Already have an account!<p onClick={() => history.push("/login")}> Login</p></span>
                    </div>
                    <Divider className='signup-divider'>or sign up with</Divider>
                    <div className='social-login-btn-wrapper'>
                        <GoogleIcon style={{
                            color: '#db4437',
                            marginRight: "10px",
                            cursor: "pointer",
                            fontSize: "30px"
                        }} className='google-icon' />
                        <FacebookIcon style={{
                            color: '#3b5998',
                            marginRight: "10px",
                            cursor: "pointer",
                            fontSize: "30px"
                        }} className='google-icon' />
                        <LinkedInIcon style={{
                            color: '#0077b5',
                            cursor: "pointer",
                            fontSize: "30px",
                        }} className='google-icon' />
                    </div>
                </div>
            </div>
        </div>
    )
}

const mapStateToProps = (state) => ({
    console: console.log(state),
    signupInfo: state.signup.signupInfo,
    error: state.signup.error,
    requesting: state.signup.requesting,
});

const mapDispatchToProps = (dispatch) => ({
    signupRequest: (data) => dispatch(signupRequest(data)),
    signupRequestFailure: (data) => dispatch(signupRequestFailure(data)),
});

export default connect(mapStateToProps, mapDispatchToProps)(SignUpScreen);
