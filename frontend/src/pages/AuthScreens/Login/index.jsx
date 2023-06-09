import React, { useState, useCallback, useEffect } from 'react'
import './style.scss'
import Button from '../../../components/Button/index'
import UInput from '../../../components/UInput/index'
import { Divider } from '@mui/material'
import GoogleIcon from '@mui/icons-material/Google';
import FacebookIcon from '@mui/icons-material/Facebook';
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import { history } from '../../../reduxStore/store'
import useForm from '../../../utils/useForm'
import { loginRequest, loginRequestFailure } from './redux/action'
import { connect } from 'react-redux';
import { LoginSocialFacebook } from 'reactjs-social-login';

const LoginScreen = (props) => {
    const [provider, setProvider] = useState('')
    const [profile, setProfile] = useState([])
    const [PassError, setPassError] = useState("")
    const [emailError, setEmailError] = useState("")

    const {
        loginRequest,
        BEError,
        requesting,
        loginRequestFailure,
    } = props

    const stateSchema = {
        email: {
            value: "",
            error: ""
        },
        password: {
            value: "",
            error: ""
        }
    }

    const validationStateSchema = {
        email: {
            required: true,
        },
        password: {
            required: true,
        },
    }

    const { state, handleOnChange, setState } = useForm(
        stateSchema,
        validationStateSchema,
    );

    const onSubmit = () => {
        const data = {
            email: state.email.value.trim(),
            password: state.password.value,
        };
        loginRequest(data);
    };

    const onLoginStart = useCallback(() => {
        alert('Sure? you want to login with facebook');
    }, []);

    const onLogoutSuccess = useCallback(() => {
        setProfile(null);
        setProvider('');
        alert('logout success');
    }, []);

    return (
        <div className='login-section-wrapper'>
            <div className='login-form-container'>
                <div className='login-form-section'>
                    <h1>Login</h1>
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
                            loginRequestFailure(false);
                        }}
                        inputError={emailError?.length > 0 ? emailError : BEError?.email}
                        errorText={emailError?.length > 0 ? emailError : BEError?.email || state.email.error}
                        errorClass={
                            BEError?.email || state.email.error || emailError?.length > 0 ? 'opacity-1' : ''
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
                        }
                        }
                        onFocus={() => loginRequestFailure(false)}
                        inputError={PassError?.length > 0 ? PassError : BEError?.password}
                        errorText={PassError?.length > 0 ? PassError : BEError?.password || state.password.error}
                        errorClass={
                            BEError?.password || state.password.error || PassError?.length > 0 ? 'opacity-1' : ''
                        }
                    />
                    <Button
                        title={requesting ? '' : 'Sign In'}
                        className='signin-btn'
                        showSpinner={requesting}
                        onClick={() => onSubmit()}
                        disabled={PassError?.length > 0 || emailError?.length > 0 ? true : false}
                    />
                    <div className='account-wrapper'>
                        <p className='forgot-pass' onClick={() => history.push("/forgot-pass")}>Forgot Password?</p>
                        <span className='create-account'>Dont have an account!
                            <p onClick={() => history.push("/signup")}>Create one</p>
                        </span>
                    </div>
                    <Divider className='signin-divider'>or sign in with</Divider>
                    <div className='social-login-btn-wrapper'>
                        <GoogleIcon style={{
                            color: '#db4437',
                            marginRight: "10px",
                            cursor: "pointer",
                            fontSize: "30px"
                        }} className='google-icon' />
                        <LoginSocialFacebook
                            appId={'697608738742008'}
                            fieldsProfile={
                                'id,first_name,last_name,middle_name,name,name_format,picture,short_name,email,gender'
                            }
                            onLoginStart={onLoginStart}
                            onLogoutSuccess={onLogoutSuccess}
                            redirect_uri={'https://09ac-39-53-124-139.ngrok-free.app/'}
                            onResolve={({ provider, data }) => {
                                setProvider(provider);
                                console.log("0000000000000000000", data);
                                setProfile(data);
                            }}
                            onReject={err => {
                                console.log(err);
                            }}>
                            <FacebookIcon style={{
                                color: '#3b5998',
                                marginRight: "10px",
                                cursor: "pointer",
                                fontSize: "30px"
                            }} className='google-icon' />
                        </LoginSocialFacebook>
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
    loginInfo: state.login.loginInfo,
    BEError: state.login.error,
    requesting: state.login.requesting,
});

const mapDispatchToProps = (dispatch) => ({
    loginRequest: (data) => dispatch(loginRequest(data)),
    loginRequestFailure: (data) => dispatch(loginRequestFailure(data)),
});

export default connect(mapStateToProps, mapDispatchToProps)(LoginScreen);
